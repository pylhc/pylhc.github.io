# Managing the Repositories

While many people contribute to our code-bases, this page is for the elect few who are responsible for maintaining them.
You will need access to the service accounts to make use of the information contained in this page.

## Lintrack

`lintrack` refers to the location of the codebase in the TN

```bash
/afs/cern.ch/eng/sl/lintrack/
```

as well as the service account handling the access to it.

The service account was created as in the past direct access to these repositories lead to
accidental changes that affected all users.
Limiting access to the service account ensures an active decision to make changes and thus avoids unwanted changes and even data loss,
which can be especially troublesome if only detected online during CCC measurements.

You can log into the `lintrack` account with the following command:

```bash
ssh lintrack@lxplus.cern.ch
```

You will then be greeted with a welcome message and some information about shortcuts we have set up for quick access and management of the repositories.

!!! info "Access"
    Due to CERN regulations, you cannot log into the `lintrack` account from outside CERN.

## Github

The settings for the organization `pylhc` should be automatically available to you, if you have been given the right permissions (either `admin` or `code owner`).

Our repositories use the [`.github`][pylhc_github] configuration repository to manage

- Issue Templates
- Workflows
- Labels

Of these, the workflow to [assign labels to all repositories][pylhc_labels_workflow] is special:
This workflow is triggered on pushes to the `master` branch of this repository and assigns
the [defined labels][pylhc_labels_json] to all repositories defined in the workflow.

While the other workflows are usually triggered directly via workflow inheritance from the other repositories, e.g. via

```yaml
jobs:
    tests:
        uses: pylhc/.github/.github/workflows/cron.yml@master
```

they automatically inherit the `GITHUB_TOKEN` of that repository and have access to that repositories data.
The labels-workflow does not have this access and is using a limited personal access token (PTA) instead,
which is saved as the `ISSUE_WRITE_TOKEN` secret.
This token is provided by the `pylhctokens` service account and needs to be renewed on a regular basis.

!!! info "Update Github Actions!"
    Many of the workflows are using pre-defined github actions.<br>
    Check them sometimes for updates and try to keep their versions up-to-date!

### pylhctokens

This service account was originally created to give workflows access to the repos, until github introduced the automatically generated `GITHUB_TOKEN`.
Nowadays we only use it to assign labels to all repositories.

To log into the `pylhctokens` account you need password and 2FA authentication.

### CODEOWNERS

To avoid malicious or accidental changes to the repositories, the `master` branches are locked (Repo -> Settings -> Branch protection)
and reviews are required before pull requests can be merged.

The approved reviewers are handled via the `approved-reviewers` group in the `pylhc` organization's teams
which are assigned as code owners to each repository.
For that purpose, each repository has a `CODEOWNERS` file, which can be found in the `.github` folder of the repository.

For more details, see the [official documentation][github_codeowners].

## PyPI

The access to [PyPI][pypi] is provided by the `pylhc` service account, for which you will need password and 2FA authentication.

Publishing access is given to the github workflows via [API-Token](https://pypi.org/help/#apitoken) (Settings -> Account Settings -> API Tokens) to all repositories of the `pylhc` organization.
This is done by using the [publish workflow][pylhc_publish] and passing the token as secret:

- `PYPI_USERNAME` : `__token__` (literal string)
- `PYPI_PASSWORD` : the token value, including the pypi- prefix

which are usually inherited from each of the repos publishing workflows.

## Zenodo

There is no special account for [Zenodo][zenodo] access.
Zenodo should be able to be reached with your normal account, preferrably your `github`,
which, if linked correctly, will allow Zenodo to also reach the `pylhc`-Organization repositories.

To add a new repository to Zenodo, you need to make sure that the `.zenodo.json` file is correct (examples can be found in our repositories).
**Before making your first release**, you need to go into the [Zenodo github settings][zenodo_github] (down-arrow on your user on the top right) and follow the instructions there:

- Flip the switch to `On`
- Create a release on `github` -> The page for your repo should now be visible on Zenodo!
- Add the `badge` to your `README.md`


[pypi]: https://pypi.org
[zenodo]: https://zenodo.org
[zenodo_github]: https://zenodo.org/account/settings/github/
[pylhc_github]: https://github.com/pylhc/.github
[pylhc_publish]: https://github.com/pylhc/.github/blob/master/.github/workflows/publish.yml
[pypi_apitoken]: https://pypi.org/help/#apitoken
[pylhc_labels_workflow]: https://github.com/pylhc/.github/blob/master/.github/workflows/assign_labels_to_all_repos.yml
[pylhc_labels_json]: https://github.com/pylhc/.github/blob/master/labels/labels.json
[github_codeowners]: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners