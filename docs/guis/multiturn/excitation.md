# Performing Beam Excitation

Once [all the checks](safety.md) have been performed, one can start measurements.
In the Multiturn GUI one can perform beam excitation with either the AC Dipole or the ADT, and both procedures are very similar.
Select either the `ACDipole` or `ADTACDipole` tab at the top of the GUI, depending on the desired excitation device.

## Common Settings

The following settings are set identically for both the AC Dipole and the ADT, in the left-hand side of the GUI:

### Kick Groups

Before exciting the beam, one should select or create a kick group.
This is done by clicking the ++"Select Active group"++ button in the top left corner of the GUI, which will open the following dialog:

<figure>
    <center>
    <img src="../../assets/images/multiturn_gui/select_kick_group.png" width="85%" alt="Select Active Group Dialog" />
    <figcaption> Select Active Group Dialog </figcaption>
    </center>
</figure>

Typically one wants to create a new kick group.
To do so:

- Click the ++"Create new Group"++ button at the bottom in the centre, which will open the following dialog, with a default naming scheme:

<figure>
    <center>
    <img src="../../assets/images/multiturn_gui/create_kick_group.png" width="85%" alt="Create New Group Dialog" />
    <figcaption> Create New Group Dialog </figcaption>
    </center>
</figure>

- Adapt the text entry under `Group Name` to reflect the measurements to be done in this group.
A good naming practice is to lead with the date and beam number as suggested, e.g. `YYYY-MM-DD_BEAM1_Measurement_description`.
Make sure to press ++"Enter"++ after typing the name.
Optionally add a description in the field below, and click the ++"Create"++ button.
Once created the new group will appear at the bottom of the list of available groups.

- Select the new group and click the ++"Activate selected"++.
This should then create a new entry in the `LHC-OMC` logbook with information about the group, and all acquisitions done in this group will be logged to that entry automatically.

### Tunes Setup

The fields in this section expect the values of the horizontal and vertical tunes for the selected beam:

<figure>
    <center>
    <img src="../../assets/images/multiturn_gui/tunes_setup.png" width="85%" alt="Tunes setup section" />
    <figcaption> Tunes Setup Section </figcaption>
    </center>
</figure>

They should be the natural tunes used in the machine during measurements.
Either enter the values manually or, to enter the current tunes click the ++"Acquire QH"++ and ++"Acquire QV"++ buttons which will update the value to the current one measured with the BBQ.
These values can be manually refined if necessary.

### Concentrator Settings

These settings refer to the excitation to be performed.
The excitation device needs to know which bunches to excite and how long the excitation should last (in terms of turns).

<figure>
    <center>
    <img src="../../assets/images/multiturn_gui/concentrator_settings.png" width="85%" alt="Concentrator settings section" />
    <figcaption> Concentrator Settings Section </figcaption>
    </center>
</figure>

- To select the bunches, click the ++"Select ..."++ button under the `Bunches` section, which opens the following dialog:
<!-- TODO: Need to add a screenshot of the multiturn -->
Choose ++"Select Bunches with Beam"++ to select all bunches present in the machine.
We typically do not inject bunches that won't be excited for optics measurements.
It is also possible to manually enter the bunches, each number separated by a space.

- Set the number of turns to maintain the excitation for in the `Turns` field below.
These correspond to the excitation plateau length, and does not include ramp-up and ramp-down times.

!!! tip "Excitation Duration"
    For AC-Dipole measurements, this setting is typically __6600 turns__, while for ADT measurements it is typically __40,000 turns__.
    Do not set these values higher than these for the respective measurements, as this can lead to the AC Dipole being damaged or the BPM buffers overflowing causing data to be lost or overwritten.

## AC Dipole Excitation

Selecting the `ACDipole` tab will change the right-hand side of the GUI window to display the following:

<figure>
    <center>
    <img src="../../assets/images/multiturn_gui/default_view.png" width="85%" alt="AC-Dipole Tab" />
    <figcaption>AC-Dipole Tab</figcaption>
    </center>
</figure>

There are two important steps to take before starting the measurements:

## Tune Deltas

- Set the Tune Deltas, this is done by changing the `start` text fields in the `Tune deltas` of the `Horizontal settings` and `Vertical settings` sections of the GUI.

!!! tip "Typical Default Values"
    - The horizontal tune delta is typically set to **-0.01**.
    - The vertical tune delta is typically set to **0.012**.
    - These values result in typical excitation tunes of **Qx = 0.27** and **Qy = 0.322**.
    Depending on the measurements you are performing, these values may need to be adjusted. Always consult with the experts on shift if you are unsure about the tune deltas to use.

- Set the Kick Amplitudes by changing the `Excitation amplitude (%)` text fields in the `Horizontal settings` and `Vertical settings` sections of the GUI.

You can see the excitation tunes under `Start Excitation tune` below the `Tune deltas` section.

## Selecting the Kick Amplitudes

Kick amplitudes are important as they determine the excitation strength. Generally higher kicks lead to better measurements, but come with the risk of beam losses and beam dump.

!!! warning
    Always ask the experts on shift if you are unsure about the kick amplitudes to use.

### Kick amplitudes at injection

At injection the beam is not particularly hard and small kick amplitudes lead to large peak to peak oscillations. We generally use small amplitudes, starting from **1%** or **3%** and going up slowly in steps of **2%** or **3%**, until beam losses during kicks stop being reasonable.

!!! tip "Losses on Kicks"
    Sometimes when increasing the kick amplitude, one will notice large losses. In this case it is recommended to kick a couple times at this amplitude or just below to see if the losses reduce or are consistent.

    Should they reduce the beam might have just needed cleaning and one can increase the kick amplitude further. Otherwise, stop increasing unless a beam dump is affordable. Refer to the experts on shift if you are unsure about the losses, and whether you can increase the kick amplitude further.

### Kick amplitudes during the ramp

An example of a table of amplitudes during the ramp is as follows:

|  Time  | Energy (TeV) | Phase Knob | ATS  | Kick Amplitude (%) |
|--------|--------------|------------|------|--------------------|
| 30s    | 0.46         | 100%       | 1    | 3                  |
| 240s   | 1.0          | 50%        | 1    | 7                  |
| 405s   | 1.9          | 0%         | 1    | 13                 |
| 580s   | 2.9          | 0%         | 1    | 19                 |
| 720s   | 3.7          | 0%         | 1    | 24                 |
| 860s   | 4.5          | 0%         | 1    | 30                 |
| 1010s  | 5.5          | 0%         | 0.75 | 36                 |
| 1160s  | 6.2          | 0%         | 0.57 | 41                 |
| 1247s  | 6.6          | 0%         | 0.5  | 45                 |

This table scales the kick amplitudes with the energy, and hence the kick amplitudes are larger at higher energies. The values in the table are a good starting point, but it is important to monitor the losses and reduce the kick amplitudes accordingly.

### Kick amplitudes top energy

When at top energy, the beam is quite hard, and hence we can use larger kick amplitudes. Starting from **5%** and going up in steps of **5%** until the losses start to increase significantly usually works well.

!!! warning
    Always ask the experts on shift if you are unsure about the kick amplitudes to use.

*[AC Dipole]: Alternating Current Dipole
*[ADT]: LHC Transverse Damper
*[BBQ]: Base Band Q, a system used to continuously measure the beam's tunes.
