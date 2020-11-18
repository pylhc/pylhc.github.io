# Useful Setup How-To's

## Mounting TN resources on GPN and other machines

To be able to run the GUI or CBNG seamlessly from computers which are not in the technical network, it might be useful to mount `/user`, `/nfs` and `/eos` via `sshfs` using the following recipe:

1. Create mountpoints and symbolic links (only once)
```bash
mkdir -p ~/mnt/user && ln -nfs ~/mnt/user /user
mkdir ~/mnt/nfs && ln -nfs ~/mnt/nfs /nfs
mkdir ~/mnt/eos && ln -nfs ~/mnt/eos /eos
```
2. Mount network resources (repeat after timeouts and restarts)
```bash
sshfs username@cs-ccr-dev3.cern.ch:/user/ ~/mnt/user
sshfs username@cs-ccr-dev3.cern.ch:/nfs/ ~/mnt/nfs
sshfs username@lxplus.cern.ch:/eos/ ~/mnt/eos
```
3. If outside of GPN, jump through `lxplus` to mount `dev3`-folders:
```bash
sshfs username@cs-ccr-dev3.cern.ch:/user/ ~/mnt/user -o ssh_command='ssh -t username@lxplus.cern.ch ssh'
sshfs username@cs-ccr-dev3.cern.ch:/nfs/ ~/mnt/nfs -o ssh_command='ssh -t username@lxplus.cern.ch ssh'
```

!!! info ""
    To avoid getting asked for your password all the time, you should have your `ssh` properly configured with kerberos.

??? tip "In case you need to unmount these"
    ```
    sudo fusermount -u ~/mnt/user
    sudo fusermount -u ~/mnt/nfs
    sudo fusermount -u ~/mnt/eos
    ```


## Running GUIs Locally

To use the [KMod GUI][kmod_gui] or the `KnobPanel` in the [Beta-Beat-Gui][bb_gui], it is required to be on the TN, as they need to connect to LSA.
If you are in the GPN but not on the TN, you will need to tunnel through some machines to be able to, as it needs to connect to LSA.

First, install the program [sshuttle][sshuttle]{target=_blank}, which should be available in your package manager.
Then, run this command in a terminal and leave it open:
```bash
sshuttle -vr <username>@cs-ccr-dev2 172.18.0.0/16
```

All traffic related to the technical network will be redirected through the `cs-ccr-dev2` machine which has access to both networks. In case it isn't available, the other `cs-ccr-devX` machines can be used. 


*[TN]: Technical Network
*[GPN]: General Purpose Network, the main CERN network
*[CBNG]: Common Build Next Generation
*[LSA]: LHC Software Architecture

[kmod_gui]: ../../../guis/kmod/gui/
[bb_gui]: ../../../guis/betabeat/gui/

