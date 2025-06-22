# Releasing the Beta-Beating GUI

!!! warning "GUI Releases"
    This page describes the process of releasing a new version of the [Beta-Beating GUI](../betabeat/gui.md),
    as this is the main Java GUI we are responsible for.
    The python GUIs are released following the standard [python release process](../../packages/development/howto_release.md).
    The release of the other Java GUIs should be similar to this guide, but please contact the respective maintainer of the GUI for further details.

## Normal Release

!!! tip "Preparation"
    - Add new features to the [changelog][bbgui_changelog]:<br>
      To track changes and easily identify breaking changes, please add them to the [CHANGELOG.md][bbgui_changelog].
      Preferrably, this should be done already before merging the changes into the master branch, but should be at least be ensured to be **up-to-date during release**.
    - Update version in [product.xml][bbgui_product_xml]:<br>
      The version number needs to be updated in the [product.xml][bbgui_product_xml] file.
      **If an already used version number/identifyer is used, the release procedure will fail.**
    - Have a clean repository and no uncommitted changes:<br>
      The release process runs in the current folder of your local machine and will fail if there are any uncommitted changes in the repository.
      **Make sure your repository is synced and up-to-date.**

!!! success "How to run"
    To run the task for a **normal release**, start CBNG's `release` from the GUI (e.g. in VSCode in `Gradle > Gradle Projects > betabeating-app > Tasks > cbng > release`) or run

    ```bash
    bob release
    ```

    from commandline.

This task will build the project, run tests (if they existed, see admonition below) and automatically upload the `.jnlp` file to the
[be deployment servers][deployment_url] at:

    http://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-app-beta-beating-omc3/

On this server, all previous versions can be found, and the latest version is automatically linked within the `PRO` folder,
which is used to start the GUI from the CCM in the CCC.
Older versions can be run directly via [jws using the links to the `.jnlp` file][jws_programs].
An entry on the [CAS][cas_cern] will be created for the new release.
The release is also [automatically tagged][bbgui_tags] with the prefix `release-` and the version number in the [product.xml][bbgui_product_xml] file.

!!! warning "Breaking Things"
    In contrast to our `python` backend development, there is no real CI and testing for the GUIs.
    This means, that you **need to make sure** manually, that everything works as expected and no functionality is broken, before release.
    In case of major bugs occuring online, you can always revert to using a previous version from the [CAS][cas_cern] (search for `omc3` or `beta-beating`).

## Dev-Release

!!! success "How to run"
    To run the task for a **dev release**, start CBNG's `devrelease` from the GUI (e.g. in VSCode in `Gradle > Gradle Projects > betabeating-app > Tasks > cbng > devrelease`) or run

    ```bash
    bob devrelease
    ```

    from commandline.

This release procedure will upload the `.jnlp` file to the [be deployment servers][deployment_dev_url] at:

    http://bewww.cern.ch/ap/deployments-dev/applications/cern/lhc/lhc-app-beta-beating-omc3/

(note the `deployments-dev` distinction).
Older versions can be run directly via [jws using the links to the `.jnlp` file][jws_programs].
An entry on the [CAS][cas_cern] will be created for the new release yet the entry it will be only available for 30 days.
After that time you need to find the `.jnlp` file manually from the [deployment servers][deployment_url].

There is no special preparations required for this release type and tests are not autoamatically run.
The version from the [product.xml][bbgui_product_xml] will be used, but if the same version has been released already, **the files on the [deployment servers][deployment_url] will be overwritten**.



## Creating a JAR

Creating a `.jar` needs to be done via CBNG as well, so that the correct dependencies are included and the main class is set.
To achieve this, a new task has been implemented in the [`build.gradle`][bbgui_build_gradle], which automatically creates a `lhc-app-beta-beating-omc3-X.X.X-all.jar` file in the `build/libs` folder.

!!! success "How to run"
    To run the task to **create a JAR**, start CBNG's `omcJar` from the GUI (e.g. in VSCode in `Gradle > Gradle Projects > betabeating-app > Tasks > other > omcJar`) or run

    ```bash
    bob omcJar
    ```

    from commandline.

??? info "Pitfalls creating a JAR"
    Creating a runnable `.jar` file is not a trivial task and there had been a lot of trial-and-error to get it right.
    For some reason, a lot of files need to be **excluded** from the `.jar` file, as otherwise it will not run.
    If you need to create a new method to create the `.jar`, check the [build.gradle][bbgui_build_gradle] for reference.

[bbgui_build_gradle]: https://gitlab.cern.ch/acc-co/lhc/lhc-app-beta-beating/-/blob/master/build.gradle
[bbgui_product_xml]: https://gitlab.cern.ch/acc-co/lhc/lhc-app-beta-beating/-/blob/master/product.xml
[bbgui_changelog]: https://gitlab.cern.ch/acc-co/lhc/lhc-app-beta-beating/-/blob/master/CHANGELOG.md
[deployment_url]: http://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-app-beta-beating-omc3/
[deployment_dev_url]: http://bewww.cern.ch/ap/deployments-dev/applications/cern/lhc/lhc-app-beta-beating-omc3/
[bbgui_tags]: https://gitlab.cern.ch/acc-co/lhc/lhc-app-beta-beating/-/tags
[cas_cern]: https://cas.cern.ch
[jws_programs]: ../../resources/links.md#jws-programs

*[CCC]: CERN Control Center
*[CCM]: Common Console Manager
*[CBNG]: Common Build Next Generation
*[GUI]: Graphical User Interface
*[CAS]: Controls Artifact Service
*[jws]: Java Web Start
