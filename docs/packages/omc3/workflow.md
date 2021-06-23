# OMC3 Software Workflow

## The OMC3 Analysis Workflow

A typical workflow with `omc3` consists in performing analysis of measurement or simulation files, and eventually calculating corrections to apply.
While `omc3` provides python modules to handle the different aspects of these tasks, it also provides entrypoint scripts to be called from the commandline.

The first step in the workflow consists in a harmonic frequency analysis performed with the `harpy` module, while the second one is an optics analysis performed with the `measure_optics` module.
The table below shows a general analysis workflow from BPM turn-by-turn measurements or simulation file to results, as well as the corresponding files at each step:

| Workflow & Files       |                        |                        |                        |                                   |
| :--------------------- | :--------------------: | :--------------------: | :--------------------: | --------------------------------: |
| Turn-by-Turn BPM Data  | :material-arrow-right: | Frequency Spectra      | :material-arrow-right: | Various Lattice Optics Parameters |
| SDDS files:  `*.sdds`  | :material-arrow-right: | TFS files: `*.lin[xy]` | :material-arrow-right: | TFS files: `*.tfs`                |

In this page, we will go through the essential steps in preparing and performing an analysis, by going from start to finish with a simple example.

!!! example  ""
    For our example, we will start from data obtained in `MAD-X` with the `TRACK` command for the LHC machine with a scenario adapted from the 2018 machine configurations.
    Changes from the nominal scenario in your simulation could be including errors tables, orbit bumps, speculative magnet errors, additional elements etc.
    It is also easy for the reader to follow along if starting from measurements files.

## Preparing Data for Analysis

Analysis in `omc3` is mostly done from measurement data, which has to be given in the LHC's [SDDS][sdds] binary format.
If your starting point is one or more measurement files in `SDDS` format from a similar machine, then you are set.
However, if your data is in another format you will need to first convert it to `SDDS`.

For this `omc3` provides the `tbt_converter` entrypoint script.
A typical use consists in specifying the location of your turn-by-turn measurement files, the data type of said files and the location in which to write the converted `SDDS` data.
The formats supported by the converter are:

- Machine formats: `lhc`, `iota` and `esrf`, or any machine using one of these.
- Simulation formats: the `trackone` and `ptc` formats from tracking data from `MAD-X` or `PTC`.

??? info "The `trackone` and `ptc` formats"
    What is referred to here as the `trackone` or `ptc` format is obtained by giving the `DUMP` and `ONETABLE` options to the `TRACK` or `PTC_TRACK` commands (respectively) in `MAD-X`.
    This way, all tracking data is written to a single file on disk, which you can feed to the `tbt_converter`.
    Remembering which tracking module was used is important as `PTC_TRACK` does not write in the same format as `MAD-X`'s `TRACK`.

For our example, let us say that when setting up tracking we have asked `MAD-X` to output the data into a file called `trackone` (this is actually the defaults name).
Using the converter to make a compatible `SDDS` file then goes as:
```bash
python -m omc3.tbt_converter \
    --files trackone \
    --tbt_datatype trackone \
    --outputdir .
```

Other actions are supported, such as adding noise to the data or averaging across particles.
To use them, refer to the [converter's API documentation][tbt_converter].

The converter will create new files with the `.sdds` suffix appended to the original filename.
In our case, a `trackone.sdds` file will be created.

## Frequency Analysis

Once measurement or simulation is in the appropriate format, the first step as seen in the table above consists in a harmonic analysis of the data.
To do so, `omc3` provides the `hole_in_one` entrypoint script, which will perform harmonic analysis of the data when provided with the `--harpy` flag.

The script provides options involved in both data cleaning and parameter tweaking for the harmonic analysis, which is useful when you have relevant information about your measurements. 
To use these, refer to the `Harpy Kwargs` in the [hole_in_one API documentation][hole_in_one_harpy].

In our example we will leave these to their default values to keep the analysis simple, and that `harpy` outputs all the computed results.
Running the frequency analysis then goes as:
```bash
python -m omc3.hole_in_one --harpy \
    --files trackone.sdds \
    --tbt_datatype lhc \
    --turns 0 1023 \
    --autotunes transverse \
    --to_write lin spectra full_spectra bpm_summary \
    --outputdir harpy_output
```

In the output directory, `harpy` will create TFS files with the results of the analysis for both BPMs good and identified bad BPMs.
The filenames are determined by appending the appropriate suffixes to the entry files.

!!! info "Bad BPMs"
    BPMs are determined as bad or not depending on several options from the cleaning phase.
    While these are given sensible defaults, one might need to tweak them manually depending on their measurement. 
    Additionally, known bad BPMs can be given with the `--bad_bpms` flag.

In the ooutput files, various properties are given in column form for each observation point.
Running `ls harpy_output/` yields the following result:
```bash
trackone.sdds.ampsx		    trackone.sdds.freqsx
trackone.sdds.ampsy		    trackone.sdds.freqsy
trackone.sdds.bad_bpms_x	trackone.sdds.linx
trackone.sdds.bad_bpms_y	trackone.sdds.liny
```

??? question "Column Nomenclature"
    TODO: add a reference with the meaning of each column.

## Creating a Model

In order to perform the optics analysis, one needs a model of the given machine to compare to.
For this, `omc3` provides the `model_creator` entrypoint script, which allows you to run a model simulation of the desired machine and output the needed files.

??? example "Supported Machines"
    The supported machines for model creation are `lhc`, `ps`, `esrf`, `psbooster`, `skekb`, `JPARC`, `petra` and `iota`.
    It is possible to extend this list by defining an `Accelerator` class and a model creator for your machine.
    See [this guide][new_machine_guide] for implementation steps.

In our example, we would like to compare our data to the nominal model of the 2018 LHC. 
Using the script to create a nominal model of the 2018 LHCB1, with the machine configuration defined in `opticsfile.22`, goes as:
```bash
python -m omc3.model_creator.py \
    --accel lhc \
    --type nominal \
    --year 2018 \
    --beam 1 \
    --nat_tunes 62.31 60.32 \
    --modifiers opticsfile.22 \
    --outputdir lhc_model
```

Some of these options belong to the `model_creator` itself, while others depend explicitely on the chosen machine, here the LHC.
Refer to the [model creator's API documentation][model_creator] for the list of options.

The model creation runs a `MAD-X` scenario and outputs the relevant twiss results to the desired directory.
Running `ls lhc_model/` yields:
```bash
macros			twiss.dat		twiss_elements.dat
```

## Optics Analysis

TODO: write this section.

!!! tip "Hole in One"
    The harmonic analysis and optics analysis don't necessarily have to be seperated steps.
    It is possible to run the `hole_in_one` entrypoint with both `--harpy` and `--optics` flags, even though the command might become cumbersome.
    The associated flags and options do not change.

[sdds]: https://ops.aps.anl.gov/SDDSIntroTalk/slides.html
[tbt_converter]: https://pylhc.github.io/omc3/entrypoints/other.html#tbt-converter
[hole_in_one_harpy]: https://pylhc.github.io/omc3/entrypoints/analysis.html#omc3.hole_in_one.hole_in_one_entrypoint
[new_machine_guide]: know_how.md#how-to-create-files-for-your-file-accelerator
[model_creator]: https://pylhc.github.io/omc3/entrypoints/other.html#model-creator