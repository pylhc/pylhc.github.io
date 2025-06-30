# AC Dipole Scheduler

It is possible to automate the process of running measurements with different kick amplitudes using the AC Dipole Scheduler.
To access the scheduler, select the `ACDipoleScheduled` tab at the top of the GUI.
The right-hand side of the GUI window will then display the following:

<figure>
    <center>
    <img src="../../assets/images/multiturn_gui/ACDipoleScheduler.png" width="85%" alt="AC-Dipole Scheduler Tab" />
    <figcaption>AC-Dipole Scheduler Tab</figcaption>
    </center>
</figure>

## Creating a Kick Schedule

A kick schedule can be created either manually or by loading a prewritten template schedule from file.
It is also possible to edit the template that is already present in the GUI by changing the `H Amplitude (%)` and `V Amplitude (%)` values in the table.
It is not possible to edit the `Index` column.
To reset this template table, select the button ++"Reload from Template"++ below the table.

### Manual Creation

To create a kick schedule from scratch, select the ++"Create Table"++ button below the table.
This will open the following dialog:

<figure>
    <center>
    <img src="../../assets/images/multiturn_gui/create_schedule_table.png" width="85%" alt="Create Kick Schedule Dialog" />
    <figcaption>Create Kick Schedule Dialog</figcaption>
    </center>
</figure>

Set the start and end amplitudes as well as the step size in their respective fields.
Note that the start and end are inclusive, and entries would only be created up to the `End Amplitude`.
Click the ++"Create Kick Table"++ when done.

This will bring you back to the previous view, with the `H Amplitude (%)` and `V Amplitude (%)` columns filled with the inferred kick steps.
The `Index` column is automatically filled with row numbers, don't mind it.

For instance the scenario from the screenshot above will create a table with 4 rows - `3%`, `5%`, `7%`, and `9%` for both the horizontal and vertical kick amplitudes.

### Prewritten Schedules

To load a prewritten kick schedule, select the button `Import .csv` below the table. This will open a file dialog where you can select the `.csv` file containing the kick schedule. There exists a small repository of prewritten kick schedules that can be used as a starting point for your measurements, which can be found in the `/user/slops/data/LHC_DATA/OP_DATA/Betabeat/MULTITURN_KICK_SCHEDULES/` directory:

<figure>
    <center>
    <img src="../../assets/images/multiturn_gui/prewritten_schedules.png" width="85%" alt="Prewritten Kick Schedules" />
    <figcaption>Prewritten Kick Schedules</figcaption>
    </center>
</figure>

## Running a Kick Schedule

Once you have created or loaded a kick schedule, it is necessary to setup the horizontal and vertical kick tune deltas. Refer to the [AC-Dipole Measurements](acdipole.md) page for context on what to set these to.

Now all the settings are ready, it is possible to run the kick schedule from the very beginning of the table by selecting the button `Acquire with ACDipoleScheduled excitation` at the bottom left of the GUI (highlighted in yellow). This will start the measurement with the first row of the table, and will automatically move to the next row once the measurement is complete.

!!! info
    To cancel the acquisition while running a kick schedule, press the `Stop` button. Note that if a kick was just done when pressing `Stop`, the schedule will stop after the next kick is complete. There is no way to cancel the next kick once it is waiting for the AC-Dipole to be ready.

It is also possible to run the kick schedule from a specific row. This is done by selecting the row in the table and then selecting the button `Start from Selection`. This will start the measurement from the selected row and will automatically move to the next row once the measurement is complete.

*[AC Dipole]: Alternating Current Dipole
