# LHC Local Coupling Corrections with a Rigid Waist Shift

!!! note ""
    Please keep in mind the [general checks](general_checks.md) for measurements.

??? info "The Procedure in Short"

      This methods aims to find the MQSX correction settings that would minimize betatron coupling and its impact on beam size *at IP*.
      The method breaks the symmetry of the optics in the IR and forces local coupling RDTs to leak thoughout the machine, which makes them measurable through the $|C^{-}|$.


      After global corrections are done and trimmed in the machine, one applies a rigid waist shift in a given IR and scans the colinearity knob for the value that minimises the $|C^{-}|$.
      These settings, when taking away the rigid waist shift, will minimize local coupling and its impact at IP.

## Preliminary Setup

- [ ] <details class="nodeco"><summary>Do Global Corrections</summary>
      <p> This procedure needs global corrections to be trimmed in the machine first, so optics and *global* coupling should be taken care of beforehand.
      </p></details>

- [ ] <details class="nodeco"><summary>**Optional:** Scan the Colinearity Knob to Check Conditions</summary>
      <p> If time allows, ideally we would scan the colinearity knob to ensure we see very small variations of the $|C^{-}|$.
      If strong variations are noticed, then the expected conditions for the procedure are not met: either the phase advance between left and right MQSXs is off, or the $\sqrt{\beta_x \beta_y}$ is significantly wrong at these elements.
      </p></details>

## Procedure Per IP

One should do this for earch of IP1, IP2, IP5 and IP8 which are the ones requiring local corrections.
Keep in mind that this does beam 1 and 2 at the same time.

!!! warning "Orbit Feedback"
      Please remember to **always** keep the orbit feedback system ON during this procedure.

- [ ] <details class="nodeco"><summary>Trim in the Waist Shift Knob</summary>
      <p> Trim the prepared knob in the machine, for a certain direction (waist left/right of IP).
      Remember that this affects both beams at the same time.
      </p></details>

- [ ] <details class="nodeco"><summary>Scan the Colinearity Knob</summary>
      <p> Trim the colinearity knob, about half a unit at a time.
      For each setting, do some kicks and measure the $|C^{-}|$.
      </p></details>

- [ ] <details class="nodeco"><summary>Go Back to Nominal Machine</summary>
      <p> Trim out the rigid waist shift, and ensure that no drift from nominal is observed.
      If needed, do another round of global corrections.
      </p></details>

- [ ] <details class="nodeco"><summary>Trim in the Opposite Waist Shift Knob</summary>
      <p> Trim the prepared knob in the machine, for the other direction (waist right/left of IP).
      </p></details>

- [ ] <details class="nodeco"><summary>Scan the Colinearity Knob</summary>
      <p> Trim the colinearity knob, about half a unit at a time.
      For each setting, do some kicks and measure the $|C^{-}|$.
      </p></details>

- [ ] <details class="nodeco"><summary>Determine the Correction</summary>
      <p> Plot the evolution of the $|C^{-}|$ against the setting of the colinearity knob, and pick the setting that minimizes it.
      The curves for each beam might not be minimized exactly around the same point, and a compromise may be needed.
      Eventually do a fit of the data to get a more accurate estimate of the correction.
      </p></details>

- [ ] <details class="nodeco"><summary>**Optional:** Perform a Luminosity Scan of the Colinearity Knob</summary>
      <p> In commissioning and if conditions allow, one can validate and fine tune the correction with a luminosity scan.
      This has to be performed without a rigid waist shift.
      </p></details>

- [ ] <details class="nodeco"><summary>**Optional:** Do Global Corrections After Trimming</summary>
      <p> One might want to do another round of global corrections, mainly coupling, after applying the determined colinearity knob setting.
      </p></details>

*[MQSX]: The skew quadrupole correctors localed next to Q3
*[IP]: Interaction Point
*[IR]: Insertion Region
*[RDT]: Resonance Driving Terms
*[Colinearity Knob]: This is a powering setting of the MQSXs, which corresponds to a K1S value of +/- 1E-4 m^-2.