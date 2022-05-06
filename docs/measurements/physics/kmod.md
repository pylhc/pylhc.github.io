
# K-Modulation

This section gives a brief overview over the K-Modulation method.
A more detailed description can be found in M. Minty and F. Zimmermann's book[^MintyZimmermann] and the references therein.

Also available on this site is a [checklist for conducting K-Modulation measurements][kmod_procedure] in the LHC.

The full K-Modulation analysis is two-fold:
The [K-Modulation GUI][kmod_gui] is used for LHC measurements, and the following analysis is part of the [`omc3` package][omc3_package].

K-Modulation is a complementary optics measurement method which consists in changing the gradient of a quadrupole and measuring the induced tune variation.
The average $\beta$-function in the modulated quadrupole is linked to the gradient change $\Delta K$ and tune change $\Delta Q_{x,y}$ via[^MintyZimmermann]:

$$
\beta_{x,y} = \pm 2 \Delta K^{-1}\Big[ cot(2 \pi Q_{x,y}) [ 1 - cos(2 \pi \Delta Q_{x,y}) ] + sin(2 \pi \Delta Q_{x,y}) \Big]
$$

If these measurements are conducted for two adjacent quadrupoles, the evolution of the $\beta$-function in-between the modulated quadrupoles can also be inferred[^FelixKmodPaper].
Here, the average $\beta$-function in the quadrupole is expressed in terms of the optics functions $\beta_0$, $\alpha_0$, and $\gamma_0$ at the end of the quadrupole.

Assuming a drift space between the quadrupoles, these coordinates can then be expressed in terms of the distance of the quadrupole end to the middle of the drift-section $L^*$, the minimum $\beta$-function $\beta^*$, and $w$, the offset of this minimum with respect to the center of the drift.
The length $L^*$ is usually obtained from the machine layout.
Using the two average $\beta$-functions in the quadrupoles, the other two variables $\beta^*$ and $w$ can then be calculated.
The $\beta$-function at other elements in the drift space can then be determined by propagation.

Compared to other methods, K-Modulation allows to infer a potential waist shift and its direction, which is not possible using the turn-by-turn based methods.
However, K-Modulation is usually more time-intensive, and is only applicable with individually powered quadrupoles.

## Measuring $\beta^{*}$ Using K-Modulation in the LHC

!!! note ""
    Please keep in mind the [general checks][general_checks] for measurements.

??? info "The Procedure in Short"
        The important stuff.
        This decides over luminosity and lives in the experiments.

### Measurement

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
      <p> Fire up the [K-Mod application][kmod_gui].
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

### Analysis

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


[^MintyZimmermann]:
    ??? abstract "Measurement and Control of Charged Particle Beams, `Michiko G. Minty, Frank Zimmermann`, [https://doi.org/10.1007/978-3-662-08581-3](https://link.springer.com/book/10.1007%2F978-3-662-08581-3){target=_blank}"
        ```
        @book{Minty:629879,
          author = {Minty, Michiko G and Zimmermann, Frank},
          title = {Measurement and control of charged particle beams},
          publisher = {Springer},
          address = {Berlin},
          series = {Particle acceleration and detection},
          year = {2003},
          url = {https://cds.cern.ch/record/629879},
          doi = {10.1007/978-3-662-08581-3}
        }
        ```

[^FelixKmodPaper]:
    ??? abstract "Accuracy and Feasibility of the Beta* Measurement for LHC and High Luminosity LHC Using K Modulation, `F. Carlier, and R. Tomás`, [Phys. Rev. Accel. Beams **20**, 2017](https://link.aps.org/doi/10.1103/PhysRevAccelBeams.20.011005){target=_blank}"
        ```
        @article{PhysRevAccelBeams.20.011005,
          title = {Accuracy and Feasibility of the Beta* Measurement for {{LHC}} and {{High Luminosity LHC}} Using k Modulation},
          author = {Carlier, F. and Tom{\'a}s, R.},
          year = {2017},
          month = jan,
          volume = {20},
          pages = {011005},
          doi = {10.1103/PhysRevAccelBeams.20.011005},
          url = {https://link.aps.org/doi/10.1103/PhysRevAccelBeams.20.011005},
          journal = {Phys. Rev. Accel. Beams},
          keywords = {read},
          number = {1}
        }
        ```

*[CO]: Closed Orbit
*[BSRT]: Beam Synchrotron Radiation Telescope
*[OFB]: Orbit Feed Back
*[LSA]: LHC Software Architecture

[omc3_package]: ../../packages/omc3/getting_started.md
[kmod_procedure]: ../../measurements/procedures/kmod.md
[kmod_gui]: ../../guis/kmod/gui.md
[general_checks]: ../procedures/general_checks.md

[get_kmod_files_python2]: https://github.com/pylhc/Beta-Beat.src/blob/master/kmod/gui2beta/get_kmod_files.py
[kmod_python2]: https://github.com/pylhc/Beta-Beat.src/blob/master/kmod/gui2beta/gui2kmod.py
[kmod_python3]: https://github.com/pylhc/omc3/blob/master/omc3/run_kmod.py