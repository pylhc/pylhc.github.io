# The Physics of OMC

This section documents the physics and methods that underpin the OMC team's optics measurement activities.
The connecting thread across all methods is the extraction of optics quantities (optics functions, dispersion, coupling, resonance driving terms etc) from turn-by-turn BPM data, and their comparison to a reference model to identify and correct lattice imperfections.

## Background Reading

For readers new to the field, or in need of a refresher before exploring the sub-pages, the following resources are recommended.
References for specific methods are also given on the individual sub-pages.
One can have a look at this [page providing a list of our published works](../../omc_team/publications.md).

### General

[Ewen's 2019 presentation at Uni Goettingen][maclean_goettingen_2019]{target=_blank} gives a good general introduction into the topic of LHC related accelerator physics, covering from basic principles to linear optics, some non-linear dynamics, and LHC specifics.
For a more comprehensive textbook treatment, [Minty & Zimmermann][minty_zimmermann]{target=_blank} remains a standard reference for beam measurement methods, with a thorough chapter on optics.

### Harmonic Analysis

The spectral analysis at the core of our measurement pipeline is described in the proceedings paper by [Malina et al.][malina_harpy]{target=_blank}, which documents the `harpy` algorithm used in `omc3` and its error propagation.

### Phase Advances and Optics Functions

A good reference for the reconstruction of optics functions from phase advances, as implemented in `omc3`, is the [analytical N-BPM method paper][analytical_nbpm]{target=_blank} by Wegscheider et al. (Phys. Rev. Accel. Beams 20, 2017).
For more references see the dedicated section.

### Coupling and Resonance Driving Terms

The [coupling page](coupling.md) make heavy use of normal form theory and resonance driving terms.
The [CAS lectures given in Trondheim][herr_cas]{target=_blank} by W. Herr provide an illustrative entry point into these topics, while the chapter by [Herr and Forest][herr_forest_nf]{target=_blank} covers the same material with full mathematical rigour.
The spectral-line approach to measuring the coupling RDTs that underlies our analysis is derived in [R. Tomás' paper on RDTs][tomas_rdt]{target=_blank}.

### K-Modulation

The K-modulation method, as implemented in `omc3` and performed when using the [K-Mod GUI](../../guis/kmod/gui.md), is described in detail by [Carlier & Tomás][carlier_kmod]{target=_blank} (Phys. Rev. Accel. Beams 20, 2017), including its application to beta-star measurements in the LHC interaction regions.

*[OMC]: Optics Measurements and Corrections
*[LHC]: Large Hadron Collider
*[BPM]: Beam Position Monitor
*[RDT]: Resonance Driving Term
*[RDTs]: Resonance Driving Terms

[maclean_goettingen_2019]: https://indico.cern.ch/event/788195/contributions/3364867/attachments/1886006/3109100/2019_07_25_HASCO_lcomp.pdf
[minty_zimmermann]: https://link.springer.com/book/10.1007%2F978-3-662-08581-3
[malina_harpy]: https://accelconf.web.cern.ch/ipac2022/doi/JACoW-IPAC2022-WEPOMS035.html
[analytical_nbpm]: https://link.aps.org/doi/10.1103/PhysRevAccelBeams.20.111002
[herr_cas]: https://cds.cern.ch/record/1507631
[herr_forest_nf]: https://cds.cern.ch/record/2743949/files/Herr-Forest2020_Chapter_Non-linearDynamicsInAccelerato%20(1).pdf
[tomas_rdt]: https://inspirehep.net/literature/680877
[carlier_kmod]: https://link.aps.org/doi/10.1103/PhysRevAccelBeams.20.011005
