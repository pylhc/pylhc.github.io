# CERN Help and Contacts

On this page, you can find the contact information for various services and support related to accelerator operations, hardware, and software outside of the OMC-Team.
For privacy reasons, only their names are listed here, but you can find their contact details in the [CERN phonebook][phonebook]{target=_blank .cern_login}.
Most of them are also very active on [Mattermost][mattermost]{target=_blank .cern_login} and you can contact them there as well.

Depending on the urgency of your issue, you can also search the [Knowledge Base][knowledge_base]{target=_blank}, open a [ServiceNow ticket][service_tickets]{target=_blank}, contact the [helpdesk][helpdesk]{target=_blank} or reach out in one of the dedicated [Mattermost][mattermost]{target=_blank .cern_login} channels, which are also listed below.

Maybe also check the [Service Status Board][status_board]{target=_blank} to see if there are any ongoing issues with the service you are interested in.

## Services

This section lists general services that are not specific to a certain hardware or software component.

Normally, each service has a specific [ServiceNow form][service_tickets]{target=_blank}, that you should use to open a ticket,
but sometimes it is not obvious which one to use.
Remember to that you can always open a [general SNOW ticket][snow_general]{target=_blank .cern_login} for any issue,
which will be routed to the appropriate service - but this can take longer than opening a specific form.

### HTCondor

For questions/issues regarding LxBatch/HTCondor the following help is available:

- [HTCondor Documentation][cern_htcondor_docs]{target=_blank}
- [LXBatch SNOW ticket][snow_htcondor]{target=_blank .cern_login}
- [Mattermost: Batchers][mm_htcondor]{target=_blank .cern_login}

**Contact(s):**

- Ben Jones

### LxPlus/AFS/EOS

For questions/issues regarding the LxPlus environment in general or
the AFS and EOS file systems multiple contact options are available,
but as these commonly experience issues/updates, please first check the
[Status Board][status_board]{target=_blank} first.

In case you have issues with the file systems, you can also check the
[Services Portal][services]{target=_blank .cern_login} first, to
see if your account is correctly configured.
In particular, when running out of AFS quota, you might need to [adjust your settings][afs_settings]{target=_blank .cern_login} there.

- [AFS Settings][afs_settings]{target=_blank .cern_login}
- [LXPlus SNOW ticket][snow_lxplus]{target=_blank .cern_login}
- [Mattermost: lxplus][mm_lxplus]{target=_blank .cern_login}

**Contact(s):**

- Steve Traylen
- Vincent Brillault
- Jan Iven
- Ben Jones

## Hardware

### LHC

#### OP

If you are planning an MD session or you have operational questions regarding commissioning,
the first person to contact is the **EIC during your shift**.

That being said, **Matteo** has always been a close contact for optics related topics in OP,
and **Michi** is also very knowledgeable and involved in this area (see also [Software](#software)).

As OP is lead by **Jörg** he is of course also a good contact for general OP questions.

**Contact(s):**

- Matteo Solfaroli
- Michi Hostettler
- Jörg Wenninger

#### AC-Dipole

**Contact(s):**

- Nicolas Magnin

### SPS

#### General

**Contact(s):**

- Stephane Cettur Cave

#### RF

**Contact(s):**

- Giulia Papotti

#### Optics

**Contact(s):**

- Panos Zisopoulos

### BPMs (LHC, SPS)

In recent years, cooperation between the BI BPM teams and OMC has increased significantly,
as they can profit for our measurements and [statistical analysis of BPM data quality][bad_bpms],
and we can use their expertise for BPM related issues and shortcomings, improving the quality of measurements.

**Contact(s):**

- Manuel Gonzalez Berges
- Michal Krupa

## Software

!!! heart "A Special Thanks to Michi Hostettler"
    While not the official support for software, due to his experience,
    involvment in development and regular use of different tools,
    **Michi Hostettler** is incredibly knowledgable and
    can very often help with questions/issues regarding various
    software packages used in accelerator operations.
    If you run into an issue, it is likely he has already encountered it before,
    and most likely has a solution.

    That is to say, if you are reading this, **THANK YOU MICHI FOR ALL YOUR HELP** in the past,
    it has been invaluable!

     -- Joschua

### Acc-Py

As described in the sections on [our python environments][python_prod_env]  and [virtual environments][python_venvs],
we use the [Acc-Py][acc-py]{target=_blank} distribution as our main Python environment.
This distribution system is maintained by the Acc-Py team at CERN,
who can be contacted for questions regarding its usage, installation or development.

- [Mattermost: acc-py][mm_acc_py]

**Contact(s):**

- Ivan Sinkarenko
- Philip Elson

### Java

Questions regarding the Java infrastructure we are using, like deployment of applications,
the CBNG build system or the Acc-Java libraries our software depends on, can be directed to:

- [Mattermost: acc-java][mm_acc_java]

**Contact(s):**

- Felix Ehm

### NXCals

The NXCals team is always interested in feedback regarding the user experience and use-cases of NXCals,
at CERN in general, but also for each individual section - as they might have very different needs.

They regularly organize meetings to gather feedback and discuss new features,
so feel free to reach out to the contacts below to be added to the mailing list.

While not directly involved in the development of NXCals, Michi Hostettler is taking care of data collection
and organization for the LHC, which is stored using the NXCals framework and is therefore a good contact for
questions with regards to that topic.

- [Mattermost: NXCals][mm_nxcals]

**Contact(s):**

- Jakub Wozniak
- Piotr Sowinski
- Vito Baggiolini
- (Michi Hostettler)

### Acc-Models

- Riccardo de Maria

### MAD-X

- Riccardo de Maria

### MAD-NG

- Laurent Deniau
- Joshua Gray (python interface)
- Bernardo Abreu Figueiredo (Xsuite interface)

### Xsuite

- Giovanni Iadarola
- Szymon Lopaciuk

[acc-py]: https://confluence.cern.ch/pages/viewpage.action?spaceKey=ACCPY&title=Getting+started+with+Acc-Py
[cern_htcondor_docs]: https://batchdocs.web.cern.ch/index.html

[service_tickets]: https://cern.service-now.com/service-portal?id=browse_forms
[knowledge_base]: https://cern.service-now.com/service-portal?id=kb_category
[status_board]: https://cern.service-now.com/service-portal?id=service_status_board
[snow_general]: https://cern.service-now.com/service-portal?id=get_help
[helpdesk]: https://cern.service-now.com/service-portal?id=service_desk

[phonebook]: https://phonebook.cern.ch/

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

[python_prod_env]: ../packages/about.md#the-omc-production-environments
[python_venvs]: ../packages/development/howto_venv.md
[bad_bpms]: ../measurements/physics/bpm_filtering.md