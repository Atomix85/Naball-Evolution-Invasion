# -*-coding:utf-8 -*
from bge import logic
import os
import scripts.GameSave.SaveGame as SaveGame
import scripts.Ressources.I18n as I18n
import time

path = logic.expandPath(os.environ['APPDATA'] + "//Naball/")


def get_list():
	
	i = 1
	while i <= 4:
		if os.path.exists(path+"save"+str(i)+"/"):
			print("save_"+str(i))
			logic.sendMessage("Found","","save_"+str(i))
		i += 1
			
def get_elements():
	own = logic.getCurrentController().owner
	file = open(path+"save"+str(own['reg'])+"/"+"stats.gs",'r')
	line = eval(file.read())
	file.close()
	scn = logic.getCurrentScene()
	clims = scn.objects[own['clims']]
	ato = scn.objects[own['ato']]
	percent = scn.objects[own['percent']]
	time = scn.objects[own['time']]
	func_1 = I18n.getLang()
	elementsBloc = {}
	if func_1 == 'fr' or func_1 == 'en' or func_1 == 'es' or func_1 == 'de':
		elementsBloc = {'clims':' Clims','ato':' Atomiums'}
	elif func_1 == 'ru':
		elementsBloc = {'clims':' Климс','ato':' Атомюмс'}
	else:
		print('Problème avec la langue !!')
		
	clims['Text'] = str(line["clims"]) + str(elementsBloc['clims'])
	ato['Text'] = str(line["ato"]) + str(elementsBloc['ato'])
	percent['Text'] = str(int(line["percent"])) + " %"
	time['Text'] = str(line["lastSession"]['time'])
	
def statsUpdate():
	hudFile = open(str(SaveGame.getPathBloc())+'hud.gs','r') #Charge MainPath + NomDuBloc + Hud.gs
	hudArray = eval(hudFile.read())
	hudFile.close()
	
	array = {'lastSession': {'level': -1,'time': '',},'__INIT__': 'statsInstance','clims': 0,'ato': 0,'percent': 0}
	array['lastSession']['time'] = time.strftime("%d/%m/%y-%H:%M", time.gmtime())
	array['clims'] = hudArray['nbClim']
	array['ato'] = hudArray['nbAto']
	array['percent'] = int(hudArray["nbClim"] * 100 / 92)
	SaveGame.save(array,"stats.gs")