# The Segment-by-Segment GUI

The Segment-by-Segment GUI provides a graphical interface to run the segment-by-segment method on various parts of the machine.
The interface allows users to easily input data, configure settings, run segments and visualize results for various observables.
For information about the Segment-by-Segment method, see its dedicated [explanatory page](../../measurements/physics/sbs.md).

The GUI is launched from the Beta-Beat GUI's [Optics Panel](../betabeat/optics_panel.md) after running a full optics analysis.
With an analysis selected, clicking the ++"Segment-by-Segment"++ button will trigger the GUI to start.
<!-- TODO: check button name -->

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/blank_window.png" width="100%" alt="Blank Window"/>
  <figcaption>Blank window of SbS-GUI as seen when starting the GUI.</figcaption>
  </center>
</figure>

## General Workflow

The typical workflow begins by loading the optics measurement data into the GUI, then defining the segments of the accelerator that you wish to analyse.
Optionally, corrections can also be defined at this stage; these are applied to the model before the analysis is run.

Once the setup is complete, the segment-by-segment analysis can be launched.
During the analysis, optics parameters are propagated from the start and end BPMs through each defined segment.
The propagated values are then compared against the measured data to compute the differences.
Errors from the original BPMs are also propagated through the segment and added in quadrature to the measurement uncertainty.

!!! tip "Choice of First and Last BPMs"
    The measurement values and errors at the location of the first BPM in the segment are the ones used for the propagation.
    Depending on the quality of the measurement at said BPM, the propagation might yield low quality data.
    It can sometimes be a good idea to attempt the segment with a different start BPM (and end BPM for reverse propagation) if encountering this issue.

