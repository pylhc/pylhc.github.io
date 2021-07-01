# BPM Calibration

The Beam Position Monitors (BPM) are used to get the position of the beam at a
certain longitudinal position in the accelerator. The returned values are 
though often off by a certain factor. Those factors are called the BPM 
calibration factors.
Those factors can be applied to the measurements to obtain more accurate 
measurements.

Those factors can be computed via several methods: the ratio between the
computed β from phase and β from amplitude, and the ratio between the
dispersion from phase and dispersion from amplitude.

The most efficient way to get those factors is via an undisturbed
function, i.e. in a drift. _Ballistic Optics_ have thus been designed to get
the most accurate calibration factors, by turning off quadrupoles, creating a 
void between BPMs.  

!!! warning "Calibration for Ballistic Optics"
    The computation of BPM calibration factors is only done for ballistic 
    optics and their related BPMs because the β-function and dispersion are 
    known in such drifts.

The β-function and dispersion can also be fitted (parabolic and linear) to get
more precise values. Those columns are, to date (2021-07), not used in OMC3.

!!! info "Fit of Functions"
    The β-function and dispersion are fitted between a set of BPMs defined by
    the ballistic optics. The list can be found
    [here](https://github.com/pylhc/PyLHC/blob/master/pylhc/constants/calibration.py#L32).  
    For the dispersion, those BPMs are located between the separation dipoles,
    where the dispersion propagates linearly.


## Calibration Factors

### From the β-function

The calibration factors based off the β-functions $β^A$ and $β^\phi$ are defined 
as:

$$
C^A_{x,y} = \sqrt{\frac{β^\phi_{x,y}}{β^A_{x,y}}}
$$

It is important to note that the β-function is proportional to the amplitude
square, and therefore the use of the square root. Calibration factors obtained
via this method are not absolute values but relative values to the average
calibration factor used for the action calculation.


### From the Dispersion Function

Dispersion from phase refers to the reconstruction of dispersion measurements
based on the normalised dispersion and $\beta^{\phi}$ function. The normalised
dispersion is used here as it is a calibration independent observable: its
quantities are both proportional calibration-wise.

$$
D_{x}^\phi= D_{N,x}^{A}\sqrt{\beta_{x}^{\phi}}
$$

with an associated error given by:

$$
(\Delta D_{x}^{\phi})^{2}
= (D^\phi_x)^2
+ \left(\frac{1}{2}\frac{D^A_{N,x}}{\sqrt{\beta_{x}^{\phi}}}\Delta \beta^{\phi}_{x}\right)^{2}
$$

Calibration factors based on dispersion function calculations obtained via
direct dispersion measurements (calibration dependent observable) and
normalised dispersion (calibration independent observable) \cite{rama} are
defined as:

$$
C_{x}^{A} = \frac{D^A_{N,x}\sqrt{\beta^{\phi}_x}}{D^A_x}
$$

It is important to note that calibration factors from dispersion are only computed in the horizontal plane.


## Using PyLHC to Compute Calibration Factors

The BPM Calibration module of PyLHC can be used to compute calibration factors,
its documentation can he found 
[here](https://pylhc.github.io/PyLHC/entrypoints/bpm_calibration.html#).  
Only one entrypoints exists for both methods, the argument `method` can be used
to select it, and defaults to `beta`.

Example of call to the script:

```bash
python3 bpm_calibration.py --input <measurement directory>
                           --output <output directory>
                           --ips 1, 5
                           --method beta
```

The measurements directory needs to contain the TFS files with the beta
functions obtained with the analysis done via OMC3.
The output directory will then contain, depending on the method, tfs files for
the calibration: `calibration_{beta,dispersion}_{x,y}.tfs`.
 
### TFS File for Beta Calibration

The TFS files produced via the beta method contain the following columns:

* S: Longitudinal position

* CALIBRATION: Calibration factor defined as:

$$
        C^A_{x,y} = \sqrt{\frac{\beta^{\phi}_{x,y}}{\beta^A_{x,y}}}
$$

* ERROR$\_$CALIBRATION: Error associated to the calibration factor calculation\footnote{See Appendix A for the derivation}.

$$
        {\left(\Delta C_{x,y}^{A}\right)^{2}} = \frac{\left(\Delta \beta_{x,y}^{\phi}\right)^{2}}{4 \beta_{x,y}^{A}\beta_{x,y}^{\phi}} + \frac{\beta_{x,y}^{\phi}\left(\Delta \beta_{x,y}^{A}\right)^{2} }{4(\beta_{x,y}^{A})^{3}}
$$

* CALIBRATION$\_$PHASE$\_$FIT: Calibration factor defined as:

$$
        C^A_{x,y} = \sqrt{\frac{\beta^{\phi,fit}_{x,y}}{\beta^A_{x,y}}}
$$

* ERROR$\_$CALIBRATION$\_$PHASE$\_$FIT: Error associated to the inverse of the calibration:

$$
            \left(  {\Delta C_{x,y}^{A}}\right)^{2} = \frac{\left(\Delta \beta_{x,y}^{\phi,fit}\right)^{2}}{4 \beta_{x,y}^{A}\beta_{x,y}^{\phi,fit}} + \frac{\beta_{x,y}^{\phi,fit}\left(\Delta \beta_{x,y}^{A}\right)^{2} }{4(\beta_{x,y}^{A})^{3}}
$$

### TFS File for Dispersion Calibration

* S: Longitudinal position

* CALIBRATION: Calibration factor defined as:

$$
        {C_{x}^{A}}
        = \frac{D^\phi_x}{D^A_x}
        = \frac{D^A_{N,x}\sqrt{\beta_{x}^{\phi}}}{D^A_{x}}.
$$

* ERROR$\_$CALIBRATION: Error associated to the calibration factor calculation:

$$
         \left(\Delta {C^A_x}\right)^{2} = \left(\frac{\Delta D^\phi_x}{D^A_x}\right)^2 + \left(\Delta D^A_x \frac{D^\phi_x}{(D^A_x)^2}\right)^2
$$

* CALIBRATION$\_$FIT: Calibration factor defined as:

$$
        {C_{x}^{A}}
        = \frac{D^{\phi,fit}_x}{D^A_x}
        = \frac{\left(D^A_{N,x}\sqrt{\beta_{x}^{\phi}}\right)^{fit}}{D_{x}^{A}}.
$$

* ERROR$\_$CALIBRATION$\_$FIT: Error associated to the calibration factor calculation:

$$
         \left(\Delta {C^A_x}\right)^{2} = \left(\frac{\Delta D^{\phi,fit}_x}{D^A_x}\right)^2 + \left(\Delta D^A_x \frac{D^{\phi,fit}_x}{(D^A_x)^2}\right)^2
$$
