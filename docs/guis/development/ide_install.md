# IDE Setup
The easiest way to develop the GUI is using the modified [eclipse](#eclipse) versions provided by [Accsoft-Eclipse][accsoft_eclipse].<br>
There is also an [installation guide available][accsoft_eclipse_wiki].

For people using pycharm it might make sense to use [Intellij IDEA](#intellij-idea), yet this comes with some disadvantages, 
as we do not know how to export a JAR (see also [release of GUI](releases.md))

As both IDEs require [CommonBuildNextGeneration (CBNG)][cbng_wiki] to resolve dependencies and make releases,
one should either run these from somewhere in the Technical Network (e.g. from the dev-server) or mount the required paths via `sshfs` as described [here](../../general/tricks.md#mounting-tn-resources-on-gn-machines).


## Installation


### Eclipse

Download your preferred version from their [download page][accsoft_eclipse]
and install.

With this version CBNG comes automatically installed and can be used by simply dragging
the desired project into the [CBNG window][cbng_eclipse].


For more info see the [accsoft eclipse wiki][accsoft_eclipse_wiki].



### IntelliJ IDEA

Download your preferred version from their [download page][idea_download]
and install.

CBNG needs to be setup in IDEA manually, by setting the Gradle home path in 
```
File -> Settings -> Build, Execution, Deployment -> Build Tools -> Gradle
```

<a id="gradlehome"></a>
to the `Specified location`:
```
/user/pcrops/devtools/CBNG/PRO/
```

A more extensive guide can be found in the [CBNG Wiki for IDEA integration][cbng_idea]. 

Alternatively, and sometimes more easily, run CBNG directly [from the commandline](#cbng-from-commandline) instead.


### CBNG from commandline
Another alternative that works with any IDE, and is sometimes even easier to use,
 is to run CBNGs `bob` with the desired command (e.g. `build`, `dependencies`, `eclipse`, `idea`)
in the folder of the project from the commandline. 

The full path to `bob` is:
```
/user/pcrops/devtools/CBNG/PRO/bin/bob
```

!!! info
    See `bob --help` for instructions about its commands.


## Importing a Project
### Clone the Repository

First you should clone the desired repository to an adequate location on your harddrive,
depending on which project you want to work on:



!!! important "Beta-Beat Gui"
    ```
    git clone https://gitlab.cern.ch/acc-co/lhc/lhc-app-beta-beating
    ```


!!! important "KMod Gui"
    ```
    git clone https://gitlab.cern.ch/acc-co/lhc/lhc-app-kmod
    ```


### Import Project

You then simply import the project into your IDE.

!!! note 
    For IntelliJ you might have to

    - create an empty `build.gradle` file if you want to trigger a gradle import dialogue
    where you need to choose **use local gradle distribution** and set the **gradle home** to `/user/pcrops/devtools/CBNG/PRO/bin/bob` ([as above](#gradlehome))
    - go to `File -> Project Structure ... -> Modules` and set the **Dependencies storage format** to `Eclipse (.classpath)`.
    This one you should check on a regular basis, as it tends to reset itself.


To make it runnable you will have to use CBNG to **resolve dependencies** and **build** the project first.
Depending on your IDE you should run CBNGs `eclipse` or `idea` followed by `build`. 
Also running `dependencies` can help.

!!! warning
    To be honest, no one in the OMC-Team is a CBNG expert and sometimes it feels like, that depending on 
    the color of the DG's clothing on that day, running these commands in either order or multiple times 
    leads to the desired outcome (of a runnable project).


## Running the Gui
If everything worked fine, the Gui should now be runnable via the `void main()` function in the `main.Main.java`,
which can be invoked by **right-clicking on `main.Main`** and choosing **Run** or manually setting a Java **Run configuration**
in the `Run` menu.



## Useful Links
[CBNG Wiki][cbng_wiki]<br>
[Accsoft-Eclipse Downloads][accsoft_eclipse]<br>
[Accsoft Eclipse Wiki][accsoft_eclipse_wiki]<br>

[idea_download]: https://www.jetbrains.com/idea/download/
[cbng_wiki]: https://wikis.cern.ch/display/DVTLS/CBNG
[cbng_eclipse]: https://wikis.cern.ch/display/DVTLS/CBNG+-+Eclipse+Integration
[cbng_idea]: https://wikis.cern.ch/display/DVTLS/CBNG+-+IntelliJ+IDEA+integration
[accsoft_eclipse]: http://eclipse.cern.ch/
[accsoft_eclipse_wiki]: https://wikis.cern.ch/display/DVTLS/Eclipse+IDE

*[DG]: Director General: Fabiola Gianotti