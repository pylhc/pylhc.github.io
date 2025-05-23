# BSRT Logger and BSRT Analysis

!!! todo
    Description of a typical use-case, with easy examples for first-timers.

[See the docs][documentation] for a detailed code description.

## Analysis

Main script to query BRST data, then perform an analysis and output the generated plots.
The analysis script runs through the following steps:

- Processes the output files of ``BSRT_logger.py`` for a given time-frame, returns them in as a `TfsDataFrame` for further processing.
- Additionally, plots for quick checks of fit parameters, auxiliary variables and beam evolution are generated.
- If provided a `TfsDataFrame` file with timestamps, plots of the 2D distribution and comparison of fit parameters to cross sections are added.

## Logger

Script used during Run II to log detailed BSRT data and save it for later analysis.
Data from the BSRT for each timestep is put in a `dictionary` and append to a `list`.
The `list` is then saved to disk through pickling.
Proper testing requires communication with ``FESA``s class, possible only from the Technical Network.

*[BSRT]: Beam Synchrotron Radiation Telescope

[documentation]: https://pylhc.github.io/PyLHC/entrypoints/bsrt_analysis.html
