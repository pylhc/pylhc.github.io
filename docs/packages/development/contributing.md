# Contributing to the PyLHC Packages

Want to report a bug, request a feature or simply contribute some code?
We welcome contributions, but before you do, please read the following guidelines.

## Submission context

#### Got a question or problem?

If you have questions on some of the packages' functionality, and the available documentation does not provide answers, you can submit them as new issues on GitHub.
If you spot missing parts in the documentation, feel free to report it in an issue and open a Pull Request that fixes it. 

#### Found a bug?

If you found a bug in the source code, you can help us by submitting a bug report in a new issue on GitHub.
If you wish to contribute a solution, you can submit a Pull Request with a fix.
However, before doing so, please read the submission guidelines bellow.

#### Missing a feature?

You can request a new feature by opening an issue on GitHub.
If you would like to implement a new feature, please submit an issue with a proposal first, to be sure that it is necessary and appropriate to the package, and to discuss implementation details.

This will also allow us to better coordinate our efforts, prevent duplication of work, and help you craft the change so that it is successfully accepted into the project.

??? info "Our Availability"
    Please note we are busy people and developping these packages is not our primary priority at work.
    We may take some time to reply.

## Submission guidelines

#### Submitting an issue

Before you submit an issue, please search the issue tracker, maybe an issue for your problem already exists and the discussion might inform you of fixes or workarounds readily available.

If you are submitting a bug report, please also provide a minimal scenario to reproduce it.

#### Submitting a Pull Request (PR)

First, search GitHub for an open or closed PR that relates to your submission.
If you do not find a related issue or PR, or if your PR is the implementation for an issue you open, go ahead.

1. **Development**: Clone the project, set up your branch and development environment, make your changes, and add descriptive messages to your commits.
  Please reference the issue number in your commit header messages so that your commits appear on the issue tracker.

2. **Build**: Before submitting changes, please make sure tests pass and that the package properly installs.
  Most projects come with a Makefile to help with this, and you can get an overview of the available targets with `make help`.

3. **Pull Request**: After having worked on your changes and pushed them to Github, open a Pull Request to the master branch.
  Review and approval by at least one of our team members is required before accepting changes.
  If new changes are suggested, make the required updates and push the changes again.
  Please do not require a review until all the quality checks pass.

#### Quality checks

- Unit and accuracy tests are run automatically through CI [Github Actions][gh_actions]{target=_blank}.
  A `README.md` file in the `.github/workflows` directory details our CI jobs.
- Additional checks for code-complexity, design-rules, test-coverage and duplication are made through [CodeClimate][codeclimate]{target=_blank}.
- Pull requests implementing functionality or fixes are merged into the master branch after passing CI, and a reviewer's approval.

After your PR is accepted by a team member, please select **`squash and merge`** to merge into master.
Afterwards, you can safely delete your branch and close the issue. 

## Python Guidelines

We strive to use a common codestyle for our software.
Please follow these guidelines to keep code cohesion up, and git diffs down.

In case you want to contribute to a package's development, you should install it in `editable` mode:
```
git clone https://github.com/pylhc/package_name
pip install --editable package_name
```

??? tip "Installing Extras"
    You can install extra dependencies (as defined in `setup.py`) suited to your use case with the following commands:
    ```
    pip install --editable package_name[test]
    pip install --editable package_name[test,doc]
    pip install --editable package_name[all]
    ```
    
    For development purposes, we recommend using the `all` extra to be fully set up.

### Naming Conventions

Overall, please abide by [PEP8][pep8]{target=_blank}:

- Module, functions, methods, attributes and local variable names: use **`snake_case`**.
  Example: `segment_by_segment.py`, `get_phase.py`.
- Class names: use **`PascalCase`**.
  Example: `FileWriter`, `FixedTfs`.
- Module constants: Uppercase words divided by underscores.
  Example: `INDEX_ID`, `DEFAULT_COLUMN_WIDTH`.
- Private methods, functions and variables: see above, but precede the name by an underscore.
  Example: `_validate_index_type`, `_get_header_line`.

### Code Structure

Make the code as readable as possible, both for collaborators and future you.

- Use descriptive variable names.
- Use descriptive function names.
- Type hint your code.
- Respect the max line length of 100 characters as much as possible.
- Divide code blocks into simple functions.
- Strive to write [pure functions][pure_functions]{target=_blank}.
- Avoid code duplication.
- Respect the [Zen of Python][zen_python]{target=_blank}.

We use [PyCharm][pycharm]{target=_blank} as IDE in the team.

### Docstrings Convention

To be compatible with our automatic API documentation generator, please respect [Sphinx][sphinx]{target=_blank} conventions.


[omc3_issues]: https://github.com/pylhc/omc3/issues/new
[gh_actions]: https://github.com/features/actions
[codeclimate]: https://codeclimate.com/
[pep8]: https://www.python.org/dev/peps/pep-0008/
[pure_functions]: https://en.wikipedia.org/wiki/Pure_function
[zen_python]: https://www.python.org/dev/peps/pep-0020/
[pycharm]: https://www.jetbrains.com/pycharm/
[sphinx]: https://www.sphinx-doc.org/en/master/
