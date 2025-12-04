# The OMC Python Packages

| Package                                                                       | Description                                                                                                  | Version                                                                                                                                                                         | Documentation                                                         | Wiki                                                                   |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------------|
| [**OMC3**][omc3]{target=\_blank}                                              | Frequency analysis, optics computation from turn-by-turn data, corrections calculations and results plotting | [![PyPI version for OMC3](https://img.shields.io/pypi/v/omc3.svg)][omc3_pypi]{target=\_blank}                                                                                   | [:fontawesome-solid-book:][omc3_doc]{target=\_blank}                  | [:fontawesome-solid-circle-question:](omc3/about.md)                   |
| [**OMC3 GUI**][omc3]{target=\_blank}                                          | Graphical User Interface for OMC3 Segment-by-Segment Analysis                                                | [![PyPI version for OMC3 GUI](https://img.shields.io/pypi/v/omc3_gui.svg)][omc3_gui_pypi]{target=\_blank}                                                                       | [:fontawesome-solid-book:][omc3_gui_doc]{target=\_blank}              |                                                                        |
| [**TFS-Pandas**][tfspandas]{target=\_blank}                                   | TFS files I/O functionality                                                                                  | [![PyPI version for TFS-Pandas](https://img.shields.io/pypi/v/tfs-pandas.svg)][tfs_pypi]{target=\_blank}                                                                        | [:fontawesome-solid-book:][tfspandas_doc]{target=\_blank}             |                                                                        |
| [**Turn-by-Turn**][turnbyturn]{target=\_blank}                                | Particle accelerators turn-by-turn BPM measurements I/O functionality                                        | [![PyPI version for Turn-by-Turn](https://img.shields.io/pypi/v/turn_by_turn.svg)][tbt_pypi]{target=\_blank}                                                                    | [:fontawesome-solid-book:][turnbyturn_doc]{target=\_blank}            |                                                                        |
| [**SDDS**][sdds]{target=\_blank}                                              | SDDS files I/O functionality                                                                                 | [![PyPI version for SDDS](https://img.shields.io/pypi/v/sdds.svg)][sdds_pypi]{target=\_blank}                                                                                   | [:fontawesome-solid-book:][sdds_doc]{target=\_blank}                  |                                                                        |
| [**PyLHC-Tools**][pylhc]{target=\_blank}                                      | Useful OMC-related scripts                                                                                   | [![PyPI version for PyLHC-Tools](https://img.shields.io/pypi/v/PyLHC.svg)][pylhc_pypi]{target=\_blank}                                                                          | [:fontawesome-solid-book:][pylhc_doc]{target=\_blank}                 | [:fontawesome-solid-circle-question:](pylhc/about.md)                  |
| [**PyLHC-Submitter**][pylhc_submitter]{target=\_blank}                        | Wrapper for HTCondor job submission                                                                          | [![PyPI version for PyLHC-Submitter](https://img.shields.io/pypi/v/pylhc-submitter.svg)][pylhc_submitter_pypi]{target=\_blank}                                                  | [:fontawesome-solid-book:][pylhc_submitter_doc]{target=\_blank}       | [:fontawesome-solid-circle-question:](pylhcsubmitter/job_submitter.md) |
| [**Optics-Functions**][optics_functions]{target=\_blank}                      | Calculate various beam optics functions from TFS-Dataframes                                                  | [![PyPI version for Optics-Functions](https://img.shields.io/pypi/v/optics-functions.svg)][optics_functions_pypi]{target=\_blank}                                               | [:fontawesome-solid-book:][optics_functions_doc]{target=\_blank}      |                                                                        |
| [**Generic-Parser**][generic_parser]{target=\_blank}                          | Entrypoint argument parser functionality                                                                     | [![PyPI version for Generic-Parser](https://img.shields.io/pypi/v/generic-parser.svg)][generic_parser_pypi]{target=\_blank}                                                     | [:fontawesome-solid-book:][generic_parser_doc]{target=\_blank}        |                                                                        |
| [**IRNL RDT Correction**][irnl_rdt_correction]{target=\_blank}                | Calculate powering of IR NL-correctors based on RDT compensation.                                            | [![PyPI version for IRNL RDT Correction](https://img.shields.io/pypi/v/irnl-rdt-correction.svg)][irnl_rdt_correction_pypi]{target=\_blank}                                      | [:fontawesome-solid-book:][irnl_rdt_correction_doc]{target=\_blank}   | [:fontawesome-solid-circle-question:](irnl/about.md)                   |
| [**IR Amplitude Detuning Correction**][ir_amplitude_detuning]{target=\_blank} | Correct amplitude detuning via IR correctors.                                                                | [![PyPI version for IR Amplitude Detuning Correction](https://img.shields.io/pypi/v/ir-amplitude-detuning.svg)][ir_amplitude_detuning_pypi]{target=\_blank}                     | [:fontawesome-solid-book:][ir_amplitude_detuning_doc]{target=\_blank} |                                                                        |
| [**Example Study Scripts**][mess]{target=\_blank}                             | Collection of example MAD-X studies                                                                          | [![GitHub release for MESS](https://img.shields.io/github/v/release/pylhc/MESS?color=orange&label=Release&logo=Github)][mess_releases]{target=\_blank}                          |                                                                       | [:fontawesome-solid-circle-question:](mess/about.md)                   |
| [**Beta-Beat.src**][betabeatsrc]{target=\_blank}                              | Frequency analysis, optics computation from turn-by-turn data and corrections calculations                   | [![GitHub release for Beta-Beat.src](https://img.shields.io/github/v/release/pylhc/Beta-Beat.src?color=orange&label=Release&logo=Github)][betabeatsrc_releases]{target=\_blank} | [:fontawesome-solid-book:][betabeatsrc_doc]{target=\_blank}           |                                                                        |

## The OMC Python Ecosystem

This section of the website goes over our Python computing and analysis softwares and environments.
Our main software for optics analysis exists in two versions: a legacy Python 2 version, `Beta-Beat.src`, and its Python 3 successor `omc3`.
Development of `Beta-Beat.src` is limited to bug fixes while new features are reserved for `omc3`.

Our other packages provide useful tools and scripts for our day-to-day work as well as specific I/O functionality and entrypoint utilities for our codes.
All our Python codes, including legacy repositories, can be found on the [PyLHC organisation][pylhc_github]{target=_blank}'s page on Github.

## The OMC Production Environments

The OMC Python 3 production environment for use for instance in the CCC is based on the CERN BE/CO [Acc-Py][accpy_docs]{target=_blank .cern_internal} distribution, although an OMC-specific one.
The environment, along with many of our important files, is located in the `/afs/cern.ch/eng/sl/lintrack/` directory on `afs`.

The environment is located at `/afs/cern.ch/eng/sl/lintrack/omc_python3/` and can be used in two different ways:

- Activate the environment (`source /afs/cern.ch/eng/sl/lintrack/omc_python3/bin/activate`) then run `python` to execute your programs.
- Point to the Python executable directly (`/afs/cern.ch/eng/sl/lintrack/omc_python3/bin/python`) to execute your programs.

!!! warning "Modifying the Environment"
    You cannot modify this environment, [unless you are one of the maintainers](development/managing.md).
    Should you need specific packages, reach out to us or consider [setting up your own environment](development/howto_venv.md#creating-virtual-environments-with-acc-py) from our `Acc-Py` distribution.

??? question "Python 2 Environment"
    We do have a `miniconda2` installation in `lintrack` for legacy Python2 codes.
    This distribution is frozen and the use of Python 2 codes should be avoided as much as possible.

[accpy_docs]: https://wikis.cern.ch/display/ACCPY/Accelerating+Python+Home
[betabeatsrc]: https://github.com/pylhc/Beta-Beat.src
[betabeatsrc_doc]: https://pylhc.github.io/Beta-Beat.src
[betabeatsrc_releases]: https://github.com/pylhc/Beta-Beat.src/releases

[tfspandas]: https://github.com/pylhc/tfs
[tfspandas_doc]: https://pylhc.github.io/tfs
[turnbyturn]: https://github.com/pylhc/turn_by_turn
[turnbyturn_doc]: https://pylhc.github.io/turn_by_turn/
[sdds]: https://github.com/pylhc/sdds
[sdds_doc]: https://pylhc.github.io/sdds
[generic_parser]: https://github.com/pylhc/generic_parser
[generic_parser_doc]: https://pylhc.github.io/generic_parser
[generic_parser_pypi]: https://pypi.org/project/generic-parser/
[mess]: https://github.com/pylhc/MESS
[mess_releases]: https://github.com/pylhc/MESS/releases
[irnl_rdt_correction]: https://github.com/pylhc/irnl_rdt_correction
[irnl_rdt_correction_doc]: https://pylhc.github.io/irnl_rdt_correction
[irnl_rdt_correction_pypi]: https://pypi.org/project/irnl_rdt_correction/
[ir_amplitude_detuning]: https://github.com/pylhc/ir_amplitude_detuning
[ir_amplitude_detuning_doc]: https://pylhc.github.io/ir_amplitude_detuning
[ir_amplitude_detuning_pypi]: https://pypi.org/project/ir_amplitude_detuning/
[omc3]: https://github.com/pylhc/omc3
[omc3_doc]: https://pylhc.github.io/omc3
[omc3_pypi]: https://pypi.org/project/omc3/
[omc3_gui]: https://github.com/pylhc/omc3_gui
[omc3_gui_doc]: https://pylhc.github.io/omc3_gui
[omc3_gui_pypi]: https://pypi.org/project/omc3_gui/
[optics_functions]: https://github.com/pylhc/optics_functions
[optics_functions_doc]: https://pylhc.github.io/optics_functions
[optics_functions_pypi]: https://pypi.org/project/optics-functions/
[pylhc]: https://github.com/pylhc/pylhc
[pylhc_doc]: https://pylhc.github.io/PyLHC
[pylhc_github]: https://github.com/pylhc/
[pylhc_pypi]: https://pypi.org/project/pylhc/
[pylhc_submitter]: https://github.com/pylhc/submitter
[pylhc_submitter_doc]: https://pylhc.github.io/submitter/
[pylhc_submitter_pypi]: https://pypi.org/project/pylhc-submitter/
[sdds_pypi]: https://pypi.org/project/sdds/
[tbt_pypi]: https://pypi.org/project/turn-by-turn/
[tfs_pypi]: https://pypi.org/project/tfs-pandas/
