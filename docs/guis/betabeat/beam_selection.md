# The Beam Selection Window

<figure>
  <center>
  <img src="../../assets/images/betabeat_gui/beam_selection.png" width="100%" alt="The beam selection window" />
  <figcaption>The Beam Selection Window.</figcaption>
  </center>
</figure>

The Beam Selection Window is your entry point to the GUI.
Here, you set which machine you will be using and which `python` backend to run.
The options chosen here will also define the **folder-structure** you will be using during your current analysis session.

!!! tip "Setting Your Defaults"
    You can set all entries in this window to your preferred defaults for a quick start!
    Check the [Defaults Page](defaults.md) for more details.

## Beam

In this field you can choose from the implemented Beams of the LHC or machines in general.
Use the `generic` accelerator, if your machine does not have its own accelerator class.

The beam you choose not only determines some of the **default settings**, which can be overwritten by user [defaults](defaults.md)
or changed later on, but also the **folder-structure** of the GUI, which cannot be changed without restarting the GUI.

## Output

In this field you can set the output folder for the GUI.
Depending on your choice of `Beam` a default is already preselected for you.

!!! warning "Write Access"
    The GUI needs to be able to write to the selected folder.
    If you do not have write access to the folder, you will get a warning and cannot continue to start the GUI.

#### Special Entries

- _LHC-Betabeat_: `/user/slops/data/LHC_DATA/OP_DATA/Betabeat/`
- _Other_: Lets you choose your own path, starting from your default (usually `home`) folder for file dialogs.
- _Other (Last Selected)_: Lets you choose your own path, starting from the last selected folder in this dropdown.
- _Other (Accel)_: Lets you choose your own path, starting from default of the selected beam/accelerator.

#### Folder Structure

Within your selected output folder, a new folder for the current date will be created.
Withing that folder, a folder for the selected beam/accelerator will be created.
Within that folder in turn, folders for `Measurements`, `Results` and `Models` will be created.
If any of these folders already exist, they will be used, e.g.:

```text
LHC-Betabeat
└── YYYY-MM-DD
    ├── LHCB1
    │   ├── Measurements
    │   ├── Results
    │   └── Models
    └── LHCB2
        ├── Measurements
        ├── Results
        └── Models
```

!!! info "Continue Analysis"
    If this structure has already been created, you can also choose the Date-folder directly and continue your analysis.
    No new date-subfolder will be created in that case.
    The selected folder does not even need to be of date-format, as long as the substructre for the selected beam/accelerator exists.<br><br>
    This is useful, if you want to continue a previously started analysis on a different date, e.g. if the GUI crashes after midnight.<br>
    **:fontawesome-solid-triangle-exclamation:{.warning-colored} To later be able to find data belonging together easily, you should always use the same date folder per CCC measurement session!**

### Load Data

If this tickbox is activated and you select a folder, which contains either already the current date or the substructure for the selected beam/accelerator,
the GUI will load the analysis and results data from that folder.
Turn-by-Turn data is skipped to avoid memory issues.

This feature is very useful, when continuing a previously started analysis,
yet deactivated by default as reloading the data can **take a lot of time and memory**.

### Old Structure

!!! warning "Deprecated"
    The old structure had been used with the old Betabeat GUI until 2020 and is now deprecated.
    There is no real reason to ever use it today, in particular with the `omc3` backend,
    as the GUI does not even import the old `BetaBeat.src` data automatically in that case.

If this tickbox is activated, the GUI will use the old folder structure, i.e. the `Models` folder will be as `models` at the top level,
containing in turn again beam/accelerator folders which then contain the models.

```text
LHC-Betabeat
└── YYYY-MM-DD
    ├── LHCB1
    │   ├── Measurements
    │   └── Results
    ├── LHCB2
    │   ├── Measurements
    │   └── Results
    └── models
        ├── LHCB1
        │   ├── b1_inj
        │   └── b1_30cm
        └── LHCB2
            ├── b2_inj
            └── b2_30cm
```

## Input

This field lets you choose the default input folder for the GUI,
meaning that file dialogs will usually start from that folder.

!!! warning "Read Access"
    The GUI needs to be able to read from the selected folder.
    If you do not have read access to the folder, you will get a warning and cannot continue to start the GUI.

Special Entries:

- _LHC-Fill Latest_: `/user/slops/data/LHC_DATA/OP_DATA/Fill_DATA/FILL_DIR/BPM/`, where `FILL_DIR` is a symlink pointing to the latest fill directory.
- _LHC-Fill_: `/user/slops/data/LHC_DATA/OP_DATA/Fill_DATA/`
- _(Same as Output)_: Uses the same path as selected in the `Output` field.
- _Other_: Lets you choose your own path, starting from your default (usually `home`) folder for file dialogs.
- _Other (Last Selected)_: Lets you choose your own path, starting from the last selected folder in this dropdown.
- _Other (Accel)_: Lets you choose your own path, starting from default of the selected beam/acceelerator.

## Python Executable

In this field you can choose the `python` binary you want to use for the GUI.
By default this is our production `python3` binary on `lintrack` (`/afs/cern.ch/eng/sl/lintrack/omc_python3/bin/python`),
but you can also choose other versions from `lintrack` (all in `/afs/cern.ch/eng/sl/lintrack/omc_acc_py/envs/` are automatically picked up)
or choose your own environment (e.g. `.venv/bin/python`).

!!! note "Settings"
    You can change this environment at any time later on the the [Settings](settings.md).

!!! warning "omc3 installation"
    The environment needs to have `omc3` installed as a package,
    i.e. be able to call `python -m omc3.module arg1 arg2 ...`.<br>

    This can be done by running

    ```bash
    python -m pip install omc3
    ```
    or

    ```bash
    python -m pip install git+https://github.com/pylhc/omc3.git
    ```

    See [omc3 on github][omc3_github]{target=_blank}.

[omc3_github]: https://github.com/pylhc/omc3
