# OMC3 Optics Analysis Workflow

This page contains a walk-through of a typical but simple analysis workflow with the `omc3` codes.
To follow along, the reader needs to [have installed](getting_started.md) the `omc3` package and to have measurement or simulation data to use the codes on.
In case the reader does not have appropriate data to follow along with, a script is provided below to create some.

## The Analysis Workflow

A typical workflow with `omc3` consists in performing analysis of measurement or simulation files, and eventually calculating corrections to apply.
While `omc3` provides python modules to handle the different aspects of these tasks, it also provides entrypoint scripts to be called from the commandline.

The first step in the workflow consists in a harmonic frequency analysis performed with the `harpy` module, while the second one is an optics analysis performed with the `measure_optics` module.
The table below shows a general analysis workflow from BPM turn-by-turn measurements or simulation file to results, as well as the corresponding files at each step:

| Workflow & Files       |                        |                        |                        |                                   |
| :--------------------- | :--------------------: | :--------------------: | :--------------------: | --------------------------------: |
| Turn-by-Turn BPM Data  | :material-arrow-right: | Frequency Spectra      | :material-arrow-right: | Various Lattice Optics Parameters |
| SDDS files:  `*.sdds`  | :material-arrow-right: | TFS files: `*.lin[xy]` | :material-arrow-right: | TFS files: `*.tfs`                |

In this page, we will go through the essential steps in preparing and performing an analysis, by going from start to finish with a simple example.
In this walk-through, we will cover the use of the different entrypoints available to perform necessary steps.

!!! example  ""
    For our walk-through example, we will start from data obtained in `MAD-X` with the `TRACK` command for the 1023 turns in the LHC machine, with a scenario adapted from the 2018 configuration.
    Changes from the nominal scenario in your simulation could be including errors tables, orbit bumps, speculative magnet errors, additional elements etc.
    It is also easy for the reader to follow along if starting from measurements files.

