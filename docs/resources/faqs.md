# Frequently Asked Questions

!!! info 
    We are gradually including here different pieces of useful information, possibly from questions answered in meetings or on Mattermost, which don't really fit anywhere else as their whole page.

## Beta-Beat.src Output Files

The naming of output files in Beta-Beat.src analysis can be very unintuitive.
Namely, one will see similar output files for a quantity which go as `get_*.out`, `get_*_free.out` and `get_*_free2.out`, where `*` is the calculated quantity (betas, phase, etc.).
These each correspond to a variation of the calculated quantity, explained below.

!!! question "Why Various Outputs?"
    When doing our measurements, we use AC-Dipole driven excitations of the beam for a better signal-to-noise ratio in data acquisition.
    However, as the AC-Dipole has an effect on the beam optics functions the reconstructed optics from these measurements are the driven optics, not those of the accelerator itself.
    One can correct for this deviation in different ways, which is why there are several output files for each optics quantity computed.

The files correspond to the following meanings:

| Nomenclature      | Meaning                                                                          |
| :---------------- | :------------------------------------------------------------------------------- |
| `get_*.out`       | The optics functions **without** recalibration, from the driven excitation data. |
| `get_*_free.out`  | The optics functions recalibrated **analytically** using an equation.            |
| `get_*_free2.out` | The optics functions recalibrated **the other way**, see bellow.                 |

In the case of the `get_*_free2.out` files, the recalibration is done differently depending on the computed quantity.
For some quantities (for instance for $\beta$ from phase) this uses the model values, for others (for instance the coupling RDTs $f_{1001}$ and $f_{1010}$) it is a rescaling in which the model values are used *indirectly*.

## MAD-X Pitfalls

`MAD-X` can sometimes be a bit tricky to work with.
This section is intended to put together some common pitfalls encountered when creating a MAD-X script.  

!!! warning "MAD-X Errors"
    As a reminder, `MAD-X` ignores all the code that does not work.
    It does not raise errors or crash like other languages, which can make it difficult to identify your mistakes.
    As a reminder: each instruction should end with a semicolon and `MAD-X` will consider everything a single command until the next `;` is encountered.

### Tracking, Beam 2 and Beam 4

You might have noticed that an `lhcb4.seq` file is included in the `acc-models-lhc` repository.
There is a specific caveat for the beam 2 sequence definition that one needs to be aware in order to do tracking.

For practical reasons, the properties of all elements of the LHC are defined (in the `lhc.seq`) as if they apply to a clockwise proton beam (beam 1).
This allows a single definition for elements traversed by both beams.
Their effects on a beam with identical particle charge but running in the opposite direction (beam 2) must then be reversed inside the program, which is achieved by creating a beam with a [bv=-1 flag](madx_doc_bv) (section `7.4`).

However, in order to perform tracking for the `lhcb2` sequence the exact elements definitions are necessary, as well as a `bv` flag of 1.
This is done in the `lhcb4.seq` file.
There is no such caveat for tracking with beam 1, which is why there is no "beam 3".

!!! example "Tracking Cheatsheet"
    === "Beam 1"

        Tracking for Beam 1 does not have any caveat:
        
        - Load the `lhc.seq` sequence file
        - Create your beam for the `lhcb1` sequence with the `bv=1` flag
        - Slice the `lhcb1` sequence and track

    === "Beam 2"
        When tracking for beam 2, remember to:

        - Load the `lhcb4.seq` sequence file
        - Create your beam for the `lhcb2` sequence with the `bv=1` flag
        - Slice the `lhcb2` sequence and track
        
        !!! tip "What about model creation?"
            If analysing the tracking data with either `Beta-Beat.src` or `omc3`, one will need a model. The model **has** to have been made with the regular `lhc.seq` file, `lhcb2` sequence, and a beam with `bv=-1`.

## LSA Pitfalls

### Querying LSA is Slow

You might run into an issue with the [`pylhc.machine_settings_info`](../packages/pylhc/machine_settings_info.md) script where your query hangs for a (very) long time.
This is due to the fact that `pjlsa` will look for the beamprocess at the given time and extract *all trims* for the required knobs through this beamprocess, even though only the last trim is displayed.

!!! example "Workarounds"
    To speed up the script's runtime, try the following:

    - Do not extract knobs if you are only after the summary information (this is now default behaviour)
    - Only ask for the knobs you need (e.g. `--knobs name1 name1`), or just default ones (e.g. `--knobs default`) if you're unsure
    - Give a time range that is as small as possible using the `--start-time` and `--time` flags. This way a small trim history will be queried by `pjlsa`. For instance:
    
    ```bash
    python -m pylhc.machine_settings_info \
        --knobs name1 name2 \  # with real names ;)
        --start-time "2022-10-19 17:00:00.0" \
        --time "2022-10-19 17:30:00.0"
    ```
    
    Be aware though that if no trim for the knobs are in the defined time range, no values will be returned at all.


[madx_doc_bv]: http://madx.web.cern.ch/madx/releases/last-rel/madxuguide.pdf