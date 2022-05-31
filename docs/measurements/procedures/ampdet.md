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
        **"LOAD COARSE SETTINGS FOR NLO AT 30 CM"** 
        is the current (run 3, 2022) collimation sequence for AC-Dipole kicks in the LHC at $\beta^* = 30$cm up to $\pm170\mu$rad IP1-V/IP5-H crossing
        and $\pm15\mu$rad IP1-H, $-150\mu$rad - $+140\my$rad IP5-V separation.
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
    - [ ] Try to reach 0.015 $\mu m$ - 0.020 $\mu m$ in action in both planes
    - [ ] Get around 15-20 kicks
    - [ ] When kicking with crossing: head the warning above!

!!! info "Action Estimation"

    The action can be calculated if $\beta$ and peak-to-peak is known for a specific BPM by $2J = \frac{(0.5 \cdot pk2pk)^2}{\beta}$.

## Analysis

Analysis performed with the Beta-Beat GUI omc3 v0.1.0.

- [ ] Load data
- [ ] Check data for correct tunes
- [ ] Analyse data
- [ ] Run BBQ correction
