# PyLHC Submitter

[See the docs][documentation] for a detailed code description.
Note that the full functionality is only available under Linux with `HTCondor` configured, e.g. on CERN's `lxplus` service.
Currently, only local job execution is possible in Windows or macOS.

## Description

The PyLHC submitter allows to execute a parametric study using a script-mask and a `dictionary` with parameters to replace, from the command line.
The parameters to be replaced must be present in the given mask as `%(PARAMETER)s` (other types apart from string also allowed).
The type of script and executable is freely choosable, but defaults to `madx` - for which this submitter was originally written.

When submitting to `HTCondor`, data to be transferred back to the working directory must be written in a sub-folder defined by `job_output_directory` which defaults to **Outputdata**.
This script also allows to check if all `HTCondor` jobs finished successfully, for resubmissions with a different parameter grid, and for local execution.

A **Jobs.tfs** file is created in the working directory containing the Job Id, parameter per job and job directory for further post processing.

??? info "Detailed Arguments of the Script"
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

## Various Examples:

In the following examples, we will perform a tune sweep using a `MAD-X` mask.
The simulations will be parametrized for both beams over a range of tunes in each plane.
Parameters in the template script (see below) are indicated in the `%(PARAMETER)s` format. 

??? example "The `my_madx.mask` Template File"
    ```fortran
    ! ----- Create Soft Links and Directories ----- !
    option, warn,info;
    system, "mkdir Outputdata";
    system, "ln -fns /afs/cern.ch/eng/lhc/optics/V6.503 db5";
    system, "ln -fns /afs/cern.ch/eng/lhc/optics/SLHCV1.0 slhc";
    system, "ln -fns /afs/cern.ch/eng/lhc/optics/runII/2018 optics2018";
    !option, -echo,warn,-info;

    ! ----- Make macros available  ----- !
    call,file="optics2018/toolkit/macro.madx";

    ! ----- Beam Options  ----- !
    mylhcbeam=%(BEAM)s; ! Will be replaced by values given to the submitter
    qxinit=%(TUNEX)s; ! Will be replaced by values given to the submitter
    qyinit=%(TUNEY)s; ! Will be replaced by values given to the submitter
    emittance=7.29767146889e-09;
    Nb_0=1.0e10;   ! number of particles in beam

    ! ----- Set up Lattice ----- !
    call,file="optics2018/lhc_as-built.seq"; 

    ! -----  Definine the optics ----- !
    call, file="optics2018/PROTON/opticsfile.1";         ! Basic optics setup (injection optics)
    call, file="optics2018/PROTON/opticsfile.22_ctpps2"; ! Redefine Optics to Round 30cm collision optics

    beam, sequence=lhcb1, bv= 1, energy=NRJ, particle=proton, npart=Nb_0, kbunch=1, ex=emittance,ey=emittance;
    beam, sequence=lhcb2, bv=-1, energy=NRJ, particle=proton, npart=Nb_0, kbunch=1, ex=emittance,ey=emittance;

    ! ----- Tune Matching and Output ----- !
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
    twiss, chrom, file='Outputdata/b%(BEAM)s.twiss.tfs'; ! Will be replaced by values given to the submitter

    ! ----- Cleanup Symlinks ----- !
    system, "unlink db5";
    system, "unlink slhc";
    system, "unlink optics2018";
    ```

### Starting Studies from Python

The parametrizing of simulations and submission to `HTCondor` through Python is as simple as calling the `main` function of the submitter with the desired parameters.
See below:
```python
from pylhc_submitter.job_submitter import main as htcondor_submit
import numpy as np

if __name__ == "__main__":
    htcondor_submit(
        executable="madx",  # points to the latest MAD-X on afs
        mask="my_madx.mask",  # the file to execute MAD-X on
        replace_dict=dict(  # parameters to look for and replace in the file
            BEAM=[1, 2], 
            TUNEX=np.linspace(62.3, 62.32, 11).tolist(), 
            TUNEY=np.linspace(60.31, 60.33, 11).tolist(),
        ),
        jobid_mask="b%(BEAM)d.qx%(TUNEX)s.qy%(TUNEY)s",  # naming of the files
        working_directory="/afs/cern.ch/work/u/username/study.tune_sweep",  # outputs
        jobflavour="workday"
    )
```

### Starting Studies from a Config File

The same can also be achieved by specifying the previously called parameters in a **config.ini** file.
It is worth noting that with any submission, the `job_submitter` will create such a file.
See below the equivalent **config.ini** of the above Python example:
```
[DEFAULT]
executable="madx"
mask="my_madx.mask"
working_directory="/afs/cern.ch/work/u/username/study.tune_sweep"
replace_dict={
    "BEAM"=[1, 2],
    "TUNEX"=[62.3, 62.302, 62.304, 62.306, 62.308, 62.31, 62.312, 62.314, 62.316, 62.318, 62.32],
    "TUNEY"=[60.31, 60.312, 60.314, 60.316, 60.318, 60.32, 60.322, 60.324, 60.326, 60.328, 60.33],
}
jobid_mask="b%(BEAM)d.qx%(TUNEX)s.qy%(TUNEY)s"
jobflavour="workday"
```

The jobs are then started by calling the submitter on this file from the command line:
```bash
python -m pylhc_submitter.job_submitter --entry_cfg config.ini
```

### Starting Studies with Mask Strings

