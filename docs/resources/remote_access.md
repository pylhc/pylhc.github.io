# Remote Access Things

How to get access to things, that you have no problem accessing from the CERN-Network, the GPN.

## Accessing CERN-internal websites

Adapted from the [teleworking tricks from IT][codi_teleworking]{target=_blank}, you can create a web proxy:

```bash
ssh -D 8090 username@lxtunnel.cern.ch
```

The above command opens a tunnel at port `8090` which can be accessed via browser through `localhost:8090`.

## Accessing Journal Papers etc.

Lots of journals and resources can be accessed via the `CERN ezproxy` by prepending the viewing url with `https://ezproxy.cern.ch/login?url=`.
See this [website][ezproxy_website]{target=_blank} for a list.

*[RDP]: Remote Desktop Protocol
*[GPN]: General Purpose Network, the main CERN network

[codi_teleworking]: https://codimd.web.cern.ch/vjC8BHbTS7etHwJve-K2Uw
[plugin_firefox]: https://addons.mozilla.org/en-US/firefox/addon/switchyomega/
[plugin_chrome]: https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif
[ezproxy_website]: https://login.ezproxy.cern.ch/
