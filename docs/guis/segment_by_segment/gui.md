# The Segment-by-Segment GUI

The Segment-by-Segment GUI provides a graphical interface to run the [segment-by-segment method][sbs_method] on various parts of the machine.
It allows users to input data, configure settings, run segments, determine corrections and visualise results for various observables.
This section will guide you through the GUI's layout and functionality.

The GUI is a Python application built on `acc-widgets`.
It can be run either from the Beta-Beat GUI's [Optics Panel][bbgui_optics_panel] after running a full optics analysis, or the command line:

=== "From the Beta-Beat GUI"

    After performing an optics analysis, navigate to the optics panel.
    With an analysis selected, click the ++"Segment-by-Segment"++ button to start the GUI.
    <!-- TODO: check button name -->

=== "From the Command Line"

    The SbS GUI is a Python program and part of the `omc3_gui` package.
    It can be started from the command line by providing desired arguments to the following call:

    ```bash
    python -m omc3_gui.sbs_gui # args here
    ```

    Note that this GUI requires the `omc3` package, recent QT bindings (`PyQT` / `PySide`) and the `accwidgets` package which is quite CERN specific.
    It is recommended to run it from the Beta-Beat GUI.

After opening, the GUI should open to the main window:

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/sbs_gui/blank_window.png" width="100%" alt="Blank Window"/>
  <figcaption>Blank window of SbS-GUI as seen when starting the GUI.</figcaption>
  </center>
</figure>

The following pages are available:

- [Loading Data and Running Segments](segments.md) for how to load measurement data, define and run segments, and interpret the plots.
- [Determining Corrections](corrections.md) for how to attempt determining corrections and testing their effect through the segments.
- [Menus & Settings](settings.md) for the available menus and the meaning of various options.

*[SbS]: Segment-by-Segment

[sbs_method]: ../../measurements/physics/sbs.md
[bbgui_optics_panel]: ../betabeat/optics_panel.md
