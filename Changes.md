# Changes to do to website

## Theming

- [x] The html footer template should mention we're powered by Zensical and not mkdocs + mkdocs-material

## OMC Team

- [x] Admonition should not read like we just made the new site, just that it is constantly being updated.

## Python Ecosystem

- [x] Main page, move "The OMC Python Ecosystem" up
- [x] Main page, rewrite "The OMC Python Ecosystem" to not really talk about BBsrc as a viable thing
- [x] Main page, mention BBsrc in last admonition
- [x] Main page, split table in "main packages" and "dummy useful little ones"
- [x] OMC3 main page, do not hardcode Python3.7+ just mention Python 3
- [x] OMC3 Getting started, installation method outdated
- [x] OMC3 Getting started, update scripts with readme from the repo
- [x] OMC3 analysis, BIG admonition that the command line use is discouraged because of complexity of the tasks and using the GUIs is the preferred way
- [x] OMC3 analysis, insert a link to TFS format definition from tfspandas doc.
- [x] OMC3 analysis, make MESS link point to a self contained example folder in MESS.
- [x] OMC3 analysis, model creation, update supported machines admonition
- [x] OMC3 analysis, model creation, update command to omit afs, fodmat output files, point to ACD model MESS.
- [x] OMC3 analysis, frequency analysis, make link blank target.
- [x] OMC3 analysis, optics analysis the error definitions should be provided by the model not simulation. Can link to the paper.
- [x] OMC3 analysis, mention that for correction you should use the GUI or that we build later, create a last section like ampdet and point to the GUI page?
- [x] PyLHC main page, update the scripts present
- [x] PyLHC main page, dont explicitely mention python 3.7
- [x] PyLHC machine settings info refer to the omc3 version
- [x] PyLHC kick groups page, example or info?
- [ ] PyLHC etc do we need to duplicate what is in their documentations?
- [x] pylhcsubmitter, study from command line add line breaks to command
- [x] pylhcsubmitter add a link to my presentation
- [x] pylhcsubmitter max number of jobs (in njobs admonition) add link to the HTCondor documentation?
- [ ] pylhcsubmitter resubmitting, explain why job_outputdir is indicator
- [x] Move IRNL correction to "links to other package"
- [x] REMOVE MESS COMPLETELY
- [x] developping, there are no makefiles anymore
- [x] developping, make a step for the tests
- [x] developping, we don't use codeclimate anymore
- [x] developping, recommend test + doc extras. In all we might have CERN-network stuff
- [x] releasing, create new tag should be in point 2
- [x] IDE setup, add ty as recommended extension
- [x] virtual environments, maybe update with the next refresh? (names etc)
- [x] managing, explain TN means Technical Network when talking about lintrack
- [x] managing, the TODO admonition should be renamed "Checks" or something for when making changes

## GUIs

- [x] Main page, running in the CCC in 2025 -> 2026?

## Measurements and Corrections

- [x] main page could use a little more content
- [x] main page should be named "about" like in other places.
- [x] main page, wrong capitalized word
- [x] Physics, introduction, add links to various PhD theses?
- [ ] Physics, BPM filtering -> remove all the colors? Don't want all that CSS...
- [x] Physics, BPM filtering, move admonition a little up in Isolation Forest
- [x] Physics, optics analysis is not written
- [x] Physics, LHC IR linear optics not written
- [x] Physics, LHC IR nonlinear optics not written
- [x] Physics, 3D kicks not written
- [ ] Procedures, crossing angle scan not written. Ask Ewen?
- [x] Procedures, point to the `omc3` version of the machine_settings_info script.

## Resources

- [x] main page, links, the lhc app kmod link is outdated.
- [x] main page, links, the multiturn link is outdated. Follow it and use the recommended new path given by gitlab instead
- [x] main page, jws programs, beta-beat and beta-beat omc3 are just one now, figure out what to put. Ask Josch?
- [x] main page, jws programs, remove kmod app as it's outdated
- [x] main page, review all the links one by one
- [x] Computing, git, very end of the page when expanding point 8 and yaml admonition the links do not render
- [x] Computing, shared filesystems, typos in EOS section title
- [x] Editing, wrong in boxes about ??? -> mixup between collapsible + extended by default or only extended
- [ ] Publications - GATHER FOR 2024 and 2025 WE SURELY HAVE SOMETHING TO SHOW??

## Logbook

- [x] Some LHC pages have an admonition pointing to a commissioning folder on lintrack but that might not exist since they stopped doing it after I left. Remove admonitions.
