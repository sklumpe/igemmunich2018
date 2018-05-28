#!/usr/bin/env python2

from interface import TagInserter as Base
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
        cmd.do("color "+stickColors[0]+", not pol")
        cmd.do("util.cnc('not pol')")

    def loadModel(self,path,form):
        if form=="pdb" or form=="prmtop":
            try:
                cmd.load(path, "obj"+str(self.count),0,form )
                self.count+=1
            except:
                print("Something went wrong when loading the PDB file")
        else:
            print("Unsupported File Format.")

    def zoom(self, model, sel):
        cmd.do("zoom " + str(model) + " and " + str(sel))

