# Menus & Settings

This page documents the menu bar, configurable settings, and log console of the Segment-by-Segment GUI.

## Menus

### SbS-Gui

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/menu_sbs_gui.png" width="100%" alt="Menu SbS-Gui"/>
  <figcaption>The SbS-Gui menu.</figcaption>
  </center>
</figure>

- **Settings**: Open the [settings dialog](#settings).
- **Exit**: Close the GUI.

### View

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/menu_view.png" width="100%" alt="Menu View"/>
  <figcaption>The View menu.</figcaption>
  </center>
</figure>

- **Full Screen**: Toggle full-screen mode.
- **Plotting Settings**: Quick access to the checkboxes of the [plot settings](#plot-settings).
- **Log Console**: Show or hide the [log console](#log-console) at the bottom of the GUI.

### Help

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/menu_help.png" width="100%" alt="Menu Help"/>
  <figcaption>The Help menu.</figcaption>
  </center>
</figure>

- **Reload Data**: Reload the data from the input files. This is useful if you have made changes to the input files and want to see the updated results without restarting the GUI.
- **Show Help**: Open the help dialog with some main instructions on how to use the GUI.
- **About**: Opens the about dialog, which displays some information about the GUI, e.g. the version.

## Settings

The settings dialog is accessible from the `SbS-Gui` menu.
Hints are available on hovering over each setting's text.

### Main Settings

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/settings_main.png" width="100%" alt="Main Settings"/>
  <figcaption>The main settings.</figcaption>
  </center>
</figure>

- **Working Directory**:
The directory where the input files are located.
The GUI will use this directory as the default directory when opening file dialogs for loading optics and measurement data.

- **Autoload Segments**:
Automatically load existing segments when loading a new measurement optics directory.
This looks for files created by the GUI in earlier runs and for now only works if the segment has actually been run.
(Future implementation: also check for json files - see `Save` and `Load` buttons.)

- **Auto-Add Default Segments**:
Automatically add default segments when loading a new measurement optics directory.

- **Suggest Correctors**:
When opening the [corrections dialog](corrections.md#corrected-and-expected-plots) for a new/not yet existing correction file, suggest correctors based on the optics and measurement data.

### Plot Settings

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/settings_plotting.png" width="100%" alt="Plot Settings"/>
  <figcaption>The plotting settings.</figcaption>
  </center>
</figure>

- **Show Model**: Adds markers for the location of elements in the model to the plots.
- **Show Legend**: Show legends in the plots.
- **Marker Size**: Size of the markers in the plots.
- **Expectation**: If run with corrections, show the expected measurement difference instead of the corrected model difference (details in [Finding Corrections](corrections.md#corrected-and-expected-plots)).
- **Forward Propagation**: Show forward propagation results (arrows to the right).
- **Backward Propagation**: Show backward propagation results (arrows to the left).
- **Connect X**: Keep the same X-Axis limits for both charts when zooming.
- **Connect Y**: Keep the same Y-Axis limits for both charts when zooming.
- **Reset Zoom**: When changing segments, reset the zoom to the original view.
                  When deactivated, the current limits will be kept when changing segments, which can be useful for comparing different segments or optics with the same zoom level.
- **Same Segment Start**: Plot segments together, even if they have different start BPMs. Not recommended, as it can lead to confusion and misinterpretation of the results, as they will both start at the same point in the plot, even though they represent different locations in the accelerator.
- **Model Location**: Plot segments relative to the model location, i.e. their position in the accelerator, which allows for easy comparison of segments with different start BPMs. If deactivated, segments will start at a location of zero at their start BPM.

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/view_model_location.png" width="100%" alt="Model Location"/>
  <figcaption>Example of two segments with different start BPMs when plotted with `Model Location` activated.</figcaption>
  </center>
</figure>

## Log Console

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/log_console.png" width="100%" alt="Log Console"/>
  <figcaption>The log console.</figcaption>
  </center>
</figure>

The log console displays logging output from both GUI actions and the underlying Python modules called during the analysis.
It can be expanded or collapsed using the arrow control and closed entirely with the "X" button on its right side; if closed, it can be re-enabled through the [View menu](#view).
The console panel is also movable and resizable within the GUI window.
Right-clicking inside the console opens a context menu that provides access to additional preferences.

!!! tip "Debug Logging"
    By default, the log console is initialized with log level `INFO`.
    To enable more detailed output for debugging purposes, launch the GUI with the `-d` flag (e.g. `python -d`), which sets the log level to `DEBUG`.
