# The Beam Selection Window

<figure>
  <center>
  <img src="../../assets/images/betabeat_gui/beam_selection.png" width="100%" alt="The beam selection window" />
  <figcaption>The Beam Selection Window.</figcaption>
  </center>
</figure>

The Beam Selection Window is your entry point to the GUI.
Here, you set which machine you will be using and which `python` backend to run.
The options chosen here will also define the **folder-structure** you will be using during your current analysis session.

!!! tip "Setting Your Defaults"
    You can set all entries in this window to your preferred defaults for a quick start!
    Check the [Defaults Page](defaults.md) for more details.

## Beam

## Output

## Input

## Python Executable

In the Beam-Selection Window you need to give it a python-binary (e.g. `.venv/bin/python`).
Best would be if you have a local virtual environment.
This **needs to have omc3 installed as a package**.
See [omc3 on github][omc3_github]{target=_blank}.

```bash
pip install git+https://github.com/pylhc/omc3.git
```

This is because python calls are now made by module, i.e.:

```bash
python -m omc3.module arg1 arg2 ...
```

[omc3_github]: https://github.com/pylhc/omc3
