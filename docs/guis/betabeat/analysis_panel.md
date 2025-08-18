# The Analysis Panel

The analysis panel provides graphical interface to visualize results from harmonic analysis performed on the given data.

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/betabeat_gui/analysis_panel.png" width="100%" alt="The Analysis Panel"/>
  <figcaption>The Analysis Panel.</figcaption>
  </center>
</figure>


## Loading Files

The buttons at the top of the panel provide functionality to load and remove files from the analysis table as well as to start the [optics analysis](#do-optics-dialog).

- ++"Open Files"++{.green-gui-button}: Opens a dialog to select files to be loaded. The files will be **copied** into the `Measurements` folder and opened from there.
- ++"Attach Files"++{.yellow-gui-button}: Opens a dialog to select files to be loaded. The files will be **opened from their current location**.
- ++"Delete Files"++{.red-gui-button}: Removes the selected files from the analysis table.
- ++"Get Optics"++{.green-gui-button}: Opens [the optics analysis dialog](#do-optics-dialog) which can trigger an external python script to compute the optics functions from the harmonic analysis data of the selected files.

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/betabeat_gui/analysis_panel_table.png" width="100%" alt="Table of loaded files."/>
  <figcaption>The table of currently loaded files.</figcaption>
  </center>
</figure>


## The Time / Space Tab

In the `Time / Space` tab one can examine the phases and amplitudes, and can clean the values if needed (only `TUNEX` and `TUNEY` or `NATTUNEX` and `NATTUNEY`).

If some values are obviously not inside a given bound, the 2 marker lines (see screenshot below) can be used to set the boundaries and to remove all data outside those boundaries.
The GUI will check if the removal is inside some predefined bounds to prevent accidental removal of too much data.

!!! todo
    Include a screenshot of the time / space panel with relevant info highlighted (see twiki)

### Cleaning of harmonic analysis output data

The harmonic analysis data used to obtain the optics functions can be cleaned using [Isolation Forest algorithm][sklearn_IF].
It should prevent the appearance of unphysical spikes in the optics functions which are caused by the faulty BPMs remaining in the data after the TbT-data cleaning.

Isolation Forest perfroms anomaly detection on the whole set of selected measurements data.
Clicking on "Detect and remove bad BPMs"-button triggers an external python script which analyses the selected files.
The output file is written in the TFS format and contains the list of detected bad BPMs is written to the folder of the first selected measurement in the analysis table.

The output can be found in:  `Measurements/.../bad_bpms_iforest_{x,y}`.

During IF-cleaning, the lines corresponding to detected faulty BPMs will be removed from the lin-files.
Cleaning can be reverted (the original lin files will be restored) by clicking <kbd>Revert</kbd>.

After cleaning is finished, the optics function can be computed from the harmonic analysis data by clicking <kbd>Get optics</kbd>.

<figure>
  <center>
  <img src="../../assets/images/betabeat_gui/analysis_panel_time_space_clean.png" width="100%" alt="Cleaning before optics analysis" />
  <figcaption> Cleaning before optics analysis </figcaption>
  </center>
</figure>

=== "Before Cleaning"

    <figure>
    <center>
    <img src="../../assets/images/betabeat_gui/analysis_panel_time_space_manual_clean_before.png" width="100%" alt="Natural Tune before cleaning." />
    <figcaption>Identified natural tunes per BPM with outliers. </figcaption>
    </center>
    </figure>

=== "After Cleaning"

    <figure>
    <center>
    <img src="../../assets/images/betabeat_gui/analysis_panel_time_space_manual_clean_after.png" width="100%" alt="Natural Tune after cleaning." />
    <figcaption>Identified natural tunes per BPM after cleaning outliers.</figcaption>
    </center>
    </figure>


!!! tip "Keep BPMs"
    Some BPMs, e.g. the AC-Dipole BPMs, are required for the optics analysis and **the analysis will fail** if they are not found in the data.
    You can therefore specify to **keep these BPMs** in the [GUI Cleaning section of the Cleaning Settings Tab](settings.md#gui-cleaning) and they will be kept,
    even if they are outside the given cut-offs or identified as outliers.

### Additional cleaning based on the tune

Additionally, BPMs can be cleaned based on the tune values computed by harmonic analysis. The chart displaying the selected columns of harmonic analysis data has interactive cursors. These cursors can be moved manually to set the thresholds for tune-based cleaning - all BPMs having tune values outside of the set range will be removed. The cursors can be also automatically set to e.g. 4 sigmas deviation from the average tune values over all BPMs.

### Summary of cleaning steps before optics analysis

- [ ] Before loading tbt-files: check SVD settings and signal cuts in the global settings panel
- [ ] After harmonic analysis: Detect bad BPMs with Isolation Forest
- [ ] If neccessary: check tunes in the chart, set cursors, clean tune outliers.

## The Frequency Tab

The `Frequency` tab displays the computed frequencies for every BPM.

A `Get Optics` button can be used to start the optics calculation.
This will call an external python script again, with the results available in the [Optics Panel](optics_panel.md).

### Nattune Updater

- You can set a frequency range and it does not redo the analysis but just picks the highest peak in that range and assigns it to `NATTUNE` in the lin-file.
- This should be very helpful for amplitude detuning analysis.
- Do NOT use the Nattune-Updater if you have free kicks (it adds a `NATTUNE`-Column to the lin-file).

!!! todo
    Include a screenshot of the frequency panel.

  [sklearn_IF]: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html

## Do Optics Dialog


=== "Closed Settings"

    <figure>
    <center>
    <img src="../../assets/images/betabeat_gui/do_optics_dialog.png" width="100%" alt="The 'Do Optics' Dialog"/>
    <figcaption>The "Do Optics" Dialog.</figcaption>
    </center>
    </figure>

=== "Open Settings"

    <figure>
    <center>
    <img src="../../assets/images/betabeat_gui/do_analysis_dialog_open_settings.png" width="100%" alt="The 'Do Optics' Dialog with open settings"/>
    <figcaption>The "Do Optics" Dialog with open settings.</figcaption>
    </center>
    </figure>

[bpm_panel_analyse]: bpm_panel.md#start-analysis