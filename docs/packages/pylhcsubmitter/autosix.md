# AutoSix
[See the docs][documentation] for a detailed code description.

## Description

A wrapper for SixDesk to perform the setup and steps needed automatically.

The idea is, to call this script with the same parameters and it runs through
all the steps automatically.

The functionality is similar to the `pylhc_submitter.job_submitter` in that
the inner product of a ``replace_dict`` is used to automatically create a set of
job-directories to gather the data.
To avoid conflicts each of these job-directories is a SixDesk workspace,
meaning there will be only one "study" per directory.

The ``replace_dict`` contains variables for your mask as well as variables
for the SixDesk environment. See the description of ``replace_dict`` below.
In any other way, these *special* variables behave like normal variables and
can also be inserted in your mask. They are also looped over in the same manner
as any other variable (if given as a list).

!!! warning
    As the loop over Seeds is handled by SixDesk you need to set
    `FIRSTSEED` and `LASTSEED` to ``None`` or ``0`` to deactivate this loop.
    Otherwise a ``%SEEDRAN`` placeholder is required in your mask,
    which needs to be present **after** filling in the variables (see example below).

!!! note
    Unlike in the `pylhc_submitter.job_submitter`, the output directory of the
    HTCondor job (the 'mask-job') is not automatically transferred to the
    workspace. To have access to this data, you will need to specify different
    output-directories in your mask manually, e.g. using strings containing
    the variable placeholders.

```python
    from pathlib import Path
    from omc3.utils import logging_tools
    from submitter import autosix

    LOG = logging_tools.get_logger(__name__)

    if __name__ == '__main__':
        autosix.main(
            working_directory=Path('/afs/cern.ch/work/u/user/sixdeskbase'),
            mask=Path('my_madx.mask'), # can contain any of the parameters used in replace_dict
            python=Path('/afs/cern.ch/work/u/user/my_venv/bin/python'),
            ignore_twissfail_check=False,  # if script prints 'check if twiss failed' or similar
            replace_dict=dict(
                # Part of the sixdesk-environment:
                TURNS=100000,
                AMPMIN=4, AMPMAX=30, AMPSTEP=2,
                ANGLES=11,
                # Examples for mask:
                BEAM=[1, 4],
                TUNE=[62.29, 62.30, 62.31, 62.31]
                OUTPUT='/afs/cern.ch/work/u/user/study_output/',
                SEED='%SEEDRAN',  # puts '%SEEDRAN' in the mask and lets sixdesk handle this loop
            ),
            jobid_mask="B%(BEAM)d-QX%(TUNE)s",
            # unlock=True,
            # resubmit=True,
            # ssh='lxplus.cern.ch',
        )
```

Upon running the script the job-matrix is created
(see *Jobs.tfs* in working directory) and the following stages are run per job:

- ``create_jobs``: create workspace; fill sysenv, sixdeskenv, mask.
- ``initialize_workspace``: initialize workspace from the env-files.
- ``submit_mask``: submit mask-job to HTCondor. (*interrupt*)
- ``check_input``: check if sixdesk input is complete.
- ``submit_sixtrack``: submit sixdesk-jobs to HTCondor. (*interrupt*)
- ``check_sixtrack_output``: check if all sixdesk jobs are completed.
- ``sixdb_load``: create database and load jobs output.
- ``sixdb_cmd``: calculated DA from database data.
- ``post_process``: extract data from database, write into *.tfs* and plot.
- ``final``: announce everything has finished

To keep track of the stages, they are written into the *stages\_completed.txt*
in the *autosix\_output* directory in the workspaces.
Stages that are written in this file are assumed to be done and will be skipped.
To rerun a stage, delete the stage and all following stages in that file and
start your script anew.

The stages are run independently of each job, meaning different jobs can be
at different stages. E.g. if one job has all data for the ``six_db`` analysis
already, but the others are still running on sixdesk the
``check_sixtrack_output`` stage will fail for these jobs but the other one will
just continue.

Because the stages after ``submit_mask`` and ``submit_sixtrack`` need only be
run after the jobs on HTCondor are completed, these two stages interrupt the
execution of stages if they have successfully finished. Check your scheduler
via ``condor_q`` and run your script again after everything is done, to
have autosix continue its work.

