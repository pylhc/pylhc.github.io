# The beam selection Window

!!! tip "Setting Your Defaults"
    You can set all entries in this window to your preferred defaults for a quick start!
    Check the [Defaults Page](defaults.md) for more details.

!!! todo
    Include screenshot of Beam-Selection Window and describe the settings.

### Python

In the Beam-Selection Window you need to give it a python-binary (e.g. `venv/bin/python`).
Best would be if you have a local virtual environment.
This **needs to have omc3 installed as a package**.
See [omc3 on github][omc3_github_getting_started]{target=_blank}.
```bash
pip install git+https://github.com/pylhc/omc3.git
```
This is because python calls are now made by module, i.e.:
```bash
python -m omc3.module arg1 arg2 ...
```