Instead of using mask file, `job_submitter` can also use a mask string as input for the executable.
This can be used if instead of using a file as input, the executable has a number of variable input parameters, i.e. `executable --param1 X --param2 Y`.

A simple mask string call using the **config.ini** input to the pylhc-submitter would look like this:
```
[DEFAULT]
executable="expr"
mask="%(SUMMAND1)s + %(SUMMAND2)s > Outputdata/result.txt"
working_directory="/afs/cern.ch/work/u/username/study.addition"
replace_dict={"SUMMAND1"= [1, 2, 3, 4], "SUMMAND2"= [6, 7, 8, 9]}
run_local=True
num_processes=4
```

Note that again, the user has to take care that the required results are saved in the correct `job_output_dir`.
The `mask` string can be a more complicated multiline string, executing multiple commands.

??? example "Example Multiline Config File"
    ```
    [DEFAULT]
    executable=None
    mask="madx < Job%(SEED)s.madx\n
          python -m analysis.main --method %(METHOD)s"
    working_directory="/afs/cern.ch/work/u/username/study.multiline"
    replace_dict={"SEED"= [1, 2, 3, 4], "METHOD"= ['fast', 'slow', 'new']}
    run_local=True
    num_processes=4
    ```

### Starting Studies from the Command Line

!!! warning "Users Beware!"
    While doing so is possible, using a simple command line call is discouraged.
    As you will see below, this method is much less clear and reproducible.

It is possible to skip the creation of a Python or a **config.ini** file completely when submitting, by providing each parameters as a flag at the command line.
The above examples would be done through a (very lengthy) command line call as below:
```bash
python -m pylhc_submitter.job_submitter --executable madx --mask my_madx.mask --working_directory /afs/cern.ch/work/u/username/study.tune_sweep --replace_dict "{'BEAM': [1, 2], 'TUNEX': [62.3, 62.302, 62.304, 62.306, 62.308, 62.31, 62.312, 62.314, 62.316, 62.318, 62.32], 'TUNEY': [60.31, 60.312, 60.314, 60.316, 60.318, 60.32, 60.322, 60.324, 60.326, 60.328, 60.33]}" --jobid_mask b%(BEAM)d.qx%(TUNEX)s.qy%(TUNEY)s --jobflavour workday
```

## What Happens After Submitting

When submitting, the `job_submitter` will issue several logging statements to keep you updated.
In more details, here is what happens behind the scenes.

A folder structure is created in the given `working directory`, in which one will find:

- A **Job.tfs** file, a global summary dataframe in which each row corresponds to a set of parameters filled in for one submitted job:
    - The first column, `JobId`, is either numbering of the jobs or - in our case - the filled in `jobid_mask`,
    - The next columns are the given parameters, here: `BEAM`, `TUNEX` and `TUNEY`. They contain the value filled in the respective job-instance of said row,
    - The `JobDirectory`, `JobFile` and `ShellScript` columns respectively contain the path to the job directory, the name of the filled mask file and the name of the script which are used to run the job.
- A **queuehtc.sub** file, the `HTCondor` submission file used, which tells `HTCondor` the paths to all the `ShellScripts` to run.
- Many sub-directories named according to the `jobid_mask`, one per job, each with:
    - A `ShellScript` **<Jobid>.sh**, which contains commands to create the `job_output_dir` and the `madx` command to run the script,
    - A `JobFile` which is the original `mask`, parameter values filled in.

All of these files are created submission to `HTCondor`.
In case one runs the submitter with the `dryrun` flag, the execution stops here and files are accessible, but nothing is sent to the `HTCondor` scheduler.

After submitting our tune sweep studies, we can check the status of our jobs via the `condor_q` (on the `ssh` server if not running locally).
The output should look something like this:

<figure>
    <img src="../../../assets/images/job_submitter/tune_sweep_condor_q.png" width="100%" />
    <figcaption><code>condor_q</code>: Shows the jobs in the condor queue.</figcaption>
</figure>

When all jobs are done running, the `htcondor.<jobid>.err`, `htcondor.<jobid>.log` and `htcondor.<jobid>.out` files for the respective job are transferred back to the appropriate directories.
Finally, for each job the `job_output_dir`, here containing the calculated **.twiss.tfs** file, will be transfered back as well, ready for post-processing.

## Checking for Failed Jobs

To see if and which Jobs have failed, the same command as above can be rerun using `resume_jobs` and `dryrun` flags (or use them as parameters set to `False`).
By default, Jobs are classified as successful if the specified `job_output_dir` is present.
<!-- TODO add example script output -->

## Resubmitting Failed Jobs

To resubmit the failed jobs to `HTCondor`, simply rerun the call and omit the `dryrun` flag or set its parameter to `False`.
To further refine the resubmission, the script can also check for the presence of files in the `job_output_dir` by using the `check_files` flag.
In the case of our tune sweep example, this would look like `check_files=["*.twiss.tfs"]`.

## Pitfalls and Hints

- when using the `ssh` option, the `working directory` needs to be accessible from both, the local machine as well as the ssh-server.
  `ssh` is only used for the final commit command to send the jobs to `HTCondor`, as this is quite tricky to setup on a local machine.

- the `run_local` option allows to run jobs in parallel on the local machine.
  This is only recommended for short jobs and for a small number of jobs.
  The `num_processes` option allows to specify how many concurrent processes will run (default:4).

[documentation]: https://pylhc.github.io/submitter/entrypoints/submitter.html
