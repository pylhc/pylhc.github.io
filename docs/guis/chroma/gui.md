# The Non-Linear Chromaticity GUI

The non-linear chromaticity GUI provides functionality to analyze [chromaticity scans](#performing-scans) in the LHC.
The GUI itself has no functionality for making these measurements and only serves to extract and analyze data from `NXCALS`.

!!! note "Kerberos"
    Note that using the GUI requires a valid Kerberos token.

The GUI is published with `acc-py`, and can be run with:

```bash
/acc/local/share/python/acc-py/apps/acc-py-cli/pro/bin/acc-py app run chroma-gui
```

## Performing Scans

Chromaticity scans are performed by modulating the frequency of the RF cavities in the LHC.
The tune will be impacted by the chromaticity of the machine, and online tune data is automatically recorded to `NXCALS`.

!!! warning "Feedbacks OFF"
    Make sure to turn off both the tune and orbit feedbacks before performing an RF scan.
    See with the current EIC that no other operations are ongoing that could be affected.

To perform a scan, trim the RF circuit in steps to reach the desired momentum deviation.
A good rule of thumb, _for the LHC_, is that:

$$
dpp = \frac{\Delta f_{RF}}{140} \cdot 10^{-3}.
$$

A good modulation aims to reach between $2 \cdot 10^{-3}$ and $3 \cdot 10^{-3}$ in momentum deviation.
Typically, the scans are performed with ±300Hz.

!!! tip "Max Modulation Amplitude"
    Scans have been performed safely in the past with ±400Hz, in cases where specific high orders were investigated.

## Analyzing Scans

To analyze data from a scan, start by launching the GUI as instructed above.
It should open to this default view:

<figure>
  <center>
  <img src="../../assets/images/chroma_gui/default_view.png" width="85%" alt="Chroma GUI landing page" />
  <figcaption> Chroma GUI Landing Page </figcaption>
  </center>
</figure>



*[EIC]: Engineer in Charge, operators of the LHC
