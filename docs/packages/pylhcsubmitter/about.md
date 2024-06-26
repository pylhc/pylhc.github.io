# PyLHC Submitter

[This package][repo] contains scripts to simplify the creation and submission of jobs to HTCondor.

## Functionality

- [*Job Submitter*](job_submitter.md) - Generating jobs based on a templates file and submitting them to HTCondor.
- [*AutoSix*](autosix.md) - Generating and submitting parametric SixDesk studies easily.

## Documentation

- [Autogenerated docs][documentation] via `sphinx`.

## Getting Started

!!! warning "Package Availability"
    As it requires `HTCondor` bindings, this package is unavailable on Windows.
    The package is available on:
      - `Linux` through `PyPI`.
      - `Linux` and `macOS` through `conda-forge`.

Installation is easily done via pip:
```bash
python -m pip install pylhc-submitter
```

One can also install in a conda environment via the conda-forge channel with:
```bash
conda install -c conda-forge pylhc_submitter
```

After installing, scripts can be run with either python -m pylhc_submitter.SCRIPT --FLAG ARGUMENT or by calling the Python files directly.

After installing, codes can be run with either

- from the command line with arguments: `python -m pylhc_submitter.SCRIPT --FLAG ARGUMENT`;
- from the command line providing a config file: `python -m pylhc_submitter.SCRIPT --entry_cfg config.ini`;
- by calling the main function in a Python script.

[repo]: https://github.com/pylhc/submitter
[documentation]: https://pylhc.github.io/submitter/