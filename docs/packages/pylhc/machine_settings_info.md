# Machine Settings Info

!!! todo
    Description of a typical use-case, with easy examples for first-timers.

[See the docs][documentation] for a detailed code description.

Prints an overview over the machine settings at a provided given time, or the current settings if
no time is given.

Can be run from command line, parameters as given in :meth:`print_machine_settings_overview.main`.

```bash
  print_machine_settings_overview.py [-h] [--time TIME]
                                          [--knobs KNOBS [KNOBS ...]]
                                          [--bp_regexp BP_REGEXP]
                                          [--accel ACCEL]
                                          [--out OUT]

  optional arguments:
    -h, --help            show this help message and exit
    --time TIME, -t TIME  Time as 'Y-m-d H:M:S.f' format.
    --knobs KNOBS [KNOBS ...], -k KNOBS [KNOBS ...]
                          List of knobnames.
    --bp_regexp BP_REGEXP, -r BP_REGEXP
                          Beamprocess regexp filter.
    --accel ACCEL, -a ACCEL
                          Accelerator name.
    --out OUT, -o OUT     Output path.
```

[documentation]: https://pylhc.github.io/PyLHC/entrypoints/machine_settings_info.html 