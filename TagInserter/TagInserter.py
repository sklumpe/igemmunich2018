#!/usr/bin/env python3

from pymol import stored
from pymol import cmd

class TagInserter(Base):

    def __init__(self):


    def showModel(self, model):
        cmd.do("hide")
        cmd.do("bg_color white")
        cmd.do("show cartoon, "+ str(model))
        cmd.do("show spheres, all and not bound_to all")
        cmd.do("util.cnc('all and not bound_to all')")
        cmd.do("show sticks, not pol")
        cmd.do("util.cnc('not pol')")

    def loadModel(self,path,form):
        if form=="pdb" or form=="prmtop":
            try:
                cmd.load(path, "obj1",0,form )
            except:
                print("Something went wrong when loading the PDB file")
        else:
            print("Unsupported File Format.")

    def zoom(self, model, sel):
        cmd.do("zoom " + str(model) + " and " + str(sel))

    def Model_structure():
    '''
    Given a peptide sequence, models the 3D structure using Rosetta
    '''

    def InsertTag(self, model_sequence, model_sstruc, tag_sequence):

    '''
    A Bioinfo Tool that creates a new peptide sequence based on the secondary structure prediction and
    the given TAG sequence. Secondary structure prediciton using Machine Learning maybe?
    '''

    def evaluate_model(self, 3d_prediction, initial_model, evaluation_method):
    '''
    Takes initial 3D Structure without Tag and 3D structure predicted from Rosetta with Tag and evaluates the two
    structures on behalf of secondary structure, 3D RMSD, ... (whatever one can think of)
    '''



