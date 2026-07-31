# The Screenshot GUI

The Screenshot GUI is a small utility to capture a screenshot and upload it straight to the logbook.
It is handy during operations, when one constantly wants to log settings, quick plots or the state of another GUI.

!!! info "Requirements"
    The tool needs to run inside the GPN and be logged in to write to the logbook.
    When started from the CCM under an operational account (e.g. `LHCOP` during LHC shifts), this is already taken care of.

This page provides a quick walkthrough of how to set it up to screenshot directly to the OMC logbook.

## Opening the Client

The GUI is started from the CCM.
In the search bar, type *screenshot* and launch the `Screenshot LIDB Client`.
<!-- TODO: check this is indeed screenshot lidb client -->

<!-- TODO (screenshots Monday): default view of the client after launch.
<figure>
  <center>
  <img class="clickImg" src="../../assets/images/screenshot_gui/default_view.png" width="85%" alt="Screenshot client landing page" />
  <figcaption>The Screenshot Client on launch.</figcaption>
  </center>
</figure>
-->

## Selecting the Logbook

Before capturing anything, the target logbook has to be set.

- Click the `Config` button to open the configuration popup.
- Select the specific logbook to send the screenshots to.

!!! tip "OMC Logbooks"
    Searching for "OMC" will bring up the only two OMC logbooks, `LHC_OMC` and `OMC Injectors`.

Once configured, the right part of the window lists the recent logbook entries.
Each entry is displayed with a three-digits number, corresponding to the last three digits of the actual logbook entry.

<!-- TODO (screenshots Monday): Config popup with "OMC" searched and LHC_OMC selected.
<figure>
  <center>
  <img class="clickImg" src="../../assets/images/screenshot_gui/config_popup.png" width="85%" alt="Configuration popup with the OMC logbook selected" />
  <figcaption>Selecting the target logbook in the configuration popup.</figcaption>
  </center>
</figure>
-->

## Taking a Screenshot

There are two ways to capture a screenshot, depending on where it should go:

- To create a **new** logbook entry along with the screenshot, click the `New` button in the top left.
- To add the screenshot to an **existing entry**, click the corresponding entry in the list on the right.

!!! tip "Clarifying the Entry"
    Hovering the mouse over a list item shows a preview of the corresponding logbook entry.

<!-- TODO (screenshots Monday): main view with the numbered entry list on the right (ideally a hover preview visible).
<figure>
  <center>
  <img class="clickImg" src="../../assets/images/screenshot_gui/entry_list.png" width="85%" alt="Client with the logbook entry list on the right" />
  <figcaption>The list of logbook entries, with the hover preview.</figcaption>
  </center>
</figure>
-->

After choosing either option, the client window hides itself to stay out of the capture.
From there, one can:

- Drag-select a region of the screen to capture it.
- Right-click a window to capture that entire window.

At any moment in this capture mode, pressing ++esc++ exits it and brings the client window back.

*[GPN]: General Purpose Network
*[OMC]: Optics Measurements and Corrections
