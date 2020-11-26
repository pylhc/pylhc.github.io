# OMC's Python Packages

This section of the website goes over our computing and analysis softwares, which are written in Python.

Our main analysis software exist in two versions: `Beta-Beat.src` for Python 2, and its replacement `omc3` for Python 3.
Development of the `Beta-Beat.src` package is limited to bug fixes, and new features are integrated directly into `omc3`.
The `pylhc` package provides useful tools and scripts for our day-to-day work, and our other packages provide specific I/O and entrypoint utilities for our codes. 

All our Python codes, including legacy repositories, can be found on the [PyLHC organisation][pylhc_github]{target=_blank}'s page on Github.

The OMC team develops and maintains the following packages:

- [Beta-Beat.src](betabeatsrc.md) (`Python 2.7`) for frequency analysis, optics computation from turn-by-turn data and corrections calculations.
- [omc3](omc3/about.md) (`Python 3.7+`) for frequency analysis, optics computation from turn-by-turn data, corrections calculations and results plotting.
- [pylhc](pylhc.md) (`Python 3.7+`)  for useful OMC-related scripts.
- [tfs-pandas](tfs-pandas.md) (`Python 3.6+`) for **TFS files** I/O functionality.
- [sdds](sdds.md) (`Python 3.6+`) for **SDDS files** I/O functionality.
- [generic_parser](generic_parser.md) (`Python 3.6+`) for entrypoint argument parser functionality.


[pylhc_github]: https://github.com/pylhc