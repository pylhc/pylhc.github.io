# Zensical Migration

This file records the remaining TODOs for the [zensical](https://zensical.org/) migration of the website builder.

Note: The `zensical` devs currently recommended *not* to switch from the `mkdocs.yml` to the `zensical.toml` configuration files for existing projects. Work is done on their side to make sure `zensical` ingests the previous file just fine, and will provide a migration path in a later release.

## Content

- [ ] Refresh the `How to edit this wiki page`
- [x] Transition the logbooks out of the "Resources" tab and into its own

## Cosmetic

- [ ] The header color stays white/black despite our specification for a blue that blends with the landing page's content.
- [ ] Custom heart admonition (in Resources, help & contacts) does not render properly

## Build

- [x] Prepare new GitHub Actions workflows using Zensical
- [ ] Remove the old dependencies from requirements.txt before merging
