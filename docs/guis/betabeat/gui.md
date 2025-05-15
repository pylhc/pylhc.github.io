# The Beta-Beat GUI

The Beta-Beat GUI provides different functionalities separated in multiple views, in the form of a graphical interface.
The GUI can be ran locally, provided you have access to `afs`, but most importantly directly from the CERN Control Center.
This section provides a short overview for the main features.

!!! info
    The code documentation of the Beta-Beat GUI can be found on CERN's gitlab pages.
      
      * [Master branch][bbgui_doc_bbsrc]{target=_blank}


The GUI provides several panels, each for a defined use and with a set of options and results:

- [The BPM Panel](bpm_panel.md) for loading measurements files, displaying data and launching analysis.
- [The Analysis Panel](analysis_panel.md) to display and manipulate the results of harmonic analysis on measurement data.
- [The Optics Panel](optics_panel.md) to compare computed optics to nominal models.
- [The Correction Panel](correction_panel.md) to display the computed necessary corrections to reach the nominal model.

This site will guide you through the GUI's layout and functionality.
For starters, check out [the basics of running the GUI](../about.md).

!!! warning "Bug Reporting"
    If you find bugs, please create [issues][betabeat_gui_gitlab_issues]{target=_blank} with the `OMC3-GUI` label.

## General Notes

### Opening Files

* Each tab has now an <span style="color:green;">Open Files</span> button, which opens only the files specific to this tab.
* The magic <span style="color:green">**+**</span> button is gone, as its functionality was confusing (and there were different stories about its workings).

[bbgui_doc_bbsrc]: https://lhc-app-beta-beating.docs.cern.ch/master/
[betabeat_gui_gitlab_issues]: https://gitlab.cern.ch/acc-co/lhc/lhc-app-beta-beating/-/issues
