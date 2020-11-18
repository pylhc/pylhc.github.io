# The beam selection Window

!!! todo
    Include screenshot of Beam-Selection Window and describe the settings.


!!! tip "Setting Your Defaults"
    The GUI defaults to specific locations for which `Beta-Beat.src` directory to use, the input path of you data, etc.
    Different key-value pairs can be set inside for the desired defaults, for example:
    
    ```bash
    beam = LHCB1_RUNII_2018
    inputPath = /some/afs/location/with/your/data/
    outputPath = /some/afs/location/with/your/results/
    betaBeatPath = /some/afs/location/with/your/Beta-Beat.src/
    loadData=True
    ```
    These values can be set by a file named `bbgui_user.properties` (with the above syntax) in either the current working directory, from where you run the GUI, or in your home folder. 
    The latter is only used if there is no such file in the current working directory.

    If you want to use a specific file located anywhere, you can also give the path to this file as the first and only argument when starting the GUI.
    It is also possible to set each of these default values by passing them as flag arguments to the GUI call, e.g: 
    
    ```
    --beam LHCB1_RUNII_2018 --inputPath /some/afs/location/with/your/data/
    ```

??? tip "Additional Default Settings"
    Additionally, there are some settings that can only be set via arguments.
    Their keys and default values are:
    
    ```bash
    oldFolderStructure=True
    consoleLogging=False
    checkFreeSpace=False
    ```

    - `oldFolderStructure` refers to the folder structure, where the `models` folder is at top level and contains the machines as subdirectories.
      Setting this value to `False` assumes (and creates) the models in a `Models` folder on the same level as `Measurements` and `Results`, i.e. within the machine-folders.
    - `consoleLogging` activates additional logging into the terminal.
      The effect is only visible if the GUI was started from the console.
    - `checkFreeSpace` activates a quick check of the available space upon start of the GUI.
      The result of this check is logged in the console, and hence also only visible if the GUI is started via terminal command.