# Machine Settings Info

[See the docs][documentation] for a detailed code description.

Prints an overview over the machine settings at a provided given time, or the current settings if
no time is given.

Can be run from command line, parameters as given in `print_machine_settings_overview.main`.

```bash
usage: machine_settings_info.py [-h] [--time TIME] [--start_time START_TIME]
                                [--knobs KNOBS [KNOBS ...]] [--accel ACCEL]
                                [--output_dir OUTPUT_DIR] [--knob_definitions]
                                [--source SOURCE] [--log]

optional arguments:
-h, --help            show this help message and exit
--time TIME           UTC Time as 'Y-m-d H:M:S.f' format or ISO.
                      Acts as point in time or end time
                     (if ``start_time`` is given).
--start_time START_TIME
                        UTC Time as 'Y-m-d H:M:S.f' format.
                        Defines the beginning of the time-range.
--knobs KNOBS [KNOBS ...]
                        List of knobnames.
--accel ACCEL         Accelerator name.
--output_dir OUTPUT_DIR
                        Output directory.
--knob_definitions    Set to extract knob definitions.
--source SOURCE       Source to extract data from.
--log                 Write summary into log
                      (automatically done if no output path is given).
```

[documentation]: https://pylhc.github.io/PyLHC/entrypoints/machine_info.html