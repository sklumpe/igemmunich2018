#!/usr/bin/env python3

from TagInserter import TagInserter
import pymol
from pymol import cmd
from time import sleep
pymol.finish_launching()



inserter=TagInserter()
inserter.loadModel("test.pdb","pdb")
