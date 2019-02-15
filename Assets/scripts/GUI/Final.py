# -*-coding:utf-8 -*
from bge import logic
import scripts.GameSave.SaveBloc as svBl
import scripts.GameSave.SaveGame as SaveGame
import scripts.Ressources.I18n as inter

def Main(cont):

	hud = SaveGame.load("hud.gs")

	path = logic.expandPath("//lang/"+str(inter.getLang())+"/final.lg")
	fileInstance = open(path,'r',encoding='utf-8')
	tabInstance = eval(fileInstance.read())
	
	fu = tabInstance[cont.owner.name].format(str(hud["nbClim"]))
	
	cont.owner["Text"] = fu