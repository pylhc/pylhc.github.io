# IDE Setup

The easiest way to develop the GUI is using the modified [Eclipse](#eclipse) versions provided by [Accsoft-Eclipse][accsoft_eclipse]{target=_blank}.
There is also an [installation guide available][accsoft_eclipse_wiki]{target=_blank}.

For people using pycharm it might make sense to use [IntelliJ IDEA](#intellij-idea), however we do not yet know how to export a JAR (see also [GUI Releases](releases.md)).

As both IDEs require [CommonBuildNextGeneration (CBNG)][cbng_wiki]{target=_blank} to resolve dependencies and make releases, one should either run these from somewhere in the Technical Network (e.g. from the `dev-server`) or mount the required paths via `sshfs` as described [here](../../general/tricks.md#mounting-tn-resources-on-gn-machines).

## Installation

=== "Eclipse"
    Download your preferred version from their [download page][accsoft_eclipse]{target=_blank} and install.
    With this version, `CBNG` comes automatically installed and can be used by simply dragging the desired project into the [CBNG window][cbng_eclipse]{target=_blank}.
    For more info see the [accsoft eclipse wiki][accsoft_eclipse_wiki]{target=_blank}.

=== "IntelliJ IDEA"
    Download your preferred version from their [download page][idea_download]{target=_blank} and install.
    `CBNG` needs to be setup in IDEA manually, by setting the Gradle home path in:
    ```
    File -> Settings -> Build, Execution, Deployment -> Build Tools -> Gradle
    ```
    to the specified location `/user/pcrops/devtools/CBNG/PRO/`
    
    A more extensive guide can be found in the [CBNG Wiki for IDEA integration][cbng_idea]{target=_blank}.
    Alternatively, run CBNG directly [from the commandline](#cbng-from-commandline) instead.

=== "CBNG from the Command Line"
    Another sometimes easier alternative that works with any IDE is to run CBNGs `bob` with the desired command (e.g. `build`, `dependencies`, `eclipse`, `idea`) in the folder of the project from the commandline. 
    The full path to `bob` is:
    ```
    /user/pcrops/devtools/CBNG/PRO/bin/bob
    ```
    
    !!! info ""
        See `bob --help` for instructions about its commands.

## Importing a Project

The project can be imported using the git-integrations of the IDEs directly, using the Gitlab paths below.
This should be straightforward, but you are giving up some control.
In the next subsections the manual path of getting the source-code into the IDE is outlined in the hope to point to some pitfalls that may occur and how to avoid them.

Firstly, you should clone the desired repository to an adequate location on your hard-drive, depending on which project you want to work on:

=== "Beta-Beat GUI"
    ```bash
    git clone https://gitlab.cern.ch/acc-co/lhc/lhc-app-beta-beating
    ```

=== "Kmod GUI"
    ```bash
    git clone https://gitlab.cern.ch/acc-co/lhc/lhc-app-kmod
    ```

You then simply import the project into your IDE.

??? warning "IntelliJ Specificity" 
    For IntelliJ, you might have to
    
    1. Create an empty `build.gradle` file if you want to trigger a gradle import dialogue where you need to choose **use local gradle distribution** and set the **gradle home** to `/user/pcrops/devtools/CBNG/PRO/bin/bob` ([as above](#gradlehome))
    2. Go to `File -> Project Structure ... -> Modules` and set the **Dependencies storage format** to `Eclipse (.classpath)`.
    This one you should check on a regular basis, as it tends to reset itself.

To make it runnable, you will have to use CBNG to **resolve dependencies** and **build** the project first.
Depending on your IDE you should run CBNGs `eclipse` or `idea` followed by `build`. 
Running `dependencies` can help.

!!! warning ""
    No one in the OMC-Team is a `CBNG` expert, and sometimes running these commands leads to the desired outcome (of a runnable project) or not depending on the color of the DG's clothing.

## Running the GUI

If everything worked fine, the Gui should now be runnable via the `void main()` function in the `main.Main.java`, which can be invoked by **right-clicking on `main.Main`** and choosing **Run** or manually setting a Java **Run configuration** in the `Run` menu.

## Useful Links

* [CBNG Wiki][cbng_wiki]{target=_blank}
* [Accsoft-Eclipse Downloads][accsoft_eclipse]{target=_blank}
* [Accsoft Eclipse Wiki][accsoft_eclipse_wiki]{target=_blank}

[idea_download]: https://www.jetbrains.com/idea/download/
[cbng_wiki]: https://wikis.cern.ch/display/DVTLS/CBNG
[cbng_eclipse]: https://wikis.cern.ch/display/DVTLS/CBNG+-+Eclipse+Integration
[cbng_idea]: https://wikis.cern.ch/display/DVTLS/CBNG+-+IntelliJ+IDEA+integration
[accsoft_eclipse]: http://eclipse.cern.ch/
[accsoft_eclipse_wiki]: https://wikis.cern.ch/display/DVTLS/Eclipse+IDE

*[DG]: Director General: Currently Fabiola Gianotti