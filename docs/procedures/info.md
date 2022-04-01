
# Checklists

In this section there are multiple checklists for procedures, that can be used as guidance during measurements.
To mark a task as finished, just click on the checkbox next to it!

!!! warning "Non-Persistance"
    The checked-boxes stay checked only as long as you stay on that page!
    Any reload will reset the ticks.

!!! note "Log Your Work!"
    When performing measurements or tests in the CCC, remember to add an entry into the LogBook.
    It can be accessed through the [OP Webtools][op_webtools]{target=_blank .cern_login}.

    Ideally, each measurement shift has **at least** two entries, one created at the start of the shift to outline the plan, and one summary entry at the end.
    A first entry for a shift may look like this:
    ```
    Short Title for shift (e.g. MD 1234 Measuring XYZ)

    Fill : Fill Nr. for the first beam used for measurements.
    Beam Process: Beamprocess used during measurement.
    If separate measurements are conducted for the different beams, note here which beam is used for what.

    Personnel: People joining either in person or remotely, operators and EIC.

    Plan: Quick outline of the steps to be performed and general goals.
    ```

    A potential summary entry at the end of a shift may look like this:
    ```
    Title

    Summary: Brief description of the steps taken and results.

    Follow up: Next steps to be taken offline.

    Problems: Note of problems encountered and potential solutions.
    ```

    Entries for analysis of data may look like this:
    ```
    Analyst Name, Beam number (e.g. Felix, B1)

    Fill number: number of the LHC fill used for the kicks (e.g. 7528)
    Bunch: bunch slot number of the measured bunch(es) (e.g. 894)
    Turns: number of acquisition turns (e.g. 6600)
    Tunes: natural working point of the machine (e.g. 0.28 / 0.31)
    Delta: driven delta from the kicker (e.g. -0.01 / 0.012)

    Analysed kicks:
    - kick amplitudes - kick time, acquisition file --> potential comment on the kick (e.g. 3% 3% - 09:55:31 good (Beam1@Turn@2021_10_31@08_55_39_620.sdds) --> used for coupling correction calculation)
    - etc for each kick

    Comments on analysis results and attached screenshots.
    ```

!!! tip "Machine Settings"
    There is in `pylhc` a callable module to extract the machine settings at a given time, which one can use to find the relevant information to enter into the logbook.
    A simple call would be, for instance here to get settings at call time:
    ```bash
    /afs/cern.ch/eng/sl/lintrack/omc_python3/bin/python -m pylhc.machine_settings_info
    ```

    Note that this needs to be run from a machine that has access to the technical network.
    To only get specific knobs at specific times (careful with UTC times), see the [package's documentation][pylhc_doc].


*[CCC]: CERN Control Center

[op_webtools]: https://op-webtools.web.cern.ch/index.html
[pylhc_doc]: https://pylhc.github.io/PyLHC
