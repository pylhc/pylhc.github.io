# The Multiturn GUI

The Multiturn GUI provides functionality to set up and perform beam excitation with the AC Dipole or the ADT.
Excitations feature automatic saving of turn-by-turn BPM data.
This section will guide you through the GUI's layout and functionality.

The GUI is a Java application and is typically run from the `CCM`:

=== "From the CCM"
    Have a [working `CCM`][gui_basics] running as `lhcop`, then navigate to `LHC Control` -> `LHC Beam Measurements` -> `Multiturn`.

After opening, the GUI should look like this:

<figure>
  <center>
  <img src="../../assets/images/multiturn_gui/default_view.png" width="85%" alt="Multiturn GUI landing page" />
  <figcaption> Multiturn GUI Landing Page </figcaption>
  </center>
</figure>

After opening, select at the top of the GUI either the `Acquisition BEAM1` or `Acquisition BEAM2` tab, depending on the beam you plan on measuring.

!!! warning
    It is recommended to not kick both beams from the same GUI, as it can lead to crashes and unexpected behavior.
    Open a separate GUI for each beam.

!!! tip "Closing Tabs"
    To avoid kicking the wrong beam accidentally, one can drag and drop the tab for the unused beam out of the GUI.

The following pages are available:

- [Safety Checks](safety.md) for how important checks to be performed for measurements.
- [Beam Excitation](excitation.md) for how to excite the beam with either the AC Dipole or the ADT.
- [Scheduled Excitations](scheduler.md) for how to schedule and run AC-Dipole measurements with a set of predefined kick amplitudes.

*[AC Dipole]: Alternating Current Dipole
*[ADT]: LHC Transverse Damper
*[BPM]: Beam Position Monitor

[gui_basics]: ../about.md#running-in-the-ccc-in-2025
