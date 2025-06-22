# Releasing the Beta-Beating GUI

!!! warning "GUI Releases"
    This page describes the process of releasing a new version of the [Beta-Beating GUI](../betabeat/gui.md),
    as this is the main Java GUI we are responsible for.
    The python GUIs are released following the standard [python release process](../../packages/development/howto_release.md).
    The release of the other Java GUIs should be similar to this guide, but please contact the respective maintainer of the GUI for further details.

R

```bash
bob release
```

```text
http://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-app-beta-beating-omc3/
```

!!! warning "Breaking Things"
    In contrast to our `python` backend development, there is no real CI and testing for the GUIs.
    This means, that you **need to make sure** manually, that everything works as expected and no functionality is broken, before release.
    In case of major bugs occuring online, you can always revert to using a previous version from the [CAS][cas_cern] (search for `omc3` or `beta-beating`).

## Devrelease


```bash
bob devrelease
```


```text
http://bewww.cern.ch/ap/deployments-dev/applications/cern/lhc/lhc-app-beta-beating-omc3/
```

## Creating a JAR

Creating a `.jar` needs to be done via CBNG as well, so that the correct dependencies are included and the main class is set.
To achieve this, a new task has been implemented in the [`build.gradle`][bbgui_build_gradle], which automatically creates a `lhc-app-beta-beating-omc3-X.X.X-all.jar` file in the `build/libs` folder.

To run this task, `omcJar` from the GUI (e.g. in VSCode in `Gradle > Tasks > other > omcJar`) or run

```bash
bob omcJar
```

from the command line.

??? info "Pitfalls creating a JAR"
    Creating a runnable `.jar` file is not a trivial task and there had been a lot of trial-and-error to get it right.
    For some reason, a lot of files need to be **excluded** from the `.jar` file, as otherwise it will not run.
    If you need to create a new method to create the `.jar`, check the [build.gradle][bbgui_build_gradle] for reference.

[bbgui_build_gradle]: https://gitlab.cern.ch/acc-co/lhc/lhc-app-beta-beating/-/blob/master/build.gradle
[bbgui_product_xml]: https://gitlab.cern.ch/acc-co/lhc/lhc-app-beta-beating/-/blob/master/product.xml
[cas_cern]: https://cas.cern.ch