??? example "Generating the Example Data"
    Here is the `MAD-X` script that will generate the example data used in this walk-through.
    It sets up a simple LHC configuration using files from `afs`, performs tracking and outputs a file named `trackone`.
    The script can be copy-pasted with a click in the top right of its box.
    
    For anyone without access to `afs`, you can find these files in our [MESS][mess] repository, or can simply use one of your own.
    ```fortran
    option, warn, info;
    option, echo=false, warn=false;
    
    ! ----- Set up Lattice and Define the Optics ----- !
    call, file="/afs/cern.ch/eng/lhc/optics/runII/2018/lhc_as-built.seq";  ! needs AFS access
    call, file="/afs/cern.ch/eng/lhc/optics/runII/2018/PROTON/opticsfile.22";  ! needs AFS access
    
    ! ----- Re-Cycle Sequence as in the Model ----- !
    seqedit, sequence=lhcb1;
    flatten;
    cycle, start="MSIA.EXIT.B1";
    endedit;

    ! ----- Create Beams ----- !
    beam, sequence=lhcb1, particle=proton, bv=1, energy=6500, npart=1e10, ex=5.4115e-10, ey=5.4115e-10;
    beam, sequence=lhcb2, particle=proton, bv=-1, energy=6500, npart=1e10, ex=5.4115e-10, ey=5.4115e-10;
    use, sequence=lhcb1;
    
    ! ----- Introduce Some Coupling ----- !
    CMRS.b1_sq = 0.001;
    
    ! ----- Match Tunes and Chromaticities ----- !
    match, chrom=true;
        global, sequence=lhcb1, q1=62.31, q2=60.32, dq1=2.0, dq2=2.0;
        vary, name="dqx.b1_sq", step=1e-07;
        vary, name="dqy.b1_sq", step=1e-07;
        vary, name="dqpx.b1_sq", step=1e-07;
        vary, name="dqpy.b1_sq", step=1e-07;
        lmdif, calls=100, tolerance=1e-21;
    endmatch;
    
    ! ----- Slice Lattice for Tracking ----- !
    slicefactor = 4    
    call, file="/afs/cern.ch/eng/lhc/optics/runII/2018/toolkit/myslice.madx";  ! needs AFS access
    use, sequence=lhcb1;
    makethin, sequence=lhcb1, style=teapot, makedipedge=false;
    
    ! ----- Define Observation Points and Perform Tracking ----- !
    ! These points are the BPMs from the model's twiss.dat file
    use, sequence=lhcb1;
    track, recloss=true, onepass=true, dump=true, onetable=true;
        observe, place="bpmyb.5l2.b1";
        observe, place="bpmyb.4l2.b1";
        observe, place="bpmwi.4l2.b1";
        observe, place="bpmsx.4l2.b1";
        observe, place="bpms.2l2.b1";
        observe, place="bpmsw.1l2.b1";
        observe, place="bpmsw.1r2.b1";
        observe, place="bpms.2r2.b1";
        observe, place="bpmsx.4r2.b1";
        observe, place="bpmwb.4r2.b1";
        observe, place="bpmyb.4r2.b1";
        observe, place="bpmr.5r2.b1";
        observe, place="bpm.6r2.b1";
        observe, place="bpm_a.7r2.b1";
        observe, place="bpm.8r2.b1";
        observe, place="bpm.9r2.b1";
        observe, place="bpm.10r2.b1";
        observe, place="bpm.11r2.b1";
        observe, place="bpm.12r2.b1";
        observe, place="bpm.13r2.b1";
        observe, place="bpm.14r2.b1";
        observe, place="bpm.15r2.b1";
        observe, place="bpm.16r2.b1";
        observe, place="bpm.17r2.b1";
        observe, place="bpm.18r2.b1";
        observe, place="bpm.19r2.b1";
        observe, place="bpm.20r2.b1";
        observe, place="bpm.21r2.b1";
        observe, place="bpm.22r2.b1";
        observe, place="bpm.23r2.b1";
        observe, place="bpm.24r2.b1";
        observe, place="bpm.25r2.b1";
        observe, place="bpm.26r2.b1";
        observe, place="bpm.27r2.b1";
        observe, place="bpm.28r2.b1";
        observe, place="bpm.29r2.b1";
        observe, place="bpm.30r2.b1";
        observe, place="bpm.31r2.b1";
        observe, place="bpm.32r2.b1";
        observe, place="bpm.33r2.b1";
        observe, place="bpm.34r2.b1";
        observe, place="bpm.33l3.b1";
        observe, place="bpm.32l3.b1";
        observe, place="bpm.31l3.b1";
        observe, place="bpm.30l3.b1";
        observe, place="bpm.29l3.b1";
        observe, place="bpm.28l3.b1";
        observe, place="bpm.27l3.b1";
        observe, place="bpm.26l3.b1";
        observe, place="bpm.25l3.b1";
        observe, place="bpm.24l3.b1";
        observe, place="bpm.23l3.b1";
        observe, place="bpm.22l3.b1";
        observe, place="bpm.21l3.b1";
        observe, place="bpm.20l3.b1";
        observe, place="bpm.19l3.b1";
        observe, place="bpm.18l3.b1";
        observe, place="bpm.17l3.b1";
        observe, place="bpm.16l3.b1";
        observe, place="bpm.15l3.b1";
        observe, place="bpm.14l3.b1";
        observe, place="bpm.13l3.b1";
        observe, place="bpm.12l3.b1";
        observe, place="bpm.11l3.b1";
        observe, place="bpm.10l3.b1";
        observe, place="bpm.9l3.b1";
        observe, place="bpm.8l3.b1";
        observe, place="bpm.7l3.b1";
        observe, place="bpm.6l3.b1";
        observe, place="bpmwg.a5l3.b1";
        observe, place="bpmw.5l3.b1";
        observe, place="bpmwe.4l3.b1";
        observe, place="bpmw.4l3.b1";
        observe, place="bpmw.4r3.b1";
        observe, place="bpmwe.4r3.b1";
        observe, place="bpmw.5r3.b1";
        observe, place="bpmwj.a5r3.b1";
        observe, place="bpmwc.6r3.b1";
        observe, place="bpmr.6r3.b1";
        observe, place="bpm_a.7r3.b1";
        observe, place="bpm.8r3.b1";
        observe, place="bpm.9r3.b1";
        observe, place="bpm.10r3.b1";
        observe, place="bpm.11r3.b1";
        observe, place="bpm.12r3.b1";
        observe, place="bpm.13r3.b1";
        observe, place="bpm.14r3.b1";
        observe, place="bpm.15r3.b1";
        observe, place="bpm.16r3.b1";
        observe, place="bpm.17r3.b1";
        observe, place="bpm.18r3.b1";
        observe, place="bpm.19r3.b1";
        observe, place="bpm.20r3.b1";
        observe, place="bpm.21r3.b1";
        observe, place="bpm.22r3.b1";
        observe, place="bpm.23r3.b1";
        observe, place="bpm.24r3.b1";
        observe, place="bpm.25r3.b1";
        observe, place="bpm.26r3.b1";
        observe, place="bpm.27r3.b1";
        observe, place="bpm.28r3.b1";
        observe, place="bpm.29r3.b1";
        observe, place="bpm.30r3.b1";
        observe, place="bpm.31r3.b1";
        observe, place="bpm.32r3.b1";
        observe, place="bpm.33r3.b1";
        observe, place="bpm.34r3.b1";
        observe, place="bpm.33l4.b1";
        observe, place="bpm.32l4.b1";
        observe, place="bpm.31l4.b1";
        observe, place="bpm.30l4.b1";
        observe, place="bpm.29l4.b1";
        observe, place="bpm.28l4.b1";
        observe, place="bpm.27l4.b1";
        observe, place="bpm.26l4.b1";
        observe, place="bpm.25l4.b1";
        observe, place="bpm.24l4.b1";
        observe, place="bpm.23l4.b1";
        observe, place="bpm.22l4.b1";
        observe, place="bpm.21l4.b1";
        observe, place="bpm.20l4.b1";
        observe, place="bpm.19l4.b1";
        observe, place="bpm.18l4.b1";
        observe, place="bpm.17l4.b1";
        observe, place="bpm.16l4.b1";
        observe, place="bpm.15l4.b1";
        observe, place="bpm.14l4.b1";
        observe, place="bpm.13l4.b1";
        observe, place="bpm.12l4.b1";
        observe, place="bpm.11l4.b1";
        observe, place="bpmcs.10l4.b1";
        observe, place="bpm.10l4.b1";
        observe, place="bpmcs.9l4.b1";
        observe, place="bpm.9l4.b1";
        observe, place="bpmcs.8l4.b1";
        observe, place="bpm.8l4.b1";
        observe, place="bpmcs.7l4.b1";
        observe, place="bpm.7l4.b1";
        observe, place="bpmyb.6l4.b1";
        observe, place="bpmya.5l4.b1";
        observe, place="bpmwi.a5l4.b1";
        observe, place="bpmwa.b5l4.b1";
        observe, place="bpmwa.a5l4.b1";
        observe, place="bpmwa.a5r4.b1";
        observe, place="bpmwa.b5r4.b1";
        observe, place="bpmyb.5r4.b1";
        observe, place="bpmya.6r4.b1";
        observe, place="bpmcs.7r4.b1";
        observe, place="bpm.7r4.b1";
        observe, place="bpmcs.8r4.b1";
        observe, place="bpm.8r4.b1";
        observe, place="bpmcs.9r4.b1";
        observe, place="bpm.9r4.b1";
        observe, place="bpmcs.10r4.b1";
        observe, place="bpm.10r4.b1";
        observe, place="bpm.11r4.b1";
        observe, place="bpm.12r4.b1";
        observe, place="bpm.13r4.b1";
        observe, place="bpm.14r4.b1";
        observe, place="bpm.15r4.b1";
        observe, place="bpm.16r4.b1";
        observe, place="bpm.17r4.b1";
        observe, place="bpm.18r4.b1";
        observe, place="bpm.19r4.b1";
        observe, place="bpm.20r4.b1";
        observe, place="bpm.21r4.b1";
        observe, place="bpm.22r4.b1";
        observe, place="bpm.23r4.b1";
        observe, place="bpm.24r4.b1";
        observe, place="bpm.25r4.b1";
        observe, place="bpm.26r4.b1";
        observe, place="bpm.27r4.b1";
        observe, place="bpm.28r4.b1";
        observe, place="bpm.29r4.b1";
        observe, place="bpm.30r4.b1";
        observe, place="bpm.31r4.b1";
        observe, place="bpm.32r4.b1";
        observe, place="bpm.33r4.b1";
        observe, place="bpm.34r4.b1";
        observe, place="bpm.33l5.b1";
        observe, place="bpm.32l5.b1";
        observe, place="bpm.31l5.b1";
        observe, place="bpm.30l5.b1";
        observe, place="bpm.29l5.b1";
        observe, place="bpm.28l5.b1";
        observe, place="bpm.27l5.b1";
        observe, place="bpm.26l5.b1";
        observe, place="bpm.25l5.b1";
        observe, place="bpm.24l5.b1";
        observe, place="bpm.23l5.b1";
        observe, place="bpm.22l5.b1";
        observe, place="bpm.21l5.b1";
        observe, place="bpm.20l5.b1";
        observe, place="bpm.19l5.b1";
        observe, place="bpm.18l5.b1";
        observe, place="bpm.17l5.b1";
        observe, place="bpm.16l5.b1";
        observe, place="bpm.15l5.b1";
        observe, place="bpm.14l5.b1";
        observe, place="bpm.13l5.b1";
        observe, place="bpm.12l5.b1";
        observe, place="bpm.11l5.b1";
        observe, place="bpm.10l5.b1";
        observe, place="bpm.9l5.b1";
        observe, place="bpm.8l5.b1";
        observe, place="bpmr.7l5.b1";
        observe, place="bpm.6l5.b1";
        observe, place="bpmr.5l5.b1";
        observe, place="bpmya.4l5.b1";
        observe, place="bpmwb.4l5.b1";
        observe, place="bpmsy.4l5.b1";
        observe, place="bpms.2l5.b1";
        observe, place="bpmwf.a1l5.b1";
        observe, place="bpmsw.1l5.b1";
        observe, place="bpmsw.1r5.b1";
        observe, place="bpmwf.a1r5.b1";
        observe, place="bpms.2r5.b1";
        observe, place="bpmsy.4r5.b1";
        observe, place="bpmwb.4r5.b1";
        observe, place="bpmya.4r5.b1";
        observe, place="bpm.5r5.b1";
        observe, place="bpmwt.c6r5.b1";
        observe, place="bpmwt.d6r5.b1";
        observe, place="bpmwt.a6r5.b1";
        observe, place="bpmwt.b6r5.b1";
        observe, place="bpmr.6r5.b1";
        observe, place="bpm_a.7r5.b1";
        observe, place="bpm.8r5.b1";
        observe, place="bpm.9r5.b1";
        observe, place="bpm.10r5.b1";
        observe, place="bpm.11r5.b1";
        observe, place="bpm.12r5.b1";
        observe, place="bpm.13r5.b1";
        observe, place="bpm.14r5.b1";
        observe, place="bpm.15r5.b1";
        observe, place="bpm.16r5.b1";
        observe, place="bpm.17r5.b1";
        observe, place="bpm.18r5.b1";
        observe, place="bpm.19r5.b1";
        observe, place="bpm.20r5.b1";
        observe, place="bpm.21r5.b1";
        observe, place="bpm.22r5.b1";
        observe, place="bpm.23r5.b1";
        observe, place="bpm.24r5.b1";
        observe, place="bpm.25r5.b1";
        observe, place="bpm.26r5.b1";
        observe, place="bpm.27r5.b1";
        observe, place="bpm.28r5.b1";
        observe, place="bpm.29r5.b1";
        observe, place="bpm.30r5.b1";
        observe, place="bpm.31r5.b1";
        observe, place="bpm.32r5.b1";
        observe, place="bpm.33r5.b1";
        observe, place="bpm.34r5.b1";
        observe, place="bpm.33l6.b1";
        observe, place="bpm.32l6.b1";
        observe, place="bpm.31l6.b1";
        observe, place="bpm.30l6.b1";
        observe, place="bpm.29l6.b1";
        observe, place="bpm.28l6.b1";
        observe, place="bpm.27l6.b1";
        observe, place="bpm.26l6.b1";
        observe, place="bpm.25l6.b1";
        observe, place="bpm.24l6.b1";
        observe, place="bpm.23l6.b1";
        observe, place="bpm.22l6.b1";
        observe, place="bpm.21l6.b1";
        observe, place="bpm.20l6.b1";
        observe, place="bpm.19l6.b1";
        observe, place="bpm.18l6.b1";
        observe, place="bpm.17l6.b1";
        observe, place="bpm.16l6.b1";
        observe, place="bpm.15l6.b1";
        observe, place="bpm.14l6.b1";
        observe, place="bpm.13l6.b1";
        observe, place="bpm.12l6.b1";
        observe, place="bpm.11l6.b1";
        observe, place="bpm.10l6.b1";
        observe, place="bpm.9l6.b1";
        observe, place="bpm.8l6.b1";
        observe, place="bpmya.5l6.b1";
        observe, place="bpmyb.4l6.b1";
        observe, place="bpmsx.b4l6.b1";
        observe, place="bpmsx.a4l6.b1";
        observe, place="bpmse.4l6.b1";
        observe, place="bpmsa.4r6.b1";
        observe, place="bpmsi.a4r6.b1";
        observe, place="bpmsi.b4r6.b1";
        observe, place="bpmya.4r6.b1";
        observe, place="bpmyb.5r6.b1";
        observe, place="bpm.8r6.b1";
        observe, place="bpm.9r6.b1";
        observe, place="bpm.10r6.b1";
        observe, place="bpm.11r6.b1";
        observe, place="bpm.12r6.b1";
        observe, place="bpm.13r6.b1";
        observe, place="bpm.14r6.b1";
        observe, place="bpm.15r6.b1";
        observe, place="bpm.16r6.b1";
        observe, place="bpm.17r6.b1";
        observe, place="bpm.18r6.b1";
        observe, place="bpm.19r6.b1";
        observe, place="bpm.20r6.b1";
        observe, place="bpm.21r6.b1";
        observe, place="bpm.22r6.b1";
        observe, place="bpm.23r6.b1";
        observe, place="bpm.24r6.b1";
        observe, place="bpm.25r6.b1";
        observe, place="bpm.26r6.b1";
        observe, place="bpm.27r6.b1";
        observe, place="bpm.28r6.b1";
        observe, place="bpm.29r6.b1";
        observe, place="bpm.30r6.b1";
        observe, place="bpm.31r6.b1";
        observe, place="bpm.32r6.b1";
        observe, place="bpm.33r6.b1";
        observe, place="bpm.34r6.b1";
        observe, place="bpm.33l7.b1";
        observe, place="bpm.32l7.b1";
        observe, place="bpm.31l7.b1";
        observe, place="bpm.30l7.b1";
        observe, place="bpm.29l7.b1";
        observe, place="bpm.28l7.b1";
        observe, place="bpm.27l7.b1";
        observe, place="bpm.26l7.b1";
        observe, place="bpm.25l7.b1";
        observe, place="bpm.24l7.b1";
        observe, place="bpm.23l7.b1";
        observe, place="bpm.22l7.b1";
        observe, place="bpm.21l7.b1";
        observe, place="bpm.20l7.b1";
        observe, place="bpm.19l7.b1";
        observe, place="bpm.18l7.b1";
        observe, place="bpm.17l7.b1";
        observe, place="bpm.16l7.b1";
        observe, place="bpm.15l7.b1";
        observe, place="bpm.14l7.b1";
        observe, place="bpm.13l7.b1";
        observe, place="bpm.12l7.b1";
        observe, place="bpm.11l7.b1";
        observe, place="bpm.10l7.b1";
        observe, place="bpm.9l7.b1";
        observe, place="bpm.8l7.b1";
        observe, place="bpm.7l7.b1";
        observe, place="bpm.6l7.b1";
        observe, place="bpmwc.6l7.b1";
        observe, place="bpmwe.5l7.b1";
        observe, place="bpmw.5l7.b1";
        observe, place="bpmwe.4l7.b1";
        observe, place="bpmw.4l7.b1";
        observe, place="bpmw.4r7.b1";
        observe, place="bpmwe.4r7.b1";
        observe, place="bpmw.5r7.b1";
        observe, place="bpmwe.5r7.b1";
        observe, place="bpmr.6r7.b1";
        observe, place="bpm_a.7r7.b1";
        observe, place="bpm.8r7.b1";
        observe, place="bpm.9r7.b1";
        observe, place="bpm.10r7.b1";
        observe, place="bpm.11r7.b1";
        observe, place="bpm.12r7.b1";
        observe, place="bpm.13r7.b1";
        observe, place="bpm.14r7.b1";
        observe, place="bpm.15r7.b1";
        observe, place="bpm.16r7.b1";
        observe, place="bpm.17r7.b1";
        observe, place="bpm.18r7.b1";
        observe, place="bpm.19r7.b1";
        observe, place="bpm.20r7.b1";
        observe, place="bpm.21r7.b1";
        observe, place="bpm.22r7.b1";
        observe, place="bpm.23r7.b1";
        observe, place="bpm.24r7.b1";
        observe, place="bpm.25r7.b1";
        observe, place="bpm.26r7.b1";
        observe, place="bpm.27r7.b1";
        observe, place="bpm.28r7.b1";
        observe, place="bpm.29r7.b1";
        observe, place="bpm.30r7.b1";
        observe, place="bpm.31r7.b1";
        observe, place="bpm.32r7.b1";
        observe, place="bpm.33r7.b1";
        observe, place="bpm.34r7.b1";
        observe, place="bpm.33l8.b1";
        observe, place="bpm.32l8.b1";
        observe, place="bpm.31l8.b1";
        observe, place="bpm.30l8.b1";
        observe, place="bpm.29l8.b1";
        observe, place="bpm.28l8.b1";
        observe, place="bpm.27l8.b1";
        observe, place="bpm.26l8.b1";
        observe, place="bpm.25l8.b1";
        observe, place="bpm.24l8.b1";
        observe, place="bpm.23l8.b1";
        observe, place="bpm.22l8.b1";
        observe, place="bpm.21l8.b1";
        observe, place="bpm.20l8.b1";
        observe, place="bpm.19l8.b1";
        observe, place="bpm.18l8.b1";
        observe, place="bpm.17l8.b1";
        observe, place="bpm.16l8.b1";
        observe, place="bpm.15l8.b1";
        observe, place="bpm.14l8.b1";
        observe, place="bpm.13l8.b1";
        observe, place="bpm.12l8.b1";
        observe, place="bpm.11l8.b1";
        observe, place="bpm.10l8.b1";
        observe, place="bpm.9l8.b1";
        observe, place="bpm.8l8.b1";
        observe, place="bpm.7l8.b1";
        observe, place="bpmr.6l8.b1";
        observe, place="bpm.5l8.b1";
        observe, place="bpmyb.4l8.b1";
        observe, place="bpmwb.4l8.b1";
        observe, place="bpmsx.4l8.b1";
        observe, place="bpms.2l8.b1";
        observe, place="bpmsw.1l8.b1";
        observe, place="bpmsw.1r8.b1";
        observe, place="bpms.2r8.b1";
        observe, place="bpmsx.4r8.b1";
        observe, place="bpmwb.4r8.b1";
        observe, place="bpmyb.4r8.b1";
        observe, place="bpmyb.5r8.b1";
        observe, place="bpm.6r8.b1";
        observe, place="bpm_a.7r8.b1";
        observe, place="bpm.8r8.b1";
        observe, place="bpm.9r8.b1";
        observe, place="bpm.10r8.b1";
        observe, place="bpm.11r8.b1";
        observe, place="bpm.12r8.b1";
        observe, place="bpm.13r8.b1";
        observe, place="bpm.14r8.b1";
        observe, place="bpm.15r8.b1";
        observe, place="bpm.16r8.b1";
        observe, place="bpm.17r8.b1";
        observe, place="bpm.18r8.b1";
        observe, place="bpm.19r8.b1";
        observe, place="bpm.20r8.b1";
        observe, place="bpm.21r8.b1";
        observe, place="bpm.22r8.b1";
        observe, place="bpm.23r8.b1";
        observe, place="bpm.24r8.b1";
        observe, place="bpm.25r8.b1";
        observe, place="bpm.26r8.b1";
        observe, place="bpm.27r8.b1";
        observe, place="bpm.28r8.b1";
        observe, place="bpm.29r8.b1";
        observe, place="bpm.30r8.b1";
        observe, place="bpm.31r8.b1";
        observe, place="bpm.32r8.b1";
        observe, place="bpm.33r8.b1";
        observe, place="bpm.34r8.b1";
        observe, place="bpm.33l1.b1";
        observe, place="bpm.32l1.b1";
        observe, place="bpm.31l1.b1";
        observe, place="bpm.30l1.b1";
        observe, place="bpm.29l1.b1";
        observe, place="bpm.28l1.b1";
        observe, place="bpm.27l1.b1";
        observe, place="bpm.26l1.b1";
        observe, place="bpm.25l1.b1";
        observe, place="bpm.24l1.b1";
        observe, place="bpm.23l1.b1";
        observe, place="bpm.22l1.b1";
        observe, place="bpm.21l1.b1";
        observe, place="bpm.20l1.b1";
        observe, place="bpm.19l1.b1";
        observe, place="bpm.18l1.b1";
        observe, place="bpm.17l1.b1";
        observe, place="bpm.16l1.b1";
        observe, place="bpm.15l1.b1";
        observe, place="bpm.14l1.b1";
        observe, place="bpm.13l1.b1";
        observe, place="bpm.12l1.b1";
        observe, place="bpm.11l1.b1";
        observe, place="bpm.10l1.b1";
        observe, place="bpm.9l1.b1";
        observe, place="bpm.8l1.b1";
        observe, place="bpmr.7l1.b1";
        observe, place="bpm.6l1.b1";
        observe, place="bpmr.5l1.b1";
        observe, place="bpmya.4l1.b1";
        observe, place="bpmwb.4l1.b1";
        observe, place="bpmsy.4l1.b1";
        observe, place="bpms.2l1.b1";
        observe, place="bpmwf.a1l1.b1";
        observe, place="bpmsw.1l1.b1";
        observe, place="bpmsw.1r1.b1";
        observe, place="bpmwf.a1r1.b1";
        observe, place="bpms.2r1.b1";
        observe, place="bpmsy.4r1.b1";
        observe, place="bpmwb.4r1.b1";
        observe, place="bpmya.4r1.b1";
        observe, place="bpm.5r1.b1";
        observe, place="bpmsa.a6r1.b1";
        observe, place="bpmr.6r1.b1";
        observe, place="bpmsx.7r1.b1";
        observe, place="bpm_a.7r1.b1";
        observe, place="bpm.8r1.b1";
        observe, place="bpm.9r1.b1";
        observe, place="bpm.10r1.b1";
        observe, place="bpm.11r1.b1";
        observe, place="bpm.12r1.b1";
        observe, place="bpm.13r1.b1";
        observe, place="bpm.14r1.b1";
        observe, place="bpm.15r1.b1";
        observe, place="bpm.16r1.b1";
        observe, place="bpm.17r1.b1";
        observe, place="bpm.18r1.b1";
        observe, place="bpm.19r1.b1";
        observe, place="bpm.20r1.b1";
        observe, place="bpm.21r1.b1";
        observe, place="bpm.22r1.b1";
        observe, place="bpm.23r1.b1";
        observe, place="bpm.24r1.b1";
        observe, place="bpm.25r1.b1";
        observe, place="bpm.26r1.b1";
        observe, place="bpm.27r1.b1";
        observe, place="bpm.28r1.b1";
        observe, place="bpm.29r1.b1";
        observe, place="bpm.30r1.b1";
        observe, place="bpm.31r1.b1";
        observe, place="bpm.32r1.b1";
        observe, place="bpm.33r1.b1";
        observe, place="bpm.34r1.b1";
        observe, place="bpm.33l2.b1";
        observe, place="bpm.32l2.b1";
        observe, place="bpm.31l2.b1";
        observe, place="bpm.30l2.b1";
        observe, place="bpm.29l2.b1";
        observe, place="bpm.28l2.b1";
        observe, place="bpm.27l2.b1";
        observe, place="bpm.26l2.b1";
        observe, place="bpm.25l2.b1";
        observe, place="bpm.24l2.b1";
        observe, place="bpm.23l2.b1";
        observe, place="bpm.22l2.b1";
        observe, place="bpm.21l2.b1";
        observe, place="bpm.20l2.b1";
        observe, place="bpm.19l2.b1";
        observe, place="bpm.18l2.b1";
        observe, place="bpm.17l2.b1";
        observe, place="bpm.16l2.b1";
        observe, place="bpm.15l2.b1";
        observe, place="bpm.14l2.b1";
        observe, place="bpm.13l2.b1";
        observe, place="bpm.12l2.b1";
        observe, place="bpm.11l2.b1";
        observe, place="bpm.10l2.b1";
        observe, place="bpm.9l2.b1";
        observe, place="bpm.8l2.b1";
        observe, place="bpm.7l2.b1";
        observe, place="bpmr.6l2.b1";
        start, x=0.0002, px=0, y=0.0002, py=0, t=0, pt=0;
        run, turns=1023;
    endtrack;
    ```

