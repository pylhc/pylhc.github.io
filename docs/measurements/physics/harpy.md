# Harmonic Analysis with Harpy

This page describes how the harmonic analysis is performed with the `harpy` module.
If you want to know how to use the `harpy` module, refer to the [`omc3` analysis workflow][omc3_analysis].
Harpy produces per-BPM tune, amplitude and phase information as well as their uncertainties, which feed into the optics reconstruction step.

!!! tip "Primary Reference"
    The algorithm and its derivations are described in [Malina et al., IPAC2022][malina_harpy]{target=_blank}: *Harpy: A Fast, Simple and Accurate Harmonic Analysis with Error Propagation*.

## Background

Traditional harmonic analysis methods such as NAFF ([Laskar][laskar_naff]{target=_blank}) and SUSSIX ([Bartolini & Schmidt][bartolini_sussix]{target=_blank}) iteratively interpolate in the FFT output: the strongest spectral line is located and its contribution subtracted via orthonormalisation, which is repeated hundreds of times.
Both provide tune estimates more accurate than a single FFT but not necessarily better phase estimates.

Harpy combines standard techniques such as zero-padded FFT and noise cleaning based on singular value decomposition (SVD) to exploit the correlated multi-BPM structure, achieving both speed and accuracy.

## Noise Cleaning via SVD

The TbT position matrix $\mathbf{A}$ of shape $(N_\text{BPM} \times N_\text{turns})$ is decomposed as:

$$
    \mathbf{A} = \mathbf{U} \mathbf{S} \mathbf{V}^\mathsf{T} ,
$$

where the columns of $\mathbf{U}$ and $\mathbf{V}$ are orthonormal vectors and $\mathbf{S}$ is diagonal with singular values sorted in decreasing order.
Each mode corresponds to a spatially coherent oscillation pattern.
Only $N_\text{modes}$ (by default 12) largest singular value modes are retained for reconstruction.
For elements $a_{jn}$ of the matrix $\mathbf{A}$, with $j$ and $n$ indexing BPMs
(up to $N_{BPMs}$) and turns (up to $N_{turns}$), respectively:

$$
    a_{jn} = \sum_{k,l=1}^{min(N_{BPMs}, N_{turns})} u_{jk}\, s_{kl}\, v_{nl} .
$$

If any $\mathbf{U}$ matrix element exceeds `svd_dominance_limit` (by default 0.925) and is the maximum in its column, it is zeroed and the column renormalised.
This is repeated up to `num_svd_iterations` (by default 3) times.
BPMs flagged in this step are labelled `SVD_PEAK` bad BPMs (see [BPM Cleaning](#bpm-cleaning)).

Cleaned Tbt data is recomposed in a matrix $\mathbf{C}$ using only the first $N_\text{modes}$ modes with the largest singular values (after rescaling):

$$
    c_{jn} = \sum_{k}^{N_\text{modes}} u_{jk}\, s_{kl}\, v_{nl} .
$$

The per-BPM noise level is estimated as $\sigma_\text{res} = \mathrm{std}(\mathbf{A} - \mathbf{C})$, with $\mathbf{C}$ the reconstructed matrix defined above.
This residual is used for downstream error propagation.


*[BPM]: Beam Position Monitor
*[BPMs]: Beam Position Monitors
*[TbT]: Turn-by-Turn
*[RDT]: Resonance Driving Term
*[RDTs]: Resonance Driving Terms
*[SVD]: Singular Value Decomposition
*[FFT]: Fast Fourier Transform
*[RFFT]: Real Fast Fourier Transform
*[DFT]: Discrete Fourier Transform
*[NAFF]: Numerical Analysis of Fundamental Frequencies

[omc3_analysis]: ../../packages/omc3/analysis.md
[malina_harpy]: https://accelconf.web.cern.ch/ipac2022/doi/JACoW-IPAC2022-WEPOMS035.html
[laskar_naff]: https://www.sciencedirect.com/science/article/abs/pii/001910359090084M
[bartolini_sussix]: https://cds.cern.ch/record/702438/files/sl-note-98-017.pdf
