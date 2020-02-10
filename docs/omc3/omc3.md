# The OMC3 Software Documentation

The `omc3` package, available [here on Github](https://github.com/pylhc/omc3), is the Python tool of the Optics Measurements and Corrections group at CERN.
The `omc3` repository is the new version of our codes, refactored and rewritten for Python 3.6+.

If you are not part of that group, you will most likely have no use for those codes, unless you have a 9km wide accelerator at home.
Feel free to use them anyway, if you wish!

!!! note "Note - Documentation Status"
    This site is currently under construction, incomplete, and subject to change.
    An existing but poor documentation can be found on the [OMC twiki](https://twiki.cern.ch/twiki/bin/view/BEABP/OMC).

!!! note "Note - Documentation Type"
    This site section acts as a general documentation and guide to using the `omc3` package.
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

For detailed instructions see the [getting started guide](getting_started.md).

## Implementation Progress

Currently, `omc3` is still working towards a first release.
The current working functionality are:

- Main function: Hole_in_one
- Harmonic Analysis: Harpy
- Utils: logging, iotools, file handlers, entrypoint
- Madx wrapper

The features currently being developed are:

- Optics Measurement
- K-Modulation
- Accuracy Tests
- Regression Tests

## Quality checks

- Automated tests are ran after each commit via [Travis-CI](https://travis-ci.com/pylhc/omc3). 
- Additional checks for code-complexity, design-rules, test-coverage, and duplication are handled by [CodeClimate](https://codeclimate.com/github/pylhc/omc3).

## License

This software is licensed under the GNU GPLv3 License, see [License](https://github.com/pylhc/omc3/blob/master/LICENSE).

## Authors

This work is the result of combined efforts by members of the [pylhc/omc-team](https://github.com/orgs/pylhc/teams/omc-team) working group.
Contributions are welcome, but tightly controlled, see the [Contributing](contributing.md) page.