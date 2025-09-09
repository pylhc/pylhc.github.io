# Shared Filesystems

All things related to `afs`, `eos` etc.

## Setup AFS on WSL2

Follow [this gist][gist_wsl] to set-up AFS with Kerberos on your WSL.

## Mounting EOS and CERNBox via FUSE on an unmanged CentOS machine

The CERN Service Portal has [a guide for that][eos_csp].

## Mounting TN Resources on GPN and Other Machines

To be able to run the GUI or CBNG seamlessly from computers which are not in the technical network, it might be useful to mount `/user`, `/nfs` and `/eos` via `sshfs` using the following recipe:

### Create mountpoints and symbolic links (only once)

```bash
mkdir -p ~/mnt/user && ln -nfs ~/mnt/user /user
mkdir ~/mnt/nfs && ln -nfs ~/mnt/nfs /nfs
mkdir ~/mnt/eos && ln -nfs ~/mnt/eos /eos
```

### Mount network resources (repeat after timeouts and restarts)

```bash
sshfs -o follow_symlinks username@cs-ccr-dev3.cern.ch:/user/ ~/mnt/user
sshfs -o follow_symlinks username@cs-ccr-dev3.cern.ch:/nfs/ ~/mnt/nfs
sshfs -o follow_symlinks username@lxplus.cern.ch:/eos/ ~/mnt/eos
```

??? info "Follow Symlinks"
    When mounting to a different location than `/nfs` or `/user` **locally**, one has to set the `follow_symlinks` option
    so that symlinks e.g. pointing to a folder somewhere in `/nfs/` (which locally does not exist) are followed correctly, i.e. to the path on the remote machine.
    This is not needed when mounting to `/nfs` or `/user` as the symlinks would point to these locations anyway,
    but that comes with its own problems, as the mount needs to be done as **root** in these cases and might not be valid for other users.

### If outside of the GPN, jump through `lxplus` to mount `dev3`-folders

```bash
sshfs username@cs-ccr-dev3.cern.ch:/user/ ~/mnt/user -o ssh_command='ssh -t username@lxplus.cern.ch ssh'
sshfs username@cs-ccr-dev3.cern.ch:/nfs/ ~/mnt/nfs -o ssh_command='ssh -t username@lxplus.cern.ch ssh'
```

!!! info
    To avoid getting asked for your password all the time, you should have your `ssh` properly configured with Kerberos.

??? tip "In case you need to unmount these"

    ```
    sudo fusermount -u ~/mnt/user
    sudo fusermount -u ~/mnt/nfs
    sudo fusermount -u ~/mnt/eos
    ```

*[AFS]: Andrew File System
*[WSL]: Windows Subsytem Linux

[eos_csp]: https://cern.service-now.com/service-portal-old/article.do?n=KB0003846
[gist_wsl]: https://gist.github.com/JoschD/194b3f6c6fcc408684a481fd4a2ff4e5
