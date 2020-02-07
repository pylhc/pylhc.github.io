# About OMC

The Optics Measurements and Corrections (OMC) team is responsible for the measurement and correction of the linear and nonlinear optics in the Large Hadron Collider (LHC) at CERN.
Our meetings can be found on our [Indico page](https://indico.cern.ch/category/5986/).

The `omc3` package, available [here](https://github.com/pylhc/omc3) on Github, is the Python3 version of our main tool software.


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

## Authors

This work is the result of combined efforts by members of the [pylhc/omc-team](https://github.com/orgs/pylhc/teams/omc-team) working group.
Contributions are welcome, but tightly controlled, see the [Contributing](contributing.md) page.
