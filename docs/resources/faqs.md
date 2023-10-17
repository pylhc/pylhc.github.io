# Frequently Asked Questions

!!! info 
    We are gradually including here different pieces of useful information, possibly from questions answered in meetings or on Mattermost, which don't really fit anywhere else as their whole page.

## Beta-Beat.src Caveats

### Meaning of Beta-Beat.src Output Files

The naming of output files in Beta-Beat.src analysis can be very unintuitive.
Namely, one will see similar output files for a quantity which go as `get_*.out`, `get_*_free.out` and `get_*_free2.out`, where `*` is the calculated quantity (betas, phase, etc.).
These each correspond to a variation of the calculated quantity, explained below.

When doing our measurements, we use AC-Dipole driven excitations of the beam for a better signal-to-noise ratio in data acquisition.
However, as the AC-Dipole has an effect on the beam optics functions the reconstructed optics from these measurements are the driven optics, not those of the accelerator itself.
One can compensate for this deviation in different ways, which is why there are several output files for each optics quantity computed.

!!! example "Meaning of Different Output Files"
    | Nomenclature      | Meaning                                                                                                        |
    | :---------------- | :------------------------------------------------------------------------------------------------------------- |
    | `get_*.out`       | The optics functions **without** compensation, from the driven excitation data.                                |
    | `get_*_free.out`  | The optics functions compensated **analytically** using an equation[^MiyamotoMeasurementCouplingRDTsACDipole]. |
    | `get_*_free2.out` | The optics functions compensated **the other way**, see bellow.                                                |

    In the case of the `get_*_free2.out` files, the compensation is done differently depending on the computed quantity.
    For some quantities (for instance for $\beta$ from phase) this uses the model values, for others (for instance the coupling RDTs $f_{1001}$ and $f_{1010}$) it is a rescaling in which the model values are used *indirectly*.

The method used to output the `get_*_free2.out` files is sometimes more robust as it does not rely on the existence of certain BPMs in the output (which could be missing after cleaning), and in some edge cases is more accurate[^HoydalsvikSubPerMilCouplingLHC].

!!! tip "Do Compare Outputs"
    For debugging purposes, if the final result looks unbelievable, it might be of advantage to check the uncompensated output to rule out (or confirm) a failure in the recalibration method.

## MAD-X Pitfalls

`MAD-X` can sometimes be a bit tricky to work with.
This section is intended to put together some common pitfalls encountered when creating a MAD-X script.  

!!! warning "MAD-X Errors"
    As a reminder, `MAD-X` ignores all the code that does not work.
    It does not raise errors or crash like other languages, which can make it difficult to identify your mistakes.
    As a reminder: each instruction should end with a semicolon and `MAD-X` will consider everything a single command until the next `;` is encountered.

### Tracking, Beam 2 and Beam 4

You might have noticed that an `lhcb4.seq` file is included in the `acc-models-lhc` repository.
There is a specific caveat for the beam 2 sequence definition that one needs to be aware in order to do tracking.

For practical reasons, the properties of all elements of the LHC are defined (in the `lhc.seq`) as if they apply to a clockwise proton beam (beam 1).
This allows a single definition for elements traversed by both beams.
Their effects on a beam with identical particle charge but running in the opposite direction (beam 2) must then be reversed inside the program, which is achieved by creating a beam with a [bv=-1 flag][madx_doc]{target=_blank} (section `7.4`).

However, in order to perform tracking for the `lhcb2` sequence the exact elements definitions are necessary, as well as a `bv` flag of 1.
This is done in the `lhcb4.seq` file.
There is no such caveat for tracking with beam 1, which is why there is no "beam 3".

!!! example "Tracking Cheatsheet"
    === "Beam 1"

        Tracking for Beam 1 does not have any caveat:
        
        - Load the `lhc.seq` sequence file
        - Create your beam for the `lhcb1` sequence with the `bv=1` flag
        - Slice the `lhcb1` sequence and track

    === "Beam 2"
        When tracking for beam 2, remember to:

        - Load the `lhcb4.seq` sequence file
        - Create your beam for the `lhcb2` sequence with the `bv=1` flag
        - Slice the `lhcb2` sequence and track
        
        !!! tip "What about model creation?"
            If analysing the tracking data with either `Beta-Beat.src` or `omc3`, one will need a model. The model **has** to have been made with the regular `lhc.seq` file, `lhcb2` sequence, and a beam with `bv=-1`.

## LSA Pitfalls

### Querying LSA is Slow

You might run into an issue with the [`pylhc.machine_settings_info`](../packages/pylhc/machine_settings_info.md) script where your query hangs for a (very) long time.
This is due to the fact that `pjlsa` will look for the beamprocess at the given time and extract *all trims* for the required knobs through this beamprocess, even though only the last trim is displayed.

!!! example "Workarounds"
    To speed up the script's runtime, try the following:

    - Do not extract knobs if you are only after the summary information (this is now default behaviour)
    - Only ask for the knobs you need (e.g. `--knobs name1 name1`), or just default ones (e.g. `--knobs default`) if you're unsure
    - Give a time range that is as small as possible using the `--start-time` and `--time` flags. This way a small trim history will be queried by `pjlsa`. For instance:
    
    ```bash
    python -m pylhc.machine_settings_info \
        --knobs name1 name2 \  # with real names ;)
        --start-time "2022-10-19 17:00:00.0" \
        --time "2022-10-19 17:30:00.0"
    ```
    
    Be aware though that if no trim for the knobs are in the defined time range, no values will be returned at all.


[^MiyamotoMeasurementCouplingRDTsACDipole]:
    ??? abstract "Measurement of Coupling Resonance Driving Terms with the AC Dipole", `R. Miyamoto`, [BNL--94350-2010-IR, 1013520](https://www.bnl.gov/isd/documents/74582.pdf){target=_blank}"
        ```
        @report{MiyamotoMeasurementCouplingRDTsACDipole,
            title        = {Measurement of {{Coupling Resonance Driving Terms}} with the {{AC Dipole}}},
            author       = {Miyamoto, R.},
            year         = 2010,
            month        = 10,
            number       = {BNL--94350-2010-IR, 1013520},
            doi          = {10.2172/1013520},
            url          = {https://www.bnl.gov/isd/documents/74582.pdf},
            langid       = {english}
        }
        ```

[^HoydalsvikSubPerMilCouplingLHC]:
    ??? abstract "Reaching the Sub Per Mil Level Coupling Corrections in the LHC", `E. Høydalsvik and T. Persson`, [IPAC 2021](https://accelconf.web.cern.ch/ipac2021/papers/thpab001.pdf){target=_blank}"
        ```
        @inproceedings{IPAC:Hoydalsvik:SubPerMilCouplingLHC,
            title        = {Reaching the {{Sub Per Mil Level Coupling Corrections}} in the {{LHC}}},
            author       = {Høydalsvik, Eirik and Persson, Tobias},
            booktitle    = {Proceedings of the 12th {{International Particle Accelerator Conference}}},
            publisher    = {{JACoW Publishing, Geneva, Switzerland}},
            volume       = {IPAC2021},
            doi          = {10.18429/JACOW-IPAC2021-THPAB001},
            isbn         = {978-3-95450-214-1},
            url          = {https://accelconf.web.cern.ch/ipac2021/papers/thpab001.pdf},
            date         = 2021,
            langid       = {english}
        }
        ```



[madx_doc]: http://madx.web.cern.ch/madx/releases/last-rel/madxuguide.pdf