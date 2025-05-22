# The OMC GUIs

The OMC team uses several GUIs to help running data acquisition and analysis codes, each for a defined use:

- [The Beta-Beat GUI](betabeat/gui.md) to perform analysis of measurement files and compute corrections.
- [The Kmod GUI](kmod/gui.md) to perform K-modulation, analyse data and export results.
- [The Multiturn GUI](multiturn/gui.md) to perform beam excitation and data acquisition.
- [The Chroma GUI](chroma/gui.md) to determine chromaticity from RF scan analysis and compute corrections.

Of these, only the Beta-Beat GUI is currently developed by the team.

## Running the GUIs

The GUIs can be started from your development environment or via deployed `.jnlp` from the archives:

=== "Beta-Beat-OMC3"

    - Latest [Beta-Beating production version][prod_bbgui_omc3]{target=_blank}.
    - Latest [Beta-Beating development version][dev_bbgui_omc3]{target=_blank}.
    - Complete [list of releases][releases_bbgui_omc3]{target=_blank}.

=== "Beta-Beat (Legacy)"

    - Latest [Beta-Beating production version][prod_bbgui]{target=_blank}.
    - Latest [Beta-Beating development version][dev_bbgui]{target=_blank}.
    - Complete [list of releases][releases_bbgui]{target=_blank}.

=== "Kmod"

    The K-modulations GUI is now a Python app published with `acc-py`, and can be run with:

    ```bash
    /acc/local/share/python/acc-py/apps/acc-py-cli/pro/bin/acc-py app run pykmodlhc
    ```

=== "Multiturn"

    - Latest [Multiturn production version][prod_mtgui]{target=_blank}.
    - Latest [Multiturn development version][dev_mtgui]{target=_blank}.
    - Complete [list of releases][releases_mtgui]{target=_blank}.

=== "Chroma"

    The Chroma GUI is a Python app published with `acc-py`, and can be run with:

    ```bash
    /acc/local/share/python/acc-py/apps/acc-py-cli/pro/bin/acc-py app run chroma-gui
    ```

!!! warning
    Please note these sites are currently available only to devices connected to the CERN network ([see: workaround][connect_gpn]).

Open the `.jnlp` executable inside a browser, or [call it with `jws` from the command line][jws_calls]:

!!! info "Compatibility Issues"
    Since `javaws` (java web start) causes trouble due to internal security mechanisms, a replacement named `jws` was developed and has to be used to run the `jlnp` file.
    For further information see the [jws Confluence][jws_confluence]{target=_blank .cern_internal} page.

## Requirements

The following are required to run the GUIs:

- A version of `Java>=8`.
- The [`jws`][jws]{target=_blank .cern_internal} replacement for `javaws` (in case of errors, [see below](#problems-with-execution-due-to-disabled-java)).

!!! info
    Being inside of the TN is required for the `KnobPanel`.
    To do so, either `ssh -X` to the `cs-ccr-dev` machines or use [the sshuttle method][sshuttle_method].

!!! tip "Kick Groups"
    To make use of the Kick-Groups, your machine [needs to have `/nfs` and `/user` mounted][mounting_resources], like the `cs-ccr-dev`  and `cs-ccr-optics` machines.

## Troubleshooting

You may encounter the following errors:

### Running in the CCC in 2025

On the CCC terminals, there are some issues related to finding the correct java path,
which affects `NXCals` extraction.
To avoid this, close all windows and CCMs and then run:

```bash
/user/slops/data/LHC_DATA/OP_DATA/Betabeat/launch_ccm.sh
```

This script performs the following commands, which could also be done manually in a terminal:

- Create a kerberos ticket: `kinit lhcop`
- Adapt the path/set `JAVA_HOME` to use the correct java: `export PATH=/bin:$PATH`  and/or `export JAVA_HOME=/usr/java/jdk`  (either should be fine)
- run `ccm` or `/mcr/bin/ccm`

Then select `LHCOP` and launch the Beta-Beat GUI from the new CCM window.

### Problems with execution due to disabled Java

If you encounter a complaint about `Java` being too old, try using `/mcr/bin/jws`.

!!! failure
    ```bash
    javaws https://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-app-beta-beating-omc3/PRO/BetaBeatingOMC3-Control-3t.jnlp
    ```
    :material-arrow-right-bold: Disabling Java as it is too old and likely to be insecure. To reenable use jcontrol utility

!!! success
    ```bash
    /mcr/bin/jws https://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-app-beta-beating-omc3/PRO/BetaBeatingOMC3-Control-3t.jnlp
    ```

### Unspecific Error

!!! failure
    Any random error

If so, check that you can import `numpy` from the `OMC` production Python environment.
If this leads to the previously raised error, then the permissions are broken.
Either fix the permissions on `afs` or ask someone to do so for you.

*[TN]: Technical Network
*[LSA]: LHC Software Architecture
*[GPN]: General Purpose Network

[prod_bbgui]: https://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-app-beta-beating/PRO/BetaBeating-Control-3t.jnlp
[dev_bbgui]: https://bewww.cern.ch/ap/deployments-dev/applications/cern/lhc/lhc-app-beta-beating/PRO/BetaBeating-Control-3t.jnlp
[releases_bbgui]: https://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-app-beta-beating/

[prod_bbgui_omc3]: https://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-app-beta-beating-omc3/PRO/BetaBeatingOMC3-Control-3t.jnlp
[dev_bbgui_omc3]: https://bewww.cern.ch/ap/deployments-dev/applications/cern/lhc/lhc-app-beta-beating-omc3/PRO/BetaBeatingOMC3-Control-3t.jnlp
[releases_bbgui_omc3]: https://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-app-beta-beating-omc3/

[prod_mtgui]: https://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-multiturn/PRO/lhc-multiturn-lhc-multiturn.jnlp
[dev_mtgui]: https://bewww.cern.ch/ap/deployments-dev/applications/cern/lhc/lhc-multiturn/PRO/lhc-multiturn-lhc-multiturn.jnlp
[releases_mtgui]: https://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-multiturn/

[prod_kmodgui]: https://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-app-kmod/PRO/lhc-app-kmod-lhc-app-kmod.jnlp
[dev_kmodgui]: https://bewww.cern.ch/ap/deployments-dev/applications/cern/lhc/lhc-app-kmod/PRO/lhc-app-kmod-lhc-app-kmod.jnlp
[releases_kmodgui]: https://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-app-kmod/

[jws_confluence]: https://wikis.cern.ch/display/DVTLS/jws+-+a+replacement+for+javaws
[jws]: https://wikis.cern.ch/display/DVTLS/jws+-+a+replacement+for+javaws

[mounting_resources]: ../resources/shared_filesystems.md#mounting-tn-resources-on-gpn-and-other-machines
[connect_gpn]: ../resources/remote_access.md#accessing-cern-internal-websites
[sshuttle_method]: usage/remote.md#running-guis-locally
[jws_calls]: ../resources/links.md#jws-programs
