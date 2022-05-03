# Measuring $\beta^{*}$ Using K-Modulation in the LHC

!!! note ""
    Please keep in mind the [general checks](general_checks.md) for measurements.

??? info "The Procedure in Short"
        The important stuff.
        This decides over luminosity and lives in the experiments.

## Measurement

- [ ] <details class="nodeco"><summary>Adjust Working Point</summary>
      <p> The tunes should be moved to a working point with a large tune separation, such as $Q_x = 0.28 / Q_y = 0.31$, to allow for maximum modulation amplitude.
      </p></details>

- [ ] <details class="nodeco"><summary>Check Coupling</summary>
      <p> Perform quick check for $|C^{-}|$ to avoid influence from a possible closest tune approach.
      Also check for any unwanted local coupling bumps around the modulated quadrupole.
      </p></details>

- [ ] Check feedbacks

    - [ ] <details class="nodeco"><summary>Turn on orbit feedback</summary>
        <p>In case of any (design) orbit excursion in the quadrupoles, enable orbit feedback to avoid a change of the CO around the ring.
        Caveat: for the determination of the crossing angles, orbit feedback should be off.
        </p></details>

    - [ ] <details class="nodeco"><summary>Turn off tune feedback</summary>
        <p> Otherwise modulation and feedback would work against each other.
        </p></details>

- [ ] <details class="nodeco"><summary>Run K-Modulation</summary>
      <p> Fire up the [K-Mod application][kmod_app].
       There two options are available:
      - IP Modulation : Runs a modulation on both quadrupoles closest to the selected IP.
      - Single circuit modulation : Runs a modulation on a selected quadrupole circuit (used for measuring the beta-functions in IR4, where BSRT is located).
      </p>
      </details>

    - [ ] <details class="nodeco"><summary>Chose Modulation Amplitude</summary>
        <p> Choose a modulation current such that the change in tune is roughly 0.01.
        This can either be done by looking up old shifts with similar optics or by increasing the amplitude until satisfactory tune change is observed.
        Modulation frequency is chosen by the system, with higher modulation amplitude resulting in lower modulation frequency.
        </p></details>

    - [ ] <details class="nodeco"><summary>Document Measurement</summary>
        <p> As no automatic logging of the modulation is implemented for now, parameters should be logged in the logbook.
        Parameters to log are: `Starttime`, `Endtime`, `Modulation current`, `IP`, other comments such as $\beta^{*}$, status of the `OFB`, is significant tunejitter/-jump observed.
        </p></details>

## Analysis

- [ ] <details class="nodeco"><summary>Extract Data from Timber</summary>
      <p> After the analysis, a window should open to allow for extraction of the data from `Timber`.
      Alternatively, `Extract previous trim` can be used.
      Saving in a separate directory with a descriptive name is recommended (e.g. `Kmod_IPX_beta_beforeCorrection_starttime`) and should be added to the modulation logbook entry.
      </p></details>

- [ ] <details class="nodeco"><summary>Start the Analysis</summary>
      <p> Run the python codes on the extracted Timber data to get the $\beta$ you need.
      As of now, only the Kmod analysis from `Beta-Beat.src` can be called from the K-Modulation GUI for the case of an analysis of an IP-Modulation.
      Codes and some documentation may be found [for `Python2`][kmod_python2]{target=_blank} and [for `Python3`][kmod_python3]{target=_blank}.
      </p></details>

- [ ] <details class="nodeco"><summary>Check Results</summary>
      <p> The results of the analysis should be located in the previously specified working directory and can be checked by eye using a text editor of choice.
      </p></details>

    - [ ] <details class="nodeco"><summary>Use in Beta-Beat GUI for Correction</summary>
        <p> Using this [script][get_kmod_files_python2]{target=_blank}, the results can be brought in a form which is readable for the BBGUI and can then be used to calculate a correction.
        </p></details>

    - [ ] <details class="nodeco"><summary>Publish Results</summary>
        <p> If results are satisfactory, both `Python2` and `Python3` should create a file called `lsa_results.tfs`, which can be uploaded using the LSA optics uploader for other users to access data.
        </p></details>

*[CO]: Closed Orbit
*[BSRT]: Beam Synchrotron Radiation Telescope
*[OFB]: Orbit Feed Back
*[LSA]: LHC Software Architecture

[kmod_app]: ../../guis/kmod/gui.md
[get_kmod_files_python2]: https://github.com/pylhc/Beta-Beat.src/blob/master/kmod/gui2beta/get_kmod_files.py
[kmod_python2]: https://github.com/pylhc/Beta-Beat.src/blob/master/kmod/gui2beta/gui2kmod.py
[kmod_python3]: https://github.com/pylhc/omc3/blob/master/omc3/run_kmod.py
