# The Beta-Beat GUI Analysis Panel

The analysis panel provides graphical interface to visualize results from harmonic analysis performed on measured data.
The results are given in the [`tfs`](https://mad.web.cern.ch/mad/madx.old/Introduction/tfs.html){target=_blank} format.

In the analysis panel one can edit the `dp/p` value in the corresponding column, and see the changes applied. 

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
  <img src="../../../assets/images/analysis_panel_cleaning.png" width="65%" />
  <figcaption> Cleaning before optics analysis </figcaption>
  </center>
</figure>

### Additional cleaning based on the tune ##
Additionally, BPMs can be cleaned based on the tune values computed by harmonic analysis. The chart displaying the selected columns of harmonic analysis data has interactive cursors. These cursors can be moved manually to set the thresholds for tune-based cleaning - all BPMs having tune values outside of the set range will be removed. The cursors can be also automatically set to e.g. 4 sigmas deviation from the average tune values over all BPMs.

### Summary of cleaning steps before optics analysis

- [ ] Before loading tbt-files: check SVD settings and signal cuts in the global settings panel
- [ ] After harmonic analysis: Detect bad BPMs with Isolation Forest
- [ ] If neccessary: check tunes in the chart, set cursors, clean tune outliers.

## The Frequency Tab

The `Frequency` tab displays the computed frequencies for every BPM.

A `Get Optics` button can be used to start the optics calculation.
This will call an external python script again, with the results available in the [Optics Panel](optics_panel.md).

!!! todo
    Include a screenshot of the frequency panel.
    
  
  [sklearn_IF]: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html
