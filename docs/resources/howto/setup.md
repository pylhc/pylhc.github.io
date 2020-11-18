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
3. If outside of the GPN, jump through `lxplus` to mount `dev3`-folders:
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

To use the [KMod GUI][kmod_gui] or the `KnobPanel` in the [Beta-Beat GUI][bb_gui], it is required to be on the TN, as they need to connect to LSA.
If you are in the GPN but not on the TN, you will need to tunnel through some machines.

First, install the program [sshuttle][sshuttle]{target=_blank}, which should be available in your package manager.
Then, run this command in a terminal and leave it open:
```bash
sshuttle -vr <username>@cs-ccr-dev2 172.18.0.0/16
```

All traffic related to the technical network will be redirected through the `cs-ccr-dev2` machine which has access to both networks. In case it isn't available, the other `cs-ccr-devX` machines can be used. 


## Configure gitlab CI to automatically pull into afs

If you are programming locally, but also want to have a copy on AFS, either because your colleges are not comfortable with gitlab or you need the code for other scripts that you are running on lxplus or similar, here is the guide for you:

!!! warning "Security Risk"
    Creating a new account is done, so you do not have to add the password of your main account to your gitlab repository, which is a security risk.
    Admittedly, if everything is done correctly, it is a low one, but just in case something goes wrong or leaks, you can just delete this account.
    Also, you can give this account only the necessary rights to write to AFS in the first place and do not risk that anyone can access other sensible information.

1. ??? nodeco "Create a new service account via the [CERN account management][new_account] of length 8."   
    > You need at least 8 characters to mask that name in gitlab (if you want to do so), but on the other hand, there is a warning, that AFS cannot handle names longer than 8.
    > So exactly 8 seems to be the sweetspot.
    > If you do not care about masking the name (it is not as important as masking the password, see below) you can go shorter.

1. ??? nodeco "Set a password of length &GreaterEqual; 8 containing only `[a-zA-Z0-9+/@:]`"
    > We want to hide the password later in gitlab, and this is only possible if its >= 8 characters long and only contains Base64 characters as well as `@:`.
    > You can go as long as you want. Better make this 15 characters long at least.


2. [Activate the AFS service][afs_services] for the newly created account.
3. Create git
4. Pull into afs
5. give account access rights
6. add yml

Done!<br>
Whenever you are pushing now any commits to master, the CI will automatically pull the latest commit into the AFS directory.


*[TN]: Technical Network
*[GPN]: General Purpose Network, the main CERN network
*[CBNG]: Common Build Next Generation
*[LSA]: LHC Software Architecture
*[AFS]: Andrew File System

[sshuttle]: https://sshuttle.readthedocs.io/en/stable/

[kmod_gui]: ../../guis/kmod/gui.md
[bb_gui]: ../../guis/betabeat/gui.md



[new_account]: https://account.cern.ch/account/Management/NewAccount.aspx
[afs_services]: https://resources.web.cern.ch/resources/Manage/AFS/Default.aspx
