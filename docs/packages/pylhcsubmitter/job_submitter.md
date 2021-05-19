# PyLHC Submitter
[See the docs][documentation] for a detailed code description.
Note that the full functionality is only available under Linux, with HTCondor configured e.g. on CERN's lxplus service.
Currently, only local job execution is possible in Windows.

## Description

The PyLHC submitter allows to execute a parametric study using a script-mask and a `dictionary` with parameters to
replace, from the command line. The parameters to be replaced must be present in the given mask as
``%(PARAMETER)s`` (other types apart from string also allowed).
The type of script and executable is freely choosable, but defaults to ``madx`` - for which this
submitter was originally written.

When submitting to ``HTCondor``, data to be transferred back to the working directory must be
written in a sub-folder defined by ``job_output_directory`` which defaults to **Outputdata**.
This script also allows to check if all ``HTCondor`` jobs finished successfully, for resubmissions
with a different parameter grid, and for local execution.

A **Jobs.tfs** file is created in the working directory containing the Job Id, parameter per job
and job directory for further post processing.

*--Required--*

- **mask** *(str)*: Script Mask to use, can be either the Path to a mask file or a string.
- **replace_dict** *(DictAsString)*: Dict containing the str to replace as
  keys and values a list of parameters to replace
- **working_directory** *(str)*: Directory where data should be put

*--Optional--*

- **append_jobs**: Flag to rerun job with finer/wider grid,
  already existing points will not be reexecuted.
  Action: ``store_true``
- **check_files** *(str)*: List of files/file-name-masks expected to be in the
  'job_output_dir' after a successful job (for appending/resuming). Uses the 'glob'
  function, so unix-wildcards (*) are allowed. If not given, only the presence of the folder itself is checked.
- **dryrun**: Flag to only prepare folders and scripts,
  but does not start madx/submit jobs.
  Together with `resume_jobs` this can be use to check which jobs succeeded and which failed.
  Action: ``store_true``
- **executable** *(str)*: Path to executable or job-type (of ['madx', 'python3', 'python2']) to use.
- **htc_arguments** *(DictAsString)*: Additional arguments for htcondor, as Dict-String.
  For AccountingGroup please use 'accounting_group'. 'max_retries' and 'notification' have defaults (if not given).
  Others are just passed on.
  Default: ``{}``
- **job_output_dir** *(str)*: The name of the output dir of the job. (Make sure your script puts its data there!)
  Default: ``Outputdata``
- **jobflavour** *(str)*: Jobflavour to give rough estimate of runtime of one job
  Choices: ``('espresso', 'microcentury', 'longlunch', 'workday', 'tomorrow', 'testmatch', 'nextweek')``
  Default: ``workday``
- **jobid_mask** *(str)*: Mask to name jobs from replace_dict
- **num_processes** *(int)*: Number of processes to be used if run locally
  Default: ``4``
- **resume_jobs**: Only do jobs that did not work.
  Action: ``store_true``
- **run_local**: Flag to run the jobs on the local machine. Not suggested.
  Action: ``store_true``
- **script_arguments** *(DictAsString)*: Additional arguments to pass to the script,
  as dict in key-value pairs ('--' need to be included in the keys).
  Default: ``{}``
- **script_extension** *(str)*: New extension for the scripts created from the masks.
  This is inferred automatically for ['madx', 'python3', 'python2']. Otherwise not changed.
- **ssh** *(str)*: Run htcondor from this machine via ssh (needs access to the `working_directory`)

## Example 1: Tune Sweep using a MAD-X mask

In this example we will do a quick submit to HTCondor and starting simulations for both beams over a range of tunes.

???+ "Python Code"
    ```python
    from pylhc_submitter.job_submitter import main as htcondor_submit
    import numpy as np

    if __name__ == '__main__':
        htcondor_submit(
            executable='madx',
            mask='my_madx.mask',
            replace_dict=dict(
                BEAM=[1, 2], 
                TUNEX=np.linspace(62.3, 62.32, 11).tolist(), 
                TUNEY=np.linspace(60.31, 60.33, 11).tolist(),
                ),
            jobid_mask="b%(BEAM)d.qx%(TUNEX)s.qy%(TUNEY)s",
            working_directory='/afs/cern.ch/work/u/username/study.tune_sweep'
        )
    ```

