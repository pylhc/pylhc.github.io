# Measuring $\beta^{*}$ Using K-Modulation in the LHC

!!! info "The Procedure in Short"

    We use K-modulation to determine the $\beta$-functions at the interaction points and, with better accuracy than classical measurements, at the BPMs closest to the IPs.
    The quadrupole circuits closest to the IP are modulated and the consequent tune changes are measured.
    See [this page][kmod_method] for details on the K-modulation method.

Please keep in mind the [general checks](general_checks.md) for measurements, and see the [K-Mod guide][kmod_app] for how to perform the tasks listed below.

## Procedure

- [ ] <details class="nodeco"><summary>Adjust Working Point</summary>
      <p> The tunes should be moved to a working point with a large tune separation, such as $Q_x = 0.28 / Q_y = 0.31$, to allow for maximum modulation amplitude.
      Pay attention to potential resonance crossings.
      </p></details>

- [ ] <details class="nodeco"><summary>Check Coupling</summary>
      <p> Perform quick check for $|C^{-}|$ to avoid influence from a possible closest tune approach.
      Also check for any unwanted local coupling bumps around the modulated quadrupole.
      </p></details>

- [ ] <details class="nodeco"><summary>Start the K-modulation GUI</summary>
      <p> See the [K-Mod pages][kmod_app].
      </p></details>

- [ ] <details class="nodeco"><summary>Ensure the orbit feedback is ON</summary>
      <p>In case of any (design) orbit excursion in the quadrupoles, enable orbit feedback to avoid a change of the CO around the ring.
      The status is visible in the top right corner of the GUI.
      </p></details>

- [ ] <details class="nodeco"><summary>Ensure the tune feedback is OFF</summary>
        <p> Otherwise modulation and feedback would work against each other.
        The status is visible in the top right corner of the GUI.
        </p></details>

- [ ] <details class="nodeco"><summary>Run K-Modulation</summary>
      <p> See the [following page][kmod_run] for how to perform a modulation of the desired circuit.
      Check from the modulation graph for the quality of the modulation and data.
      </p></details>

- [ ] <details class="nodeco"><summary>Start the Analysis</summary>
      <p> Analysis is now launched directly from the `Pykmod` app.
      See [this page][kmod_analysis] for details on how to analyze and export the data.
      </p></details>

- [ ] <details class="nodeco"><summary>Import Results Into the Beta-Beat GUI</summary>
      <p> The results are useful to compute optics corrections.
      See the [Beta-Beat GUI page][beta_beat_gui] for how to import the results.
      </p></details>

*[CO]: Closed Orbit
*[BSRT]: Beam Synchrotron Radiation Telescope
*[OFB]: Orbit Feed Back
*[LSA]: LHC Software Architecture

[kmod_app]: ../../guis/kmod/gui.md
[kmod_run]: ../../guis/kmod/modulating.md
[kmod_analysis]: ../../guis/kmod/analyzing.md
[kmod_method]: ../../measurements/physics/kmod.md
[beta_beat_gui]: ../../guis/beta_beat/gui.md
