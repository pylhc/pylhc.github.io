
# Optics Analysis

This page summarizes how the optics analysis is performed with our `omc3` software, from the physics point of view.

!!! info "A practical walkthrough"
    To see how to **use** the `omc3` package to do so, refer to the [`omc3` analysis workflow][omc3_analysis] page.

All quantities described here are reconstructed from the turn-by-turn (TbT) centroid positions recorded by BPMs around the ring following [beam excitation](../../guis/multiturn/gui.md).
The preceding spectral analysis step, in which the tune, amplitude and phase of spectral lines are extracted from TbT data, is documented in the [harmonic analysis page](harpy.md).

## Linear Optics

### Phase, Phase Advance and Special Phases

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

!!! tip "AC dipole phase advances"
    When the beam is driven by an AC dipole, the measured *driven* phase advances differs from the free phase advances since the AC dipole modifies the effective $\beta$-function throughout the ring.
    This can be compensated analytically, which `omc3` does before performing optics reconstruction.

The **special phases** correspond to the phase advances between specific machine elements of interest, usually the AC Dipole kicker magnet to tertiary collimators in the IRs for the LHC.

[omc3_analysis]: ../../packages/omc3/analysis.md