??? info "Submission with config file"
    The same can also be achieved by creating a `config.ini` file containing

    ```
    [DEFAULT]
    executable='madx',
    mask='my_madx.mask',
    working_directory='/afs/cern.ch/work/u/username/study.tune_sweep',
    replace_dict={
        BEAM=[1, 2],
        TUNEX= [62.3, 62.302, 62.304, 62.306, 62.308, 62.31, 62.312, 62.314, 62.316, 62.318, 62.32],
        TUNEY=[60.31, 60.312, 60.314, 60.316, 60.318, 60.32, 60.322, 60.324, 60.326, 60.328, 60.33],
    },
    jobid_mask="b%(BEAM)d.qx%(TUNEX)s.qy%(TUNEY)s",
    jobflavour="workday"
    run_local=False
    resume_jobs=False
    append_jobs=False
    dryrun=False
    num_processes=4
    ```

    and running `python -m pylhc_submitter.job_submitter --entry_cfg config.ini`

??? "my_madx.mask"
    ```
    !############################## Create Soft Links and Directories ################################################################

    option, warn,info;
    system, "mkdir Outputdata";
    system, "ln -fns /afs/cern.ch/eng/lhc/optics/V6.503 db5";
    system, "ln -fns /afs/cern.ch/eng/lhc/optics/SLHCV1.0 slhc";
    system, "ln -fns /afs/cern.ch/eng/lhc/optics/runII/2018 optics2018";
    !option, -echo,warn,-info;

    !############################## Make macros available ############################################################################

    call,file="optics2018/toolkit/macro.madx";

    !############################## Beam Options #####################################################################################

    mylhcbeam=%(BEAM)s; ! Beam to use. HINT: mylhcbeam variable is used in some macros as well!!
    qxinit=%(TUNEX)s;
    qyinit=%(TUNEY)s;
    emittance=7.29767146889e-09;
    Nb_0=1.0e10;   ! number of particles in beam

    !############################## Set up Lattice ###################################################################################

    call,file="optics2018/lhc_as-built.seq"; 

    ! Definine the optics:
    call, file="optics2018/PROTON/opticsfile.1";         ! Basic optics setup (injection optics)
    call, file="optics2018/PROTON/opticsfile.22_ctpps2"; ! Redefine Optics to Round 30cm collision optics

    beam, sequence=lhcb1, bv= 1, energy=NRJ, particle=proton, npart=Nb_0, kbunch=1, ex=emittance,ey=emittance;
    beam, sequence=lhcb2, bv=-1, energy=NRJ, particle=proton, npart=Nb_0, kbunch=1, ex=emittance,ey=emittance;

    !############################## Tune Matching and Output #########################################################################

    use, sequence=lhcb%(BEAM)s;

    match,chrom;
        global, q1=qxinit, q2=qyinit;
        vary,   name=dQx.b%(BEAM)s, step=1.0E-7 ;
        vary,   name=dQy.b%(BEAM)s, step=1.0E-7 ;
        lmdif,  calls=100, tolerance=1.0E-21;
    endmatch;

    select, flag=twiss, clear;
    select, flag=twiss, pattern="BPM", column=name,s,x,y,betx,bety,alfx,alfy,dx,dpx,mux,muy;
    select, flag=twiss, pattern="M",   column=name,s,x,y,betx,bety,alfx,alfy,dx,dpx,mux,muy;
    select, flag=twiss, pattern="IP",  column=name,s,x,y,betx,bety,alfx,alfy,dx,dpx,mux,muy;
    twiss, chrom, file='Outputdata/b%(BEAM)s.twiss.tfs';
    ```

After executing the python script, we can check the status of our jobs via `condor_q` (on the ssh server if not locally setup).
The result should look something like this:

