# Creating and Using Python Virtual Environments

Both for the development of Python codes as well as running programs, the creation of a Python virtual environment is recommended.
Not only does it prevent version conflicts and ever-growing installations, it also allows separating production and test scenarios.

!!! tip "Python Virtual Environments"
    Don't know what a **virtual environment** is or what purpose it serves?
    Here is a good (but lengthy) [primer on virtual environments][virtual_env_primer]{target=_blank} by RealPython.

## Virtual Environments at CERN with Acc-Py

The BE/CO [Acc-Py][acc-py]{target=_blank .cern_internal} distribution at CERN (at `/acc/local/share/python/acc-py/base/pro`) allows one to create Python virtual environments immediately configured for internal CERN index and apps.
`Acc-Py` is the official way to manage one's Python environments at CERN for the foreseeable future.

However, because of how Python virtual environments work, the `python` executable in such a virtual environment is a symlink to the `Acc-Py` distribution's Python executable.
This means any machine wanting to use this executable needs to also have read access to the location of the `Acc-Py` distribution in `/acc/`, which means having access to the Technical Network.
For this reason, one might want to install a standalone `Acc-Py` distribution somewhere else, for instance on `afs`.

!!! info "OMC Production Python"
    The OMC team has a stable Python 3 production environment on `afs`.
    See [this page](../about.md) to find out about it.

The following section goes over installing a standalone `Acc-Py` distribution.
If you already have one at the ready or plan to use the BE/CO `Acc-Py`, then skip ahead.

## Installing a Standalone Acc-Py

The `Acc-Py` wiki has [a section][acc_py_standalone_doc]{target=_blank} linking to installers one can download.
From there download the appropriate file.
The default distribution is recommended but installation is identical for other distributions (devel, rc).
As of writing this walk-through, this corresponds to the `acc-py-2020.11-installer.sh` file.
The installer itself is an executable to be called from the command line.
Once the file is downloaded, run it at the command line (you might need to `chmod u+x` the file):
```bash
bash acc-py-2020.11-installer.sh
```

The installation script will prompt you to enter the location in which to install the distribution.
This does not have to be an existing directory, it can be created at install.

!!! tip "Choosing the Installation Location"
    At post-install, the script will try to create a folder `apps` where it will install built applications, including the `acc-py` command line tool.
    This `apps` folder is created two directories up from the given installation location, which is a place you might not necessarily have access to.
    Should this be the case, the installation will error.
    To make sure you do not run into permission issues, it is advised to feed a nested location to the installer.

    For instance, instead of providing `dist_location` to the installer provide `dist_location/base/2020.11`.
    This way the `apps` folder will be located at `dist_location/apps` to which you are guaranteed to have rights.

When prompted by the script, enter the desired installation location (here `dist_location/base/2020.11`) and hit enter, then wait for the installation script to finish.
If you have installed anaconda or miniconda previously, the process and its output will feel familiar.
You are now done with the installation step.

## Creating Virtual Environments with Acc-Py

To make the command line tools available in the current shell, `source` the `setup.sh` script in the installed `Acc-Py` distribution:
```bash
source dist_location/base/2020.11/setup.sh
```

You should see a confirmation message output that reads: 
```
=>  Acc-Py base 2020.11 is now active within this shell.
```

You now have access to the `acc-py` command line tool, which you can verify by running `acc-py -h` and checking that you get the help command output.
The command to create a virtual environment is based on the built-in [venv][venv_module]{target=_blank} module and should feel familiar if you know `venv`.
To create a virtual environment, run:
```bash
acc-py venv /path/to/environment/
```

This will create a virtual environment at `/path/to/environment/`.
To activate this environment, run:
```bash
source /path/to/environment/bin/activate
```

You can confirm you are running the appropriate Python with `which python`, which should point to `/path/to/environment/bin/python`.
You can then install packages in this environment with:
```bash
python -m pip install <package-name>
```

Using `python -m pip` instead of simply `pip` guarantees that the right executable is called.
Thanks to `Acc-Py`, everything is already set up to look into the CERN index, which is where many CERN apps and packages have to be installed from.
Different ways to use `pip` for package installations are nicely explained in the [official documentation][pip_installs]{target=_blank}.

!!! info "Accessing the CERN Index"
    Installing from the CERN index requires the executing machine to have access to the CERN GPN (General Public Network), or to [be tunnelled into the GPN][cern_internal_websites].

## Using Your Virtual Environment

When your virtual environment has all the packages you wish, anyone with access to the distribution's `python` executable (because all environments will symlink to there) can use it.
To use the environment's Python, one can either:

- First `source /path/to/environment/bin/activate` then call `python`.
- Call the full path to the python executable `/path/to/environment/bin/python` directly.

[cern_internal_websites]: ../../howto/teleworking/access.md#accessing-cern-internal-websites 

*[GPN]: CERN General Public Network
*[PyPi]: Default Python Package Index

[virtual_env_primer]: https://realpython.com/python-virtual-environments-a-primer/
[acc-py]: https://wikis.cern.ch/display/ACCPY/Accelerating+Python+Home
[acc_py_standalone_doc]: https://wikis.cern.ch/display/ACCPY/Acc-Py+base#Acc-Pybase-Installingthebasedistributiononanothermachine
[venv_module]: https://docs.python.org/3/library/venv.html
[pip_installs]: https://pip.pypa.io/en/stable/reference/pip_install/#examples