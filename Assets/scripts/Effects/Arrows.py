# -*-coding:utf-8 -*
from bge import logic
import scripts.GameSave.SaveGame as sv
import random

def Main(cont):

	try:
		scn = logic.getCurrentScene()
		own = logic.getCurrentController().owner
	
	
		array = sv.loadInstance("Cont/Arrows/"+ sv.getSceneAct())
		
		temp1 = array["a"+str(logic.globalDict['arrowsId'])]
	
		own.position = temp1["position"]
		edi = cont.actuators["edi"]
		edi.upAxis, edi.trackAxis = temp1["rotation"]
	except:
		pass
	
def Increment(cont):
	own = cont.owner
	logic.globalDict['arrowsId'] = own["id"]
	logic.globalDict['arrowsVisible'] = False
