# Display kickgroups

When [performing beam measurements](../../guis/multiturn/gui.md), we typically create *kick groups* to gather specific kicks all relating to the same measurements into a same structure.
These

When coming back to specific measurements, instead of looking at the list of corresponding files in a kickgroup via the logbook, it can be done programatically.
The `pylhc` package provides a script to query the list of kickgroups as well as the various files in a kickgroup.

Fetching the available kickgroups goes as `python -m pylhc.kickgroups list`.
Below is an example output from the command.

```bash


       UTC                  LOCAL                    KICKGROUP
2021-10-20 15:12:46   2021-10-20 17:12:46                 2021_10_20_Beam1_for_coupling_correction
2021-10-22 07:03:05   2021-10-22 09:03:05   2021_10_22_Beam2_before_global_betabeat_correction_INJ
2021-10-22 09:07:29   2021-10-22 11:07:29   2021_10_22_Beam1_before_global_betabeat_correction_INJ
2021-10-22 09:37:46   2021-10-22 11:37:46                                  2021-10-22-B2-afterCorr
2021-10-22 11:43:31   2021-10-22 13:43:31            2021_10_22_Beam1_after_betabeat_corrction_inj
2021-10-22 12:01:23   2021-10-22 14:01:23    2021_10_22_Beam2_after_global_betabeat_correction_INJ
...
...
2026-04-15 14:45:37   2026-04-15 16:45:37                                   2026-04-15_BEAM1_onMom
2026-04-15 16:11:58   2026-04-15 18:11:58                                    2026-04-15_BEAM2_-150
2026-04-15 16:12:03   2026-04-15 18:12:03                               2026-04-15_BEAM1_-150urads
```

With knowledge of a specific kick group's name, one can also query for the various kicks, or measurements, within.
This goes through the same script as `python -m pylhc.kickgroups info <groupname>`.
The output also reports basic information on the kick settings, as well as the location of the measurement file and that of a `JSON` file with all kick settings.
Below is the output from running `python -m pylhc.kickgroups info 2026-02-27_BEAM2_ft_93cm`:

```bash
KICKGROUP: 2026-02-27_BEAM2_ft_93cm
BEAM: BEAM2
FILL: 11412
BUNCH: 32,825,1655
TURNS: 6600
BEAMPROCESS: RAMP-SQUEEZE-ROTATE-6.8TeV-ATS-1.2m-2026_V1@1275_[END]
OPTICS: R2025aRP_A120cmC120cmA10mL200cm
OPTICS_URI: gitlab+https://gitlab.cern.ch/acc-models/acc-models-lhc@v2025.13#LHC+2025&optic=R2025aRP_A120cmC120cmA10mL200cm

         UTC                  LOCAL           QX    QY   DQX   DQY   DQZ  AMPX  AMPY AMPZ                                                       SDDS                                                                                                         JSON
  2026-02-27 14:43:02   2026-02-27 15:43:02  0.28  0.31  0.27  0.322  -   25.0  25.0  -   /nfs/cs-ccr-nfs4/lhc_data/OP_DATA/FILL_DATA/11412/BPM/BUNCHTURN.BEAM2@Concentrated@2026_02_27@14_43_02_955.sdds /nfs/cs-ccr-nfs4/lhc_data/OP_DATA/FILL_DATA/11412/Multiturn/MULTITURN_ACQ_METADATA_27-02-26_15-43-02.json
  2026-02-27 14:45:16   2026-02-27 15:45:16  0.28  0.31  0.27  0.322  -   30.0  30.0  -   /nfs/cs-ccr-nfs4/lhc_data/OP_DATA/FILL_DATA/11412/BPM/BUNCHTURN.BEAM2@Concentrated@2026_02_27@14_45_16_896.sdds /nfs/cs-ccr-nfs4/lhc_data/OP_DATA/FILL_DATA/11412/Multiturn/MULTITURN_ACQ_METADATA_27-02-26_15-45-16.json
  2026-02-27 14:46:39   2026-02-27 15:46:39  0.28  0.31  0.27  0.322  -   30.0  30.0  -   /nfs/cs-ccr-nfs4/lhc_data/OP_DATA/FILL_DATA/11412/BPM/BUNCHTURN.BEAM2@Concentrated@2026_02_27@14_46_39_765.sdds /nfs/cs-ccr-nfs4/lhc_data/OP_DATA/FILL_DATA/11412/Multiturn/MULTITURN_ACQ_METADATA_27-02-26_15-46-39.json
  2026-02-27 14:48:00   2026-02-27 15:48:00  0.28  0.31  0.27  0.322  -   35.0  35.0  -   /nfs/cs-ccr-nfs4/lhc_data/OP_DATA/FILL_DATA/11412/BPM/BUNCHTURN.BEAM2@Concentrated@2026_02_27@14_48_00_367.sdds /nfs/cs-ccr-nfs4/lhc_data/OP_DATA/FILL_DATA/11412/Multiturn/MULTITURN_ACQ_METADATA_27-02-26_15-48-00.json
  2026-02-27 14:49:20   2026-02-27 15:49:20  0.28  0.31  0.27  0.322  -   40.0  40.0  -   /nfs/cs-ccr-nfs4/lhc_data/OP_DATA/FILL_DATA/11412/BPM/BUNCHTURN.BEAM2@Concentrated@2026_02_27@14_49_20_890.sdds /nfs/cs-ccr-nfs4/lhc_data/OP_DATA/FILL_DATA/11412/Multiturn/MULTITURN_ACQ_METADATA_27-02-26_15-49-20.json
  2026-02-27 14:50:47   2026-02-27 15:50:47  0.28  0.31  0.27  0.322  -   40.0  40.0  -   /nfs/cs-ccr-nfs4/lhc_data/OP_DATA/FILL_DATA/11412/BPM/BUNCHTURN.BEAM2@Concentrated@2026_02_27@14_50_47_944.sdds /nfs/cs-ccr-nfs4/lhc_data/OP_DATA/FILL_DATA/11412/Multiturn/MULTITURN_ACQ_METADATA_27-02-26_15-50-47.json
  2026-02-27 14:52:49   2026-02-27 15:52:49  0.28  0.31  0.27  0.322  -   40.0  40.0  -   /nfs/cs-ccr-nfs4/lhc_data/OP_DATA/FILL_DATA/11412/BPM/BUNCHTURN.BEAM2@Concentrated@2026_02_27@14_52_49_676.sdds /nfs/cs-ccr-nfs4/lhc_data/OP_DATA/FILL_DATA/11412/Multiturn/MULTITURN_ACQ_METADATA_27-02-26_15-52-49.json
```

See the [corresponding documentation page][script_doc]{target=_blank} for a more detailed description.

*[kick groups]: A list of beam excitations performed that represent either the same machine state or are paired for ease of analysis.

[script_doc]: https://pylhc.github.io/PyLHC/entrypoints/kickgroups.html
