# Amplitude Detuning Measurements

!!! note ""
    Please keep in mind the [general checks](general_checks.md) for measurements.

!!! info "The Procedure in Short"

    The basis of this measurement is to kick with increasing amplitude in a single plane and perform fits over the resulting tune shifts.
    To assure a good direct and cross detuning measurement, it is important to check that both natural tune lines (for the horizontal and vertical tune) are visible in the respective spectrum.
    It is of utmost importance for the detuning analysis to perform rigorous cleaning on the data. 

## Measurement

### Preparations

- [ ] <details class="nodeco"><summary>Confirm machine state</summary>
      <p>
      Make sure that the configuration of the machine is as you expect it. 
      </p></details>
    - [ ] Perform the [general checks](general_checks.md)
    - [ ] Check correct $\beta^*$ 
    - [ ] Check correct crossing angles
    - [ ] <details class="nodeco"><summary>Check collimation sequence</summary>
        <p>
        **"LOAD COARSE SETTINGS FOR NLO AT 30 CM"** is the current (run 3, 2022) collimation sequence for AC-Dipole kicks in the LHC at $\beta^* = 30 cm$ up to $\pm 170\mu rad$ IP1-V/IP5-H crossing
        and $\pm150\mu rad$ IP1-H, $-150\mu rad$ to $+140\mu rad$ IP5-V separation.
        </p></details>

- [ ] <details class="nodeco"><summary>Correct Coupling</summary>
      <p>
        As always, coupling should be well corrected to $|C-| \leq 10^{-3}$.
        This can be easily achieved by performing diagonal kicks of mediocre strength, and get the correction values from the GUI. 
        **Beware that the signs need to be switched for correction in the machine**.
      </p></details>

- [ ] <details class="nodeco"><summary>Do initial measurement</summary>
      <p>
      Start with a low AC-Dipole amplitude in both planes (e.g. 5%-10%) and analyse the resulting data.
      </p></details>
    - [ ] <details class="nodeco"><summary>Check both **Natural Tunes** are visible</summary>
        <p>
        Perform a quick harmonic analysis on the resulting data and check the spectrum.
        Both natural tunes need to be visible in their respective plane for the majority of BPMs.
        If not, maybe try to adapt the tune delta and move the driven tunes closer to the natural ones.
        See Info-box "Tune Deltas" below.
        <figure style="width:49%; display: inline-block;">
            <img src="../../../assets/images/amplitude_detuning_procedure/FrequencyChart_one_tune_not_found.png">
            <figcaption>Bad Spectrum.</figcaption>
        </figure>
        <figure style="width:49%; display: inline-block;">
            <img src="../../../assets/images/amplitude_detuning_procedure/FrequencyChart_both_tunes_found.png">
            <figcaption>Good Spectrum.</figcaption>
        </figure>
        </p></details>
    - [ ] Repeat until the spectrum looks usable

!!! info "Tune Deltas"

    in the past, clean amplitude detuning measurements could be achieved with tune deltas (signs as given in Multiturn) of <br>
    Horizontal: -0.009,<br> 
    Vertical: +0.007.


### Actual Measurement 

!!! warning "When kicking with crossing angles"

    When kicking with the crossing orbit bump in, make sure at each kick, that the **losses occur in IP6/IP7** 
    and **not in the IPs with the crossing** in (usually IP1 and IP5)!
    Losses in these IPs can appear with minor amplitude change, so **keep the amplitude increase between kicks small**.
    If you see losses in the IPs with crossing angles, but you are not yet happy with your maximum amplitude and you still have a lot of beam intensity left,
    you can kick at the same amplitude a few times and hope that the losses go down (the outermost particles are scraped) and then (carefully) continue increasing amplitude again.


- [ ] <details class="nodeco"><summary>Kicks in the vertical plane</summary>
      <p>
      While keeping the AC-Dipole amplitude in the horizontal plane constant (but not zero, to avoid weird AC-Dipole behaviour and to see if there is coupling effects),
      slowly increase the amplitude in the vertical plane.
      </p></details>
    - [ ] Kick with slowly increasing amplitude (1%-5% increase between kicks)
    - [ ] Check losses stay low after each kick, adapt amplitude increase accordingly
    - [ ] <details class="nodeco"><summary>Check for tune drift</summary>
          <p>
          If you are kicking with reduced tune deltas, it is also important to have an eye on the tune drift of the machine, 
          so that you do not further decrease the distance between natural tune and excitation. 
          Update the tune in multiturn if necessary.
          </p></details>
    - [ ] Try to reach 0.015 $\mu m$ - 0.020 $\mu m$ in action ($2J_x$)
    - [ ] Get around 15-20 kicks
    - [ ] When kicking with crossing: head the warning above!

- [ ] <details class="nodeco"><summary>Kicks in the horizontal plane</summary>
      <p>
      While keeping the AC-Dipole amplitude in the vertical plane constant (but not zero, to avoid weird AC-Dipole behaviour and to see if there is coupling effects),
      slowly increase the amplitude in the horizontal plane.
      </p></details>
    - [ ] Kick with slowly increasing amplitude (1%-5% increase between kicks)
    - [ ] Check losses stay low after each kick, adapt amplitude increase accordingly
    - [ ] <details class="nodeco"><summary>Check for tune drift</summary>
          <p>
          If you are kicking with reduced tune deltas, it is also important to have an eye on the tune drift of the machine, 
          so that you do not further decrease the distance between natural tune and excitation. 
          Update the tune in multiturn if necessary.
          </p></details>
    - [ ] Try to reach 0.015 $\mu m$ - 0.020 $\mu m$ in action ($2J_y$)
    - [ ] Get around 15-20 kicks
    - [ ] When kicking with crossing: head the warning above!

