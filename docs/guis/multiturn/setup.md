# Measurement Setup

After selecting which beam to excite and acquire data for, the next step is to prepare the correct excitation settings and check for various state flags.

!!! tip "Good Red and Bad Red"
    As one will see below, an indicator colored in red is not always a bad thing in the Multiturn GUI, due to conventions.
    Check thoroughly the meaning of each indicator (also called flag) from the instructions below and make sure they are in a correct state.

## Flag Status

At the top left of the GUI, a small section titled `Flag Status` displays simple main flags, as show below:

<figure>
    <center>
    <img src="../../assets/images/multiturn_gui/flag_status.png" width="100%" alt="Flag Status Section" />
    <figcaption> Flag Status Section </figcaption>
</figure>

Their meanings are as follows:

- `Beam Presence`: indicates whether beam is circulating in the LHC, for the beam corresponding to the selected tab. This will be green if beam is present, red otherwise. _Always make sure it is green_.
- `Setup Beam`: indicates whether the beam status set by the operator is `Setup`. It will be green if the beam is in `Setup` mode, red otherwise. _Always make sure it is green_.
- `ATLAS BCM`: indicates whether the ATLAS BCM has been masked from the interlock. It is green if the ATLAS BCM is active, red otherwise. _Always make sure it is red_, as we measure in special beam conditions and want it to be masked.

!!! info "Masking the BCM"
    The ATLAS BCM can only be masked by ATLAS operators, from their control room.
    Ask the current EIC to call the ATLAS control room and ask to mask their BCM before starting measurements.



*[ATLAS BCM]: ATLAS Beam Condition Monitor
*[EIC]: Engineer in Charge, operators of the LHC
