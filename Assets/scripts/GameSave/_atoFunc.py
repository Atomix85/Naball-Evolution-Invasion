from bge import logic
import os
import scripts.GameSave.SaveGame as SaveGame


def main():
	"""Fonction qui initialise l'entitée de chaques Clims depuis le tableau du niveau"""
	scnAct = logic.getCurrentScene()#Obtient le nom de la scène actuelle
	lvlStorage = open(str(SaveGame.getPathBloc())+str(SaveGame.getSceneAct())+'.gs','r') #Charge NomDuBloc + NomDeLaScene + .gs
	mainAto = eval(lvlStorage.read())['ato'] #Obtient le tableau des Clims du niveau
	try: #Cage trouvé et associé
		nameObj = str(SaveGame.getSceneAct())+".ato" #Initialise le nom de la cage dans le niveau : NomDeLaScène + . + NomDuCageDansLeTableau
		ato = scnAct.objects[nameObj] #Ouvre l'instance de la cage
		if mainAto == 1: #Supprime l'initialisateur si le Cage a déjà été brissé
			ato.endObject() #Fonction de suppression
			print(nameObj+" removed !")
	except: #Erreur : Cage introuvable sur la scène
		pass
	
	lvlStorage.close()
	
def alrUpdate(cont):
	lvlStorage = open(str(SaveGame.getPathBloc())+str(SaveGame.getSceneAct())+'.gs','r')
	array = eval(lvlStorage.read())
#Enregistre que le niveau à déjà été visité
	lvlStorage.close()
	if array['alr'] == 0:
		array['alr'] = 1
		#Change l'état de GER
		gerStorage = SaveGame.load("ger.gs")
		if cont.owner["dej"] >= gerStorage["alr"]:
			gerStorage["alr"] = cont.owner["dej"]
		SaveGame.save(gerStorage,"ger.gs")
		
def finalSave(cont):
	"""Fonction qui sauvegarde l'entitée de chaques Clims dans le tableau du niveau"""
	scnAct = logic.getCurrentScene()
	logic.globalDict['folder_save'] = 'save1/'
	lvlStorage = open(str(SaveGame.getPathBloc())+str(SaveGame.getSceneAct())+'.gs','r')
	array = eval(lvlStorage.read())
	lvlStorage.close()
	atoObj = scnAct.objects[str(SaveGame.getSceneAct())+".ato"]
	if "spwAt" in atoObj:
		val_58 = atoObj.name.split(".",1)[1]
		array['ato'] = atoObj["spwAt"]
		SaveGame.save(array,str(SaveGame.getSceneAct())+".gs")
	alrUpdate(cont)
	