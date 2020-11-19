# Beta-Beat Gui for `omc3`

!!! info ""
    This page is meant for people, who know the old Gui and want to use the `omc3` functionality in the GUI now!

For now, this is still in beta and has a lot of not-yet-implemented functionality.
On the up-side, it also has some new-and-improved functionality over the Beta-Beat-Source (`master`) branch.
The basic optics analysis and plotting work!

## Important changes

### Python

In the Beam-Selection Window you need to give it a python-binary (e.g. `venv/bin/python`).
Best would be if you have a local virtual environment.
This **needs to have omc3 installed as a package**.
See [omc3 on github][omc3_github_getting_started]{target=_blank}.
```bash
pip install git+https://github.com/pylhc/omc3.git
```
This is because python calls are now made by module, i.e.:
```bash
python -m omc3.module arg1 arg2 ...
```

### Settings

* Settings are now all in one place (the settings-button on top).
* Entries in the settings that are lists (e.g. 'Turns' which will be `STARTTURN ENDTURN`) are given as **space-separated** values, NOT comma separated.
* Settings can be reverted as long as you do not click apply.
* Settings are applied automatically on ++okbtn++.
* Settings are reset to last applied on ++cancelbtn++.

### Opening Files

* Each tab has now an <span style="color:green;">Open Files</span> button, which opens only the files specific to this tab.
* The magic <span style="color:green">**+**</span> button is gone, as its functionality was confusing (and there were different stories about its workings).

### Optics Plotting

* RDT and CRDT plots are added dynamically depending on the files present in the respective folders.
* Nicer names and more structure in the tree.
* Backend was rewritten, so it is now more modular and easier to add new plot-types.

### Keys in Plots

* ++lbutton++ : Draw and zoom into rectangle.
* ++mbutton++ : Auto-zoom (in 3 Steps: 4&sigma;, 3&sigma;, 2&sigma;).
* ++rbutton++ : Undo last step.
* ++shift+rbutton++ : Undo all steps (reset plot).
* ++mousewheel++ : Zoom relative to mouse position.
* ++shift+mousewheel++ : Zoom y-axis relative to mouse position.
* ++alt+mousewheel++ : Zoom relative to plot center.
* ++shift+alt+mousewheel++ : Zoom y-axis relative to plot center.

### Nattune Updater

* You can set a frequency range and it does not redo the analysis but just picks the highest peak in that range and assigns it to `NATTUNE` in the lin-file.
* This should be very helpful for amplitude detuning analysis.

## Known not to work:

* Other accelerators than the `LHC` (you can trick it a bit, though, by choosing LHC and then changing the accelerator manually in the `settings`).
* Removing turns (but you can set Start and End turn in the settings).
* BBQ compensation for amplitude detuning can't be called directly from the GUI.
* Things that do not work as they are not implemented in `omc3`:
    - Global Corrections,
    - SegmentBySegment,
    - Spectrum Plot Export cannot export both planes into one axis,
    - Optics Plot Export cannot have separate limits for the two plots,
    - Optics Plot Export cannot export CRDT plots,
* Do NOT use the Nattune-Updater (in the Spectrum panel) if you have free kicks (it adds a `NATTUNE`-Column to the lin-file).

!!! warning "Bug Reporting"
    If you find bugs, please make [JIRA tickets][jira_bug_tickets]{target=_blank} with the `OMC3-GUI` label.


[omc3_github_getting_started]: https://github.com/pylhc/omc3#getting-started
[jira_bug_tickets]: https://its.cern.ch/jira/projects/BBGUI/issues