!!! note
    While most studies should be fine with the input options given, there is the
    possibility to manually adapt the *sixdeskenv* and *sysenv* file before
    workspace initialization but adding the switch ``stop_workspace_init``.
    This will not reset automatically and one will have to remove the switch
    again to continue.
    As this is a bit of a workaround, it might be easier to define a new
    variable in the **pylhc_submitter.sixdesk_tools.mask_sixdeskenv** file and put its
    current default into **pylhc_submitter.constants.autosix.SIXENV_DEFAULT**.
    One can then use the ``replace_dict`` to change its value.
    This is left open as a task for the inspired user to implement, as only he
    knows which variable he or she needs to change.

AutoSix is not only able to run MAD-X masks, but also **cpymad** masks.
Requirement for the latter is to provide the ``executable`` path to a
python binary with **cpymad**, and all other packages used, installed.

To create the files needed for Sixtrack input, MAD-X masks need to contain

```bash
    if (NRJ<5000.0000) {VRF400:=8.;} else {VRF400:=16.;};
    LAGRF400.B1=0.5;
    LAGRF400.B2=0.;
    twiss;
    sixtrack, cavall, radius=0.017;
```

while **cpymad** masks can do the same task with

```python
    madx.globals["VRF400"] = 8 if madx.globals['NRJ'] < 5000 else 16
    madx.globals["LAGRF400.B1"] = 0.5
    madx.globals["LAGRF400.B2"] = 0.
    madx.twiss()  # used by sixtrack
    madx.sixtrack(cavall=True, radius=0.017)
```

In theory, any kind of mask is possible, given the correct ``executable``
is provided and the Sixtrack outputfiles created.

!!! note
    For the creation of polar plots, the function
    `pylhc_submitter.sixdesk_tools.post_process_da.plot_polar` is available,
    which is used for the basic polar plotting in the ``post_process`` stage,
    but provides more customization features if called manually.

Arguments:

*--Required--*

- **mask** *(PathOrStr)*:

    Program mask to use

- **replace_dict** *(DictAsString)*:

    Dict with keys of the strings to be replaced in the mask (required) as
    well as the mask_sixdeskenv and mask_sysenv files in the sixdesk_tools
    module. Required fields are TURNS, AMPMIN, AMPMAX, AMPSTEP,
    ANGLES. Optional fields are RESUBMISSION, PLATFORM, LOGLEVEL,
    FIRSTSEED, LASTSEED, ENERGY, NPAIRS, EMITTANCE, DIMENSIONS, WRITEBINS.
    These keys can also be used in the mask if needed. The values of this
    dict are lists of values to replace these or single entries.

- **working_directory** *(PathOrStr)*:

    Directory where data should be put

*--Optional--*

- **da_turnstep** *(int)*:

    Step between turns used in DA-vs-Turns plot.
    default: ``100``

- **executable** *(PathOrStr)*:

    Path to executable.
    default: ``/afs/cern.ch/user/m/mad/bin/madx``

- **apply_mad6t_hacks**:

    Apply two hacks: Removes '<' in binary call and
    ignore the check for 'Twiss fail' in the submission file.
    This hack is needed in case this check greps the wrong lines,
    e.g. in madx- comments. USE WITH CARE!!
    action: ``store_true``

- **jobid_mask** *(str)*:

    Mask to name jobs from replace_dict

- **python3** *(PathOrStr)*:

    Path to python to use with sixdb (python3 with requirements
    installed).
    default: ``python3``

- **python2** *(PathOrStr)*:

    Path to python to use with run_six.sh (python2 with requirements installed).
    ONLY THE PATH TO THE DIRECTORY OF THE `python` BINARY IS NEEDED!
    And it can't be an Anaconda Distribution.
    default: None (uses the first `python` in path)

- **resubmit**:

    Resubmits if needed.
    action: ``store_true``

- **ssh** *(str)*:

    Run htcondor from this machine via ssh (needs access to the
    `working_directory`)

- **stop_workspace_init**:

    Stops the workspace creation before initialization, so one can make
    manual changes.
    action: ``store_true``

- **unlock**:

    Forces unlocking of folders.
    action: ``store_true``

## Pitfalls and Hints

[documentation]: https://pylhc.github.io/submitter/entrypoints/submitter.html
