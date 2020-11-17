# The Beta-Beat GUI BPM Panel

The BPM panel provides a graphical interface to query and visualize information for the BPM data files.
It can load data files for all supported beams, mostly binary SDDS files or files in the SDDS ASCII format.

!!! todo
    Include a screenshot, possibly of settings when opening files?

## Opening Files and Applying SVD Cleaning

The content of the loaded files will be displayed in two charts:

- One for the horizontal BPMs,
- One for the vertical BPMs.

!!! todo
    Include a screenshot with two BPM panels.

The charts are interactive and can be used to zoom in/out, or focus on a given rectangle of the shown data.

The charts can display either the measured amplitude values over turns for every BPM from the list or display the phase space, which is calculated by two consecutive BPMs.
Additional functionality is done while loading a file.

If SVD is enabled in the settings, the external SVD cleaning python script will be called for the current file during the loading process.
If SVD cleaning detects and removes bad BPMs, they can be reviewed inside the bad BPM pane.

!!! todo
    Include a screenshot of the bad bpms panel.

## Removing Turns and Computing an Average

The buttons on the top left side of the pane provide useful features to handle the BPM data.

- `Remove Turns` can be used to cut turns from the start or the end, to focus on a specified range of the data. 

!!! todo
    Include a screenshot of before-after comparison for `Remove Turns`.

- `Create Average` allows loading several data files too visualize their average repesentations on the same graph, which helps detecting differences or reducing noise.

!!! todo
    Include a screenshot of `Create Average` effect.

- `Do Analysis` spawns the configuration dialogue for the external analysis.
  This will call an external program to perform harmonic analysis of the BPM data, in order to compute tunes and similar beam properties.
  The results from the analysis can be seen in the [Analysis Panel](analysis_panel.md).
   
!!! todo
    Include of screenshot of `Do Analysis` dialogue window.

!!! note
    The `Create Average` option requires synchronized data from withing the same bounds, otherwise the results will be meaningless.
    The figure below shows three runs from LHC beam one with synchronized peaks for every turn and their corresponding averages.