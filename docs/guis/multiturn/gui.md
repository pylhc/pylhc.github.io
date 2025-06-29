# The Multiturn GUI

The Multiturn GUI provides functionality to set up and perform beam excitation with the AC-Dipole or the ADT.
Excitations feature automatic saving of turn-by-turn BPM data.

This section will guide you through the steps to set up the Multiturn GUI, refer to the [AC-Dipole Measurements](acdipole.md) and [ADT AC-Dipole Measurements](adt.md) pages for how to perform the measurements with the AC-Dipole and ADT, respectively.

The GUI is a Java application and is typically run from the `CCM`:
=== "From the CCM"
    Have a [working `CCM`][gui_basics] running as `lhcop`, then navigate `LHC Control` -> `LHC Beam Measurements` -> `Multiturn`.

After opening, the GUI should look like this:
<figure>
  <center>
  <img src="../../assets/images/multiturn_gui/default_view.png" width="85%" alt="Multiturn GUI landing page" />
  <figcaption> Multiturn GUI Landing Page </figcaption>
  </center>
</figure>

## Steps to Setup the GUI
- After opening, select at the top of the GUI either the `Acquisition BEAM1` or `Acquisition BEAM2` tab, depending on the beam you plan on measuring. It is recommended to not kick both beams from the same GUI, as it can lead to crashes and unexpected behavior. Open a separate GUI for each beam.


### Kick Group
- Next, select or create a kick group. This is done by clicking the ++"Select Active group"++ button in the top left corner of the GUI, which will open the following dialog:
<figure>
    <center>
    <img src="../../assets/images/multiturn_gui/select_kick_group.png" width="85%" alt="Select Active Group Dialog" />
    <figcaption> Select Active Group Dialog </figcaption>
    </center>
</figure>

- Typically one wants to create a new kick group. To do so, click the ++"Create new Group"++ button at the bottom in the centre. This will open the following dialog, with a default naming scheme:
<figure>
    <center>
    <img src="../../assets/images/multiturn_gui/create_kick_group.png" width="85%" alt="Create New Group Dialog" />
    <figcaption> Create New Group Dialog </figcaption>
    </center>
</figure>

- Adapt the text entry under `Group Name` to reflect the measurements to be done in this group. A good naming practice is to lead with the date and beam number as suggested, e.g. `YYYY-MM-DD_BEAM1_Measurement_description`. Make sure to press ++"Enter"++ after typing the name. Optionally add a description in the field below, and click the ++"Create"++ button.

- Once created the new group will appear at the bottom of the list of available groups. Select it and click the `Activate Selected`. This should then create a new entry in the `LHC-OMC` logbook. <!-- Add link here? -->

### Tunes set-up
- Next, set up the tunes in the `Tunes set-up` section on the left side of the GUI. Clicking the ++"Acquire QH"++ and ++"Acquire QV"++ buttons will update the value to the current measured one. These values can be manually refined if necessary.

### Concentrator settings
- To select the bunches, click the ++"Select ..."++ button under the `Bunches` section. This will open the dialog shown in the figure below. Then, choose ++"Select Bunches with Beam"++. If you are unsure which bunches to select, please consult the expert on shift.
<!-- Need to add a screenshot of the multiturn -->

- Finally, set the number of turns to measure in the `Turns` field below. For AC-Dipole measurements, this is typically **6,600 turns**, while for ADT AC-Dipole measurements it is typically **40,000 turns**. Do not set these values higher than these for the respective measurements, as this can lead to the AC-Dipole being damaged or the BPM buffers overflowing causing data to be lost or overwritten.

## Measurement Environment

The `Measurement Environment` section on the left side of the GUI provides a quick overview of the current machine feedback and damping states, this can be seen in the image below:
<figure>
    <center>
    <img src="../../assets/images/multiturn_gui/measurement_environment.png" width="85%" alt="Measurement Environment Section" />
    <figcaption> Measurement Environment Section </figcaption>
</figure>


- **Feedback state**:  
  - `OrbitOFF` (red) indicates that the orbit feedback is currently off and will appear green and change to `OrbitON` when it is active.
  - `RadialLoopOFF` (red) shows the radial loop feedback is off; when on, it will appear green as `RadialLoopON`.
These states will automatically be turned off when you start a measurement, and will be turned back on when the measurement is complete. 

- **Tune feedback state**:  
  - Each button represents the tune feedback for a specific beam and plane:  
    - `B1 H` = Beam 1, Horizontal  
    - `B1 V` = Beam 1, Vertical  
    - `B2 H` = Beam 2, Horizontal  
    - `B2 V` = Beam 2, Vertical  
  - Red indicates the feedback is off; green indicates it is on.
This feedback will be automatically turned off when you start a measurement, and will be turned back on when the measurement is complete. Check with the experts on shift if you are unsure about the state of the tune feedback.

- **Chroma state & Landau Damping**:  
These are less important for the measurement setup and are typically left as is. Talk to the experts on shift if you are unsure about these settings.

!!! Note
    Taking a measurement always turns off the tune feedback, radial loop, and orbit feedback for that beam. Afterward, the system restores these to how they were before the last measurement. So, if you measure Beam 1, then kick and measure Beam 2, Beam 1’s feedback loops will be turned off again — because the system restores them to the state they were in during the second measurement.

## Running a Measurement
The following pages are available:

- [AC-Dipole Measurements](acdipole.md) for how to excite the beam with the AC-Dipole.
- [ADT AC-Dipole Measurements](adt.md) for how to excite the beam with the ADT.
- [AC-Dipole Scheduler](scheduler.md) for how to schedule and run AC-Dipole measurements with a set of predefined kick amplitudes.

*[AC-Dipole]: Alternating Current Dipole
*[ADT AC-Dipole]: LHC Transverse Damper
*[ADT]: LHC Transverse Damper
*[BPM]: Beam Position Monitor

[gui_basics]: ../about.md#running-in-the-ccc-in-2025