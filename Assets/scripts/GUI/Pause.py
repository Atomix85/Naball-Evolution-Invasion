# -*-coding:utf-8 -*
from bge import logic
import scripts.GameSave.SaveBloc as svBl

def ExitSaveButton():

	scn = logic.getCurrentScene()
	cont = logic.getCurrentController()
	obj = cont.owner
	
	
	if cont.sensors['ov'].positive and cont.sensors['cl'].positive:
		svBl.statsUpdate()
		logic.getSceneList()[0].replace("Menu")
		logic.globalDict['pause.isInvocated'] = False
		logic.mouse.visible = False
		logic.getSceneList()[1].end()
		
def ReturnButton():

	scn = logic.getCurrentScene()
	cont = logic.getCurrentController()
	obj = cont.owner
	
	
	if cont.sensors['ov'].positive and cont.sensors['cl'].positive:
		cont.activate(cont.actuators['rem'])
		
	
def HelpButton():

	scn = logic.getCurrentScene()
	cont = logic.getCurrentController()
	obj = cont.owner
	
	
	if cont.sensors['ov'].positive and cont.sensors['cl'].positive:
		contForm = scn.objects["hud.pause"]
		scn.addObject("pause.help", contForm)
		logic.sendMessage("Return", "", "hud.pause")
		
		
def CartButton():
	scn = logic.getCurrentScene()
	cont = logic.getCurrentController()
	obj = cont.owner
	
	
	if cont.sensors['ov'].positive and cont.sensors['cl'].positive:
		logic.addScene("Cart_world",1)

def Invocation():
	cont = logic.getCurrentController()
	obj = cont.owner
	echap = cont.sensors['ech']
	try:
		if not logic.globalDict['pause.isInvocated']:
			cont.activate(cont.actuators['ps'])
			logic.globalDict['pause.isInvocated'] = True
			logic.getSceneList()[0].suspend()
			logic.mouse.visible = True
			
	except:
		logic.globalDict['pause.isInvocated'] = False
		print("Des")
		
def Reinit():
	logic.globalDict['pause.isInvocated'] = False
	logic.getSceneList()[0].resume()
	logic.mouse.visible = False
	print("Des")