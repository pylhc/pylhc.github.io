# The Optics Panel

The `Optics` panel is where the computed optics are visualised and compared against the nominal model, but also against one another.
It is also the launch point for follow-up actions such as calculating [corrections](#computing-corrections), loading k-modulation data, starting the [Segment-by-Segment GUI][sbs_gui] and creating eLogbook entries.

Once an optics analysis has produced results (via [Get Optics][bbgui_do_optics] in the analysis panel), a new entry will appear in the list box in the top left part of the panel.
Selecting the entry for an optics analysis allows one to inspect all computed optics properties across the machine.

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/betabeat_gui/optics_panel.png" width="100%" alt="Optics Panel"/>
  <figcaption>The Optics panel, here showing the horizontal and vertical beta-beating for two loaded results.</figcaption>
  </center>
</figure>

The panel is split into two sub-tabs, **Optics** and **Action/Tune**, described below.
<!-- Shared elements — the [top bar][cc_top], the [plot area and its shortcuts][cc_plotting], the [console][cc_console] and the [running tasks][cc_running_tasks] indicator — are documented in [Common Components][cc]. -->

*[SbS]: Segment-by-Segment
*[RDT]: Resonance Driving Term
*[RDTs]: Resonance Driving Terms
*[CRDT]: Combined Resonance Driving Term
*[CRDTs]: Combined Resonance Driving Terms
*[GUI]: Graphical User Interface
*[IP]: Interaction Point
*[SVD]: Singular Value Decomposition

[sbs_gui]: ../segment_by_segment/gui.md
[cc]: common_components.md
[cc_top]: common_components.md#top-of-the-gui
[cc_plotting]: common_components.md#plotting
[cc_console]: common_components.md#console
[cc_running_tasks]: common_components.md#running-tasks
[cc_file_dialogues]: common_components.md#file-opening-dialogues
[bbgui_do_optics]: analysis_panel.md#do-optics-dialogue
[betabeatsource]: betabeatsource.md#meaning-of-the-beta-beatsrc-output-files
[ampdet]: ampdet.md
[correction_panel]: correction_panel.md
[correction_checks]: correction_panel.md#correction-checks
