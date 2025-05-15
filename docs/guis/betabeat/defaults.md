# Defaults

Defaults can be set by a file named `bbgui_user.properties` (with the above syntax) in either the **current working directory** (from where you run the GUI), or in **your home folder**.
The latter is only used if there is no such file in the current working directory.

If you want to use a specific file named anything and located anywhere, you can also **give the path to this file as the first and only argument** when starting the GUI.
It is also possible to set each of these default values by passing them as flag arguments to the GUI call, e.g:

```bash
--beam LHCB1 --inputPath /some/afs/location/with/your/data/
```

## Beam Selection Defaults

The GUI defaults to specific locations for which `python` binary to use, the input path of you data, etc.
Different key-value pairs can be set inside for the desired defaults, for example:

```ini
beam = LHCB2
inputPath = /some/afs/location/with/your/data/
outputPath = /some/afs/location/with/your/results/
pythonPath = /some/afs/location/with/your/python-env/bin/python
loadData=False  # Load already existing data in the outputPath into the GUI
oldFolderStructure=False   # Put `models` folder at top level (BBS legacy)
```

For details see the [Beam Selection](beam_selection.md) page.

## Additional GUI Defaults

Additionally, there are some GUI settings that can either only be set via arguments or
modify/set the default value in the GUI fields:

```ini
consoleLogging=False   # activate additional logging  (visible if started from terminal)
checkFreeSpace=False   # check fee space at GUI start (visible if started from terminal)

# BPM-Panel
runOptics=False  # set the tickbox next to the `Analyse` button

# Analysis-Panel
autoclean.limit=0.1  # set the autoclean limit
clean.sigmas=2       # set the number of sigmas for the autoclean
clean.bounds=0.7     # this ratio of points needs to remain otherwise cleaning aborts

# Amplitude-Detuning-Window
ampdet.tunecut=0.05  # limit around the given tune to exclude from the BBQ tune
ampdet.window=100    # length of the moving average window for the BBQ tune
ampdet.outlierLimit=0.0002  # Cut on outliears around the mean
ampdet.usePreviousBBQ=False  # Use previously extraced BBQ data if present
```

For more details about these functions see the [BPM-Panel](bpm_panel.md), [Analysis-Panel](analysis_panel.md) and [Amplitude-Detuning](ampdet.md) pages.

## Default Settings

When saving the GUI settings, a similar file `settings_xxx.properties` is created.
Instead of loading these settings manually, you can also copy all or a selection of the entries
from the output file into your `bbgui_user.properties` and they will be set automatically when the GUI is started.

For details see the [Settings](settings.md) page.