## Preparing Data for Analysis

Analysis in `omc3` is mostly done from measurement data, but can also be done on simulated tracking data.
While `omc3` codes can read data from many machine formats, we will for demonstration purposes first convert our data to the LHC's [SDDS][sdds] binary format.

For this `omc3` provides the `tbt_converter` entrypoint.
A typical use consists in specifying the location of your turn-by-turn measurement files, the data type of said files and the location in which to write the converted `SDDS` data.
The formats supported by the converter are:

- Machine formats: `lhc`, `iota` and `esrf`, or any machine using one of these.
- Simulation formats: the `trackone` and `ptc` formats from tracking data from `MAD-X` or `PTC`.

??? info "The `trackone` and `ptc` formats"
    What is referred to here as the `trackone` or `ptc` format is obtained by giving the `DUMP` and `ONETABLE` options to the `TRACK` or `PTC_TRACK` commands, respectively, in `MAD-X`.
    This way, all tracking data is written to a single file on disk, which you can feed to the `tbt_converter`.
    Remembering which tracking module was used is important as `PTC_TRACK` does not write in the same format as `MAD-X`'s `TRACK`.

For our example, let us say that when setting up tracking we have asked `MAD-X` to output the data into a file called `trackone` (this is actually the default name).
Using the converter to make a compatible `SDDS` file then goes as:
```bash
python -m omc3.tbt_converter \
    --files trackone \
    --tbt_datatype trackone \
    --drop_elements LHCB1MSIA.EXIT.B1_P_ \
    --outputdir .
```

