# -*-coding:utf-8 -*
import aud
import bge

import scripts.GameSave.SaveGame as sv
import scripts.EntityComponents.Naball as nab

import random



listStep = ["PASBOIP3.wav", "pasgril1.wav", "PASHERB2.wav"]
def Main(cont):
	own = cont.owner
	device = aud.device()
	lvl = bge.logic.getSceneList()[0]
	naballObj = lvl.objects[nab.getArrayNaball()[lvl.name]]
	path = bge.logic.expandPath("//sounds\\")
	keyboard = bge.logic.keyboard
	JUST_ACTIVATED = bge.logic.KX_SENSOR_ACTIVE
	sounds = cont.actuators["s"]
	
	posDown = [naballObj.position.x, naballObj.position.y, naballObj.position.z - 2]
	
	RAYCAST = naballObj.rayCast(naballObj, posDown, 0.0, "",1,1,0)
	if  RAYCAST[0] != None:
		
		if "s1" in RAYCAST[0]:
			path += listStep[0]
		elif "s2" in RAYCAST[0]:
			path += listStep[1]
		elif "s3" in RAYCAST[0]:
			path += listStep[2]
		else:
			path += listStep[0]
		factory = aud.Factory.file(path)
	
		if keyboard.events[bge.events.UPARROWKEY] == JUST_ACTIVATED and own["tics"] > 30:
			device.play(factory)
			own["tics"] = 0
		if keyboard.events[bge.events.UPARROWKEY] == JUST_ACTIVATED and keyboard.events[bge.events.LEFTSHIFTKEY] == JUST_ACTIVATED and own["tics"] > 15:
			device.play(factory)
			own["tics"] = 0
	
	own["tics"] += 1