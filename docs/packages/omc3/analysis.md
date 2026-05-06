# OMC3 Optics Analysis Workflow

This page contains a walk-through of a typical but simple analysis workflow with the `omc3` package.
To follow along, the reader needs to [have installed](getting_started.md) the package and to have measurement or simulation data to use the codes on.
In case the reader does not have appropriate data to follow along with, an old `MAD-X` script is provided below to create some.

!!! info "Using omc3 at the Command Line"
    Please note that using `omc3` via the command line can be tricky and is discouraged, especially to newcomers.
    Regular users typically use the codes via the [Beta-Beat GUI](../../guis/betabeat/gui.md) which provides an graphical interface to `omc3` functionality, and more.
    This quick walkthrough sticks to the command line for illustration purposes.

## The Analysis Workflow

A typical workflow with `omc3` consists in performing analysis of measurement or simulation files, and eventually calculating corrections to apply.
While `omc3` provides python modules to handle the different aspects of these tasks, it also provides entrypoint scripts to be called from the commandline.

The first step in the workflow consists in a harmonic frequency analysis performed with the `harpy` module, while the second one is an optics analysis performed with the `measure_optics` module.
The table below shows a general analysis workflow from BPM turn-by-turn measurements or simulation file to results, as well as the corresponding files at each step.
Output files are written in the [TFS format][tfs_format]{target=_blank}.

| Workflow & Files      |                        |                        |                        |                                   |
| :-------------------- | :--------------------: | :--------------------: | :--------------------: | --------------------------------: |
| Turn-by-Turn BPM Data | :material-arrow-right: |   Frequency Spectra    | :material-arrow-right: | Various Lattice Optics Parameters |
| SDDS files:  `*.sdds` | :material-arrow-right: | TFS files: `*.lin[xy]` | :material-arrow-right: |                TFS files: `*.tfs` |

In this page, we will go through the essential steps in preparing and performing an analysis, by going from start to finish with a simple example.
We will cover the use of the different entrypoints available to perform necessary steps.

!!! example "Generating the Example Data"
    For our example, we will start from data obtained with `MAD-X`, tracking a particle 1023 turns in the LHC beam 1, with a scenario adapted from the 2018 configuration.
    A self-contained `MAD-X` simulation to generate tracking data in a file named `trackone` is available publicly in our [MESS][mess_example]{target=_blank} repository.
    We recommend cloning the repo or downloading the files in this folder then running `madx` on the `job.madx` file.

    Changes from the nominal scenario in your simulation could be including errors tables, orbit bumps, speculative magnet errors, additional elements etc.
    It is also easy for the reader to follow along if starting from measurements files.

## Preparing Data for Analysis

Analysis in `omc3` is mostly done from measurement data, but can also be done on simulated tracking data.
While `omc3` codes can read data from many machine formats, we will for demonstration purposes first convert our data to the LHC's [SDDS][sdds] binary format.

For this `omc3` provides the `tbt_converter` entrypoint.
A typical use consists in specifying the location of your turn-by-turn measurement files, the data type of said files and the location in which to write the converted `SDDS` data.
All formats handled by our [turn-by-turn][tbt_doc]{target=_blank} package are supported.

??? info "The `trackone` and `ptc` formats"
    What is referred to here as the `trackone` or `ptc` format is obtained by giving the `DUMP` and `ONETABLE` options to the `TRACK` or `PTC_TRACK` commands, respectively, in `MAD-X`.
    This way, all tracking data is written to a single file on disk, which you can feed to the `tbt_converter`.
    Remembering which tracking module was used is important as `PTC_TRACK` does not write in the same format as `MAD-X`'s `TRACK`.

For our example, let us say that when setting up tracking we have asked `MAD-X` to output the data into a file called `trackone` (this is actually the default name).
Using the converter to make a compatible `SDDS` file then goes as:

```bash
python -m omc3.tbt_converter \
    --files trackone \
    --tbt_datatype trackone \
    --drop_elements LHCB1MSIA.EXIT.B1_P_ \
    --outputdir .
```

!!! info
    When tracking in `MAD-X`, by default the start of machine will be included in the list of observation points.
    As we do not want this arbitrary point, we indicate to the `tbt_converter` we intend to drop it with the `--drop_elements` flag.
    More than one element can be given to this flag.

The converter will create new files with the `.sdds` suffix appended to the original filename.
In our case, a `trackone.sdds` file will be created.

