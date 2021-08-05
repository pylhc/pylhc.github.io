# OMC Methods

!!! note
    Content about the physics and practice of OMC methods + paper references for each (K-mod, 3D kicks, N-BPM...).
    Each method should be a H2, see examples below.

## BPM Calibration

Beam Position Monitors (BPM) are instruments used to measure the transverse position of the beam at a certain longitudinal position in the accelerator.
However, the returned values are often off by a certain factor called calibration factor.
Knowledge of calibration factors can be used to increase the accuracy of measurements.

There are currently two methods to determine BPM calibration factors, using either the ratio between the dispersion or the $\beta$-functions computed from phase and from amplitude.
A special type of optics called _Ballistic Optics_ have been designed for the measurement of calibration factors.
The most efficient way to get those factors is via an undisturbed function, i.e. in a drift by turning off quadrupoles, creating a standard drift space between BPMs.  

!!! warning "Calibration for Ballistic Optics"
    The computation of BPM calibration factors is only done for ballistic optics and their related BPMs because the $\beta$-function and dispersion are known in such drifts.

!!! info "Fitting $\beta$-Functions"
    The $\beta$-function and dispersion can also be fitted (parabolic and linear) to get more precise values.
    The $\beta$-function and dispersion are fitted between a set of BPMs defined by the ballistic optics.
    The list of used BPMs can be found in the code, defined in the [calibration constants][bpm_calibration_constants]{target=_blank}.
    For the dispersion, those BPMs are located between the separation dipoles, where the dispersion propagates linearly.

### Calibration From the β-Function

The calibration factors based off the $\beta$-functions from amplitude and from phase, $\beta^A$ and $\beta^\phi$, are defined as:

$$
C^A_{x,y} = \sqrt{\frac{\beta^\phi_{x,y}}{\beta^A_{x,y}}}
$$

It is important to note that the $\beta$-function is proportional to the square of the particles' amplitude.

!!! warning "Relative Factors"
    Calibration factors obtained via this method are not absolute but relative to the average calibration factor used for the action calculation.

### Calibration From the Dispersion Function

Dispersion from phase refers to the reconstruction of dispersion measurements based on the normalised dispersion and $\beta^{\phi}$ function.
The normalised dispersion is used here as it is a calibration-independent observable.
It is defined as:

$$
D_{x}^\phi= D_{N,x}^{A}\sqrt{\beta_{x}^{\phi}}
$$

with an associated error:

$$
(\Delta D_{x}^{\phi})^{2} = (D^\phi_x)^2 + \left(\frac{1}{2}\frac{D^A_{N,x}}{\sqrt{\beta_{x}^{\phi}}}\Delta \beta^{\phi}_{x}\right)^{2}
$$

Calibration factors are then defined as \cite{rama}[^RamaDispersionCalibration]:

$$
C_{x}^{A} = \frac{D^A_{N,x}\sqrt{\beta^{\phi}_x}}{D^A_x}
$$

!!! info "Hozirontal Plane Only"
    It is important to note that calibration factors from dispersion are only computed in the horizontal plane.

## N-BPM

## K-Modulation

This section gives a brief overview over the K-Modulation method.
A more detailed description can be found in M. Minty and F. Zimmermann's book[^MintyZimmermann] and the references therein.

Also available on this site is a [checklist for conducting K-Modulation measurements](../procedures/kmod.md) in the LHC.

The full K-Modulation analysis is two-fold:
The [K-Modulation GUI](../guis/kmod/gui.md) is used for LHC measurements, and the following analysis is part of the [`omc3` package](../packages/omc3/getting_started.md).

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

## 3D Kicks

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

[^RamaDispersionCalibration]:
    ??? abstract "Accuracy and Feasibility of the Beta* Measurement for LHC and High Luminosity LHC Using K Modulation, `F. Carlier, and R. Tomás`, [Phys. Rev. Accel. Beams **20**, 2017](https://link.aps.org/doi/10.1103/PhysRevAccelBeams.20.011005){target=_blank}"
        ```
        @article{TODO,
        title = {TODO},
        author = {Rama,
        year = {TODO},
        month = TODO,
        volume = {TODO},
        pages = {TODO},
        doi = {TODO},
        url = {TODO},
        journal = {TODO},
        }
        ```

[bpm_calibration_constants]: https://github.com/pylhc/PyLHC/blob/master/pylhc/constants/calibration.py