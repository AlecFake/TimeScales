# Michele Mattioni
# Thu May 21 11:46:55 BST 2009

import visual
import visual.graph
from neuron import h
import logging



#create logger

class Visio(object):
    
    def __init__(self):
        
        self.scene = visual.display(title="nrnVisio")
        self.cyl2sec = {}
        self.drawModel()
        self.vecRefs = []
        self.logger = logging.getLogger("nrnVisio.Visio")
        self.logger.setLevel(logging.DEBUG)
        #create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        #create formatter
        formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
        #add formatter to ch
        ch.setFormatter(formatter)
        #add ch to logger
        self.logger.addHandler(ch)

        self.logger.debug("Starting Visio")

        
        
    def getVec(self,sec, var=None):
        """Return the vecs that record given a section
        
        param: 
            sec - Section of interest
            var - if None return all the vectors that record in that section
            as a list, otherwise return the vector that record the variable var"""
        vecsSection = [] 
        for vecRef in self.vecRefs:
            if vecRef.sec == sec:
                if var is None:
                    vecsSection.append(vecRef.vec)
                elif var == vecRef.var:
                    return vecRef.vec
        
        return vecsSection
                        
    
    def pickSection(self):
        self.logger.info("Click on the section of interest")
        while(True):
            if self.scene.mouse.clicked:
                 m = self.scene.mouse.getclick()
                 loc = m.pos
                 self.logger.debug(loc)
                 picked = m.pick
                 if picked:
                     picked.color = (0,0,1) #blue
                     sec = self.cyl2sec[picked]
                     return sec
                     
                     #print "Section: %s Name: %s" %(sec, sec.name())
    
    
    
    def createVector(self, var):
        sec = self.pickSection()
        vecNotPresent = True
        for vecRef in self.vecRefs:
            print "Searched: var %s, sec %s.\tCurrent var: %s sec: %s" %(var, sec, vecRef.var, vecRef.sec) 
            if vecRef.var == var and vecRef.sec == sec:
                  vecNotPresent = False
                  break
        if vecNotPresent:      
            vec = h.Vector()
            varRef = '_ref_' + var
            vec.record(getattr(sec(0.5), varRef))
            vecRef = VecRef(var, vec, sec)
            self.vecRefs.append(vecRef)
        return sec     

    def plotVector(self, tPoints, varPoints):
        funct = visual.graph.gcurve()
        try:
             for i in range(int (tPoints.size() )):
                 curve.plot(pos=(tPoints[i], varPoints[i]))
        except LookupError:
            self.logger.warning("At least one of the vector seems to be empty.\n\
            Please run the simulation first")
        
        return funct
                       
    def retrieveCoordinate(self, sec):
        coords = {}
        sec.push()
        #self.logger.debug( "section: %s n3d: %d" %(sec.name(),h.n3d()))
        coords['x0'] = h.x3d((h.n3d()- h.n3d()))
        coords['x1'] = h.x3d((h.n3d()- 1))
        coords['y0'] = h.y3d((h.n3d()- h.n3d()))
        coords['y1'] = h.y3d((h.n3d()- 1))
        coords['z0'] = h.z3d((h.n3d()- h.n3d()))
        coords['z1'] = h.z3d((h.n3d()- 1))
        h.pop_section()
        return coords
        
    
    def drawSection(self, sec):
        coords = self.retrieveCoordinate(sec)
        x_ax = coords['x1'] -coords['x0']
        y_ax = coords['y1'] -coords['y0']
        z_ax = coords['z1'] -coords['z0']
        cyl = visual.cylinder(pos=(coords['x0'],coords['y0'],coords['z0']), 
                          axis=(x_ax,y_ax,z_ax), radius=sec.diam/2)
        
        self.cyl2sec[cyl] = sec
    
    def visualizeSectionPotential(self):
        pass
    
    
    def findSecs(self, secList, secName):
        selectedSec = None
        for sec in secList:
            if hasattr(sec, "head"): # it's a spine
                spines_attr = ["head","neck","psd"]
                for attr in spines_attr:
                    #print attr, sec.__dict__[attr].name(), secName    
                    if sec.__dict__[attr].name() == secName:
                        selectedSec = sec
                        print "Found sec %s, spine %s" %(sec.__dict__[attr].name(), sec.id)
                        break
            else: # Normal secion
            
                if sec.name() == secName:
                    selectedSec = sec
                    break
        if selectedSec is None:
            return ""    
            
        return selectedSec
    
    def drawModel(self):
        
        h.define_shape()
        for sec in h.allsec():
            self.drawSection(sec)

class VecRef(object):
    
    def __init__(self, var, vec, sec):
        self.var = var
        self.vec = vec
        self.sec = sec


        