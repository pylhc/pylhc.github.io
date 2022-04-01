# General Checks

## Before Measuring

Here are a few checks to perform before starting measurements.
These are updated as much as possible for Run 3 values.

- [ ] <details class="nodeco"><summary>Make Sure Intensity Is below $10^{10}$ppb until Local Corrections Are In</summary>
      <p> After local corrections, we can move to having 3 bunches at $10^{10}$ppb evenly spaced along the ring.
      </p></details>

- [ ] <details class="nodeco"><summary>Mask the Appropriate BLMs</summary>
      <p> It is possible tp "mask" some of the BLMs, which means making sure they won't trigger any beam dump. They are essentially ignored in the interlocked system when masked.
      </p></details>

- [ ] <details class="nodeco"><summary>Turn Off the Landau Octupoles</summary>
      <p> Unless you specifically need them on for your measurements (ampdet & co).
      These are the MO elements.
      </p></details>

- [ ] <details class="nodeco"><summary>Correct the Machine Chromaticity to a Few Units</summary>
      <p> In the past we've used $2$, which we will most likely keep using in Run 3.
      </p></details>

- [ ] <details class="nodeco"><summary>Mask the ATLAS BCM</summary>
      <p> This status should be visible in the Multiturn application.
      </p></details>

- [ ] <details class="nodeco"><summary>Check the AC Dipole Keys Are In</summary>
      <p> Or MKA if that's used.
      </p></details>

- [ ] <details class="nodeco"><summary>Make Sure the Collimators Are Open</summary>
      <p> There should be a pre-made setting for this.
      </p></details>

!!! note "Timing Tables"
    Normally, starting in Run 3 the timing tables are automatically loaded by the Multiturn application.
    It can't hurt to check that they are, though.

## For Measurements

Here are some general checks on should always keep in mind when performing measurements.

- [ ] <details class="nodeco"><summary>Make Sure to Put in the Correct Tunes</summary>

- [ ] <details class="nodeco"><summary>Start with Small Kicks and Gradually Go up in Amplitude</summary>
      <p> For linear kicks we aim for $\sim 2mm$ in the arcs.
      The value should be displayed in Multiturn, and after a kick one can directly check the BPM data in the application.
      </p></details>

- [ ] <details class="nodeco"><summary>Use Asymmetrical Deltas for the Driving</summary>
      <p> Do not set $|\Delta Q_x| = |\Delta Q_y|$ for the AC Dipole.
      We usually go for $\Delta Q_x = -0.01$ and $\Delta Q_y = 0.012$.
      Don't drive on the tune, you don't want to see what happens then ;)
      </p></details>

- [ ] <details class="nodeco"><summary>Have the Losses Applications Open</summary>
      <p> When kicking from Multiturn, keep an eye on the losses application for unexpected spikes.
      </p></details>

- [ ] <details class="nodeco"><summary>Make Sure to Log All Info</summary>
      <p> Starting in Run 3 a decent amount of automatic logging should be implemented.
      However, one should always check and make sure to log all relevant information: fill number, location of measurement files etc.
      </p></details>

- [ ] <details class="nodeco"><summary>Analyse as the Data Comes</summary>
      <p> As much as possible, let's make sure people analysing the kick data do not fall behind the kickers.
      If you're a kicker, coordinate with you analyst to stay in sync.
      </p></details>

- [ ] <details class="nodeco"><summary>Give Sensible Names to Complete Sets of Data</summary>
      <p> When an analysis is done on a complete group of kicks, try to find a descriptive name.
      See the [info][../info.md] page for naming conventions.
      </p></details>

- [ ] <details class="nodeco"><summary>Log Anything of Interest in the Logbook</summary>
      <p> It doesn't hurt to have a lot of information.
      </p></details>

## General Corrections Caveats

- [ ] <details class="nodeco"><summary>Beware of the Corrections Signs</summary>
      - [ ] <details class="nodeco"><summary>Calculated Global Corrections</summary>
            <p> The calculated global correction are really corrections and should be trimmed in with a positive sign.
            </p></details>
      - [ ] <details class="nodeco"><summary>Skew Magnets</summary>
            <p> All skew magnets are inversed in LSA / MAD-X conventions and the calculated corrections for these should be trimmed in with an opposite sign (that means calculated correction * -1).
            </p></details>
      - [ ] <details class="nodeco"><summary>Triplets</summary>
            <p> The triplets are tricky as all three are powered in series with a common knob, then some have an additional trim.
            Calculated corrections should be *sign-swapped for Q1 and Q3 but not for Q2*.
            See with the EIC if you have any doubts.
            </p></details>
      - [ ] <details class="nodeco"><summary>Local Corrections</summary>
            <p> Decide on a convention for how we output the corrections (omc3 or bbsrc) and how to use them? Do checks on friday for that!
            </p></details>

- [ ] <details class="nodeco"><summary>Knob Creation Permission</summary>
      <p> It is not enough to be logged in as `lhcop` to create knobs for corrections.
      Both Tobias and Ewen have the permissions, if they aren't present see with the EIC.
      </p></details>


*[ppb]: protons per bunch
*[BLM]: Beam Loss Monitor
*[BCM]: Beam Condition Monitor
*[BPM]: Beam Position Monitor
*[LSA]: LHC Software Architecture
*[EIC]: Engineer In Charge
