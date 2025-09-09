# Computing Resources for ABP and OMC Members

This page combines information and links to computing resources for OMC members.

## The Dev & Optics Servers

A few special servers are available OMC members.
Access should be granted to your account by default when added to the OMC `e-group`.

The `dev` servers are powerful machines used to run applications when in the `CCC`, and can be ssh'd into at the `cs-ccr-dev[1-4].cern.ch` addresses.

The `optics` servers are high-end machines on which the OMC GUIs run their computations when in the `CCC`.
When not in use during shifts they are available to OMC members to run computations on.
The `optics` machines are available at the `cs-ccr-optics[1-2].cern.ch` addresses.

The servers are hooked on to the Technical Network and can only be ssh into from `lxplus` nodes.

??? tip "Convenient SSH Configuration Tricks"
    The following `ssh` config elements provide a convenient setup for users to access these machines.
    Remember to replace `your_username` below with your CERN username.
    ```bash
    Host cern
        User your_username  # replace with your lxplus username
        Hostname lxplus.cern.ch
        ForwardX11Trusted yes
        StrictHostKeyChecking no

    Host technet1
        User your_username  # replace with your lxplus username
        Hostname cs-ccr-dev1.cern.ch
        ProxyCommand ssh -X cern -W %h:%p 2> /dev/null
        ForwardX11Trusted yes
        StrictHostKeyChecking no

    Host optics1
        User your_username  # replace with your lxplus username
        Hostname cs-ccr-optics1.cern.ch
        ProxyCommand ssh -X technet1 -W %h:%p 2> /dev/null
    ```
    With this configuration, one can use the command `ssh cern` to log into `lxplus` (your password may be asked).
    As a proxy command is set up, one can directly connect from local into, say, the `optics1` machine with `ssh optics1`.

## HTCondor

CERN provides a batch service based on [HTCondor][htcondor]{target=_blank}.
Computing jobs that run on individual nodes with up to 32 CPU cores per node can be submitted to the CERN batch service.
A good documentation can be found on the [batch docs website][cern_htcondor_docs]{target=_blank}.
The OMC team maintains a python package, [pylhc_submitter](../packages/pylhcsubmitter/about.md), that can be used to submit jobs to the `HTCondor` batch service.

!!! info "Monitoring"
    Monitoring tools are deployed through [Graphana][graphana]{target=_blank} that allow to get an overview of the batch system and the jobs running on it:

    - The [general dashboard][graphana_htcondor]{target=_blank .cern_login} gives access to various pages displaying information about various parts of the batch system (log in with CERN SSO on this page).
    - The [following link][user_batch]{target=_blank .cern_login} is an overview of the batch jobs for a given user (selectable in a dropdown menu at the top left).

## ABP Computing Resources

Various resources are accessible to ABP members, from special `e-groups` with higher HTCondor priority to dedicated high-end GPU equipped machines on which to run your jobs.

Information on ABP-specific resources can be found on the [dedicated website][abpcomputing]{target=_blank}, tab `Computing resources`.

## CERN OpenStack Machines

CERN provides an Infrastructure-as-a-Service as part of their private cloud, which any member can access.
Through [OpenStack][openstack]{target=_blank} CERN allows users to create virtual machines on their computing infrastructure.
Using self-service portals one can rapidly request virtual machines for production, testing and development purposes, accessible through an ssh connection.

The machines can be of different capacities and run a variety of Windows or Linux operating systems.
For details, see both the [CERN OpenStack][cern_openstack]{target=_blank .cern_login} website and its [documentation][cern_openstack_doc]{target=_blank} pages.

*[ABP]: Accelerator and Beam Physics
*[CCC]: CERN Control Center

[abpcomputing]: https://abpcomputing.web.cern.ch
[cern_htcondor_docs]: https://batchdocs.web.cern.ch/index.html
[cern_openstack]: https://openstack.cern.ch/
[cern_openstack_doc]: https://clouddocs.web.cern.ch/index.html
[graphana]: https://grafana.com/
[graphana_htcondor]: https://monit-grafana.cern.ch
[htcondor]: https://htcondor.org/
[openstack]: https://www.openstack.org/
[user_batch]: https://monit-grafana.cern.ch/d/000000869/user-batch-jobs?from=now-1h&orgId=5&refresh=5m&to=now&var-cluster=cernprod&var-datasource=fifemon-graphite
