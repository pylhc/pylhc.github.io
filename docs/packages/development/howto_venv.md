# Creating and Using Python Virtual Environments

Both for the development of Python codes as well as running programs, the creation of a Python virtual environment is recommended.
Not only does it prevent version conflicts and ever-growing installations, it also allows separating production and test scenarios.

!!! tip "Python Virtual Environments"
    Don't know what a **virtual environment** is or what purpose it serves?
    Here is a good (but lengthy) [primer on virtual environments][virtual_env_primer]{target=_blank} by RealPython.

## Virtual Environments at CERN with Acc-Py

The BE/CO [Acc-Py][acc-py]{target=_blank .cern_internal} distribution at CERN (at `/acc/local/share/python/acc-py/base/pro`) allows one to create Python virtual environments immediately configured for internal CERN index and apps.
`Acc-Py` is the official way to manage one's Python environments at CERN for the foreseeable future.
You can think of it like a `miniconda` installation with all the CERN-specific hooks in place, with additional command line utilities for CERN apps.

However, because of how Python virtual environments work under the hood, the `python` executable in any such virtual environment is a symlink to the `Acc-Py` distribution's base Python executable.
This means any machine wanting to use this executable needs to also have read access to the location of the `Acc-Py` distribution in `/acc/`, which means having access to the Technical Network - not always the case.
For this reason, one might want to install a standalone `Acc-Py` distribution somewhere else, for instance on `afs`.

!!! info "OMC Production Python"
    The OMC team has a stable Python 3 production environment on `afs`.
    See [this page](../about.md) to find out about it.

The following section goes over installing a **standalone** `Acc-Py` distribution, which is how we manage the OMC environments.
If you already have one at the ready or plan to use the BE/CO-provided `Acc-Py`, then skip ahead.

## Installing a Standalone Acc-Py

The `Acc-Py` wiki has [a section][acc_py_standalone_doc]{target=_blank} linking to installers one can download.
From there download the desired file, `curl` or `wget` will work great if you are `ssh`-ed into a server.

A default distribution is recommended but installation is identical for other distributions (pro, devel, rc).
As of the last update of this walk-through, this corresponds to the `acc-py-2026.01-installer.sh` file.

The installer itself is an executable to be called from the command line.
You might need to `chmod u+x` the file once downloaded.

The installer is to be run at the command line, providing the installation root:
This *does not have to be an existing directory*, it can be created at install.

Once the installation root determined (here `dist_location`), call the installer:

```bash
bash acc-py-2026.01-installer.sh --installation-root /path/to/dist_location
```

??? info "Installation Root Location in Previous Versions"
    Up to the installers for `Acc-Py` `2023.06`, the behavior was trickier.
    The caveat is still documented below for safekeeping.

    On those versions, at post-install the script would try to create an `apps` folder (where it will install built applications, including the `acc-py` command line tool).
    This `apps` folder was created **two directories up from the given installation location**, which is a place you might not necessarily have access to.
    Should this be the case, the installation would error.
    To make sure to not run into permission issues, it was advised to feed a nested location to the installer.

    For instance, instead of providing `dist_location` to the installer, provide `dist_location/base/2023.06`.
    This way the `apps` folder will be located at `dist_location/apps` to which you are guaranteed to have rights.

    **Note:** On those versions the `--installation-root` flag did not exist; it would be prompted after simply calling the installer without options.

Wait for the installation script to finish - if you have installed anaconda or miniconda in the past, the process and its output will feel familiar.
The created structure should look like (obtained with `tree -L 3 dist_location`):

```bash
dist_location/
├── apps
│   └── acc-py-cli
│       └── latest
└── base
    └── 2026.01
        ├── bin
        ├── _conda
        ├── etc
        ├── include
        ├── lib
        ├── man
        ├── pip.conf
        ├── setup.sh
        ├── share
        └── ssl -> /etc/pki/tls
```

!!! success
    You are now done with the installation step.
    A "base" environment has been created and, much like a miniconda distribution, it should not be modified: use virtual environments.
    Read below for this step.

## Creating Virtual Environments with Acc-Py

To make the command line tools available in the current shell, `source` the `setup.sh` script in the installed `Acc-Py` distribution:

```bash
source dist_location/base/2026.01/setup.sh
```

You should see a confirmation message output that reads:

```bash
=>  Acc-Py base 2026.01 is now active within this shell.
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

When your virtual environment has all the packages you wish, anyone with access to the distribution's `python` executable (because all virtual environments will symlink to that) can use it.
To use the environment's Python, one can either:

- First `source /path/to/environment/bin/activate` then call `python`.
- Call the full path to the python executable `/path/to/environment/bin/python` directly.

[cern_internal_websites]: ../../resources/remote_access.md#accessing-cern-internal-websites

*[GPN]: CERN General Public Network
*[PyPi]: Default Python Package Index

[virtual_env_primer]: https://realpython.com/python-virtual-environments-a-primer/
[acc-py]: https://confluence.cern.ch/pages/viewpage.action?spaceKey=ACCPY&title=Getting+started+with+Acc-Py
[acc_py_standalone_doc]: https://confluence.cern.ch/display/ACCPY/Acc-Py+base+installers
[venv_module]: https://docs.python.org/3/library/venv.html
[pip_installs]: https://pip.pypa.io/en/stable/reference/pip_install/#examples