!!! info ""
    When tracking in `MAD-X`, by default the start of machine will be included in the list of observation points.
    As we do not want this arbitrary point, we indicate to the `tbt_converter` we intend to drop it with the `--drop_elements` flag.
    More than one element can be given to this flag.

The converter will create new files with the `.sdds` suffix appended to the original filename.
In our case, a `trackone.sdds` file will be created.

!!! tip "Other Uses"
    The `tbt_converter` provides additional functionality such as adding noise to the provided data or averaging across particles.
    To use these options, refer to the [converter's API documentation][tbt_converter].

## Creating a Model

In order to perform the optics analysis, one needs a model of the given machine to compare to.
For this, `omc3` provides the `model_creator` entrypoint, which allows you to run a model simulation of the desired machine and output the needed files.

??? example "Supported Machines"
    The out-of-the-box supported machines for model creation are `lhc`, `ps` and `psbooster`, machines we work on.
    While the `skekb`, `JPARC`, `petra` and `iota` have accelerator classes, no model creator has been implemented for them yet.
    It is possible to extend this list for your machine by defining an appropriate `Accelerator` class as well as a model creator.
    See [this guide][new_machine_guide] for implementation steps.

In our example, we would like to compare our data to the nominal model of the 2018 LHC. 
Using the script to create a nominal model of the 2018 LHCB1, with the machine configuration and opticsfile used in our example, goes as:
```bash
python -m omc3.model_creator \
    --accel lhc \
    --type nominal \
    --year 2018 \
    --beam 1 \
    --energy 6.5 \
    --nat_tunes 62.31 60.32 \
    --modifiers /afs/cern.ch/eng/lhc/optics/runII/2018/PROTON/opticsfile.22 \
    --outputdir lhc_model
```

Some of these options belong to the `model_creator` itself, while others depend explicitely on the chosen machine, here the LHC.
Refer to the [model creator's API documentation][model_creator] for the list of options.

The model creation runs a `MAD-X` scenario and outputs the relevant twiss results to the desired directory.
Running `ls lhc_model/` yields:
```bash
b2_errors.tfs		error_deffs.txt		    macros			twiss_elements.dat
b2_settings.madx	job.create_model.madx	twiss.dat
```

!!! question "What is a Model?"
    As one can see, a "model" is essentially one or more TFS files with optics functions at BPMs (`twiss.dat`) and elements (`twiss_elements.dat`), other files being here for the user to understand or reproduce the result.
    Had we created a driven model, then an additional `twiss_ac.dat` or `twiss_adt.dat` file would have been created, with optics functions at BPMs while driving the beam.
    One can create their own models without the `model_creator` should they want to, as it only acts as a convenience wrapper. 

    A `driven model` is the same as above, with also a `TWISS` taking into account the exciting effect of an AC dipole or ADT onto the optics.
    Creating this is easiest done with the `model_creator`, but can also be done individually with the a script installing the appropriate element into your sequence. 

## Frequency Analysis

Once measurement or simulation is in the appropriate format, the first step as seen in the table above consists in a harmonic analysis of the data.
To do so, `omc3` provides the `hole_in_one` entrypoint, which will perform frequency analysis of the data when provided with the `--harpy` flag.

The script provides options involved in both data cleaning and parameter tweaking for the harmonic analysis, which is useful when you have relevant information about your measurements. 
To use these, refer to the `Harpy Kwargs` section of the [hole_in_one API documentation][hole_in_one].

In our example we will leave most of these to their default values to keep the analysis simple, but ask from `harpy` to output all computed results.
We will input `lhc` for the `--tbt_datatype` flag, but if you skipped the use of the `tbt_converter` you should input the type of your machine there.
Running the frequency analysis then goes as:
```bash
python -m omc3.hole_in_one --harpy \
    --files trackone.sdds \
    --tbt_datatype lhc \
    --turns 0 1023 \
    --autotunes transverse \
    --to_write lin spectra full_spectra bpm_summary \
    --outputdir harpy_output
```

??? warning "Memory Requirements"
    During frequency analysis, `harpy` makes use of zero padding (with by default $2^{20}$ zeros) to improve the accuracy of results.
    In turn, the padded arrays become consequent and, coupled with a high number of observation points, processing will require a substantial amount of RAM - well into the few GBs range for our example.

    When running on limiting hardware, one can change the amount of zero padding with the `--turn_bits` flag for `harpy`.
    It is important however to remember that decreasing this number will reduce the accuracy of the results, since it increases the range between detected frequencies.
    Refer to the [hole_in_one API documentation][hole_in_one] for details that could help in determining which number to use.

In the output directory, `harpy` will create TFS files with the results of the analysis for both good BPMs and identified bad BPMs.
The filenames are determined by appending the appropriate suffixes to the entry files.

!!! info "Bad BPMs"
    If given `bpm_summary` for the `--to_write` flag (which is the case by default), `harpy` will output the `.bad_bpms_[xy]` files.
    BPMs are determined as bad or not depending on several options from the cleaning phase.
    While these are given sensible defaults, one might need to tweak them manually depending on their measurement. 
    Additionally, known bad BPMs can be given with the `--bad_bpms` flag.

In the output files, various properties are given in column form for each observation point.
Running `ls harpy_output/` yields the following result:
```bash
trackone.sdds.ampsx		    trackone.sdds.freqsx
trackone.sdds.ampsy		    trackone.sdds.freqsy
trackone.sdds.bad_bpms_x	trackone.sdds.linx
trackone.sdds.bad_bpms_y	trackone.sdds.liny
```

!!! tip "Plotting the Spectra"
    The `omc3` package provides scripts and modules to quickly plot the spectra obtained from frequency analysis.
    To use these, refer to the [Plot Spectrum][plot_spectrum] API documentation.

??? question "Column Nomenclature"
    The `*.amps[xy]`, `*.freqs[xy]` and `*.lin[xy]` files in the harmonic analysis output are **TFS** files.

    The `*.freqs[xy]` files contain for each BPM in column format the frequencies of the resonance lines detected in the spectrum, for respectively the horizontal (`.freqsx`) and vertical (`.freqsy`) planes while the `*.amps[xy]` files contain the amplitudes of said resonance lines.
    This means in the column of a given BPM, the `nth` row in the `.amps[xy]` file corresponds to the amplitude of the resonance line located at the frequency given by the `nth` row in the column of the same name in the `.freqs[xy]` file.
    For illustration purposes, simplistic plotting of the horizontal spectrum (without the spectrum plotter mentioned above) from these files would go as:
    ```python
    import tfs
    import matplotlib.pyplot as plt

    ampsx = tfs.read("harpy_output/trackone.sdds.ampsx")
    freqsx = tfs.read("harpy_output/trackone.sdds.freqsx")

    for bpm in ampsx.columns:
        if bpm in freqsx.columns:  # safety check but no reason it wouldn't be there
            plt.plot(freqsx[bpm], ampsx[bpm], ".-") 
            # plt.stem(freqsx[bpm], ampsx[bpm])  # would be more accurate but might stress your system

    plt.setp(plt.gca(), xlabel=r"$Q_x$", ylabel="Amplitude", title="Horizontal Spectrum", xlim=(0, 0.5))
    ```

    The `*.lin[xy]` files contain various data (in columns) computed for each BPM (in rows) as some summary information.
    Some column names are explicit: `BPM_RES` contains the determined BPM resolution, `CO` the closed orbit value at said BPM and `PK2PK` is the peak-to-peak value of oscillations registered by the given BPM.
    `TUNE[XY]`, `AMP[XY]` and `MU[XY]` are the detected tune, the amplitude of the tune line and the phase of the tune line for said BPM, respectively.
    
    The other columns describe the phase (`PHASE`), amplitude ratio (`AMP`) and frequency (`FREQ`) of the line identified by the number in the column name, where underscores represent a minus sign.
    Therefore, in the `.linx` file `FREQ01`, `AMP01` and `PHASE01` are respectively the frequency of the main vertical tune line in the horizontal spectrum, the ratio of this line's amplitude to that of the main horizontal line and the phase of this line.
    The equivalent columns in the `.liny` file are `FREQ10`, `AMP10` and `PHASE10`.

    Generally speaking, the frequency and amplitude of higher order lines is calculated using $m \cdot Q_x + n \cdot Q_y$  so `FREQ1_3` corresponds to $m = 1$ and $n = -3$ which is a decapolar line ($|m| + |n| = 4)$.
    For more information, [this paper on normal forms][normal_forms]{target=_blank} is a good resource.

## Optics Analysis

Once harmonic analysis has been performed, one can move on to the reconstruction of optics quantities from computed spectra and phases.
To do so, `omc3` provides the `hole_in_one` entrypoint, to be used this time with the `--optics` flag.

In our example we will ask to use the `three_bpm_method` when reconstructing beta functions from phase advances, as the default `n_bpm_method` requires providing an error definition file which our simulation did not implement.
Calling the entrypoint to perform optics analysis goes as:
```bash
python -m omc3.hole_in_one --optics \
    --accel lhc \
    --year 2018 \
    --beam 1 \
    --energy 6.5 \
    --files harpy_output/trackone.sdds \
    --model_dir lhc_model \
    --compensation none \
    --three_bpm_method \
    --outputdir measured_optics
```

!!! warning "Input Files"
    While `harpy` outputs various types of files with different suffixes, the optics analysis only looks for some of them.
    Thus, when providing the `--files` flag, no specific files should be provided, and instead the path to `harpy` outputs **without a suffix** should be given.
    In our example, this means entering `harpy_output/trackone.sdds`.

Like other entrypoints, the optics analysis provides many options on methods to use and quantities to compute.
To use these, refer to the `Optics Kwargs` section of the [hole_in_one API documentation][hole_in_one].

In the output files, various properties are given in column form for each observation point.
Running `ls measured_optics/` yields the following result:
```bash
beta_amplitude_x.tfs	    kick_x.tfs		        phase_y.tfs
beta_amplitude_y.tfs	    kick_y.tfs		        special_phase_x.tfs
beta_phase_x.tfs	        measure_optics.log	    special_phase_y.tfs
beta_phase_y.tfs	        orbit_x.tfs		        total_phase_x.tfs
interaction_point_x.tfs	    orbit_y.tfs		        total_phase_y.tfs
interaction_point_y.tfs	    phase_x.tfs
```

---

!!! tip "Hole in One"
    The harmonic analysis and optics analysis don't necessarily have to be separated steps.
    It is possible to run the `hole_in_one` entrypoint with both `--harpy` and `--optics` flags, even though the command might become cumbersome.
    The associated flags and options do not change, although only one `outputdir` should be given.
    
    Our example done in one step would be:
    ```bash
    python -m omc3.hole_in_one --harpy --optics \
        --files trackone.sdds \
        --tbt_datatype lhc \
        --turns 0 1023 \
        --autotunes transverse \
        --to_write lin spectra full_spectra bpm_summary \
        --accel lhc \
        --year 2018 \
        --beam 1 \
        --model_dir lhc_model \
        --compensation none \
        --three_bpm_method \
        --coupling_method 1 \
        --outputdir measured_optics
    ```
    In this case, the output files from `harpy` are automatically handled and put into a subfolder named `lin_files` inside of the specified `outputdir`.
    The rest is done and output as seen above.

[mess]: https://github.com/pylhc/MESS
[sdds]: https://ops.aps.anl.gov/SDDSIntroTalk/slides.html
[tbt_converter]: https://pylhc.github.io/omc3/entrypoints/other.html#tbt-converter
[plot_spectrum]: https://pylhc.github.io/omc3/entrypoints/plotting.html#plot-spectrum
[normal_forms]: https://cds.cern.ch/record/333077/files/p93.pdf
[hole_in_one]: https://pylhc.github.io/omc3/entrypoints/analysis.html#omc3.hole_in_one.hole_in_one_entrypoint
[new_machine_guide]: know_how.md#how-to-create-files-for-your-file-accelerator
[model_creator]: https://pylhc.github.io/omc3/entrypoints/other.html#model-creator
