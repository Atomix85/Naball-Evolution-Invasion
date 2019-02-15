# -*-coding:utf-8 -*
from bge import logic
import scripts.GameSave.SaveGame as sv
#
#
#
#

def getNameNaball(cont):

	scn = logic.getCurrentScene()
	array = sv.loadInstance("Cont/NameObjects/Naball")

	edi = cont.actuators['edi']
	
	edi.object = scn.objects[array[scn.name]]

def getNaball():

	scn = logic.getCurrentScene()
	array = sv.loadInstance("Cont/NameObjects/Naball")
	return array[scn.name]
	
def getArrayNaball():
	return sv.loadInstance("Cont/NameObjects/Naball")