After the analysis has completed, the results can be visualised directly in the GUI.
The plot shows the difference between the propagated model and the measurement for each segment, allowing you to identify where discrepancies exist and pinpoint the locations of optics errors.
Inspecting both forward and backward propagation helps confirm the error source: if deviations appear after the same location from both directions, that location is likely where the error originates.
See [Understanding the Plot](#understanding-the-plot) for a detailed description of the plot elements.

### Finding Corrections

The corrections applied in the GUI modify the model to match the measurement.
It is important to understand that, in order to actually correct the machine, these corrections generally need to be inverted: the GUI finds what error in the model would reproduce the observed measurement deviation, and the opposite of that error is what should be applied operationally.
Be aware that sign conventions may differ between MAD-X and LSA, so care must be taken when translating correction values from the GUI to the control system.

A practical approach to testing correction schemes is to create multiple [virtual copies](#virtual-copies) of the same measurement.
Virtual copies share the same input data but write their output to separate directories, allowing you to try different correction strategies side by side without duplicating files on disk.
Similarly, creating multiple segments with different start BPMs for the same region of the accelerator lets you evaluate how sensitive the results are to the choice of starting point and whether the correction holds regardless of which BPM anchors the propagation.

When corrections have been applied, the plot shows a dashed line in addition to the solid measurement line.
The [plot settings](settings.md#plot-settings) let you choose what this dashed line represents:

- **Matched value (corr)**: the difference between the propagated corrected model and the nominal propagated model.
  If the correction successfully reproduces the measured errors, this dashed line should lie close to the solid measurement line.
- **Expected value (expct)**: the difference between the measured values and the propagated corrected model.
  This represents the expected outcome of the SbS analysis after the correction has been applied to the machine, and should therefore be close to zero if the correction is effective.

### Segment Grouping and Comparison

When multiple optics are loaded simultaneously, identically defined segments — those sharing the same name, start BPM and end BPM — are automatically grouped together and overlaid on the same plot.
This makes it straightforward to compare results from different measurements or different correction schemes for the same region of the accelerator.
Hovering over a segment entry in the table displays a tooltip showing which loaded optics it belongs to and whether the analysis has been run for each one (i.e. whether the output file exists).
Note that segments with different start or end BPMs are never grouped together, even if they share the same name, because they represent physically different analyses.

When multiple segments are selected, the default behaviour is to only plot together those that share the same start BPM, since the horizontal axis position is relative to the start of the segment.
This constraint can be relaxed via the `Same segment start` option in the [plot settings](settings.md#plot-settings), although doing so is generally not recommended as it can lead to confusion when comparing positions.
Activating the `Model Location` option changes the horizontal axis to show absolute positions in the accelerator rather than positions relative to the segment start, which makes it meaningful to overlay segments with different start BPMs and compare their results directly.

## Understanding the Plot

The main plot area displays the results of the segment-by-segment analysis for the selected segments.
The solid line represents the difference between the propagated model and the measurement: it shows how the measurement compares to the model under the assumption that both share the same value at the start BPM (or the end BPM for backward propagation).
Arrow markers indicate the direction of propagation — rightward arrows for forward propagation and leftward arrows for backward propagation.

If corrections have been applied, a dashed line also appears.
Depending on the [plot settings](settings.md#plot-settings), this shows either the corrected model difference or the expected measurement difference after correction; see the [Finding Corrections](#finding-corrections) section for a detailed explanation of both modes.

When multiple segments or optics are selected, multiple traces can appear in the same plot; see [Segment Grouping and Comparison](#segment-grouping-and-comparison) for details on how they are overlaid.
Each combination of segment and optics is assigned a consistent color, while different markers and line styles distinguish forward propagation, backward propagation, corrected and expected traces.
When plotting many segments at once, it is advisable not to activate all trace types simultaneously, as the plot can become very crowded and difficult to read.

The tabs above the plot area allow switching between the different optics parameters that are propagated through the segments, such as the phase advance, the $\beta$-function or coupling RDTs.

### Shortcuts

The plot supports the following keyboard and mouse shortcuts for navigation and inspection:

- **Hover**: Show Optics name, BPM name and the value of the point in the plot.
- **Double Click** / **Right Click**: Zoom history back one step (only works for rectangle zoom).
- **Shift + Right Click**: Reset zoom to the original view.
- **Alt + Right Click**: Open the pyqtgraph context menu.
- **Click and Drag**: Draw a rectangle to zoom into a specific area of the plot.
- **Scroll in Graph**: Zoom in and out of the plot, both axis.
- **Scroll over one axis**: Zoom in and out of the plot, only the axis you are scrolling over.

## Menu

### SbS-Gui

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/menu_sbs_gui.png" width="100%" alt="Menu SbS-Gui"/>
  <figcaption>The SbS-Gui menu.</figcaption>
  </center>
</figure>

- **Settings**: Open the [settings dialog](settings.md).
- **Exit**: Close the GUI.

### View

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/menu_view.png" width="100%" alt="Menu View"/>
  <figcaption>The View menu.</figcaption>
  </center>
</figure>

- **Full Screen**: Toggle full-screen mode.
- **Plotting Settings**: Quick access to the checkboxes of the [plotting settings dialog](settings.md#plot-settings). For details, see the [plotting settings section](settings.md#plot-settings).
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

The GUI's settings are accessible from the SbS-Gui menu and are documented on the dedicated [Settings](settings.md) page.
This includes the [main settings](settings.md#main-settings) (working directory, autoload behaviour, corrector suggestions) and the [plot settings](settings.md#plot-settings) (visibility toggles, zoom behaviour, segment grouping options).

## Side Panel

### Loaded Optics

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/loaded_optics.png" width="100%" alt="Loaded Optics"/>
  <figcaption>The loaded optics section in the side panel.</figcaption>
  </center>
</figure>

This section displays the list of currently loaded optics measurements.
Each entry is color-coded by beam for quick identification.
Hovering over an optics name displays a tooltip with a summary of its associated paths and accelerator parameters.

#### Load Optics

Clicking the `Load` button opens a file dialog where you can select the measurement folder to load.
Alternatively, you can point directly to a previous SbS output folder, which is useful when working with [virtual copies](#virtual-copies) or when you had previously used a different output directory name than the default `sbs`.

Upon loading, the GUI attempts to automatically determine the accelerator type, beam and the appropriate model folder.
If the automatic detection is not successful, these parameters need to be set manually via the `Edit` button (see the _Edit Optics_ details below).
The SbS analysis output is stored in sub-directories of the optics folder, by default in a folder named `sbs`.
If the corresponding option is activated in the [settings](settings.md#main-settings), the GUI will automatically scan the `sbs` folder for existing segment results and load them into the segments table.

#### Virtual Copies

Clicking the `Copy` button creates a virtual copy of the currently selected optics.
A virtual copy references the same input measurement data but writes its output to a separate directory, making it possible to test multiple correction schemes side by side without duplicating files on disk.
In the side panel, virtual copies are displayed as `NAME -> OUTPUT_DIR_NAME` to distinguish them from the original optics entry.

#### Remove Optics

Clicking the `Remove` button removes the currently selected optics from the GUI.
This only unloads it from the interface and does not delete any files from disk.

#### Run Matcher

!!! warning "Not Implemented"
    This feature is not yet implemented.
    In the future, the `Run Matcher` button is intended to launch the automated matcher for the currently selected optics, which would calculate the correction and produce a correction file.
    That file could then be loaded in the [corrections dialog](#corrections) and applied to the model.

??? info "Edit Optics"

    <figure>
      <center>
      <img class="clickImg" src="../../assets/images/sbs_gui/optics_measurement.png" width="100%" alt="Edit Optics Measurement"/>
      <figcaption>The edit optics measurement dialog.</figcaption>
      </center>
    </figure>

    The edit dialog can be opened by clicking the `Edit` button or by double-clicking the optics name in the side panel.
    It allows you to modify the paths and accelerator parameters associated with the loaded optics.
    Note that the measurement path itself cannot be changed from this dialog; to use a different measurement directory, load a new measurement folder instead.

    The available fields are:

    - **Model**: Path to the model folder, which should contain the optics files for the model.
    - **Accelerator**: Accelerator name, e.g. `lhc`, `sps`, `ps`, `psbooster`.
    - **Output**: Path to the output folder where the SbS analysis results are stored.
    - **Corrections**: Path to the corrections file containing all corrections to be applied to the model. The corrections are executed by MAD-X as-is to correct the model, so they must be written in MAD-X syntax and represent the "inverse" of the corrections applied in the machine (MAD-X/LSA sign conventions apply).
    - **Year**: Year of the accelerator optics to use, corresponding to the `acc-models` branch from which the appropriate model is created (see the `omc3` model creators).
    - **Ring**: Ring to use, if applicable (relevant for PSB).
    - **Beam**: LHC beam to use, if applicable, e.g. `1` or `2`.

    The parameters are validated when clicking `OK`. Which parameters are required depends on the selected accelerator.

#### Corrections

Clicking the `Corrections` button opens the corrections dialog, where you can load or create a correction file to apply to the model.
If a correction file is already associated with the selected optics, the dialog displays its contents and allows you to edit them directly.
When no correction file is loaded, the dialog may suggest correctors based on the optics and measurement data, provided this feature is activated in the [settings](settings.md#main-settings).

The correction file path is applied to all currently selected optics and can also be edited from the edit optics dialog (see the _Edit Optics_ details above).
If some of the selected measurements already have the same correction file loaded while others have none, a dialog will ask whether you want to apply the same correction file to all of them.
If there is a conflict between different correction files across the selected optics, an error message is shown.

### Segments

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/side_panel.png" width="100%" alt="Side Panel"/>
  <figcaption>The side panel.</figcaption>
  </center>
</figure>

This section displays the defined segments for the currently selected optics.
Each segment is shown with its name, start element and end element.
The `start` and `end` fields are optional: if either one is left empty, both are ignored and only the segment name is used.
In that case, the SbS analysis will automatically find the closest BPMs before and after the named element to use as the propagation boundaries.

Hovering over a segment entry in the table displays a tooltip indicating which loaded optics it belongs to and whether the analysis has been run for each one (i.e. whether the output file exists).
Clicking on a segment name selects it and displays the corresponding results in the plot, provided the analysis has already been performed.
See ["Segment Grouping and Comparison"](#segment-grouping-and-comparison) for details on how segments from multiple optics or selections are overlaid.

!!! warning "Start and End Elements vs. Actual BPMs"
    The start and end elements specified here do not need to be BPMs — they can be any element in the model.
    The SbS analysis will locate the nearest BPM in the measurement data and use that as the actual start or end of the segment.
    This means that for different measurements, the actual start BPM may differ even if the defined segment uses the same start element, depending on which BPMs are present or filtered in the measurement data.
    Since the GUI checks only the segment definition and not the actual SbS output, this can lead to confusion when plotting multiple segments together: they will appear to start at the same point in the plot despite corresponding to different physical locations.
    Activating the `Model Location` option in the [plot settings](settings.md#plot-settings) avoids this issue by plotting positions in the accelerator frame rather than relative to the segment start.

#### Run Segment-by-Segment Analysis

Clicking the `Run Segment(s)` button launches the segment-by-segment analysis for the currently selected segments and optics.
If the output file already exists for a given combination, it will be overwritten by the new run.
While the analysis is running in the background, a spinner icon appears at the bottom right of the GUI.
Hovering over the "running tasks" text next to the spinner displays the name of the currently running task (e.g. `SbS for <optics name>`).

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/task_running.png" width="100%" alt="Running Task"/>
  <figcaption>Running task indicator.</figcaption>
  </center>
</figure>

#### New Segment

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/segment_editor.png" width="100%" alt="New Segment"/>
  <figcaption>The new segment dialog.</figcaption>
  </center>
</figure>

Clicking the `New` button opens the segment editor dialog for the currently selected optics.
In the dialog, you enter the segment name along with the start element and end element.
If either the start or end element is left empty, both are ignored and only the segment name is used to define the segment; the analysis will then automatically determine the nearest BPMs.

#### Default Segments

Clicking the `Add Defaults` button populates the segments table with a predefined set of segments appropriate for the currently selected accelerator.
For example, in the LHC the default segments cover IP1, IP2, IP5 and IP8 — spanning from `BPM.L12` to `BPM.R12` — which contain the main interaction points and are therefore of particular interest for the SbS analysis.

If the corresponding option is activated in the [settings](settings.md#main-settings), these default segments are automatically added whenever a new measurement optics directory is loaded.

#### Copy Segment

Clicking the `Copy` button creates a duplicate of the currently selected segment for the currently selected optics.
The copy retains the same start and end elements but is given a different name.
This is particularly useful for quickly creating variants of a segment — for instance with different start BPMs — to evaluate how the choice of starting point affects the results.

#### Remove Segment

Clicking the `Remove` button deletes the currently selected segment from the segments table for the currently selected optics.
This only removes the segment definition from the GUI; it does not delete any output files from disk.

#### Save/Load Segment

!!! warning "Not Implemented"
    This feature is not yet implemented.
    In the future, segment definitions (name, start, end) will be saved as a JSON file in the output directory of the optics (e.g. `sbs/segments.json`) and reloaded automatically when the optics are loaded or when the user clicks the `Load` button.
    This will allow segment definitions to persist even if the analysis has not been run yet and will make it easy to share segment configurations between different measurements by copying the JSON file.

## Log Console

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/log_console.png" width="100%" alt="Log Console"/>
  <figcaption>The log console.</figcaption>
  </center>
</figure>

The log console displays logging output from both GUI actions and the underlying Python modules called during the analysis.
It can be expanded or collapsed using the arrow control and closed entirely with the "X" button on its right side; if closed, it can be re-enabled through the [`View` menu](#view).
The console panel is also movable and resizable within the GUI window.
Right-clicking inside the console opens a context menu that provides access to additional preferences.

!!! tip "Debug Logging"
    By default, the log console is initialized with log level `INFO`.
    To enable more detailed output for debugging purposes, launch the GUI with the `-d` flag (e.g. `python -d`), which sets the log level to `DEBUG`.