<figure>
    <img src="../../../assets/images/job_submitter/tune_sweep_condor_q.png" width="100%" />
    <figcaption><code>condor_q</code>: Shows the jobs in the condor queue.</figcaption>
</figure>

At the same time, a folder structure has been created in the given `working directory`:

- In the main directory will be the **Job.tfs**, were each row corresponds to instance of parameters filled in and contains infos that.
  - The first column will be `JobId` which is either just a numbering of the jobs, or - in our case - the filled in `jobid_mask`.
  - The next columns are the parameters given, here: `BEAM`, `TUNEX` and `TUNEY`. They contain the value the respective job-instance as filled in.
  - `JobDirectory` contains the path to the job directory, while `JobFile` is the name of the file and `ShellScript` the name of the script within thisdirectory, which are used to run the job.
- The **queuehtc.sub** is the submission file, which tells HTCondor the paths to all the `ShellScripts` to run.
- In the `JobDirectories`, also named according to the `jobid_mask`, there will be some files present already:
  - The `ShellScript` **_Jobid_.sh**, which contains commands to create the `job_output_dir` and the `madx` command to run the script
  - And the `JobFile` which is the original `mask`, parameter values filled in.
All of these files are created before the submit to HTCondor.

After all jobs have finished, `htcondor.___.err`, `htcondor.___.log` and `htcondor.___.out` files for the respective job are transferred to these directories,
containing the printouts of the outputstreams of the job.

And finally, also the `job_output_dir`, here **Outputdata** containing the calculated **.twiss**-file, will be in there as well, ready for post-processing.

### Check for failed jobs

To see if and which Jobs have failed, the same command as above can be rerun, but using `resume_jobs=True` and `dryrun=True`.
<!-- TODO add example script output -->
By default, Jobs are classified as successful if the `job_output_dir`, here **Outputdata**, is present.
To further refine the resubmission, the script can also check for the presence of files in the `job_output_dir` by using the `check_files` flag, which for the above example would look like this `check_files=["*.twiss.tfs"]`.
If the `dryrun` flag is omitted or set to `False`, failed Jobs will be resubmitted to HTCondor.

## Example 2: Run with mask string

Instead of using mask file, the PyLHC submitter can also use a mask string as input for the executable.
This can be used if instead of using a file as input, the executable has a number of variable inputparameters, i.e. `executable --param1 X --param2 Y`.

??? info "Example config file"
    ```
    [DEFAULT]
    executable='expr',
    mask=' %(SUMMAND1)s + %(SUMMAND2)s > Outputdata/result.txt',
    working_directory='/afs/cern.ch/work/u/username/study.addition',
    replace_dict={
        SUMMAND1= [1, 2, 3, 4],
        SUMMAND2= [6, 7, 8, 9],
    },
    run_local=True
    num_processes=4
    ```

Note that again, the user has to take care that the required results are saved in the correct `job_output_dir`.
The `mask` string can be are more complicated multiline string, executing multiple commands.

??? info "Example multiline config file"
    ```
    [DEFAULT]
    executable=None,
    mask='madx < Job%(SEED)s.madx\n
          python -m analysis.main --method %(METHOD)s',
    working_directory='/afs/cern.ch/work/u/username/study.multiline',
    replace_dict={
        SEED= [1, 2, 3, 4],
        METHOD= ['fast', 'slow', 'new'],
    },
    run_local=True
    num_processes=4
    ```

## Pitfalls and Hints

- when using the `ssh` option, the `working directory` needs to be accessible from both, the local machine as well as the ssh-server.
  `ssh` is only used for the final commit command to send the jobs to HTCondor, as this is quite tricky to setup on a local machine.

- the `run_local` option allows to run jobs in parallel on the local machine.
  This is only recommended for short jobs and for a small number of jobs.
  The `num_processes` option allows to specify how many concurrent processes will run (default:4).

[documentation]: https://pylhc.github.io/submitter/entrypoints/submitter.html
