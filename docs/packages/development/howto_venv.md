# How to create a virtual python enviroment

Both for the development of python codes as well as running some of the existing codes,
the creation of a virtual python enviroment is recommended. This not only prevents
conflicts when installing multiple packages with different required versions of the same package,
but also allows to separate production and test scenarios. 

Python enviroments are created using the `venv` module, with the old `pyvenv` being deprecated
since `python 3.6` and as such not recommened. The following description is a summary 
of the steps presented [here][venv_module]{target=_blank} and [here][pip_venv]{target=_blank},
specifically targetting Linux users.

Note that [Anaconda Python distribution][anaconda]{target=_blank} provides the `conda` tool, which also the
creation of python enviroments. However, due to the simplicity of the `venv` module,
only this module will be described in the following.

## Creating a virtual enviroment

To create a virtual enviroment in the folder `testpython`, run the command

```
python -m venv ./testpython
```

This creates a python enviroment in the `testpython` folder, linking to the original python installation.
As such, all packages of the original installation are available. Any `python 3` installation,
however, using a clean installation is recommended. 

!!! note "Python installations"
    Multiple installationa are available in the GPN, such as an installation maintained
    by the OMC-team found here `/afs/cern.ch/eng/sl/lintrack/anaconda3/bin`
    or the general python distribution, maintained by BE/CO, which can be found [here][acc-py]{target=_blank .cern_internal}.
    
To activate the created python installation, run 

```
source ./testpython/env/activate
```

Now, the alias `python` should link to to installation in the `testpython` folder instead of the standard installation,
which under Linux can be checked using 

```
which python
```

Note that the command

```
./testpython/bin/python
```

also provides access.
To leave the python enviroment, run

```
deactivate
```

After the activation of the enviroment, packages can be installed using `pip install`.
The packages installed this way will be put in the `testpython` folder structure and
will thus not affect the main installation. Packages installed here will have priority over the
packages of the original distribution.

To install packages available in PyPi, such as [tfs-pandas][tfspandas]{target=blank}, run

```
pip install tfs-pandas
```

For packages available only from Github/Gitlab, such as [omc3][omc3]{target=blank}, run

```
pip install git+https://github.com/pylhc/omc3.git
```

Alternatively, to obtain the full codebase for further development, run

```
git clone https://github.com/pylhc/omc3
pip install --editable ./omc3
```

This clones the codebase from github to the folder `omc3` and installs the `omc3` such that
modifications are taken into account once the module is loaded.

## Example use case

In the following, a typical example is shown how to create a virtual enviroment in 
the current working directory and install `omc3` to perform an optics analysis.

```
/afs/cern.ch/eng/sl/lintrack/anaconda3/bin/python -m venv ./omcpython
source ./omcpython/env/activate
git clone https://github.com/pylhc/omc3
pip install --editable ./omc3[all]
python -m omc3.hole_in_one --harpy --files ...
```


Note when installing `omc3`, required packages such as `tfs-pandas` are automatically
fetched from PyPi. Furhtermore, additional required packages for run the unittest, such as `pytest`,
are also installed. To run the tests, run 
```
python -m pytest ./omc3/tests
```

*[python]: if you don't know what python is, this website might not be for you
*[GPN]: CERN General Public Network
*[PyPi]: Default Python Package Index

[venv_module]: https://docs.python.org/3/library/venv.html
[pip_venv]: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
[anaconda]: https://www.anaconda.com/products/individual
[acc-py]: https://wikis.cern.ch/display/ACCPY
[tfspandas]: https://github.com/pylhc/tfs
[omc3]: https://github.com/pylhc/omc3

