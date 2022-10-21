# The OMC3 Software Documentation

The `omc3` package is the python tool of the Optics Measurements and Corrections team at CERN.
The `omc3` repository is the new version of our codes, refactored and rewritten for `Python 3.7+`.

!!! info
    This section acts as a general documentation and guide to using the `omc3` package.
    The package's source can be found on [Github][omc3_gh]{target=_blank} and its API documentation can be found at the [following link][omc3_doc]{target=_blank}.

## Installing

Installation is easily done via pip:
```bash
python -m pip install omc3
```

Additionally, some features require access to the CERN Technical Network and require CERN-specific dependencies.
Those are installable from the CERN `Acc-Py` index through the `cern` extra, and can be installed from the CERN network or by providing the `index-url`:
```bash
python -m pip install --index-url http://acc-py-repo.cern.ch:8081/repository/vr-py-releases/simple --trusted-host acc-py-repo.cern.ch "omc3[cern]"
```

## What to expect

The `omc3` package serves the following purposes:

- Providing an all-in-one package for frequency analysis and optics measurements and corrections algorithms in particle accelerators.
- Providing an easily callable entrypoint to run your analytics from measurement / simulation files.
- Providing a convenient wrapper to effortlessly run `MAD-X` jobs.

For installation instructions and detailed content see the [getting started guide](getting_started.md).
For a step by step walk-through of an `omc3` analysis workflow, see the [workflow guide](analysis.md).

## License

This software is licensed under the `MIT` License, see [License][license]{target=_blank}.

## Authors

This work is the result of combined efforts by members of the [pylhc/omc-team][omc_team]{target=_blank} working group.
Contributions are welcome, but tightly controlled, see the [guidelines](../development/contributing.md) page.

[omc3_gh]: https://github.com/pylhc/omc3
[omc3_doc]: https://pylhc.github.io/omc3/
[omc3_changelog]: https://github.com/pylhc/omc3/blob/master/CHANGELOG.md
[license]: https://github.com/pylhc/omc3/blob/master/LICENSE
[omc_team]: https://github.com/orgs/pylhc/teams/omc-team
