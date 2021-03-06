Launching the simulations
=========================

This describe how to launch the simulation of the Hybrid Model on the EBI cluster, using sumatra.
You can run the same simulation just passing the param file if you are not using Sumatra, 
to the main script `spineIntegration.py`.

For example the following simulation:

::

    bsub -M 20000 -R "rusage[mem=20000]" smt run param/allspines.param -r "Testing the new synchro mechanism." -t "test, all"

becomes

::
	
	python spineIntegration.py param/allspines.param
	
All the rest is used for the LSF Cluster (`bsub` and options), and to record the 
simulation with sumatra and the reason to describe it.

Small memory, for testing
-------------------------

::

    bsub -M 4000 -R "rusage[mem=4000]" smt run param/default.param -r "Testing the new synchro mechanism." -t "test, twospines"
    
    bsub -M 4000 -R "rusage[mem=4000]" -q research-rh6 smt run param/short_tstop_double_stim.param -r "Double stims applied for short tstop." -t "test, twospines"
    
    bsub -M 10000 -R "rusage[mem=10000]" -q research-rh6 smt run param/short_tstop_onebranch_several_stimulation.param -r "Short tstop for testing. One branch populated with spines. Using 10 Gb" -t "onebranch"


K flux investigation
--------------------

::

    bsub -M 4000 -R "rusage[mem=4000]" smt run param/short_tstop_k_flux_investigation.param -r "Testing different calcium sampling" -t "k_flux"

Long tStop test
---------------

::
	
	bsub -M 4000 -R "rusage[mem=4000]" -q research-rh6 smt run param/long_tstop.param -r "Running a long simulation." -t "test, twospines"

    bsub -M 10000 -R "rusage[mem=6000]" -q research-rh6 smt run param/long_tstop_double_stim_two_spines.param -r "Running a double excitation with two spines." -t "twospines"
    
    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/long_tstop_double_stim_all_spines.param -r "Running a double excitation with two spines." -t "all"
    
    bsub -M 10000 -R "rusage[mem=6000]" -q research-rh6 smt run param/long_tstop_one_pulse.param -r "Running one pulse event in one spine." -t "twospines"

One branch stim
---------------

::

    bsub -M 10000 -R "rusage[mem=6000]" -q research-rh6 smt run param/long_tstop_onebranch_several_stimulation.param -r "Several stims across one branch populated with spines. Using 10 Gb" -t "onebranch"
    
    bsub -M 10000 -R "rusage[mem=6000]" -q research-rh6 smt run param/long_tstop_onebranch_1_spine_1Hz.param -r "One branch: One spine double stim. 1Hz. Using 10 Gb" -t "onebranch"
    
    bsub -M 10000 -R "rusage[mem=6000]" -q research-rh6 smt run param/long_tstop_onebranch_1_spine_4Hz.param -r "One branch: One spine double stim. 4Hz. Using 10 Gb" -t "onebranch"
    
    bsub -M 10000 -R "rusage[mem=6000]" -q research-rh6 smt run param/long_tstop_onebranch_1_spine_8Hz.param -r "One branch: One spine double stim. 8Hz. Using 10 Gb" -t "onebranch"
    
    bsub -M 10000 -R "rusage[mem=6000]" -q research-rh6 smt run param/long_tstop_onebranch_1_spine_20Hz.param -r "One branch: One spine double stim. 20Hz. Using 10 Gb" -t "onebranch"
    
    bsub -M 10000 -R "rusage[mem=6000]" -q research-rh6 smt run param/long_tstop_onebranch_1_spine_50Hz.param -r "One branch: One spine double stim. 50Hz. Using 10 Gb" -t "onebranch"
    
    bsub -M 10000 -R "rusage[mem=6000]" -q research-rh6 smt run param/long_tstop_onebranch_1_spine_100Hz.param -r "One branch: One spine double stim. 100Hz. Using 10 Gb" -t "onebranch"

    
