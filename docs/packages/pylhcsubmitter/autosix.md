# AutoSix

[See the API documentation][documentation] for a detailed description of the code and the different parameters.

## Using AutoSix

??? tip "Recommended Reading"
    It is recommended to have read the section about the [job submitter](job_submitter.md) before this one, as these share many similarities and details are explained in the previous page.

The parametrizing of simulations and submission can be done very similarly to `job_submitter` through Python, also by calling the `main` function of `autosix` with the desired parameters.

!!! warning "SixTrack SEEDS"
    As the loop over seeds is handled by `SixDesk`, you need to set `FIRSTSEED` and `LASTSEED` to ``None`` or ``0`` to deactivate this loop.
    Otherwise, a ``%SEEDRAN`` placeholder is required in your mask, which needs to be present **after** filling in the variables (see example below).

!!! hint "Output Directories"
    Unlike with `job_submitter`, the output directory of the `HTCondor` job is not automatically transferred to the workspace.
    To have access to this data, you will need to specify different output directories in your mask manually, e.g. using strings containing the variable placeholders.

```python
from pathlib import Path
from pylhc_submitter import autosix

if __name__ == "__main__":
    autosix.main(
        working_directory=Path("/afs/cern.ch/work/u/user/sixdeskbase"),
        mask=Path("my_madx.mask"),  # contains parameters used in replace_dict
        python=Path("/afs/cern.ch/work/u/user/my_venv/bin/python"),
        ignore_twissfail_check=False,  # if script prints 'check if twiss failed' or so
        replace_dict=dict(
            # Part of the sixdesk-environment:
            TURNS=100_000,
            AMPMIN=4,
            AMPMAX=30,
            AMPSTEP=2,
            ANGLES=11,
            # Examples for mask:
            BEAM=[1, 4],
            TUNE=[62.29, 62.30, 62.31, 62.31],
            OUTPUT="/afs/cern.ch/work/u/user/study_output/",
            SEED="%SEEDRAN",  # put '%SEEDRAN' in the mask & let sixdesk handle this loop
        ),
        jobid_mask="B%(BEAM)d-QX%(TUNE)s",
        # unlock=True,
        # resubmit=True,
        # ssh='lxplus.cern.ch',
    )
```

AutoSix is not only able to run MAD-X masks, but also Python scripts using `cpymad`.
Requirement for the latter is to provide the as `executable` the path to a Python binary with `cpymad` and all relevant packages installed in the appropriate environment.
In theory, any kind of mask is possible, given the correct `executable` is provided and the `Sixtrack` output files created.

!!! info "Necessary Input Files"
    To create the files needed for `Sixtrack` input in (HL-)LHC simulations, MAD-X masks need to contain:
    ```fortran
    if (NRJ<5000.0000) {VRF400:=8.;} else {VRF400:=16.;};
    LAGRF400.B1=0.5;
    LAGRF400.B2=0.;
    twiss;
    sixtrack, cavall, radius=0.017;
    ```

    Python masks using `cpymad` can do the same task with:
    ```python
    from cpymad.madx import Madx
    madx = Madx()
    # setup your study
    madx.globals["VRF400"] = 8 if madx.globals["NRJ"] < 5000 else 16
    madx.globals["LAGRF400.B1"] = 0.5
    madx.globals["LAGRF400.B2"] = 0.
    madx.twiss()  # used by sixtrack
    madx.command.sixtrack(cavall=True, radius=0.017)
    ```

## What Happens After Submitting

Upon running the script, the **Jobs.tfs** file is created similarly to `job_submitter`, and the following stages are run per job:

1. `create_jobs`: create workspace, fill sysenv, sixdeskenv and mask.
2. `initialize_workspace`: initialize workspace from the env-files.
3. `submit_mask`: submit job to `HTCondor` from filled mask. (*interrupt*)
4. `check_input`: check if sixdesk input is complete.
5. `submit_sixtrack`: submit sixdesk jobs to `HTCondor`. (*interrupt*)
6. `check_sixtrack_output`: check if all sixdesk jobs are completed.
7. `sixdb_load`: create database and load jobs output.
8. `sixdb_cmd`: calculate DA from database data.
9. `post_process`: extract data from database, write into **.tfs** files and plot.
10. `final`: announce every stage has completed.

To keep track of the stages, they are written into a **stages\_completed.txt** file in the `autosix\_output` directory in the workspaces.
Stages that are written in this file are assumed to be done and will be skipped.
To rerun a stage, delete its entry and that of all following stages in the **stages\_completed.txt** file and start your run anew.

??? info "Execution Order"
    The stages are ran independently of each job, meaning different jobs can be at different stages.
    For instance, if one job has all data for the `six_db` analysis already, but the others are still running on `Sixdesk`, the `check_sixtrack_output` stage will fail for these jobs but continue for the job that is ready.

Because the stages after `submit_mask` and `submit_sixtrack` need only be ran after the jobs on `HTCondor` are completed, they will interrupt execution if previous stages have successfully finished.
To have `AutoSix` continue its work, check your scheduler via `condor_q` and run your script again after everything is done.
It will pick up where it left as written in the **stages\_completed.txt** file.

!!! tip "Custom sixdesk envs"
    While most studies should be fine with the input options given, there is the possibility to manually adapt the **sixdeskenv** and **sysenv** files before workspace initialization by using the `stop_workspace_init` flag.
    This will not reset automatically and one will have to remove the switch again to continue.

??? example "Polar Plots"
    For the creation of polar plots, the function `pylhc_submitter.sixdesk_tools.post_process_da.plot_polar` is available.
    It is used for the basic polar plotting in the `post_process` stage, but provides more customization features if called manually.
    Details on its use can be found at the `PyLHC Submitter` API documentation.

[documentation]: https://pylhc.github.io/submitter/entrypoints/submitter.html#autosix