- [ ] <details class="nodeco"><summary>Diagonal Kicks (optional)</summary>
      <p>
      To increase the accuracy of the cross-term measurement, 2D kicks (and 3.5D fitting) can be performed.
      If this is desired, it makes sense to throw some diagonal kicks, i.e. kicks with (more or less, not too important for the fitting) equal amplitude into the mix.
      </p></details>
    - [ ] Kick with slowly increasing amplitude (1%-5% increase between kicks)
    - [ ] Check losses stay low after each kick, adapt amplitude increase accordingly
    - [ ] <details class="nodeco"><summary>Check for tune drift</summary>
          <p>
          If you are kicking with reduced tune deltas, it is also important to have an eye on the tune drift of the machine, 
          so that you do not further decrease the distance between natural tune and excitation. 
          Update the tune in multiturn if necessary.
          </p></details>
    - [ ] Try to reach 0.015 $\mu m$ - 0.020 $\mu m$ in action in both planes
    - [ ] Get around 15-20 kicks
    - [ ] When kicking with crossing: head the warning above!

!!! info "Action Estimation"

    The action can be calculated if $\beta$ and peak-to-peak is known for a specific BPM by $2J = \frac{(0.5 \cdot pk2pk)^2}{\beta}$.
    Otherwise it can always be checked running optics analysis on a file and looking into the Optics &rarr; Action/Tune tab or the kick-file.

## Analysis

Analysis performed with the Beta-Beat GUI omc3 v0.1.0.

The analysis of amplitude detuning data requires very accurate estimates of the natural tunes, 
which can be hard to find if they get lost in the BPM noise or when they are close to resonances in the spectrum.
Multiple features have been implemented in python and GUI to ease the detuning analysis.

As the main steps follow the standard optics analysis, the entries described here are mostly hints and tricks 
on how to optimize the analysis and only need to be applied where necessary.

- [ ] <details class="nodeco"><summary>Load Data</summary>
      <p>
      Simply load the data in the BPM panel.
      Make sure you are loading the correct data and check the logbook for misfired kicks etc.
      </p></details>
- [ ] <details class="nodeco"><summary>Run Spectral Analysis</summary>
      <p>
      A bad spectral analysis can be recovered by the steps mentioned in "Cleaning", 
      but a good frequency spectrum and well found natural tunes will save you a lot of time later on.
      </p></details>
    - [ ] <details class="nodeco"><summary>Good Frequency Resolution (`TurnBits > 15`)</summary>
          <p>
          As the tune drift can be very small, we would want a good resolution in frequency, which can be controlled by `TurnBits`.
          The standard value of `TurnBits` of `20` (leading to $2^{20}$ complex coefficients, i.e. $2^{21}$ spectral lines) is a good start, but can lead to excessive memory use when analysing 15-20 files at once. 
          I estimate (from experience), that with `19` turn-bits, you will need 70-90GB of RAM, while `18` halves that value.
          Both of these should be good values to use (see Infobox "TurnBit Estimation" below).<br>
          The `OutputBits` on the other hand can be smaller, as the highest line stored per "bucket" will keep the frequency location calculated from the higher resolution form `TurnBits`.
          Therefore, even if the wrong line is selected (see Tolerance), the correct tune line will still be available in its bucket. 
          The only issue would be, if there is a resonance really close by. 
          A value of `10`-`12` ($0.5 \cdot 10^{-4} - 10^{-4}$ tune units) should be enough, to keep the file-size manageable and allow to open all the files in the GUI.
          </p></details>
    - [ ] <details class="nodeco"><summary>Small Tolerance</summary>
          <p>
          To not accidentally capture 
          <figure style="width:90%;">
              <img src="../../../assets/images/amplitude_detuning_procedure/tune_settings.png">
              <figcaption>Tune settings.</figcaption>
          </figure>
          </p></details>
    - [ ] <details class="nodeco"><summary>Use Autotunes and Nat-Deltas</summary>
          <p>
          As the 
          <figure style="width:90%;">
              <img src="../../../assets/images/amplitude_detuning_procedure/tune_settings.png">
              <figcaption>Tune settings.</figcaption>
          </figure>
          </p></details>
- [ ] Check data for correct tunes
- [ ] Analyse data
- [ ] Run BBQ correction

??? info "Quick TurnBit Estimation"
    Let's assume a small detuning of $10 \cdot 10^3 m^{-1}$ and an action increase between kicks of $0.016 \mu m / 20$,
    leading to a detuning difference between two kicks of $\Delta Q = 8 \cdot 10^{-6}$.
    The frequency resolution $\Delta f$ is the inverse of the length of the turns-data (halfed, as we have pairs), so $2^{-TurnBits-1}$ :<br>
    `TurnBits = 20`: $\Delta f = 4.8 \cdot 10^{-7}$<br>
    `TurnBits = 19`: $\Delta f = 9.5 \cdot 10^{-7}$<br>
    `TurnBits = 18`: $\Delta f = 1.9 \cdot 10^{-6}$<br>
    `TurnBits = 17`: $\Delta f = 3.8 \cdot 10^{-6}$<br>
    `TurnBits = 16`: $\Delta f = 7.6 \cdot 10^{-6}$<br>
    `TurnBits = 15`: $\Delta f = 1.5 \cdot 10^{-5}$<br>
    We therefore need to set `TurnBits` to at least `16` to assure that we will see the change $\Delta Q$ between kicks.