# Determining Corrections

After having identified potential sources of errors through the forward and backward [propagation](segments.md#inspecting-results), the next step is to determine and test corrections.
This page covers how to apply corrections in the GUI, test different correction schemes and interpret the resulting plots.

## Applying Corrections

Once you have inspected the results and identified optics errors, the next step is to determine corrections.
Clicking the `Corrections` button in the side panel opens the corrections dialog, where you can load or create a correction file to apply to the model.
If a correction file is already associated with the selected optics, the dialog displays its contents and allows you to edit them directly.
When no correction file is loaded, the dialog may suggest correctors based on the optics and measurement data, provided this feature is activated in the [settings](settings.md#main-settings).

The correction file path is applied to all currently selected optics.
If some of the selected measurements already have the same correction file loaded while others have none, a dialog will ask whether you want to apply the same correction file to all of them.
If there is a conflict between different correction files across the selected optics, an error message is shown.

After applying a correction file, [re-run the analysis](segments.md#running-segments) to see the corrected results as dashed lines in the plot.

!!! warning "Run Matcher — Not Implemented"
    In the future, the `Run Matcher` button is intended to launch the automated matcher for the currently selected optics, which would calculate the correction and produce a correction file that can then be loaded in the corrections dialog.

## Correction Sign Conventions

The corrections applied in the GUI modify the model to match the measurement.
In order to actually correct the machine, these corrections generally need to be inverted: the GUI finds what error in the model would reproduce the observed measurement deviation, and the opposite of that error is what should be applied operationally.
Be aware that sign conventions may differ between MAD-X and LSA, so care must be taken when translating correction values from the GUI to the control system.

## Testing Multiple Correction Schemes

A practical approach to testing different correction strategies is to create virtual copies of the same measurement.
Click the `Copy` button in the loaded optics section to create a virtual copy.
It references the same input measurement data but writes its output to a separate directory, making it possible to try multiple correction schemes side by side without duplicating files on disk.
In the side panel, virtual copies are displayed as `NAME -> OUTPUT_DIR_NAME` to distinguish them from the original optics entry.

Similarly, creating multiple segments with different start BPMs for the same region lets you evaluate sensitivity to the starting point.
This helps confirm whether the correction holds regardless of which BPM anchors the propagation.

## Corrected and Expected Plots

When corrections have been applied and the analysis is re-run, the plot shows a dashed line in addition to the solid measurement line.
The [plot settings](settings.md#plot-settings) let you choose what this dashed line represents:

- **Matched value (corr)**: the difference between the propagated corrected model and the nominal propagated model.
  If the correction successfully reproduces the measured errors, this dashed line should lie close to the solid measurement line.
- **Expected value (expct)**: the difference between the measured values and the propagated corrected model.
  This represents the expected outcome of the SbS analysis after the correction has been applied to the machine, and should therefore be close to zero if the correction is effective.
