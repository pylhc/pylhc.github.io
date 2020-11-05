# Contributing

Want to report a bug, request a feature or contribute some code?

We welcome contributions, but before you do, please read the following guidelines.

## Submission context

#### Got a question or problem?

For quick questions there's no need to open an issue as you can reach us at [`pylhc@github.com`](mailto:pylhc@github.com).

??? note "Our Availability"
    Please note we are busy people and developping `omc3` is not our primary priority at work.
    We may take some time to reply.

#### Found a bug?

If you found a bug in the source code, you can help us by [submitting an issue][omc3_issues]{target=_blank} on GitHub.
If you wish to contribute a solution, you can submit a Pull Request with a fix.
However, before doing so, please read the submission guidelines bellow.


#### Missing a feature?

You can request a new feature by [submitting an issue][omc3_issues]{target=_blank} on GitHub.
If you would like to implement a new feature, please submit an issue with a proposal first, to be sure that it is necessary and appropriate to this package.

This will also allow us to better coordinate our efforts, prevent duplication of work, and help you to craft the change so that it is successfully accepted into the project.

## Submission guidelines

#### Submitting an issue

Before you submit an issue, please search the issue tracker, maybe an issue for your problem already exists and the discussion might inform you of workarounds readily available.

We want to fix all the issues as soon as possible, of course, but before fixing a bug we need to reproduce and confirm it: please provide a minimal reproduction scenario.

Unfortunately, we are not able to investigate or fix bugs without a minimal reproduction scenario, so if we don't hear back from you we may close the issue.

#### Submitting a Pull Request (PR)

First, search GitHub for an open or closed PR that relates to your submission.
You don't want to duplicate effort.
If you do not find a related issue or PR, go ahead.

1. **Development**: Clone the project, set up your branch and development environment, make your changes, and add descriptive messages to your commits.
  Please reference the issue number in your commit header messages so that your commits appear on the issue tracker.

2. **Build**: Before submitting changes, please make sure tests pass and that the package properly installs.
  The project comes with a Makefile to help with this, you can get an overview of the available targets with `make help`.
  This is a mandatory requirement for your PR to get accepted, as the package should at all times be installable without trouble through GitHub.

3. **Pull Request**: After having worked on your changes and pushed them to Github, open a Pull Request to the master branch.
  Review and approval by at least one of our team members is required before accepting changes.
  If new changes are suggested, make the required updates and push the changes again, which will automatically update your PR.

After your PR is accepted by a team member, **please select `squash and merge`** to merge into master.
Afterwards, you can safely delete your branch and close the issue. 

## Python Coding Guidelines

We strive to use a common codestyle for our software.
Please follow these guidelines to keep code cohesion up, and git diffs down.

### Naming Conventions

Overall, please abide by [PEP8][pep8]{target=_blank}:

- Module, functions, methods, attributes and local variable names: use `snake_case`.
  Example: `segment_by_segment.py`, `get_phase.py`.
- Class names: use `PascalCase`.
  Example: `FileWriter`, `FixedTfs`.
- Module constants: Uppercase words divided by underscores.
  Example: `INDEX_ID`, `DEFAULT_COLUMN_WIDTH`.
- Private methods, functions and variables: see above, but precede the name by an underscore.
  Example: `_validate_index_type`, `_get_header_line`.

### Code Structure

Make the code as readable as possible, both for collaborators and future you.

- Use descriptive variable names.
- Use descriptive function names.
- Respect the max line length of 100 characters.
- Divide code blocks into simple functions.
- Avoid code duplication.
- Respect the [Zen of Python][zen_python]{target=_blank}.

We use [PyCharm][pycharm]{target=_blank} as IDE in the team.

### Docstrings Convention

To be compatible with our automatic API documentation generator, please respect [Sphinx][sphinx]{target=_blank} conventions.

[omc3_issues]: https://github.com/pylhc/omc3/issues/new
[pep8]: https://www.python.org/dev/peps/pep-0008/
[zen_python]: https://www.python.org/dev/peps/pep-0020/
[pycharm]: https://www.jetbrains.com/pycharm/
[sphinx]: https://www.sphinx-doc.org/en/master/