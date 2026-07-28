# CERN Help and Contacts

Find on this page information for various services and support related to accelerator operations, hardware, and software outside of the OMC-Team.

!!! danger "No Identifying Information"
    For CERN privacy policy reasons, no names can be listed here.
    A complete list of relevant contacts can be found in the instructions of the OMC logbook, and will display automatically on opening.
    Note that logbook access requires a login.

    The OMC logbook can be found at the following links:

    - [Insider logbook][omc_logbook_insider]{target=_blank .cern_login .cern_internal} (requires to be in the GPN and can make edits),
    - [Outsider logbook][omc_logbook_outsider]{target=_blank .cern_login} (read only).

Depending on the urgency of your issue, you can also search the [Knowledge Base][knowledge_base]{target=_blank}, open a [ServiceNow ticket][service_tickets]{target=_blank}, contact the [helpdesk][helpdesk]{target=_blank} or reach out in one of the dedicated [Mattermost][mattermost]{target=_blank .cern_login} channels, which are also listed below.

## Services

This section lists general services that are not specific to a certain hardware or software component.

Normally, each service has a specific [ServiceNow form][service_tickets]{target=_blank}, that you should use to open a ticket, but sometimes it is not obvious which one to use.
Remember to that you can always open a [general SNOW ticket][snow_general] for any issue, which will be routed to the appropriate service, but this can take longer than opening a specific form.

### HTCondor

For questions/issues regarding LxBatch/HTCondor the following help is available:

- [HTCondor Documentation][cern_htcondor_docs]{target=_blank}
- [LXBatch SNOW ticket][snow_htcondor]{target=_blank .cern_login}
- [Mattermost: Batchers][mm_htcondor]{target=_blank .cern_login}

**Contact(s):** See logbook instruction.

### LxPlus/AFS/EOS

For questions/issues regarding the LxPlus environment in general or the AFS and EOS file systems multiple contact options are available.
As these commonly experience issues/updates, please first check the [Status Board][status_board]{target=_blank} first.

In case you have issues with the file systems, you can also check the [Services Portal][services]{target=_blank .cern_login} first, to see if your account is correctly configured.
In particular, when running out of AFS quota, you might need to [adjust your settings][afs_settings]{target=_blank .cern_login} there.

- [AFS Settings][afs_settings]{target=_blank .cern_login}
- [LXPlus SNOW ticket][snow_lxplus]{target=_blank .cern_login}
- [Mattermost: lxplus][mm_lxplus]{target=_blank .cern_login}
- **Contact(s):** See logbook instruction.

## LHC

When planning an MD session or you have operational questions regarding commissioning, the first person to contact is the *EIC during your shift*.

- **General Contact(s):** See logbook instruction.
- **AC-Dipole Contact(s):** See logbook instruction.

## SPS

- **General Contact(s):** See logbook instruction.
- **RF Contact(s):** See logbook instruction.
- **Optics Contact(s):** See logbook instruction.

## BPMs (LHC, SPS)

In recent years, cooperation between the BI BPM teams and OMC has increased significantly, as they can profit for our measurements and [statistical analysis of BPM data quality][bad_bpms].
It has helped sharing expertise for BPM related issues and shortcomings, improving the quality of measurements.

- **Contact(s):** See logbook instruction.

## Software

### Acc-Py

As described in the sections on [our python environments][python_prod_env]  and [virtual environments][python_venvs], we use the [Acc-Py][acc-py]{target=_blank .cern_internal} distribution as basis for our production Python environments.
This distribution system is maintained by the Acc-Py team at CERN, who can be contacted for questions regarding its usage, installation or development.

- [Mattermost: acc-py][mm_acc_py]
- **Contact(s):** See logbook instruction.

### Java

Questions regarding the Java infrastructure we are using, such as the deployment of applications, the CBNG build system or the Acc-Java libraries our software depends on, can be directed to:

- [Mattermost: acc-java][mm_acc_java]
- **Contact(s):** See logbook instruction.

