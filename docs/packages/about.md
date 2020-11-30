# OMC's Python Packages

This section of the website goes over our computing and analysis softwares, which are written in Python.

Our main analysis software exist in two versions: `Beta-Beat.src` for Python 2, and its replacement `omc3` for Python 3.
Development of the `Beta-Beat.src` package is limited to bug fixes, and new features are integrated directly into `omc3`.
The `pylhc` package provides useful tools and scripts for our day-to-day work, and our other packages provide specific I/O and entrypoint utilities for our codes. 

All our Python codes, including legacy repositories, can be found on the [PyLHC organisation][pylhc_github]{target=_blank}'s page on Github.

The OMC team develops and maintains the following packages:

## Quick Access Links

- **OMC3** (Python 3.7+): [:fontawesome-solid-question-circle:](omc3/about.md) [:fontawesome-brands-github:][omc3]{target=\_blank} [:fontawesome-solid-book:][omc3_doc]{target=\_blank} <br>
  <!-- _frequency analysis, optics computation from turn-by-turn data, corrections calculations and results plotting._ -->
- **PyLHC-Tools** (Python 3.7+): [:fontawesome-solid-question-circle:](pylhc/about.md) [:fontawesome-brands-github:][pylhc]{target=\_blank} [:fontawesome-solid-book:][pylhc_doc]{target=\_blank} <br>
  <!-- _useful OMC-related scripts._ -->
- **Example Study Scripts** (MAD-X): [:fontawesome-solid-question-circle:](mess/about.md) [:fontawesome-brands-github:][mess]{target=\_blank} <br>
  <!-- _collection of example studies._ -->
- **Beta-Beat.src** (Python 2.7): [:fontawesome-brands-github:][betabeatsrc]{target=\_blank} [:fontawesome-solid-book:][betabeatsrc_doc]{target=\_blank} <br>
  <!-- _frequency analysis, optics computation from turn-by-turn data and corrections calculations._ -->
- **TFS-Pandas** (Python 3.6+): [:fontawesome-brands-github:][tfspandas]{target=\_blank} [:fontawesome-solid-book:][tfspandas_doc]{target=\_blank} <br>
  <!-- _*TFS files* I/O functionality._ -->
- **SDDS-Reader** (Python 3.6+): [:fontawesome-brands-github:][sdds]{target=\_blank} [:fontawesome-solid-book:][sdds_doc]{target=\_blank} <br>
  <!-- _*SDDS files* I/O functionality._ -->
- **Generic-Parser** (Python 3.6+): [:fontawesome-brands-github:][generic_parser]{target=\_blank} [:fontawesome-solid-book:][generic_parser_doc]{target=\_blank} <br>
  <!-- _entrypoint argument parser functionality._ -->


[pylhc_github]: https://github.com/pylhc/ 
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
[mess]: https://github.com/pylhc/MESS