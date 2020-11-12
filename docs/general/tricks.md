# Tricks

## Mounting TN resources on GN machines
To be able to run the GUI or CBNG seamlessly from computers which are not
in the technical network, it might be useful to mount `/user` and `/nfs`
via `sshfs` using the following recipe:

- create mountpoints and symbolic links (only once)
```
mkdir ~/mnt
mkdir ~/mnt/user
ln -s ~/mnt/user /user
mkdir ~/mnt/nfs
ln -s ~/mnt/nfs /nfs
```

- mount network resources (upon timeouts and restarts)
```
sshfs username@cs-ccr-dev3.cern.ch:/user/ ~/mnt/user
sshfs username@cs-ccr-dev3.cern.ch:/nfs/ ~/mnt/nfs
```

- if outside of GN, jump through lxplus:
```
sshfs username@cs-ccr-dev3.cern.ch:/user/ ~/mnt/user -o ssh_command='ssh -t username@lxplus.cern.ch ssh'
sshfs username@cs-ccr-dev3.cern.ch:/nfs/ ~/mnt/nfs -o ssh_command='ssh -t username@lxplus.cern.ch ssh'
```


And in case you need to unmount these:
```
sudo fusermount -u ~/mnt/user
sudo fusermount -u ~/mnt/nfs
```

## Teleworking related

### Accessing CERN-internal websites
Adapted from [here][codi_teleworking]:

```
ssh -D 8090 username@lxtunnel.cern.ch
```

opens a tunnel at port 8090 which can be accessed via browser through `127.0.0.1:8090`, (e.g. 
with the switchyomega extension 
[Chrome][plugin_chrome], 
 [Firefox][plugin_firefox]
 )


### Accessing Journal Papers etc.
Lots of journals and resources can be accessed via the CERN ezproxy by adding 
 ```
 https://ezproxy.cern.ch/login?url=
 ```
 in front of the url. See the [website][ezproxy_website] for a list.


### Running Graphical Software on lxplus or the TN (e.g. GUI, Eclipse)


[codi_teleworking]: https://codimd.web.cern.ch/vjC8BHbTS7etHwJve-K2Uw
[plugin_firefox]: https://addons.mozilla.org/en-US/firefox/addon/switchyomega/
[plugin_chrome]: https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif
[ezproxy_website]: https://login.ezproxy.cern.ch/