# The Correction Panel

The `Correction` panel is where global corrections [computed in the `Optics` panel](optics_panel.md#computing-global-corrections) are loaded, reviewed and tested, with the aim of bringing the measured machine as close as possible to nominal model conditions.
It also gives access to the `Knob Panel`, used to turn a correction into a knob in the LSA database for use in operations.
The panel is split into two sub-tabs: `Correction` and `Correction test`.

The default view is the `Correction` tab, which loads correction files and displays the strengths (powering changes) of affected magnets or knobs.
The `Correction test` tab will be covered further down, see [checking corrections](#checking-corrections).

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/betabeat_gui/correction_panel/correction_panel_default.png" width="95%" alt="Correction Panel Default Look"/>
  <figcaption>The <code>Correction</code> panel's default appearance.</figcaption>
  </center>
</figure>

The `Correction` tab is organised into three areas.
On the left is a table listing the loaded correction files, named as the relative path to the corresponding `changeparameters` file.
Any correction computed in the [`Optics` panel](optics_panel.md#computing-global-corrections) will appear here automatically
Clicking the ++"Load Correction Files"++{.green-gui-button} button above the table opens a dialogue to select and load previously determined corrections from disk.

To the right, the `Strengths` plot displays the powering changes assigned by the selected correction to each affected magnet or knob.
Below the table, the ++"Open Knob Panel"++{.blue-gui-button} button allows exporting a correction as a knob, see [knob creation](#knob-creation).

## Viewing Corrections

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/betabeat_gui/correction_panel/corrections_strengths.png" width="95%" alt="Correction Panel with Loaded Corrections and Strengths Plot"/>
  <figcaption>The <code>Correction</code> tab with correction files loaded; the <code>Strengths</code> plot on the right shows the powering change assigned to each corrector.</figcaption>
  </center>
</figure>

!!! tip "Global Coupling Corrections Trims"
    In the special case of global coupling corrections computed with the [coupling preset](optics_panel.md#presets), and to facilitate the user's work, double clicking on the correction file name in the table will spawn a popup detailing the exact trim to apply in the accelerator cockpit app.

    <figure>
      <center>
      <img class="clickImg" src="../../assets/images/betabeat_gui/correction_panel/coupling_corrections_trim.png" width="65%" alt="Global coupling trim details"/>
      <figcaption>The global coupling trim popup, highlighting the exact determined corrections and corresponding trims to apply on each knob.</figcaption>
      </center>
    </figure>

## Checking Corrections

The `Correction test` tab lets one apply a correction to the model and inspect its effect before committing to it in the machine.


<figure>
  <center>
  <img class="clickImg" src="../../assets/images/betabeat_gui/correction_panel/corrections_correction_test.png" width="95%" alt="Correction Test Sub-tab"/>
  <figcaption>The <code>Correction test</code> tab, where a correction is applied to the model to inspect its effect before use.</figcaption>
  </center>
</figure>

<!-- TODO: show the correction test in python -->

## Knob Creation

It provides an `Open Knob Panel` button to access the LHC beam process list.

### The Knob Panel

Through the `Knob Panel`, corrections can be provided directly inside the LHC beam system.

<figure>
  <center>
  <img class="clickImg" src="../../assets/images/betabeat_gui/correction_panel/corrections_knob_panel.png" width="95%" alt="Knob Panel Creation Tab"/>
  <figcaption>The <code>Knob Panel</code> on its <code>Creation</code> tab, listing the beam processes from which a knob is built.</figcaption>
  </center>
</figure>

!!! warning "Technical Network Access Needed"
    Being inside of the Technical Network is required for the `Knob panel` functionality.

In the `Knob Panel`, one can create Knobs (in the `Creation` tab) by using the previously computed corrections.

To create a knob, one or several beam processes have to be selected.
Once selected, the corresponding optics will appear.
At least one optic has to be selected.

After providing a `Knob name`, the `Create Knob` button will create a new Knob in the LSA database.

The `View Knobs` tab displays a list of all BETA-BEATING Knobs.
By selecting one, the user can examine or visualise the values attributed to each component.


<!-- TODO: Include a screenshot of the Knob Panel view knobs table -->

<!-- TODO: Include a screenshot of the Knob Panel view knobs chart -->


*[LSA]: LHC Software Architecture
