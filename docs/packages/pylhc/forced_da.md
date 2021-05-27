# Forced Dynamic Aperture Analysis

!!! todo
    Description of a typical use-case, with easy examples for first-timers.

[See the docs][documentation] for a detailed code description.

Top-level script to run the forced DA analysis, following the procedure described in [Felix Carliers Forced DA Paper][CarlierForcedDA2019]{target=_blank}.

Arguments:

*--Required--*

- **beam** *(int)*: Beam to use.
  Flags: **['-b', '--beam']**
  Choices: ``[1, 2]``
- **energy** *(MultiClass)*: Beam energy in GeV.
  Flags: **['-e', '--energy']**
- **kick_directory** *(MultiClass)*: Analysis kick_directory containing kick files.
  Flags: **['-k', '--kickdir']**
- **plane** *(str)*: Plane of the kicks.
  Flags: **['-p', '--plane']**
  Choices: ``['X', 'Y']``

*--Optional--*

- **emittance_outlier_limit** *(float)*: Limit, i.e. cut from mean, on emittance outliers in meter.
  Default: ``5e-07``
- **emittance_tfs** *(MultiClass)*: Dataframe or Path of pre-saved emittance tfs.
- **emittance_type** *(str)*: Which BSRT data to use (from database).
  Choices: ``['fit_sigma', 'average']``
  Default: ``average``
- **emittance_window_length** *(int)*: Length of the moving average window. (# data points).
  Default: ``100``
- **fill** *(int)*: Fill that was used. If not given, check out time_around_kicks.
  Flags: **['-f', '--fill']**
- **fit** *(str)*: Fitting function to use (rearranges parameters to make sense).
  Choices: ``['exponential', 'linear']``
  Default: ``exponential``
- **intensity_tfs** *(MultiClass)*: Dataframe or Path of pre-saved intensity tfs.
- **intensity_time_after_kick** *(int)*: Defines the times after the kicks (in seconds) which is used for intensity averaging to calculate the losses.
  Default: ``[5, 30]``
- **intensity_time_before_kick** *(int)*: Defines the times before the kicks (in seconds) which is used for intensity averaging to calculate the losses.
  Default: ``[30, 5]``
- **normalized_emittance** *(float)*: Assumed NORMALIZED nominal emittance for the machine.
  Default: ``3.7499999999999997e-06``
- **output_directory** *(MultiClass)*: Output kick_directory, if not given subfolder in kick kick_directory
  Flags: **['-o', '--outdir']**
- **pagestore_db** *(MultiClass)*: (Path to-) presaved timber database
- **show**: Show plots.
  Action: ``store_true``
- **show_wirescan_emittance** *(BoolOrPathOrDataFrame)*: Flag if the emittance from wirescan should also be shown, can also be a Dataframe or Path of pre-saved emittance bws tfs.
  Default: ``False``
- **timber_db** *(str)*: Which timber database to use.
  Choices: ``['all', 'mdb', 'ldb', 'nxcals']``
  Default: ``all``
- **time_around_kicks** *(int)*: If no fill is given, this defines the time (in minutes) when data before the first and after the last kick is extracted.
  Default: ``10``
- **plot_styles** *(str)*: Which plotting styles to use, either from omc3 styles or default mpl.
  Default: ``['standard']``
- **manual_style** *(DictAsString)*: Additional style rcParameters which update the set of predefined ones.
  Default: ``{}``

[documentation]: https://pylhc.github.io/PyLHC/entrypoints/forced_da_analysis.html
[CarlierForcedDA2019]: https://journals.aps.org/prab/pdf/10.1103/PhysRevAccelBeams.22.031002