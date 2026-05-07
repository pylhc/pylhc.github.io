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
BPMs flagged in this step are labelled `SVD_PEAK` bad BPMs (see [BPM Filtering](bpm_filtering.md)).

Cleaned Tbt data is recomposed in a matrix $\mathbf{C}$ using only the first $N_\text{modes}$ modes with the largest singular values (after rescaling):

$$
    c_{jn} = \sum_{k}^{N_\text{modes}} u_{jk}\, s_{kl}\, v_{nl} .
$$

The per-BPM noise level is estimated as $\sigma_\text{res} = \mathrm{std}(\mathbf{A} - \mathbf{C})$, with $\mathbf{C}$ the reconstructed matrix defined above.
This residual is used for downstream error propagation.

## Zero-Padded RFFT

For a real signal $x$ of $N_\text{turns}$ samples, the DFT gives $N_\text{turns}/2$ positive-frequency coefficients with frequency resolution $1/N_\text{turns}$.
To increase this resolution without additional data, the signal is zero-padded to $N_\text{padded} = 2^{\texttt{turn_bits}}$ (by default $2^{20} \approx 10^6$) samples before the transform.

A normalizing windowing function $w_n$ is applied to the signal prior to zero-padding.
Harpy uses the output of RFFT of zero-padded signal $x$:

$$
    X_m = \sum_{n=0}^{N_\text{turns}-1} x_n\, w_n\, e^{-2i\pi  m n / N_\text{padded}} .
$$

The available window functions — `rectangle`, `welch`, `triangle`, `hann` (default), `hamming`, `nuttal3`, `nuttal4` — are ordered by increasing main-lobe width and decreasing spectral leakage.
The Hann window provides a good balance between frequency resolution and leakage suppression.

In practice the RFFT is computed at $2 \times N_\text{padded}$ points to further suppress leakage, then the output is binned to $2^{\texttt{output_bits}}$ (by default $2^{12} = 4096$) frequency bins.
Within each bin the frequency with the highest amplitude is retained.

!!! note "Free-kick measurements"
    Free kick measurements produce decaying oscillations where the bunch centroid amplitude decreases each turn due to beam decoherence.
    In this scenario harpy fits an exponential damping envelope per BPM and corrects the signal before the FFT step (via the `kicker` module).
    The rectangle window is forced in this mode.
    This is distinct from AC dipole excitation, where the amplitude is constant on the flat-top plateau.

## Harmonic Analysis of Decomposed Data

Rather than applying the FFT independently to each BPM, harpy FFTs the $N_\text{modes}$ rows of $\mathbf{S}\mathbf{V}^\mathsf{T}$ and recombines with $\mathbf{U}$.
The complex spectral coefficient at BPM $j$ and frequency $m / N_\text{padded}$ is:

$$
    C_{jm} = \sum_{k=1}^{N_\text{modes}} u_{jk} \sum_{n=1}^{N_\text{turns}} s_{kk}\, v_{nk}\, w_n\, e^{-2i\pi m (n-1) / N_\text{padded}} .
$$

This separates the transform cost ($N_\text{modes}$ FFTs of $N_\text{turns}$ points) from the recombination cost (a single matrix multiplication), and allows restricting computation to frequency ranges of interest.
Frequency windows of width `tolerance` are retained around multiples of the driven and natural tunes and the synchrotron tune; all other frequency content is discarded before binning.

Unless provided by the user, the tune is estimated from the mean row of the cleaned $\mathbf{S}\mathbf{V}^\mathsf{T}$ matrix: the row is windowed, FFT'd, and the dominant peak located.

Beam-related harmonics are identified as the strongest spectral line in given frequency intervals around multiples of the driven or natural tunes in the BPM frequency spectra.

The tolerance scales with resonance order as $\mathrm{tol} \propto (|j-k| + |l-m|) \times \max(10^{-4},\, 1/N_\text{turns})$, giving wider search windows for higher-order resonances.
<!-- Resonances up to order `resonances` (by default 4, allows up to 8) are searched using the RDT framework from `optics_functions`. -->

The amplitude and phase are extracted from the complex coefficient: $A = |C_{jm}|$ and $\varphi = \arg(C_{jm}) / 2\pi$ (converted to fractional turns and realigned to $[-0.5,\, 0.5]$).

!!! info "BPM Cleaning"

    BPM data is filtered in several stages throughout the above process.
    In harpy's approach,

    - **SVD-based**: BPMs whose $\mathbf{U}$-matrix element exceeds `svd_dominance_limit` are excluded. In output files, they are labelled with `SVD_PEAK`.
    - **Tune-based** (post-FFT): BPMs whose measured tune deviates from the mean by more than `tune_clean_limit` (default: $10^{-5}$) are removed. Those with no tune result are also removed.

    See the [BPM filtering page](bpm_filtering.md) for the full list of criteria.

## Accuracy and Error

The phase and relative amplitude uncertainty at a spectral line of amplitude $A$ are:

$$
    \sigma_{\varphi,\, \text{rel. amp}} \approx \sqrt{\frac{2}{N_\text{turns}}}\, \frac{\sigma_\text{orbit}}{A} ,
$$

where $\sigma_\text{orbit}$ is the per-BPM orbit resolution estimated from the SVD residual.

In practice $\sigma$ the spectral noise entering error propagation, the phase error is:

$$
    \sigma_\varphi = \frac{\sigma}{A \cdot 2\pi} .
$$

When the signal-to-noise ratio is very low ($\sigma_\varphi > 0.25$), the phase distribution is approximated as uniform and $\sigma_\varphi$ is capped at $0.3$.
The amplitude error for normalised secondary lines propagates through the ratio as $\sigma_{A,\text{norm}} = \sigma \sqrt{1 + A_\text{norm}^2}$.

For more details on accuracy and error estimates please consult the reference paper linked at the top of this page.

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
