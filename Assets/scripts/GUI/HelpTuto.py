# -*-coding:utf-8 -*
from bge import logic
import scripts.GameSave.SaveBloc as svBl
import scripts.GameSave.SaveGame as sg
import DlgInvocation

def CreateButton(cont):
	scn = logic.getCurrentScene()
	own = cont.owner
	logic.mouse.visible = True
	helpFile = sg.loadInstance("Cont/help")
	if helpFile["nbTuto"] > own["tutoID"]:
		
		scn.addObject("help.tuto.gen", own)
		own.position.y -= 0.5
		own["tutoID"] += 1
		logic.globalDict["help.selectable"] = False
	else:
		logic.globalDict["help.selectable"] = True
def getNameOfTuto(cont):

	scn = logic.getCurrentScene()
	own = cont.owner
	helpFile = sg.loadInstance("Cont/help")
	root = scn.objects["help.genButton"]
	superoot = scn.objects["pause.help"]
	bt = own.parent.children[1]
	own.parent.setParent(superoot)
	own["Text"] = helpFile["tuto"+str(root["tutoID"])]["name"]
	bt["tuto"] = "tuto"+str(root["tutoID"])
	
def lauchDialogs(cont):
	own = cont.owner
	scn = logic.getCurrentScene()
	if cont.sensors["l"].positive and cont.sensors["o"].positive and logic.globalDict["help.selectable"]:
		helpFile = sg.loadInstance("Cont/help")
		own["dlg.name"] = helpFile[own["tuto"]]["dlgInvoke"]
		dat = sg.load("tmp/__dialogs__.gs")
		dat[own["dlg.name"]] = 0
		sg.save(dat,"tmp/__dialogs__.gs")
		
		root = scn.objects["pause.help"]
		DlgInvocation.RegDlgAt(helpFile[own["tuto"]]["startAt"])
		logic.mouse.visible = False
		
		root.endObject()
		
		
		
		