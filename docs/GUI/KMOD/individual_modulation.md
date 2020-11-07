# Performing Individual Magnet Modulation

The Kmod GUI also allows for a modulation of a given magnet circuit.
This is used for example for the quadrupoles in the matching section of the experimental insertions, or in the RF insertion, where one circuits corresponds to one quadrupole.
The Kmodulation data can then be used to extract the beta-functions at instruments (e.g. BSRT) between the quadrupoles.

As of 2018, the instruments for which the measured beta-function has been used for calibration are the Wirescanner (`BWS.5`) and the undulator (`MU.B5`) or dipole D3 (`MBRS.5`) for the BSRT.
All these instruments are located between `Q5R` and `Q5L`. 
Additionally, in beam 2, between `MQM.7L4.B2` and `MQY.6L4.B2` the `BGV` demonstrator is located (`B7L4.B2`).

## Circuit Selection

The first step is to select a magnet circuit to use.
You can do so under `Parameter Selection` -> `Select Quadrupole`.

The circuit corresponding to the quadrupole to be modulated has to be selected on the right hand side of the panel and added via the `add quadrupole` button to the left hand side.
As example for the naming convention, the circuit `RQ5/.R4B2/K1` corresponds to the `MQY.5R4.B2` in the LHC sequence file.
Under `Trim Function`, select `Sine Function` before continuing.

!!! todo
    Include screenshot of circuit selection

## Trim Start

The trim current, frequency, and number of cycles should be entered on the right hand side of the window and need to be set via the `apply settings` button.
Normal values for trim I in IR4 are 2A at injection for the `Q5` and 12A at 6.5 TeV for the `Q5`.
Values for other magnets can be found in the elogbook in the shifts logs of the `28/04/2018` and `07/10/2016`.

Data acquisition is started with the `Start Acquiring` button, following by starting the trim with the `Start trim` button.
After the trim is finished, acquisition of data needs to be stopped using the `Stop Acquiring` button.

!!! todo
    Include screenshot of trim start

!!! warning
    The start and end time should be noted down in the elogbook for later data extraction, as no automatic extraction like in the IP modulation case exists. 

## Trim Extraction

After acquisition during a trim, data can then be extracted by selecting the circuit in the `Select Quadrupole` panel under `Parameter selection` and pushing the `extract previous trim` button.
The trim start and end times as well as the beam energy need to be entered.
In the following panel, the trim data can then be saved via the `Save magnet measurement` button.

!!! todo
    Include screenshot of trim extraction

The analysis of the extracted Kmod data is described in the [next section](trim_analysis.md).


*[BSRT]: Beam Synchrotron Radiatin Telescope
*[BGV]: Beam Gas Vertex detector (for beam size measurement)
*[LHC]: Large Hadron Collider