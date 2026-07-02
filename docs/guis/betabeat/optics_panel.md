# The Optics Panel

!!! warning "Incomplete"
    This page is a placeholder and is not yet complete.
    Information here is outdated and needs to be revised for the `omc3` version of the Beta-Beat GUI.

The `Optics Panel` provides graphical interface to compare the computed optics to the nominal model.
There are in total three main tabs for the optics panel:

- The [Optics](#optics-tab) tab, where a tree menu (on the left) provides many physical properties to be displayed.

## Optics Tab

A wide variety of computed physical properties can be visualised across the entire machine.

!!! todo
    Include a screenshot with the main optics tab.

### Open Files

- TODO: Open files (also takes BBS files! [outputfiles](betabeatsource.md#meaning-of-the-beta-beatsrc-output-files))

### Optics Plotting

- RDT and CRDT plots are added dynamically depending on the files present in the respective folders.
- Nicer names and more structure in the tree.
- Backend was rewritten, so it is now more modular and easier to add new plot-types.

## Computing Corrections

The `Correction` button at the bottom left of the optics panel can be used to calculate the optics corrections for the beam process.

The settings dialogue offers a wide range of different options for corrections.
This will call different external python scripts again.

These scripts calculate corrections for beta-beat, coupling and horizontal and vertical dispersion using the computed response matrices.
The following methods implement different correction algorithms:

- `Coupling`: Single beam correction of coupling resonances and vertical dispersion.
- `Global correction`: Single beam correction of phase, beta and horizontal dispersion.
- `Iterative correction`: Two-beams version of the global correction.
- `Chromatic coupling`: Single beam correction of chromatic coupling using skew sextupoles at dispersive locations.

??? note
    The `Iterative correction` method is currently not compatible and thus disabled.

The results are output in the `changeparameters` files.
These files store the magnet names and corresponding correction strengths.

They are also displayed in the [Correction Panel](correction_panel.md).
