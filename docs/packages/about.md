# The OMC Python Ecosystem

This section of the website goes over our Python computing and analysis softwares and environments.
Our main software for optics analysis exists in two versions: a legacy Python 2 version, `Beta-Beat.src`, and its Python 3 successor `omc3`.
Development of `Beta-Beat.src` is limited to bug fixes while new features are reserved for `omc3`.

Our other packages provide useful tools and scripts for our day-to-day work as well as specific I/O functionality and entrypoint utilities for our codes.
All our Python codes, including legacy repositories, can be found on the [PyLHC organisation][pylhc_github]{target=_blank}'s page on Github.

## The OMC Production Environments

The OMC Python 3 production environment for use for instance in the CCC is based on the CERN BE/CO [Acc-Py][accpy_docs]{target=_blank .cern_internal} distribution, although an OMC-specific one.
The environment, along with many of our important files, is located in the `lintrack` directory on `afs` at `/afs/cern.ch/eng/sl/lintrack/`. 

The environment is located at `/afs/cern.ch/eng/sl/lintrack/OMC_Python3/` and can be used in two different ways:

- Activate the environment (`source /afs/cern.ch/eng/sl/lintrack/OMC_Python3/bin/activate`) then run `python` to execute your programs.
- Point to the Python executable directly (`/afs/cern.ch/eng/sl/lintrack/OMC_Python3/bin/python`) to execute your programs.

!!! warning "Modifying the Environment"
    Please do not try to modify this environment.
    Should you need specific packages, reach out to us or consider [setting up your own environment](development/howto_venv.md#creating-virtual-environments-with-the-acc-py-distribution) from our `Acc-Py` distribution.

??? question "Python 2 Environment"
    We do have a `miniconda2` installation in `lintrack` for legacy Python2 codes.
    This distribution is frozen and the use of Python 2 codes should be avoided as much as possible.

## The OMC Python Packages

The OMC team develops and maintains the following packages:

- **OMC3** (Python 3.7+): [:fontawesome-solid-question-circle:](omc3/about.md) [:fontawesome-brands-github:][omc3]{target=\_blank} [:fontawesome-solid-book:][omc3_doc]{target=\_blank} <br>
  _frequency analysis, optics computation from turn-by-turn data, corrections calculations and results plotting._
- **PyLHC-Tools** (Python 3.7+): [:fontawesome-solid-question-circle:](pylhc/about.md) [:fontawesome-brands-github:][pylhc]{target=\_blank} [:fontawesome-solid-book:][pylhc_doc]{target=\_blank} [:fontawesome-solid-cube:][pylhc_pypi]{target=\_blank} <br>
  _useful OMC-related scripts._
- **PyLHC-Submitter** (Python 3.7+): [:fontawesome-brands-github:][pylhc_submitter]{pylhcsubmitter/about.md} [:fontawesome-solid-book:][pylhc_submitter_doc]{target=\_blank} [:fontawesome-solid-cube:][pylhc_submitter_pypi]{target=\_blank} <br>
  _Wrapper for HTCondor Job submission._
- **Optics-Functions** (Python 3.6+): [:fontawesome-brands-github:][optics_functions]{target=\_blank} [:fontawesome-solid-book:][optics_functions_doc]{target=\_blank} [:fontawesome-solid-cube:][optics_functions_pypi]{target=\_blank} <br>
  _calculate various beam optics functions from TFS-Dataframes._
- **Example Study Scripts** (MAD-X): [:fontawesome-solid-question-circle:](mess/about.md) [:fontawesome-brands-github:][mess]{target=\_blank} <br>
  _collection of example studies._
- **Beta-Beat.src** (Python 2.7): [:fontawesome-brands-github:][betabeatsrc]{target=\_blank} [:fontawesome-solid-book:][betabeatsrc_doc]{target=\_blank} <br>
  _frequency analysis, optics computation from turn-by-turn data and corrections calculations._
- **TFS-Pandas** (Python 3.6+): [:fontawesome-brands-github:][tfspandas]{target=\_blank} [:fontawesome-solid-book:][tfspandas_doc]{target=\_blank} [:fontawesome-solid-cube:][tfs_pypi]{target=\_blank} <br>
  _*TFS files* I/O functionality._
- **SDDS-Reader** (Python 3.6+): [:fontawesome-brands-github:][sdds]{target=\_blank} [:fontawesome-solid-book:][sdds_doc]{target=\_blank} [:fontawesome-solid-cube:][sdds_pypi]{target=\_blank} <br>
  _*SDDS files* I/O functionality._
- **Generic-Parser** (Python 3.6+): [:fontawesome-brands-github:][generic_parser]{target=\_blank} [:fontawesome-solid-book:][generic_parser_doc]{target=\_blank} [:fontawesome-solid-cube:][generic_parser_pypi]{target=\_blank} <br>
  _entrypoint argument parser functionality._

[pylhc_github]: https://github.com/pylhc/
[accpy_docs]: https://wikis.cern.ch/display/ACCPY/Accelerating+Python+Home
[betabeatsrc]: https://github.com/pylhc/Beta-Beat.src
[betabeatsrc_doc]: https://pylhc.github.io/Beta-Beat.src
[omc3]: https://github.com/pylhc/omc3
[omc3_doc]: https://pylhc.github.io/omc3
[pylhc]: https://github.com/pylhc/pylhc
[pylhc_doc]: https://pylhc.github.io/PyLHC
[tfspandas]: https://github.com/pylhc/tfs
[tfspandas_doc]: https://pylhc.github.io/tfs
[sdds]: https://github.com/pylhc/sdds
[sdds_doc]: https://pylhc.github.io/sdds
[generic_parser]: https://github.com/pylhc/generic_parser
[generic_parser_doc]: https://pylhc.github.io/generic_parser
[pylhc_submitter]: https://github.com/pylhc/submitter
[pylhc_submitter_doc]: https://pylhc.github.io/submitter/
[mess]: https://github.com/pylhc/MESS
[pylhc_pypi]: https://pypi.org/project/pylhc/
[sdds_pypi]: https://pypi.org/project/sdds/
[tfs_pypi]: https://pypi.org/project/tfs-pandas/
[generic_parser_pypi]: https://pypi.org/project/generic-parser/
[pylhc_submitter_pypi]: https://pypi.org/project/pylhc-submitter/
[optics_functions]: https://github.com/pylhc/optics_functions
[optics_functions_doc]: https://pylhc.github.io/optics_functions
[optics_functions_pypi]: https://pypi.org/project/optics-functions/
