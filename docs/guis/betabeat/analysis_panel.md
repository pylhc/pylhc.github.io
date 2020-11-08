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
    
## The Frequency Tab

The `Frequency` tab displays the computed frequencies for every BPM.

A `Get Optics` button can be used to start the optics calculation.
This will call an external python script again, with the results available in the [Optics Panel](optics_panel.md).

!!! todo
    Include a screenshot of the frequency panel.