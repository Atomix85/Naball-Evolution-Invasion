# -*-coding:utf-8 -*
from bge import logic
import os
import scripts.GameSave.SaveGame as SaveGame
import scripts.EntityComponents.Naball as nab

path = logic.expandPath(os.environ['APPDATA'] + "//Naball/")

defautlPw = {"Move" : False,"Jump" : False, "Eta": False, "Solidify": False}

getPw =  {"Move" : 1, "Jump": 2,"Eta": 3, "Solidify" : 4}

def getNbAto():

	hud = logic.getSceneList()[1]
	nbAto = hud.objects['Hud.nbAto']['nb']
	
	return nbAto

def addPower(cont):
	
	own = cont.owner
	edi = cont.actuators['par']
	try:
		arrayPower = SaveGame.load("power.gs")
	except:
		arrayPower = defautlPw
	
	for pw in getPw:
		if getNbAto() >= getPw[pw]:
			if not arrayPower[pw]:
				cont.activate(edi)
				arrayPower[pw] = True
	SaveGame.save(str(arrayPower),"power.gs")
	if own["pw"] == "Move":
		MovePw(True)
	
def ShootPw(activate)	:
	scn = logic.getCurrentScene()
	etaObj = scn.objects[SaveGame.getSceneAct()+'.eta']
	if activate:
		etaObj['CanShoot'] = True
		etaObj.state = 1
	else:
		etaObj['CanShoot'] = False
		etaObj.state = 2
		logic.sendMessage("unShow","","Target")
		logic.globalDict['targetAlr'] = False
		
def MovePw(activate)	:
	scn = logic.getCurrentScene()
	naball = scn.objects[nab.getNaball()]
	if activate:
		naball['CanDN'] = True
		naball['CanRun'] = True
	else:
		naball['CanDN'] = False
		naball['CanRun'] = False
		
def JumpPw(activate)	:
	scn = logic.getCurrentScene()
	naball = scn.objects[nab.getNaball()]
	if activate:
		naball['CanJump'] = True
	else:
		naball['CanJump'] = False
		
def SolidifyPw(activate)	:
	scn = logic.getCurrentScene()
	if scn.name == "Underground":
		obs = scn.objects[nab.getNaball()].children[3]
	else:
		obs = scn.objects[nab.getNaball()].children[0]
	if activate:
		obs["act"] = True
	else:
		obs["act"] = False
		
def PowerActive():

	
	own = logic.getCurrentController().owner
	specialPw = logic.globalDict['pw']
	arrayPower = SaveGame.load("power.gs")
	if arrayPower["Move"]:
		MovePw(True)
	if arrayPower["Jump"]:
		JumpPw(True)
	
	if specialPw == 0 and arrayPower["Eta"]:
		ShootPw(True)
		SolidifyPw(False)
	elif specialPw == 1 and arrayPower["Solidify"]:
		SolidifyPw(True)
		ShootPw(False)
	else:
		ShootPw(False)
		SolidifyPw(False)
		
def getLilySeed(cont):

	if cont.sensors["1"].positive and cont.sensors["2"].positive:
		hudSav = SaveGame.load("hud.gs")
		hudSav["haveLilySeed"] = True
		SaveGame.save(str(hudSav),"hud.gs")
		cont.activate(cont.actuators["comp"])
		if cont.owner["prop"] == 0:
			logic.sendMessage("Add","","Hud.Bar_life")
		cont.owner["prop"] = 1
		logic.sendMessage("GenEnn","","swp1.genTer.003")
		