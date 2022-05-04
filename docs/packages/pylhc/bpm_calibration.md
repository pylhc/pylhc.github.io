# Using PyLHC to Compute Calibration Factors

The `bpm_calibration` module of `PyLHC` can be used to compute [BPM calibration factors][bpm_calibration].
Only one entrypoints exists for both methods, the argument `method` can be used to select it, and defaults to `beta`.
Using the script to make compute calibration factors through $\beta$-functions for instance from IP1 and IP5 goes as:
```bash         
python -m pylhc.bpm_calibration \
    --input <measurements directory> \
    --output <output directory> \
    --ips 1 5 \
    --method beta
```

The provided `input` measurements directory needs to contain the **TFS** files with the beta functions obtained with the analysis done via `omc3`.
The output directory will then contain, depending on the chosen method, **TFS** files for the calibration: `calibration_{beta,dispersion}_{x,y}.tfs`.
[See the API documentation][documentation]{target=_blank} for a detailed description of the code and the different parameters.

## Nomenclature of Output Files

### Calibration From the β-Function

The output **TFS** files produced via the $\beta$ method contain the following columns:

| Column Name                 | Meaning                                                           | Calculation                                                                                                                                                                                                                                |
| :-------------------------- | :---------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| S                           | Longitudinal Position                                             | -                                                                                                                                                                                                                                          |
| CALIBRATION                 | Calibration factor determined from $\beta$-functions              | $C^A_{x,y} = \sqrt{\frac{\beta^{\phi}_{x,y}}{\beta^A_{x,y}}}$                                                                                                                                                                              |
| ERROR_CALIBRATION           | Error associated to the calibration factor from $\beta$           | ${\left(\Delta C_{x,y}^{A}\right)^{2}} = \frac{\left(\Delta \beta_{x,y}^{\phi}\right)^{2}}{4 \beta_{x,y}^{A}\beta_{x,y}^{\phi}} + \frac{\beta_{x,y}^{\phi}\left(\Delta \beta_{x,y}^{A}\right)^{2} }{4(\beta_{x,y}^{A})^{3}}$               |
| CALIBRATION_PHASE_FIT       | Calibration factor determined from fitting of the phase function  | $C^A_{x,y} = \sqrt{\frac{\beta^{\phi,fit}_{x,y}}{\beta^A_{x,y}}}$                                                                                                                                                                          |
| ERROR_CALIBRATION_PHASE_FIT | Error associated to the calibrator factor from $\Psi$             | $\left(  {\Delta C_{x,y}^{A}}\right)^{2} = \frac{\left(\Delta \beta_{x,y}^{\phi,fit}\right)^{2}}{4 \beta_{x,y}^{A}\beta_{x,y}^{\phi,fit}} + \frac{\beta_{x,y}^{\phi,fit}\left(\Delta \beta_{x,y}^{A}\right)^{2} }{4(\beta_{x,y}^{A})^{3}}$ |

