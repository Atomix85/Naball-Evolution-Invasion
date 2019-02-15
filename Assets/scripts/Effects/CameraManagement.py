# -*-coding:utf-8 -*
from bge import logic
import scripts.GameSave.SaveGame as sv
import scripts.EntityComponents.Naball as nab
import random


def Main(cont):
	
	own = cont.owner
	scn = logic.getCurrentScene()
	nameCol = own.name
	
	array = sv.loadInstance("Cont/CameraManagement/"+ sv.getSceneAct())
    
	scn.active_camera = scn.objects[array[nameCol]]

def NormalCam(cont):

	cam = cont.actuators['cam']
	cam.height = 5
	cam.min = 10
	cam.max = 20
	
def ZoomCam(cont):

	cam = cont.actuators['cam']
	sound = cont.actuators['flash']
	if logic.globalDict['targetAlr.var1'] == 0:
		cam.height = 1
		cam.min = 7
		cam.max = 7
		cont.activate(sound)
		logic.globalDict['targetAlr.var1'] = 1
	elif logic.globalDict['targetAlr.var1'] == 2:
		cam.height = 5
		cam.min = 10
		cam.max = 10
		cont.activate(sound)
		logic.globalDict['targetAlr.var1'] = 1
def CameraFollowing(cont):
	cam = cont.actuators['cam']
	naballObj = logic.getCurrentScene().objects[nab.getNaball()]
	
	objHit = cont.owner.rayCast(naballObj, cont.owner, 0.0, "wall", 0, 1, 0)
	
	if str(objHit[0]) != "None":
		cam.height = 0.1
		cam.min = 0.1
		cam.max = 0.1
		
	else:
	
		if logic.globalDict['targetAlr']:
			ZoomCam(cont)
		else:
			NormalCam(cont)
			logic.globalDict['targetAlr.var1'] = 0
	
	
	
	
	cont.activate(cam)
	