# How to setup for OMC Members useful things

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
