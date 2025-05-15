# The Beta-Beat GUI

The Beta-Beat GUI provides different functionalities separated in multiple views, in the form of a graphical interface.
The GUI can be ran locally, provided you have access to `afs`, but most importantly directly from the CERN Control Center.
This section provides a short overview for the main features.

!!! info
    The gitlab CI automatically generates an [API documentation page][bbgui_doc_omc3]{target=_blank} based on the source code.

    (A legacy version for the `BetaBeat.src` branch is [also available][bbgui_doc_bbsrc]{target=_blank}.)

The GUI provides several panels, each for a defined use and with a set of options and results:

- [The BPM Panel](bpm_panel.md) for loading measurements files, displaying data and launching analysis.
- [The Analysis Panel](analysis_panel.md) to display and manipulate the results of harmonic analysis on measurement data.
- [The Optics Panel](optics_panel.md) to compare computed optics to nominal models.
- [The Correction Panel](correction_panel.md) to display the computed necessary corrections to reach the nominal model.

This site will guide you through the GUI's layout and functionality.
For starters, check out [the basics of running the GUI](../about.md).

!!! warning "Bug Reporting"
    If you find bugs, please create [issues][betabeat_gui_gitlab_issues]{target=_blank} with the `OMC3-GUI` label.

[bbgui_doc_omc3]: https://lhc-app-beta-beating.docs.cern.ch/omc3/
[bbgui_doc_bbsrc]: https://lhc-app-beta-beating.docs.cern.ch/master/
[betabeat_gui_gitlab_issues]: https://gitlab.cern.ch/acc-co/lhc/lhc-app-beta-beating/-/issues