!!! tip "Other Uses"
    The `tbt_converter` provides additional functionality such as adding noise to the provided data or averaging across particles.
    To use these options, refer to the [converter's API documentation][tbt_converter].

## Creating a Model

In order to perform the optics analysis, one needs a model of the given machine to compare to.
For this, `omc3` provides the `model_creator` entrypoint, which allows you to run a model simulation of the desired machine and output the needed files.

??? example "Supported Machines"
    The out-of-the-box supported machines for model creation are `lhc`, `ps` and `psbooster`, machines we work on.
    While the `skekb`, `JPARC`, `petra` and `iota` have accelerator classes, no model creator has been implemented for them yet.
    It is possible to extend this list for your machine by defining an appropriate `Accelerator` class as well as a model creator.

In our example, we would like to compare our data to the nominal model of the 2018 LHC.
Using the script to create a nominal model of the 2018 LHCB1, with the machine configuration and opticsfile used in our example, goes as:

```bash
python -m omc3.model_creator \
    --accel lhc \
    --type nominal \
    --year 2018 \
    --beam 1 \
    --energy 6.5 \
    --nat_tunes 62.31 60.32 \
    --modifiers opticsfile.22 \
    --outputdir lhc_model
```

Some of these options belong to the `model_creator` itself, while others depend explicitly on the chosen machine, here the LHC.
Refer to the [model creator's API documentation][model_creator]{target=_blank} for the list of options.

The model creation runs a `MAD-X` scenario and outputs the relevant twiss results to the desired directory.
Running `ls lhc_model/` yields:

```bash
b2_errors.tfs    error_deffs.txt       macros    twiss_elements.dat
b2_settings.madx job.create_model.madx twiss.dat
```

!!! question "What is a Model?"
    As one can see, a "model" is essentially one or more TFS files with optics functions at BPMs (`twiss.dat`) and elements (`twiss_elements.dat`), other files being here for the user to understand or reproduce the result.
    Had we created a driven model (with beam excitation), then an additional `twiss_ac.dat` or `twiss_adt.dat` file would have been created, with optics functions at BPMs while exciting the beam.
    One can create their own models without the `model_creator` should they want to, as it only acts as a convenience wrapper.

    A `driven model` is the same as above, with also a `TWISS` taking into account the exciting effect of an AC dipole or ADT onto the optics.
    Creating this is easiest done with the `model_creator`, but can also be done individually with the a script installing the appropriate element into your sequence.
    See for instance [this setup][mess_acd_twiss]{target=_blank} which provides a `TWISS` with the effect of an AC Dipole.

## Frequency Analysis

Once measurement or simulation is in the appropriate format, the first step as seen in the table above consists in a harmonic analysis of the data.
To do so, `omc3` provides the `hole_in_one` entrypoint, which will perform frequency analysis of the data when provided with the `--harpy` flag.

The script provides options involved in both data cleaning and parameter tweaking for the harmonic analysis, which is useful when you have relevant information about your measurements.
To use these, refer to the `Harpy Kwargs` section of the [hole_in_one API documentation][hole_in_one]{target=_blank}.

In our example we will leave most of these to their default values to keep the analysis simple, but ask from `harpy` to output all computed results.
We will input `lhc` for the `--tbt_datatype` flag, but if you skipped the use of the `tbt_converter` you should input the type of your machine there.
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

??? warning "Memory Requirements"
    During frequency analysis, `harpy` makes use of zero padding (with by default $2^{20}$ zeros) to improve the accuracy of results.
    In turn, the padded arrays become consequent and, coupled with a high number of observation points, processing will require a substantial amount of RAM - well into the few GBs range for our example.

    When running on limited hardware, one can change the amount of zero padding with the `--turn_bits` flag for `harpy`.
    It is important however to remember that decreasing this number will reduce the accuracy of the results, since it increases the range between detected frequencies.
    Refer to the [hole_in_one API documentation][hole_in_one]{target=_blank} for details that could help in determining which number to use.

In the output directory, `harpy` will create TFS files with the results of the analysis for both good BPMs and identified bad BPMs.
The filenames are determined by appending the appropriate suffixes to the entry files.

!!! info "Bad BPMs"
    If given `bpm_summary` for the `--to_write` flag (which is the case by default), `harpy` will output the `.bad_bpms_[xy]` files.
    BPMs are determined as bad or not depending on several options from the cleaning phase.
    While these are given sensible defaults, one might need to tweak them manually depending on their measurement.
    Additionally, any known bad BPMs can be provided with the `--bad_bpms` flag.

In the output files, various properties are given in column form for each observation point.
Running `ls harpy_output/` yields the following result:

```bash
trackone.sdds.ampsx      trackone.sdds.freqsx
trackone.sdds.ampsy      trackone.sdds.freqsy
trackone.sdds.bad_bpms_x trackone.sdds.linx
trackone.sdds.bad_bpms_y trackone.sdds.liny
```

!!! tip "Plotting the Spectra"
    The `omc3` package provides scripts and modules to quickly plot the spectra obtained from frequency analysis.
    To use these, refer to the [Plot Spectrum][plot_spectrum]{target=_blank} API documentation.

??? question "Column Nomenclature"
    The `*.amps[xy]`, `*.freqs[xy]` and `*.lin[xy]` files in the harmonic analysis output are [TFS files][tfs_format]{target=_blank}.

    The `*.freqs[xy]` files contain for each BPM in column format the frequencies of the resonance lines detected in the spectrum, for respectively the horizontal (`.freqsx`) and vertical (`.freqsy`) planes while the `*.amps[xy]` files contain the amplitudes of said resonance lines.
    This means in the column of a given BPM, the `nth` row in the `.amps[xy]` file corresponds to the amplitude of the resonance line located at the frequency given by the `nth` row in the column of the same name in the `.freqs[xy]` file.
    For illustration purposes, *simplistic plotting* of the horizontal spectrum (without the spectrum plotter mentioned above) from these files would go as:
    ```python
    import tfs
    import matplotlib.pyplot as plt

    ampsx = tfs.read("harpy_output/trackone.sdds.ampsx")
    freqsx = tfs.read("harpy_output/trackone.sdds.freqsx")

    for bpm in ampsx.columns:
        if bpm in freqsx.columns:  # safety check but no reason it wouldn't be there
            plt.plot(freqsx[bpm], ampsx[bpm], ".-")
            # plt.stem(freqsx[bpm], ampsx[bpm])  # would be more accurate but might stress your system!

    plt.setp(plt.gca(), xlabel=r"$Q_x$", ylabel="Amplitude", title="Horizontal Spectrum", xlim=(0, 0.5))
    plt.show()
    ```

    The `*.lin[xy]` files contain various data (in columns) computed for each BPM (in rows) as some summary information.
    Some column names are explicit: `BPM_RES` contains the determined BPM resolution, `CO` the closed orbit value at said BPM and `PK2PK` is the peak-to-peak value of oscillations registered by the given BPM.
    `TUNE[XY]`, `AMP[XY]` and `MU[XY]` are the detected tune, the amplitude of the tune line and the phase of the tune line for said BPM, respectively.

    The other columns describe the phase (`PHASE`), amplitude ratio (`AMP`) and frequency (`FREQ`) of the line identified by the number in the column name, where underscores represent a minus sign.
    Therefore, in the `.linx` file `FREQ01`, `AMP01` and `PHASE01` are respectively the frequency of the main vertical tune line in the horizontal spectrum, the ratio of this line's amplitude to that of the main horizontal line and the phase of this line.
    The equivalent columns in the `.liny` file are `FREQ10`, `AMP10` and `PHASE10`.

    Generally speaking, the frequency and amplitude of higher order lines is calculated using $m \cdot Q_x + n \cdot Q_y$  so `FREQ1_3` corresponds to $m = 1$ and $n = -3$ which is a decapolar line ($|m| + |n| = 4)$.
    For more information, [this paper on normal forms][normal_forms]{target=_blank} is a good resource.

## Optics Analysis

Once harmonic analysis has been performed, one can move on to the reconstruction of optics quantities from computed spectra and phases.
To do so, `omc3` provides the `hole_in_one` entrypoint, to be used this time with the `--optics` flag.

In our example we will ask to use the `three_bpm_method` when reconstructing beta functions from phase advances, as the default `n_bpm_method` (which is more accurate) requires providing a systematic errors definition file which our simulation does not provide (see the [analytical n-bpm paper][analytical_nbpm]{target=_blank}).
Calling the entrypoint to perform optics analysis goes as:

```bash
python -m omc3.hole_in_one --optics \
    --accel lhc \
    --year 2018 \
    --beam 1 \
    --energy 6.5 \
    --files harpy_output/trackone.sdds \
    --model_dir lhc_model \
    --compensation none \
    --three_bpm_method \
    --outputdir measured_optics
```

!!! warning "Input Files"
    While `harpy` outputs various types of files with different suffixes, the optics analysis only looks for some of them.
    Thus, when providing the `--files` flag, no specific files should be provided, and instead the path to `harpy` outputs **without a suffix** should be given.
    In our example, this means entering `harpy_output/trackone.sdds`.

Like other entrypoints, the optics analysis provides many options on methods to use and quantities to compute.
To use these, refer to the `Optics Kwargs` section of the [hole_in_one API documentation][hole_in_one]{target=_blank}.

In the output files, various properties are given in column form for each observation point.
Running `ls measured_optics/` yields the following result:

```bash
beta_amplitude_x.tfs      kick_x.tfs           phase_y.tfs
beta_amplitude_y.tfs      kick_y.tfs           special_phase_x.tfs
beta_phase_x.tfs          measure_optics.log   special_phase_y.tfs
beta_phase_y.tfs          orbit_x.tfs          total_phase_x.tfs
interaction_point_x.tfs   orbit_y.tfs          total_phase_y.tfs
interaction_point_y.tfs   phase_x.tfs
```

---

!!! tip "Hole in One"
    The harmonic analysis and optics analysis don't necessarily have to be separated steps.
    It is possible to run the `hole_in_one` entrypoint with both `--harpy` and `--optics` flags, even though the command might become cumbersome.
    The associated flags and options do not change, although only one `outputdir` should be given.

    Our example done in one step would be:
    ```bash
    python -m omc3.hole_in_one --harpy --optics \
        --files trackone.sdds \
        --tbt_datatype lhc \
        --turns 0 1023 \
        --autotunes transverse \
        --to_write lin spectra full_spectra bpm_summary \
        --accel lhc \
        --year 2018 \
        --beam 1 \
        --model_dir lhc_model \
        --compensation none \
        --three_bpm_method \
        --coupling_method 1 \
        --outputdir measured_optics
    ```
    In this case, the output files from `harpy` are automatically handled and put into a subfolder named `lin_files` inside of the specified `outputdir`.
    The rest is done and output as seen above.
    Again, we recommend using all this functionality [through the GUI](../../guis/betabeat/gui.md) instead.

## Amplitude Detuning Analysis

From the optics output files, in particular the `kick_[xy].tfs` files, one can perform amplitude detuning analysis.
The detailed steps to run this from the GUI are described in [the amplitude detuning analysis procedure](../../measurements/procedures/ampdet.md#analysis).

## Determining Corrections

From the results of an optics analysis, it is possible with `omc3` to compute corrections in order to try and bring chosen parameters closer to the model values.
However, due to the complexity of this workflow we will not provide a CLI walkthrough, and instead direct the user to [use this functionality through the dedicated GUI](../../guis/betabeat/correction_panel.md).

<!-- Links in 'analysis workflow' section -->
[tfs_format]:https://pylhc.github.io/tfs/tfsformat.html
[mess_example]: https://github.com/pylhc/MESS/tree/master/LHC/Website_Example
<!-- Links in 'preparing data' section -->
[sdds]: https://ops.aps.anl.gov/SDDSIntroTalk/slides.html
[tbt_doc]: https://pylhc.github.io/turn_by_turn/
[tbt_converter]: https://pylhc.github.io/omc3/entrypoints/other.html#tbt-converter
<!-- Links in 'creating a model' section -->
[model_creator]: https://pylhc.github.io/omc3/entrypoints/other.html#model-creator
[mess_acd_twiss]: https://github.com/pylhc/MESS/tree/master/LHC/AC_Dipole_Model
<!-- Links in 'frequency analysis' section -->
[hole_in_one]: https://pylhc.github.io/omc3/entrypoints/analysis.html#omc3.hole_in_one.hole_in_one_entrypoint
[plot_spectrum]: https://pylhc.github.io/omc3/entrypoints/plotting.html#plot-spectrum
[normal_forms]: https://cds.cern.ch/record/333077/files/p93.pdf
<!-- Links in 'optics analysis' section -->
[analytical_nbpm]: https://link.aps.org/doi/10.1103/PhysRevAccelBeams.20.111002
