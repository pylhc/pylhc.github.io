# OMC Methods

!!! note
    Very long content about the physics and practice of OMC methods + paper references for each (K-mod, 3D kicks, N-BPM...).
    Each method should be a H2, see examples below.

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
