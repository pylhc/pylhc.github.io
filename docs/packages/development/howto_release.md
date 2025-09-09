# Release Process of OMC Packages

Our packages' release process to PyPI is automated through [Github Actions][github_actions]{target=_blank}, and triggered by manually creating a release from the Github repository.

When the final changes for a release, including updating the package's version number and updating the `Changelog.md` file, have been merged into the `master` branch, the release process is as follows:

1. Go to the `Releases` section and click `Draft a new release` in the top right.
2. Enter the package's version number in the `tag version` field.
3. Enter a `Release title` - we usually go by `Release <version_number>`.
4. Enter a description for the `added`, `fixed` and `changed` elements, which is usually the same content as the one added to the `CHANGELOG.md` file.
5. Click `Publish Release`. A snapshot of the source code from `master` will automatically be attached.

A `publish` workflow will be triggered, build source distribution and wheels and upload these to [`pylhc`'s PyPI][pypi_releases]{target=_blank}.

*[PyPI]: The Python Package Index

[github_actions]: https://github.com/features/actions
[pypi_releases]: https://pypi.org/search/?q=pylhc
