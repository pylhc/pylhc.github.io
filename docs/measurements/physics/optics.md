
# Optics Analysis

This page summarizes how the optics analysis is performed with our `omc3` software, from the physics point of view.

!!! info "A practical walkthrough"
    To see how to **use** the `omc3` package to do so, refer to the [`omc3` analysis workflow][omc3_analysis] page.

All quantities described here are reconstructed from the turn-by-turn (TbT) centroid positions recorded by BPMs around the ring following [beam excitation](../../guis/multiturn/gui.md).
The preceding spectral analysis step, in which the tune, amplitude and phase of spectral lines are extracted from TbT data, is documented in the [harmonic analysis page](harpy.md).

## Linear Optics

### Phase Advances

The betatron phase $\phi_{x,y}(s)$ at the curvilinear coordinate $s$ is defined by the integral:

$$
    \phi_{x,y}(s) = \int_0^s \frac{ds}{\beta_{x,y}(s)} .
$$

The phase advance corresponds to the difference of the betatron phase functions at two points, typically also taken with respect to an arbitrary initial point at $s = 0$:

$$
    \phi_{s_1 \rightarrow s_2} = \phi(s_{2}) - \phi(s_{1}) = \int_{s_{1}}^{s_{2}} \frac{1}{\beta(s)} ds .
$$

The tune $Q_{x,y}$ is the total phase advance per revolution, and given $C$ the machine circumference is written as:

$$
    Q_{x,y} = \frac{1}{2 \pi} \Delta \phi_{x,y} = \frac{1}{2 \pi} \oint_C \dfrac{ds}{\beta_{x,y} (s)} ,
$$

The phase advance between two BPMs is extracted from TbT data as the difference of the spectral line phases at the tune frequency at the two locations.

In the N-BPM method (see [Beta from Phase](#beta-from-phase)), the relevant inputs are phase advances between non-consecutive BPMs.
Combinations with phase separations well away from $0$ and $\pi$ are preferred, as these minimise the sensitivity of the cotangent terms to measurement noise.

!!! info "Special phases"
    The special phases correspond to the phase advances between specific machine elements of interest, usually the AC Dipole kicker magnet to tertiary collimators in the IRs for the LHC.

### Action

The Courant-Snyder action $J_z$ is the conserved invariant of free betatron motion, related to the oscillation amplitude by $J_{x,y} = A_{x,y}^2(s)/(2\beta_{x,y}(s))$ at any location $s$.
Since it cannot be read off from a single BPM without knowing $\beta_{x,y}(s)$, a calibration-dependent estimate is formed by averaging over $N$ BPMs:

$$2J_{x,y} = \frac{1}{N} \sum_{n=1}^N \frac{\left(\text{peak-to-peak}/2\right)_n^2}{\beta_{x,y}^m(s_n)} .$$

For an AC dipole excitation, $J_{x,y}$ is modulated during the ramp-up and ramp-down phases but is constant on the flat-top plateau; only plateau turns enter the analysis.

### Beta from Amplitude

The $\beta$-function can be estimated from the oscillation amplitude $A_{x,y}$ recorded at each BPM.
From the Courant-Snyder parameterisation, the oscillation amplitude is $A_{x,y}(s) = \sqrt{2J_{x,y}\,\beta_z(s)}$, giving:

$$\beta_{x,y}^\text{amp}(s_i) = \frac{A_{x,y}^2(s_i)}{2 J_{x,y}} .$$

Because the action $J$ must itself be estimated from the peak-to-peak amplitudes and model $\beta$-functions (see above), this method is sensitive to BPM calibration errors and is generally less accurate than $\beta$ from phase.
It is used as a cross-check and as a diagnostic for BPM calibration.

### Beta from Phase

The $\beta$-function at BPM $i$ can be determined from the measured phase advances to two other BPMs $j$ and $k$, with normalisation using model values.
The three-BPM combination formula reads:

$$
    \beta_{x,y}^\text{phase}(s_i) = \frac{\cot\!\left(\phi_{x,y}(i \to j)\right) + \cot\!\left(\phi_{x,y}(i \to k)\right)}
    {\cot\!\left(\phi_{x,y}^m(i \to j)\right) + \cot\!\left(\phi_{x,y}^m(i \to k)\right)}
    \, \beta_{x,y}^m(s_i) ,
$$

where superscript $m$ denotes model values.

!!! tip "The analytical N-BPM method"
    The [analytical N-BPM method][analytical_nbpm]{target=_blank} (Wegscheider et al., Phys. Rev. Accel. Beams **20**, 111002, 2017) extends this calculation by averaging over $N$ specifically chosen BPM combinations which remove unfavorable phase advances.
    The method also includes the known statistical uncertainties of various elements for error estimation.

When the beam is driven by an AC dipole, the measured *driven* beta functions differs from the *free* ones since the AC dipole modifies the parametrization of the particle coordinates.
Details on this effect can be found in [F. Soubelet's PhD Thesis][soubelet_thesis]{target=_blank}.
This effect can be compensated analytically.

### Beta-Beating

The very commonly looked at $\beta$-beating, the deviation from model values, goes as:

$$\frac{\Delta\beta_{x,y}(s)}{\beta_{x,y}(s)} = \frac{\beta_{x,y}^\text{phase}(s) - \beta_{x,y}^m(s)}{\beta_{x,y}^m(s)} .$$

It is a primary value of interest for the quantification of the optics' quality throughout the machine.

### Dispersion and Normalized Dispersion

The dispersion function $D_{x,y}(s)$ quantifies the sensitivity of the closed orbit to a relative momentum offset $\delta = \Delta p / p_0$:

$${x,y}_\text{co}(s,\,\delta) = {x,y}_{\text{co},0}(s) + D_{x,y}(s)\,\delta + \mathcal{O}(\delta^2) .$$

To determine dispersion in practice, $\delta$ is varied by adjusting the RF frequency away from its nominal value, which shifts the beam energy.
The resulting mean orbit change at each BPM, plotted versus $\delta$, yields $D_{x,y}(s)$ as the slope.

!!! note "3D Excitation"
    A more efficient approach is to perform measurements with AC dipole excitation in which the RF frequency is simultaneously modulated, providing an "excitation" of the three degrees of freedom at once.
    This method was explored but is not currently actively used.

The **normalized dispersion**, written as $D_{x,y} / \sqrt{\beta_{x,y}}$, is independent of both the model $\beta$-function and BPM calibration factors, making it a more robust observable of the sensitivity to energy deviations.

### Coupling

Linear betatron coupling mixes the motions of horizontal and vertical planes.
It is parameterised by the [resonance driving terms](#resonance-driving-terms) $f_{1001}$ and $f_{1010}$.

These are reconstructed from the cross-plane spectral lines of the same TbT data used for the linear optics.
A dedicated page on reconstructing the [coupling](coupling.md) terms is available.


*[BPM]: Beam Position Monitor
*[BPMs]: Beam Position Monitors
*[TbT]: Turn-by-Turn
*[RDT]: Resonance Driving Term
*[RDTs]: Resonance Driving Terms
*[CRDT]: Combined Resonance Driving Term
*[CRDTs]: Combined Resonance Driving Terms
*[SVD]: Singular Value Decomposition

[analytical_nbpm]: https://link.aps.org/doi/10.1103/PhysRevAccelBeams.20.111002
[soubelet_thesis]: https://repository.cern/records/jey15-71v76
[tomas_rdt]: https://inspirehep.net/literature/680877
[omc3_analysis]: ../../packages/omc3/analysis.md
