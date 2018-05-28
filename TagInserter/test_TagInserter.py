#!/usr/bin/env python2

from TagInserter import TagInserter
import pymol
from pymol import cmd
from time import sleep
pymol.finish_launching()



inserter=TagInserter()
#default hiding everything
#cmd.do("hide everything")


inserter.loadModel("test.pdb","pdb")





#

