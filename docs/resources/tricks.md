# Tricks

## Mounting TN resources on GN machines

To be able to run the GUI or CBNG seamlessly from computers which are not in the technical network, it might be useful to mount `/user`, `/nfs` and `/eos` via `sshfs` using the following recipe:

1. Create mountpoints and symbolic links (only once)
```bash
mkdir -p ~/mnt/user && ln -s ~/mnt/user /user
mkdir ~/mnt/nfs && ln -s ~/mnt/nfs /nfs
mkdir ~/mnt/eos && ln -s ~/mnt/eos /eos
```
2. Mount network resources (upon timeouts and restarts)
```bash
sshfs username@cs-ccr-dev3.cern.ch:/user/ ~/mnt/user
sshfs username@cs-ccr-dev3.cern.ch:/nfs/ ~/mnt/nfs
sshfs username@lxplus.cern.ch:/eos/ ~/mnt/eos
```
3. If outside of GN, jump through lxplus to mount dev3-folders:
```bash
sshfs username@cs-ccr-dev3.cern.ch:/user/ ~/mnt/user -o ssh_command='ssh -t username@lxplus.cern.ch ssh'
sshfs username@cs-ccr-dev3.cern.ch:/nfs/ ~/mnt/nfs -o ssh_command='ssh -t username@lxplus.cern.ch ssh'
```

??? info "In case you need to unmount these"
    ```
    sudo fusermount -u ~/mnt/user
    sudo fusermount -u ~/mnt/nfs
    sudo fusermount -u ~/mnt/eos
    ```

!!! tip
    To avoid getting asked for your password all the time, you should have your `ssh` properly configured with kerberos.

## Teleworking related

### Accessing CERN-internal websites

Adapted from [here][codi_teleworking]:
```bash
ssh -D 8090 username@lxtunnel.cern.ch
```

The above command opens a tunnel at port `8090` which can be accessed via browser through `localhost:8090`.

### Accessing Journal Papers etc.

Lots of journals and resources can be accessed via the `CERN ezproxy` by prepending the viewing url with `https://ezproxy.cern.ch/login?url=`.
See this [website][ezproxy_website]{target=_blank} for a list.

### Running Graphical Software on lxplus or the TN (e.g. GUI, Eclipse)

The  most intuitive way to run graphical software on computers within the CERN network from your own PC would be connecting to them by `ssh -X` and control their GUI via the forwarded X-Server.
While this usually works fine from within CERN itself, where connection speeds are high, depending on the ping and bandwidth of your local connection this can be a frustrating experience.

Using RDP is a way to avoid this, as with this protocol the graphical interface is rendered locally and only the picture of the screen is transmitted.
Sadly, the machine you want to work on (_dev-server_, _optics-server_) will not have this installed.
There is another way: **cernts.cern.ch** allows you to connect to a windows machine via `Remote Desktop Connection` from Windows or e.g. `Remmina` from Linux.
Once logged in with your CERN-credentials (Add `CERN.CH\` in front of your username to specify your domain) you can run:

!!! note ""
    `Start` &rarr; `X-Win32 18` &rarr; `Lxplus (Default)`

which opens a putty-terminal connected to `lxplus` and starts a `X-Server` in the background. 

<figure>
  <img src="../../assets/images/tricks/putty_and_xserver_cernts.png" width=90%>
  <figcaption>Putty and XServer on cernts</figcaption>
</figure>

Executing any graphical software from this terminal will ask for connection authorization, which you need to approve.

<figure>
  <img src="../../assets/images/tricks/allow_xserver_connection.png" width=60%>
  <figcaption>Approve connection to XServer</figcaption>
</figure>

This way you can run any graphical application smoothly.
If your internet connection fails, you should still be able to resume your current session, at least for a while.

!!! help "Creating Shortcut to Other Machines"
    In order to connect to another machine directly (instead of hopping through `lxplus`) you can create a shortcut:
    
    1. open `X-Win32 18 Configuration`
    2. `Manual...` &rarr; `More...` &rarr; `command`
    3. Target: `"C:\Program Files (x86)\PuTTY_CERN\putty.exe" -ssh -X machine_at_cern.cern.ch`
    
    Fill out the other fields to your liking.
    You can even create a shortcut on the screen, from the right-click menu on the newly created connection.

!!! example "Alternative way to create configuration"

    1. Create a file with the ending `.xw32`, e.g on the desktop
    2. Fill it with
    ```xml
    <Session>
    <HideOnStart>false</HideOnStart>
    <Module>command</Module>
    <Name>name_you_want_to_give</Name>
    <NewInstance>never</NewInstance>
    <Settings>
        <Target>"C:\Program Files (x86)\PuTTY_CERN\putty.exe" -ssh -X machine_at_cern.cern.ch</Target>
    </Settings>
    <ShowStatus>false</ShowStatus>
    <WindowMode>multiple</WindowMode>
    </Session>
    ```
    3. Click on file


*[RDP]: Remote Desktop Protocol

[codi_teleworking]: https://codimd.web.cern.ch/vjC8BHbTS7etHwJve-K2Uw
[plugin_firefox]: https://addons.mozilla.org/en-US/firefox/addon/switchyomega/
[plugin_chrome]: https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif
[ezproxy_website]: https://login.ezproxy.cern.ch/