# The OMC GUIs

!!! note "About this"
    Include a foreword about the GUIs, potentially a list doing dispatch like the betabeat one does with its panels.

The OMC team develops several GUIs, each for a defined use:

- [The Beta-Beat GUI](betabeat/gui.md) to perform analysis of measurement files and compute corrections.
- [The Kmod GUI](kmod/gui.md) to perform K-modulation in different ways and extract the configuration and results data.
- [The Multiturn GUI](multiturn/gui.md) to ???.

## Running the GUIs

The GUIs can be started from your development environment or via deployed `.jnlp` from the archives:

=== "Beta-Beat"

    - Latest [Beta-Beating production version][prod_bbgui]{target=_blank}.
    - Latest [Beta-Beating development version][dev_bbgui]{target=_blank}.
    - Complete [list of releases][releases_bbgui]{target=_blank}.
    
=== "Beta-Beat-OMC3"

    - Latest [Beta-Beating production version][prod_bbgui_omc3]{target=_blank}.
    - Latest [Beta-Beating development version][dev_bbgui_omc3]{target=_blank}.
    - Complete [list of releases][releases_bbgui_omc3]{target=_blank}.
    
=== "Kmod"

    - Latest [Kmod production version][prod_kmodgui]{target=_blank}.
    - Latest [Kmod development version][dev_kmodgui]{target=_blank}.
    - Complete [list of releases][releases_kmodgui]{target=_blank}.
    
=== "Multiturn"

    - Latest [Multiturn production version][prod_mtgui]{target=_blank}.
    - Latest [Multiturn development version][dev_mtgui]{target=_blank}.
    - Complete [list of releases][releases_mtgui]{target=_blank}.


!!! warning
    Please note that these site are currently available only to devices connected to the CERN network ([workaround][connect_gpn]).

Open the `.jnlp` executable inside a browser, or [call it with `jws` from the command line][jws_calls]:

!!! info "Compatibility Issues"
    Since `javaws` (java web start) makes trouble due to intenal security mechanisms, a replacement named `jws` was developed and has to be used to run the `jlnp` file.
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

#### Problems with execution due to disabled Java

If you encounter a complaint about `Java` being too old, try using `/mcr/bin/jws`.

!!! failure
    ```bash
    javaws https://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-app-beta-beating/PRO/BetaBeating-Control-3t.jnlp
    ```
    :material-arrow-right-bold: Disabling Java as it is too old and likely to be insecure. To reenable use jcontrol utility

!!! success
    ```bash
    /mcr/bin/jws https://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-app-beta-beating/PRO/BetaBeating-Control-3t.jnlp
    ```

#### Unspecific Error

!!! failure
    Any random error

If so, check that you can import `numpy` from the `omc-anaconda-python`.
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

[mounting_resources]: ../../resources/howto/setup/#mounting-tn-resources-on-gn-machines
[connect_gpn]: ../../resources/howto/teleworking/#accessing-cern-internal-websites
[sshuttle_method]: ../../resources/howto/setup/#running-guis-locally
[jws_calls]: ../../resources/links/#jws-programs
