# Defaults

## Beam Selection Defaults

(For details see the [Beam Selection](beam_selection.md) page)

The GUI defaults to specific locations for which `python` binary to use, the input path of you data, etc.
Different key-value pairs can be set inside for the desired defaults, for example:

```bash
beam = LHCB1
inputPath = /some/afs/location/with/your/data/
outputPath = /some/afs/location/with/your/results/
pythonPath = /some/afs/location/with/your/python-env/bin/python
loadData=False  # True: Load already existing data in the outputPath into the GUI
oldFolderStructure=False   # True: Put `models` folder at top level instead of the current machine folder (BBS legacy)
```
These values can be set by a file named `bbgui_user.properties` (with the above syntax) in either the **current working directory** (from where you run the GUI), or in **your home folder**. 
The latter is only used if there is no such file in the current working directory.

If you want to use a specific file located anywhere, you can also give the path to this file as the first and only argument when starting the GUI.
It is also possible to set each of these default values by passing them as flag arguments to the GUI call, e.g: 

```
--beam LHCB1 --inputPath /some/afs/location/with/your/data/
```

## Additional GUI Defaults

Additionally, there are some GUI settings that can either only be set via arguments or
modify the default value in the GUI:

```bash
consoleLogging=True   # activate additional logging into the terminal (only visible if started from terminal)
checkFreeSpace=True   # check fee space at GUI start (only visible if started from terminal)

# BPM-Panel
runOptics=True  # set the tickbox next to the `Analyse` button to also run the optics analysis by default

# Analysis-Panel
autoclean.limit=0.1  # set the autoclean limit 
clean.sigmas=2  # set the number of sigmas for the autoclean
clean.bounds=0.7  # when cleaning, this ratio needs to remain otherwise the cleaning is aborted

# Amplitude-Detuning-Window 
ampdet.tunecut=0.05  # limit around the given tune to exclude from the natural tune when fitting
ampdet.window=100  # length of the moving average window for the natural tune
ampdet.outlierLimit=0.0002   # Cut on outliears around the mean 
ampdet.usePreviousBBQ=True  # Do not extract BBQ data if there is already data present
```

For more details about these functions see the [BPM-Panel](bpm_panel.md), [Analysis-Panel](analysis_panel.md) and [Amplitude-Detuning](ampdet.md) pages.

## Default Settings

(For details see the [Settings](settings.md) page)

When saving the GUI settings, a similar file `settings_xxx.properties` is created.
Instead of loading these settings manually, you can also copy all or a selection of these settings
from the output file into the `bbgui_user.properties` and they will be set automatically when the GUI is started.
