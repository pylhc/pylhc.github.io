# How to Create a Python Virtual Environments

Both for the development of Python codes as well as running some of the existing codes, the creation of a virtual Python enviroment is recommended.
This not only prevents conflicts when installing multiple packages with different required versions of the same package, but also allows to separate production and test scenarios. 

!!! tip "Python Virtual Environments"
    Don't know what a **virtual environment** is or the difference between these many tools?
    Here is a good (but lengthy) [primer on virtual environments][virtual_env_primer]{target=_blank} by RealPython.

Python environments are created using the built-in `venv` module, with the old `pyvenv` being deprecated since `Python 3.6` and as such not recommended.
The following description is a summary of the steps presented [here][venv_module]{target=_blank} and [here][pip_venv]{target=_blank}, targetting Unix users.

??? question "What About Anaconda?"
    Note that the [Anaconda Python distribution][anaconda]{target=_blank} provides the `conda` tool as a package manager, which also allows the creation of Python virtual environments.
    However, due to the simplicity of the `venv` module, only this module will be described in the following.

## Virtual Environments with pyvenv

To create a virtual enviroment in the folder `testpython`, run the command
```
python -m venv ./testpython
```

This creates a python enviroment in the `testpython` folder, linking to the original Python installation.
As such, all packages of the original installation are available.
However, using a clean and up-to-date `Python 3` installation is recommended. 

!!! note "Python Installations"
    Multiple installations are available in the GPN.
    An installation maintained by the OMC-team can be found at `/afs/cern.ch/eng/sl/lintrack/anaconda3/bin`.
    The general Python distribution `acc-py`, maintained by BE/CO, is detailed in [this wiki][acc-py]{target=_blank .cern_internal}.
    
To activate the created python installation, run 
```
source ./testpython/env/activate
```

Now, the alias `python` should link to the installation in the `testpython` folder instead of the standard installation.
This can be checked on Unix systems with the command `which python`.
Note that the following command also provides access to the new installation and can be used to run scripts:
```
./testpython/bin/python
```

To leave the Python enviroment, run:
```
deactivate
```

After the activation of the enviroment, packages can be installed with `pip`.
The packages installed this way will be put in the `testpython` folder structure and will thus not affect the main system installation.
Packages installed here will have priority over the packages of the original distribution when you have activated the environment.
Different ways to use `pip` for package installations are nicely explained in the [official documentation][pip_installs]{target=_blank}.

## Example use case

In the following, a typical example is shown how to create a virtual enviroment in the current working directory and install `omc3` to perform an optics analysis.

First, create and activate a virtual environment:
```
/afs/cern.ch/eng/sl/lintrack/anaconda3/bin/python -m venv ./omcpython
source ./omcpython/env/activate
```

Then, clone and install the `omc3` package (since it is not yet deployed on PyPI):
```
git clone https://github.com/pylhc/omc3
pip install --editable ./omc3[all]
```

Finally, run your analysis:
```
python -m omc3.hole_in_one --harpy --files ...
```


Note when installing `omc3`, required packages such as `tfs-pandas` are automatically fetched and installed from PyPi.
Furthermore, additional required packages for running the unittests, such as `pytest`, are also installed when specifying the `all` or `test` extras.
To run the tests, run:
```
python -m pytest ./omc3/tests
```


*[python]: If you don't know what Python is, this section might not be for you
*[GPN]: CERN General Public Network
*[PyPi]: Default Python Package Index

[virtual_env_primer]: https://realpython.com/python-virtual-environments-a-primer/
[venv_module]: https://docs.python.org/3/library/venv.html
[pip_venv]: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
[anaconda]: https://www.anaconda.com/products/individual
[acc-py]: https://wikis.cern.ch/display/ACCPY
[pip_installs]: https://pip.pypa.io/en/stable/reference/pip_install/#examples