[comment]: <> (| Column Name  | S                     | CALIBRATION                                                   | ERROR_CALIBRATION                                                                                                                                                                                                            | CALIBRATION_PHASE_FIT                                             | ERROR_CALIBRATION_PHASE_FIT                                                                                                                                                                                                                |)
[comment]: <> (| :----------  | :-------------------: | :-----------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |)
[comment]: <> (| Meaning      | Longitudinal Position | Calibration factor determined from $\beta$-functions          | Error associated to the calibration factor from $\beta$                                                                                                                                                                      | Calibration factor determined from fitting of the phase function  | Error associated to the calibrator factor from $\Psi$                                                                                                                                                                                      |)
[comment]: <> (| Calculation  |  -                    | $C^A_{x,y} = \sqrt{\frac{\beta^{\phi}_{x,y}}{\beta^A_{x,y}}}$ | ${\left&#40;\Delta C_{x,y}^{A}\right&#41;^{2}} = \frac{\left&#40;\Delta \beta_{x,y}^{\phi}\right&#41;^{2}}{4 \beta_{x,y}^{A}\beta_{x,y}^{\phi}} + \frac{\beta_{x,y}^{\phi}\left&#40;\Delta \beta_{x,y}^{A}\right&#41;^{2} }{4&#40;\beta_{x,y}^{A}&#41;^{3}}$ | $C^A_{x,y} = \sqrt{\frac{\beta^{\phi,fit}_{x,y}}{\beta^A_{x,y}}}$ | $\left&#40;  {\Delta C_{x,y}^{A}}\right&#41;^{2} = \frac{\left&#40;\Delta \beta_{x,y}^{\phi,fit}\right&#41;^{2}}{4 \beta_{x,y}^{A}\beta_{x,y}^{\phi,fit}} + \frac{\beta_{x,y}^{\phi,fit}\left&#40;\Delta \beta_{x,y}^{A}\right&#41;^{2} }{4&#40;\beta_{x,y}^{A}&#41;^{3}}$ |)

### Calibration From the Dispersion Function

The output **TFS** files produced via the dispersion method contain the following columns:

| Column Name                 | Meaning                                                                | Calculation                                                                                                                                           |
| :-------------------------- | :--------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: |
| S                           | Longitudinal Position                                                  | -                                                                                                                                                     |
| CALIBRATION                 | Calibration factor determined from dispersion function                 | ${C_{x}^{A}} = \frac{D^\phi_x}{D^A_x} = \frac{D^A_{N,x}\sqrt{\beta_{x}^{\phi}}}{D^A_{x}}$                                                             |
| ERROR_CALIBRATION           | Error associated to the calibration factor from dispersion             | $\left(\Delta {C^A_x}\right)^{2} = \left(\frac{\Delta D^\phi_x}{D^A_x}\right)^2 + \left(\Delta D^A_x \frac{D^\phi_x}{(D^A_x)^2}\right)^2$             |
| CALIBRATION_FIT             | Calibration factor determined from fitting of the dispersion function  | ${C_{x}^{A}} = \frac{D^{\phi,fit}_x}{D^A_x} = \frac{\left(D^A_{N,x}\sqrt{\beta_{x}^{\phi}}\right)^{fit}}{D_{x}^{A}}$                                  |
| ERROR_CALIBRATION_FIT       | Error associated to the calibrator factor from dispersion fit          | $\left(\Delta {C^A_x}\right)^{2} = \left(\frac{\Delta D^{\phi,fit}_x}{D^A_x}\right)^2 + \left(\Delta D^A_x \frac{D^{\phi,fit}_x}{(D^A_x)^2}\right)^2$ |

[comment]: <> (| Column Name  | S                     | CALIBRATION                                                                               | ERROR_CALIBRATION                                                                                                                                                                                                                             | CALIBRATION_FIT                                                                                                      | ERROR_CALIBRATION_FIT                                                                                                                                                                         |)
[comment]: <> (| :----------  | :-------------------: | :---------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |)
[comment]: <> (| Meaning      | Longitudinal Position | Calibration factor determined from dispersion function                                    | Error associated to the calibration factor from dispersion                                                                                                                                                                                    | Calibration factor determined from fitting of the dispersion function                                                | Error associated to the calibrator factor from dispersion fit                                                                                                                                 |)
[comment]: <> (| Calculation  |  -                    | ${C_{x}^{A}} = \frac{D^\phi_x}{D^A_x} = \frac{D^A_{N,x}\sqrt{\beta_{x}^{\phi}}}{D^A_{x}}$ | $\left&#40;\Delta {C^A_x}\right&#41;^{2} = \left&#40;\frac{\Delta D^\phi_x}{D^A_x}\right&#41;^2 + \left&#40;\Delta D^A_x \frac{D^\phi_x}{&#40;D^A_x&#41;^2}\right&#41;^2$ | $C^A_{x,y} = \sqrt{\frac{\beta^{\phi,fit}_{x,y}}{\beta^A_{x,y}}}$ | ${C_{x}^{A}} = \frac{D^{\phi,fit}_x}{D^A_x} = \frac{\left&#40;D^A_{N,x}\sqrt{\beta_{x}^{\phi}}\right&#41;^{fit}}{D_{x}^{A}}$ | $\left&#40;\Delta {C^A_x}\right&#41;^{2} = \left&#40;\frac{\Delta D^{\phi,fit}_x}{D^A_x}\right&#41;^2 + \left&#40;\Delta D^A_x \frac{D^{\phi,fit}_x}{&#40;D^A_x&#41;^2}\right&#41;^2$ |)

[bpm_calibration]: ../../measurements/physics/calibration.md

[documentation]: https://pylhc.github.io/PyLHC/entrypoints/bpm_calibration.html