### NXCals

The NXCals team is always interested in feedback regarding the user experience and use-cases of NXCals, at CERN in general but also for each individual sections.
They regularly organise meetings to gather feedback and discuss new features, so feel free to reach out to the contacts below to be added to their mailing list.

- [Mattermost: NXCals][mm_nxcals]
- **Contact(s):** See logbook instruction.

### Acc-Models

- [Gitlab][acc_models_gitlab]{target=_blank} / [Issues][acc_models_gitlab_issues]{target=_blank}
- **Contact(s):** See logbook instruction.

### MAD-X

- [Website][madx_web]{target=_blank} / [GitHub][madx_github]{target=_blank} / [Issues][madx_github_issues]{target=_blank}
- **Contact(s):** See logbook instruction.

### MAD-NG

- [GitHub][madng_github]{target=_blank} / [Issues][madng_github_issues]{target=_blank}
- **Contact(s):** See logbook instruction.

### Xsuite

- [GitHub][xsuite_github]{target=_blank} / [Issues][xsuite_github_issues]{target=_blank}
- **Contact(s):** See logbook instruction.

*[GPN]: General Purpose Network, the main CERN network
*[CBNG]: Common Build Next Generation

[omc_logbook_insider]: https://logbook.cern.ch/elogbook-server#/logbook?logbookId=1081
[omc_logbook_outsider]:https://be-op-logbook.web.cern.ch/elogbook-server/#/logbook?logbookId=1081

[acc-py]: https://confluence.cern.ch/pages/viewpage.action?spaceKey=ACCPY&title=Getting+started+with+Acc-Py
[cern_htcondor_docs]: https://batchdocs.web.cern.ch/index.html

[service_tickets]: https://cern.service-now.com/service-portal?id=browse_forms
[knowledge_base]: https://cern.service-now.com/service-portal?id=kb_category
[status_board]: https://cern.service-now.com/service-portal?id=service_status_board
[snow_general]: https://cern.service-now.com/service-portal?id=get_help
[helpdesk]: https://cern.service-now.com/service-portal?id=service_desk

[services]: https://resources.web.cern.ch/resources/Manage/ListServices.aspx
[afs_settings]: https://resources.web.cern.ch/resources/Manage/AFS/Settings.aspx

[mattermost]: https://mattermost.web.cern.ch/

[mm_acc_java]: https://mattermost.web.cern.ch/acc-java/channels/town-square
[mm_nxcals]: https://mattermost.web.cern.ch/nxcals/channels/nxcals-community
[mm_acc_py]: https://mattermost.web.cern.ch/acc-py/channels/town-square

[snow_htcondor]: https://cern.service-now.com/service-portal?id=functional_element&name=LXBATCH
[mm_htcondor]: https://mattermost.web.cern.ch/it-dep/channels/batchers

[snow_lxplus]: https://cern.service-now.com/service-portal?id=sc_cat_item&name=request&fe=LXPLUS
[mm_lxplus]: https://mattermost.web.cern.ch/it-dep/channels/lxplus

[madx_web]: https://madx.web.cern.ch/
[madx_github]: https://github.com/MethodicalAcceleratorDesign/MAD-X
[madx_github_issues]: https://github.com/MethodicalAcceleratorDesign/MAD-X/issues

[madng_github]: https://github.com/MethodicalAcceleratorDesign/MAD-NG
[madng_github_issues]: https://github.com/MethodicalAcceleratorDesign/MAD-NG/issues

[xsuite_github]: https://github.com/xsuite/xsuite
[xsuite_github_issues]: https://github.com/xsuite/xsuite/issues

[acc_models_gitlab_issues]: https://gitlab.cern.ch/groups/acc-models/-/issues/
[acc_models_gitlab]: https://gitlab.cern.ch/acc-models

[python_prod_env]: ../packages/about.md#the-omc-production-environments
[python_venvs]: ../packages/development/howto_venv.md
[bad_bpms]: ../measurements/physics/bpm_filtering.md
