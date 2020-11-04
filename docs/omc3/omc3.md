# The OMC3 Software Documentation

The `omc3` package is the python tool of the Optics Measurements and Corrections group at CERN.
The `omc3` repository is the new version of our codes, refactored and rewritten for Python 3.6+.

If you are not part of that group, you will most likely have no use for the codes provided here, unless you have a 9km wide accelerator at home.
Feel free to use them anyway, if you wish!

!!! note "Note - Documentation Status"
    This site is currently under construction, incomplete, and subject to change.
    An existing but poor documentation can be found on the [OMC twiki](https://twiki.cern.ch/twiki/bin/view/BEABP/OMC).

!!! note "Note - Documentation Type"
    This site acts as a general documentation and guide to using the `omc3` package.
    The package's API documentation can be found at the [following link](https://pylhc.github.io/omc3/).

## Quick start

Install the latest version of this package with `pip`:

```bash
pip install omc3 
```

## What to expect

The `omc3` package serves the folowing purposes:

- Providing an all-in-one package for frequency analysis and optics measurements and corrections algorithms in particle accelerators.
- Providing an easily callable entrypoint to run your analytics from measurement / simulation files.
- Providing a convenient wrapper to effortlessly run `MAD-X` jobs.

For detailed instructions see the [getting started guide][getting_started.md].

## License

This software is licensed under the GNU GPLv3 License, see [License](https://github.com/pylhc/omc3/blob/master/LICENSE).
