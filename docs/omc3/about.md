# The OMC3 Software Documentation

The `omc3` package is the python tool of the Optics Measurements and Corrections group at CERN.
The `omc3` repository is the new version of our codes, refactored and rewritten for Python 3.6+.

!!! note "Note - Documentation Type"
    This section acts as a general documentation and guide to using the `omc3` package.
    The package's source can be found on [Github][omc3]{target=_blank} and its API documentation can be found at the [following link][omc3_doc]{target=_blank}.

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

This software is licensed under the GNU GPLv3 License, see [License][license]{target=_blank}.

## Authors

This work is the result of combined efforts by members of the [pylhc/omc-team][omc_team]{target=_blank} working group.
Contributions are welcome, but tightly controlled, see the [Contributing](contributing.md) page.

[omc3]: https://github.com/pylhc/omc3
[omc3_doc]: https://pylhc.github.io/omc3/
[license]: https://github.com/pylhc/omc3/blob/master/LICENSE
[omc_team]: https://github.com/orgs/pylhc/teams/omc-team