# Author: Michele Mattioni
# Tue Nov 11 11:54:40 GMT 2008

import neuron
from neuron import h
import numpy
import os
import sys

from spine import *
from synapse import Synapse
from helpers.loader import Loader


class Event():
    """Event will be added to the cvode queue list"""
    def __init__(self, eventTime, cvode, nrnSim):
        self.eventTime = eventTime
        self.cvode = cvode
        self.fih = h.FInitializeHandler(1, self.callback)
        
    def callback(self, eventTime, nrnSim) :
        print "event at %f " %h.t
        self.cvode.event(self.eventTime, self.callback(eventTime, nrnSim))


class NeuronSim():
    """General class to control NEURON"""
    def __init__(self, hoc_path="hoc", mod_path="mod", msn=True, spines_dist=None,
                 biochemical_filename="biochemical_circuits/biomd183.eml"):
        """Load and initiate all the hoc and mod file. Can load the model of the neuron
        or otherwise can just expose general method"""
        
        # Mod file are always in a mod directory
        if not os.path.exists(mod_path) :
            print "ERROR mod path %s doesn't exist" %os.path.realpath(mod_path)
            sys.exit(1)
        neuron.load_mechanisms(mod_path)
        
        if not os.path.exists(hoc_path):
            print "ERROR hoc path %s doesn't exist" %os.path.realpath(hoc_path)
            sys.exit(1)
        # Hoc file assumes all the file are launched from a top directory
        head, tail  = os.path.split(os.path.realpath(hoc_path))

        preface_pos = head
        
        h('strdef preface, dirstr') # preface and dirstr used in each hoc
        preface_string = "preface = \"" + preface_pos + "\""
        h(preface_string)
        
        if msn:
            # Loading the MSN model
            h.load_file(os.path.join(hoc_path, "nacb_main.hoc"))
            self._set_geometry()
            
            self.biochemical_filename = biochemical_filename
            # Adding the spines
            self.__distributeSpines(spines_dist)
        
        h.load_file("stdrun.hoc")
        h.v_init = -87.75 #Setting the vinit 
        
    def _set_geometry(self):
        """Set the geometry of the Neuron to the normal value, without
        the spine correcting factors applied as in Wolf 2005"""
        for dend in h.MSP_Cell[0].Mid_Dend:
            dend.diam = 1 # um
            dend.L = 20 #um
            
        for dend in h.MSP_Cell[0].Dist_Dend:
            dend.diam = 0.5 #um
            dend.L = 190 #um 
        
        
    def run(self, tStop):
        """Run the simulation until tStop"""
        h.tstop = tStop
        while h.t < h.tstop :
            h.fadvance()
            # update the plotting system here.
        
    def init(self, v_init=-87.75):
        """Initialize the simulator"""
        h.v_init = v_init
        h.finitialize()
        
    def initAndRun(self, tStop):
        """Initialize and run the simulation until tStop""" 
        self.init()
        self.run(tStop)
    
    def __distributeSpines(self, spine_dist):
        """Attach spines to the dendrites"""
        self.spines = {}
        if spine_dist == 'zero':
          pass  
        elif spine_dist == 'two':
            ## Trying some spines only for test
            spine_positions = [0.3, 0.5]
            self.__populateDend(spine_positions, [h.MSP_Cell[0].dend3_1[1]])
        elif spine_dist == 'all':
            l = Loader()
            
            # Mid:
            spines_pos_mid = l.load('branch_dist/mid_spines_per_branch.pickle')
            
            first_half = [h.MSP_Cell[0].dend1_1[0], h.MSP_Cell[0].dend2_1[0], h.MSP_Cell[0].dend3_1[0],
            h.MSP_Cell[0].dend4_1[0]]
            
            self.__populateDend(spines_pos_mid[0], first_half)
            
            second_half = [h.MSP_Cell[0].dend1_2[0], h.MSP_Cell[0].dend2_2[0], h.MSP_Cell[0].dend3_2[0],
            h.MSP_Cell[0].dend4_2[0]]
            
            self.__populateDend(spines_pos_mid[1], second_half)
            
            # Distal:
            spines_pos_dist = l.load('branch_dist/dist_spines_per_branch.pickle')
            
            first_dist = [h.MSP_Cell[0].dend1_1[1], h.MSP_Cell[0].dend2_1[1],
                          h.MSP_Cell[0].dend3_1[1], h.MSP_Cell[0].dend4_1[1]] 
            
            self.__populateDend(spines_pos_dist[0], first_dist)
            
            second_dist = [h.MSP_Cell[0].dend1_1[2], h.MSP_Cell[0].dend2_2[2], 
                           h.MSP_Cell[0].dend3_2[2], h.MSP_Cell[0].dend4_2[2]]
            
            self.__populateDend(spines_pos_dist[1], second_dist)
            
            third_dist = [h.MSP_Cell[0].dend1_2[1], h.MSP_Cell[0].dend2_2[1], 
                          h.MSP_Cell[0].dend3_2[1], h.MSP_Cell[0].dend4_2[1]]
            
            self.__populateDend(spines_pos_dist[2], third_dist)
            
            fourth_dist = [h.MSP_Cell[0].dend1_2[2], h.MSP_Cell[0].dend2_1[2], 
                           h.MSP_Cell[0].dend3_1[2], h.MSP_Cell[0].dend4_1[2]]
            
            self.__populateDend(spines_pos_dist[3], fourth_dist)
        else:
            print "Value for the spine not understood"
            sys.exit()
        
        
        #spine_positions = [0.1, 0.21, 0.23, 0.25, 0.27, 0.29, 0.30, 0.50, 0.7]
        #spine_positions = [0.1, 0.21, 0.25, 0.30, 0.50, 0.7]
        #self.__populateDend(spine_positions, h.MSP_Cell[0].Dist_Dend)
        
        
        # Mid
        #print "Adding the Mid spines"
        #spine_positions = [0.3, 0.7, 0.9]
        #self.__populateDend(spine_positions, h.MSP_Cell[0].Mid_Dend)
    
    def __populateDend(self, spine_positions, dendList):
        """Distribuete the psines among the dends"""
        
        for sec in dendList :
            for pos in spine_positions:
                tmpName = sec.name()
                tmpName = tmpName.split('.')[1] # Get rid of the MSP_Cell[0] prefix
                spine_number = len (self.spines) + 1
                id = 'spine' + str(spine_number)
                # Instantiate the spine with the biochemical model
                spine = Spine(id, filename_bioch_mod=self.biochemical_filename)
                spine.attach(sec, pos, 0) # Attaching the spine in the right pos
                self.spines[spine.id] = spine
                print "Addedd spine: %s, pos %s, sec %s" % (spine.id, pos, sec.name())
                
    def updateSpines(self):
        "Update the calcium inside the spine"
        for spine in self.spines:
            ca_from_NEURON = spine.vecs['ca'].x[-1] 
            spine.ecellMan.ca['Value'] = ca_from_NEURON 
            spine.ecellMan.ses.run(caSamplingInterval)
            print "Equilibrium for spine: %s, dend: %s, bio sim time: %f" % (spine.head.name(), 
                                                                     spine.parent.name(),
                                                                     spine.ecellMan.ses.getCurrentTime())    
    
    def iClampPointProcess(self, delay=100, dur=500, amp=0.2480):
        """Creating an IClamp in the soma"""
        # Creating an ICLAMP just for testing
        
        iClamp = h.IClamp(0.5, sec = h.MSP_Cell[0].soma)
        
        iClamp.delay = delay
        iClamp.dur = dur
        iClamp.amp = amp
        
        return iClamp