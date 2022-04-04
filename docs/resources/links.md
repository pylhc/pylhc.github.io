# Links to Various Useful Resources

???+ info "Hyperlinks Legend"

    * Publicly Accessible Page
    {: style="color:var(--md-typeset-a-color);"}
    * Webpage needs CERN login
    {: .cern_login}
    * Only accessible from the CERN Network
    {: .cern_internal}

## OMC

* [OMC Mattermost][omc_mattermost]{target=_blank .cern_login}
* [Meetings (OMC Team Indico)][omc_indico]{target=_blank}
* [Rogelio's Website][roro_website]{target=_blank}
* [OMC Logos][omc_logos]{target=_blank}

### GUI Links

=== "Beta-Beat"

    * [Beta-Beat Gitlab][betabeat_gui_gitlab]{target=_blank .cern_login}
    * [Jira Bugtracker][jira_bugtracker]{target=_blank .cern_login}
    * [Artifactory][betabeat_artifactory]{target=_blank .cern_internal}

=== "Kmod"

    * [Kmod Gitlab][kmod_gui_gitlab]{target=_blank .cern_login}
    * [Artifactory][kmod_artifactory]{target=_blank .cern_internal}

=== "Multiturn"

    * [Multiturn Gitlab][multiturn_gitlab]{target=_blank .cern_login}
    * [Artifactory][multiturn_artifactory]{target=_blank .cern_internal}

### JWS Programs

!!! warning ""
    All of these are <span class="cern_internal"> only accessible from CERN Network </span>.

=== "Beta-Beat"

    _PRO_
    ```bash
    jws https://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-app-beta-beating/PRO/BetaBeating-Control-3t.jnlp
    ```

    _DEV_
    ```bash
    jws https://bewww.cern.ch/ap/deployments-dev/applications/cern/lhc/lhc-app-beta-beating/PRO/BetaBeating-Control-3t.jnlp
    ```
    
=== "Beta-Beat-OMC3"

    _PRO_
    ```bash
    jws https://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-app-beta-beating-omc3/PRO/BetaBeatingOMC3-Control-3t.jnlp
    ```

    _DEV_
    ```bash
    jws https://bewww.cern.ch/ap/deployments-dev/applications/cern/lhc/lhc-app-beta-beating-omc3/PRO/BetaBeatingOMC3-Control-3t.jnlp
    ```

=== "Kmod"

    ```bash
    jws https://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-app-kmod/PRO/lhc-app-kmod-lhc-app-kmod.jnlp
    ```

=== "Multiturn"

    ```bash
    jws https://bewww.cern.ch/ap/deployments/applications/cern/lhc/lhc-multiturn/PRO/lhc-multiturn-lhc-multiturn.jnlp
    ```

=== "LSA-App-Suite"

    ```bash
    jws http://bewww.cern.ch/ap/deployments/applications/cern/lsa/lsa-app-suite/PRO/lsa-app-suite-lhc.jnlpx
    ```

    _LHC Panel open_
    ```bash
    jws 'http://bewww.cern.ch/ap/deployments/applications/cern/lsa/lsa-app-suite/PRO/lsa-app-suite-lhc.jnlpx?accelerator=LHC&lsa.server=lhc&lsa.contextfamily=BP&arg0=lsa-app-settings-management'
    ```

=== "Timber"

    ```bash
    jws http://bewww.cern.ch/ap/deployments/applications/cern/accsoft/cals/accsoft-cals-extr-app/PRO/timber.jnlpx
    ```

## Computer Setup at CERN

* [Computing Accounts Management][accounts_cern]{target=_blank .cern_login}
* [CERN Resources Portal][services_cern]{target=_blank .cern_login}
* [AFS and Kerberos (for Ubuntu)][afs_kerberos_ubuntu]{target=_blank}
* [AFS and Kerberos (for WSL)][afs_kerberos_wsl]{target=_blank}
* [Using Kerberos for SSH][kerberos_ssh]{target=_blank}

### Teleworking

* [CodiMD CERN - Teleworking Tips & Tricks][codimd]{target=_blank}
* [Cern Computing Blog - Useful tools for teleworking][cern_computing_blog]{target=_blank  .cern_login}
* [Remote Desktop Service][remote_desktop_service]{target=_blank .cern_login} (or with application, connect to **cernts.cern.ch**)

### Computing setup for Members

* [LHC Data Sources][lhc_data_sources]{target=_blank}
* [HTCondor Batch Docs][batch_docs]{target=_blank}
* [Setup HTCondor for local use][htcondor_local]{target=_blank}
* [More HTCondor hints in the Python wrapper][htcondor_python]{target=_blank}

## CERN 

### Webtools

* [Vistars][op_vistar]{target=_blank}
* [HTCondor Grafana][htcondor_grafana]{target=_blank .cern_login}
* [OP Webtools Page][op_webtools]{target=_blank}
* [Timber][timber_cern]{target=_blank .cern_internal}
* [INCA and LSA Applications][inca_lsa_apps]{target=_blank .cern_internal}
* [LHC MD webpage][lhc_md_page]{target=_blank}
* [Beam Performance Tracking Site][bpt_site]{target=_blank}
* [SWAN][swan]{target=_blank .cern_login} (Jupyter Notebooks in CERN Cloud)
* [CERN OpenStack][cern_openstack]{target=_blank .cern_login} (Virtual Machines in Cloud)
* [Room Booking][room_booking]{target=_blank .cern_login}

### Info

* [LHC Naming Conventions - Equipment Codes][equipment_codes]{target=_blank}
* [Beam-Beam and Luminosity Studies][bblumi]{target=_blank}
* [Accelerating Python Wiki][acc_py_wiki]{target=_blank .cern_internal}
* [CERN CBNG Manual][cbng_manual]{target=_blank .cern_internal}
* [LSA Wiki][lsa_wiki]{target=_blank .cern_internal}

### Repositories

* [LHC Optics Repository][lhc_gitlab]{target=_blank}
* [CERN Optics Repository][cern_optics_repo_site]{target=_blank}

## Development Guidelines and How-To's

* [Markdown Cheatsheet][markdown_cheatsheet]{target=_blank}
* [Jira Text Formatting Notation][jira_formatting]{target=_blank}

### Git

* [Generating SSH keys for GitHub][ssh_keys_github]{target=_blank}
* [Git - configuration for symbolic links instead of files][git_configs]{target=_blank}
* [GitHub Flavored Markdown][github_markdown]{target=_blank}

### Python

* [Python Style Guide][python_style_guide]{target=_blank}
* [Python docs][python_docs]{target=_blank}

### Java

* [Java Guidelines][java_guidelines]{target=_blank .cern_internal}

[omc_mattermost]: https://mattermost.web.cern.ch/be-dep/channels/omc-team
[omc_indico]: https://indico.cern.ch/category/5986/
[roro_website]: https://rtomas.web.cern.ch/rtomas/
[omc_logos]: https://github.com/pylhc/pylhc.github.io/tree/master/docs/assets/logos

[betabeat_gui_gitlab]: https://gitlab.cern.ch/acc-co/lhc/lhc-app-beta-beating
[jira_bugtracker]: https://its.cern.ch/jira/projects/BBGUI/
[betabeat_artifactory]: http://artifactory.cern.ch/webapp/#/artifacts/browse/tree/General/beco-release-local/cern/lhc/lhc-app-beta-beating

[kmod_gui_gitlab]: https://gitlab.cern.ch/acc-co/lhc/lhc-app-kmod
[kmod_artifactory]: http://artifactory.cern.ch/webapp/#/artifacts/browse/tree/General/beco-release-local/cern/lhc/lhc-app-kmod

[multiturn_gitlab]: https://gitlab.cern.ch/acc-co/lhc/lhc-multiturn
[multiturn_artifactory]: http://artifactory.cern.ch/webapp/#/artifacts/browse/tree/General/beco-release-local/cern/lhc/lhc-multiturn

[accounts_cern]: https://account.cern.ch/account/Management/MyAccounts.aspx
[services_cern]: https://resources.web.cern.ch/resources/Manage/ListServices.aspx
[afs_kerberos_ubuntu]: https://gist.github.com/OmeGak/9530124
[afs_kerberos_wsl]: https://gist.github.com/JoschD/194b3f6c6fcc408684a481fd4a2ff4e5
[kerberos_ssh]: https://twiki.cern.ch/twiki/bin/view/Main/Kerberos
[lhc_data_sources]: https://twiki.cern.ch/twiki/bin/view/ABPComputing/LhcDataStorage
[batch_docs]: https://batchdocs.web.cern.ch/index.html
[htcondor_local]: https://twiki.cern.ch/twiki/bin/view/ABPComputing/LxbatchHTCondor
[htcondor_python]: http://pylhc.github.io/Beta-Beat.src/utils/index.html#module-utils.htcondor_wrapper

[codimd]: https://codimd.web.cern.ch/vjC8BHbTS7etHwJve-K2Uw
[cern_computing_blog]: https://computing-blog.web.cern.ch/2020/03/useful-tools-for-teleworking/
[remote_desktop_service]: https://remotedesktop.web.cern.ch/remotedesktop/RDweb/Desktops.aspx

[equipment_codes]: https://edms5.cern.ch/cedar/plsql/codes.systems
[lhc_gitlab]: https://gitlab.cern.ch/acc-models/acc-models-lhc
[cern_optics_repo_site]: https://acc-models.web.cern.ch/acc-models/
[op_webtools]: https://op-webtools.web.cern.ch/index.html
[bpt_site]: https://bpt.web.cern.ch/
[bblumi]: http://bblumi.web.cern.ch/

[op_vistar]: https://op-webtools.web.cern.ch/vistar/vistars.php
[htcondor_grafana]: https://monit-grafana.cern.ch/
[acc_py_wiki]: https://wikis.cern.ch/display/ACCPY/Getting+started+with+acc-python
[room_booking]: https://indico.cern.ch/rooms/book#
[cern_openstack]: https://openstack.cern.ch/
[swan]: https://swan.cern.ch/

[timber_cern]: https://timber.cern.ch
[inca_lsa_apps]: https://wikis.cern.ch/pages/viewpage.action?pageId=80977620
[cbng_manual]: https://wikis.cern.ch/display/DVTLS/CBNG
[lsa_wiki]: https://wikis.cern.ch/display/LSA/Home

[lhc_md_page]: https://espace.cern.ch/lhc-md/default.aspx

[github_markdown]: https://help.github.com/articles/github-flavored-markdown
[markdown_cheatsheet]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
[jira_formatting]: https://jira.atlassian.com/secure/WikiRendererHelpAction.jspa?section=all
[git_configs]: http://stackoverflow.com/questions/954560/what-does-git-do-to-files-that-are-a-symbolic-link
[python_docs]: http://docs.python.org/

[python_style_guide]: https://www.python.org/dev/peps/pep-0008/
[ssh_keys_github]: https://help.github.com/articles/generating-ssh-keys
[java_guidelines]: https://wikis.cern.ch/display/DEV/Java+development+guidelines
