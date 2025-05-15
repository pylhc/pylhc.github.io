# BetaBeat.src

Since 2025, the former `omc3` branch has been moved to the `master` branch of the GUI and is now the default for all new users.
The "BetaBeat.src" branch of the GUI has been retired from `master` to the `BetaBeatSrc` branch
and is no longer under active development.

Legacy version are still available on CAS.

## Meaning of Beta-Beat.src Output Files

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
