# BPM Calibration

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

## Calibration From the β-Function

The calibration factors based off the $\beta$-functions from amplitude and from phase, $\beta^A$ and $\beta^\phi$, are defined as:

$$
C^A_{x,y} = \sqrt{\frac{\beta^\phi_{x,y}}{\beta^A_{x,y}}}
$$

It is important to note that the $\beta$-function is proportional to the square of the particles' amplitude.

!!! warning "Relative Factors"
    Calibration factors obtained via this method are not absolute but relative to the average calibration factor used for the action calculation.

## Calibration From the Dispersion Function

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

Calibration factors are then defined as[^RamaDispersionCalibration]:

$$
C_{x}^{A} = \frac{D^A_{N,x}\sqrt{\beta^{\phi}_x}}{D^A_x}
$$

!!! info "Horizontal Plane Only"
    It is important to note that calibration factors from dispersion are only computed in the horizontal plane.

[^RamaDispersionCalibration]:
    ??? abstract "BPM Calibration Independent LHC Optics Correction, `R. Calaga, and R. Tomás, and F. Zimmermann`, [IEEE Particle Accelerator Conference, 2007](https://ieeexplore.ieee.org/document/4440536){target=_blank}"
        ```
        @inproceedings{Calaga:4440536,  
          author={Calaga, R. and Tomas, R. and Zimmermann, F.},
          booktitle={2007 IEEE Particle Accelerator Conference (PAC)},
          title={BPM calibration independent LHC optics correction},
          year={2007},
          volume={},
          number={},
          pages={3693-3695},
          url={https://accelconf.web.cern.ch/p07/PAPERS/THPAS091.PDF},
          doi={10.1109/PAC.2007.4440536}
        }
        ```

*[BPM]: Beam Position Monitor

[bpm_calibration_constants]: https://github.com/pylhc/PyLHC/blob/master/pylhc/constants/calibration.py