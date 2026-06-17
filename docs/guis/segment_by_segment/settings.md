# Settings

## Main Settings

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/settings_main.png" width="100%" alt="Main Settings"/>
  <figcaption>The main settings.</figcaption>
  </center>
</figure>

Note: Hints available on hovering over the settings text.

- **Working Directory**:
The directory where the input files are located.
The GUI will use this directory as the default directory when opening file dialogs for loading optics and measurement data.

- **Autoload Segments**:
Automatically load existing segements when loading a new measurement optics directory.
This looks for files created by the GUI in earlier runs and for now only works if the segment has actually been run.
(Future implementation: also check for json files - see `Save` and `Load` buttons.)

- **Auto-Add Default Segments**:
Automatically add default segments when loading a new measurement optics directory.

- **Suggest Correctors**:
When opening the [corrections dialog](gui.md#corrections) for a new/not yet existing correction file, suggest correctors based on the optics and measurement data.

## Plot Settings

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/settings_plotting.png" width="100%" alt="Plot Settings"/>
  <figcaption>The plotting settings.</figcaption>
  </center>
</figure>

Note: Hints available on hovering over the settings text.

- **Show Model**: Adds markers for the location of elements in the model to the plots.
- **Show Legend**: Show legends in the plots.
- **Marker Size**: Size of the markers in the plots.
- **Expectation**: If run with corrections, show the expected measurement difference instead of the corrected model difference (details in [Correction Idea](gui.md#correction-idea)).
- **Forward Propagation**: Show forward propagation results (arrows to the right).
- **Backward Propagation**: Show backward propagation results (arrows to the left).
- **Connect X**: Keep the same X-Axis limits for both charts when zooming.
- **Connect Y**: Keep the same Y-Axis limits for both charts when zooming.
- **Reset Zoom**: When chaning segments, reset the zoom to the original view.
                  When deactivated, the current limits will be kept when changing segments, which can be useful for comparing different segments or optics with the same zoom level.
- **Same Segment Start**: Plot segments together, even if they have different start BPMs. Not recommended, as it can lead to confusion and misinterpretation of the results, as they will both start at the same point in the plot, even though they represent different locations in the accelerator.
- **Model Location**: Plot segments relative to the model location, i.e. their position in the accelerator, which allows for easy comparison of segments with different start BPMs. If deactivated, segments will start at a location of zero at their start BPM.

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/view_model_location.png" width="100%" alt="Model Location"/>
  <figcaption>Example of two segements with different start BPMs when plotted with `Model Location` activated.</figcaption>
  </center>
</figure>