All Branches - Double stim one spine    
------------------------------------

::

    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/long_tstop_allspines_1_spine_1Hz.param -r "All spines: One spine double stim. 1Hz. Using 10 Gb" -t "all"
    
    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/long_tstop_allspines_1_spine_4Hz.param -r "All spines: One spine double stim. 4Hz. Using 10 Gb" -t "all"
    
    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/long_tstop_allspines_1_spine_8Hz.param -r "All spines: One spine double stim. 8Hz. Using 10 Gb" -t "all"
    
    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/long_tstop_allspines_1_spine_20Hz.param -r "All spines: One spine double stim. 20Hz. Using 10 Gb" -t "all"
    
    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/long_tstop_allspines_1_spine_50Hz.param -r "All spines: One spine double stim. 50Hz. Using 10 Gb" -t "all"
    
    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/long_tstop_allspines_1_spine_100Hz.param -r "All spines: One spine double stim. 100Hz. Using 10 Gb" -t "all"

All branches - CPM
------------------

::

    bsub -M 10000 -R "rusage[mem=6000]" -q research-rh6 smt run param/long_tstop_onebranch_clustered_plasticity_model.param -r "One branch: Clustered Plasticity Model. 9 spines stimulated. 20 Hz. Using 10 Gb" -t "onebranch"
    
    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/long_tstop_allbranch_cpm_two_branches_stims_8_Hz.param -r "CPM 2 branches, all spine 8 Hz. Using 60 Gb of RAM" -t "all"
    
    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/long_tstop_allbranch_cpm_two_branches_stims_20_Hz.param -r "CPM 2 branches, all spine 20 Hz. Using 60 Gb of RAM (5seg med)" -t "all"
    
    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/long_tstop_allbranch_cpm_two_branches_stims_40_Hz.param -r "CPM 2 branches, all spine 40 Hz. Using 60 Gb of RAM (5seg med)" -t "all"
    
    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/long_tstop_allbranch_cpm_two_branches_stims_50_Hz.param -r "CPM 2 branches, all spine 50 Hz. Using 60 Gb of RAM (5seg med)" -t "all"
    
    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/long_tstop_allbranch_cpm_two_branches_stims_40_Hz_long_train.param -r "CPM 2 branches, all spine 40 Hz long stimulation. Using 60 Gb of RAM (5seg med)" -t "all"   


Kir_investigation
-----------------

::

    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/long_tstop_allbranch_cpm_two_branches_stims_20_Hz.param -r "Kir Investigation kir_gkbar=0.00014" -t "all" kir_gkbar=0.00014

    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/long_tstop_allbranch_cpm_two_branches_stims_20_Hz.param -r "Kir Investigation kir_gkbar=0.00018" -t "all" kir_gkbar=0.00018

    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/long_tstop_allbranch_cpm_two_branches_stims_20_Hz.param -r "Kir Investigation kir_gkbar=0.00012" -t "all" kir_gkbar=0.00012

    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/long_tstop_allbranch_cpm_two_branches_stims_20_Hz.param -r "Kir Investigation kir_gkbar=0.00020" -t "all" kir_gkbar=0.00020

Neighbours spine investigation
------------------------------

::

    bsub -M 60000 -R "rusage[mem=20000]" -q research-rh6 smt run param/neighbouring_spine_20Hz.param -r "Neighboring spine with bio on" -t "all, neighbouring"

Reading simulations' results
----------------------------

Reload the storage.h5 file with neuronvisio::

    run nrnvisio path/to/Sim/storage.h5

EcellManager
============

Used to launch the biochemical alone for testing.

Launching the simulations
-------------------------

This is for the weight checking::

    bsub -M 4000 -R "rusage[mem=4000]" smt run -m ecellControl/ecellManager.py ecellControl/ecellControl.param -r "Testing AMPA weight"

Reading simulations' results
----------------------------

Open an ipython and run::

    run helpers/plotter path/to/TimeCourses
