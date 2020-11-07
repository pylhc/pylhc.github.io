# Running the Kmod GUI

## Running Locally

The GUI requires to be on the Technical Network, to which the CERN Control Center is connected.
If you are in the GPN but not on the Technical Network, you will need to VPN through some machines to be able to run `KMOD`, as it needs to connect to LSA.

First, install the program [sshuttle][sshuttle]{target=_blank}, which should be available in your package manager.
Then, run this command in a terminal and leave it open:
```bash
sshuttle -vr <username>@cs-ccr-dev2 172.18.0.0/16
```

All traffic related to the technical network will be redirected through the `cs-ccr-dev2` machine which has access to both networks. In case it isn't available, the other `cs-ccr-devX` machines can be used. 

## Loading a model

You can load the model created from the [Beta-Beat GUI](../betabeat/gui.md) or [Multiturn GUI](../multiturn/gui.md) for each beam by pressing the `load model` button.
Select the desired model directory in the popup dialog and confirm by pressing the `open` button.
If everything worked fine and the specified folder contains the needed `twiss_elements` file, the GUI will display the model's name.

You can choose another model directory by pressing on the `update model` button which appears if a model is already selected.
The model data is used for preset values in the GUI and the orbit-offset script needs the model for its calculations.

!!! todo
    Include up-to-date screenshots of model loading, see https://twiki.cern.ch/twiki/bin/view/BEABP/BasicOptions

??? tip "Setting the Beta-Beat.src directory"

    To change the setting of the used `Beta-Beat.src` directory, navigate to `File` -> `Set Beta-Beat dir` and select the location where the `Beta-Beat.src` directory to be used is located.
    The Kmod GUI will automatically take the proper Python scripts from this directory.
    This is automatically reset to the standard directory `/afs/cern.ch/eng/sl/lintrack/Beta-Beat.src/`.
    
    The GUI will check if the `Beta-Beat.src` directory contains the `ProgramVersions.properties` file, which is needed for calling an external python script.
    You can change the standard directory by creating a `user.properties` file in the project folder.
    The kmod GUI will automatically read this file and change the Beta-Beat.src directory to this new value.
    This file must contain `BetaBeatDir=[newBBdir]` (replace the placeholder correctly).

*[LSA]: LHC Software Architecture
*[GPN]: General Purpose Network

[sshuttle]: https://github.com/sshuttle/sshuttle
[archive]: http://abwww.cern.ch/ap/
[prod_gui]: http://abwww.cern.ch/ap/pro/lhc/lhc-app-beta-beating/BetaBeating-Control-3t.jnlp
[dev_gui]: http://abwww.cern.ch/ap/next/lhc/lhc-app-beta-beating/BetaBeating-Control-3t.jnlp
[releases]: https://abwww.cern.ch/ap/dist/lhc/lhc-app-beta-beating/
[jws_confluence]: https://wikis.cern.ch/display/DVTLS/jws+-+a+replacement+for+javaws
[jws]: https://wikis.cern.ch/display/DVTLS/jws+-+a+replacement+for+javaws
