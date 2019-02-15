from bge import logic
import os
import scripts.GameSave.SaveGame as SaveGame
import scripts.Ressources.Hud as hud


def main():
	"""Fonction qui initialise l'entitée de chaques Clims depuis le tableau du niveau"""
	scnAct = logic.getCurrentScene()#Obtient le nom de la scène actuelle
	logic.globalDict['folder_save'] = 'save1/' #Définie l'entité du bloc de sauvegarde
	lvlStorage = open(str(SaveGame.getPathBloc())+str(SaveGame.getSceneAct())+'.gs','r') #Charge NomDuBloc + NomDeLaScene + .gs
	tabClims = eval(lvlStorage.read())['clims'] #Obtient le tableau des Clims du niveau
	for obj in tabClims: 
		try: #Clim trouvé et associé
			nameObj = str(SaveGame.getSceneAct()+"."+str(obj)) #Initialise le nom du Clims dans le niveau : NomDeLaScène + . + NomDuClimsDansLeTableau
			clim = scnAct.objects[nameObj] #Ouvre l'instance du Clims
			if tabClims[obj] == 1: #Supprime l'initialisateur si le Clims a déjà été ramassé
				clim.endObject() #Fonction de suppression
				print(obj+" removed !")
		except: #Erreur : Clims introuvable sur la scène
			print("A clim isn't identified : "+ obj)
	lvlStorage.close()		
			
def finalSave():
	"""Fonction qui sauvegarde l'entitée de chaques Clims dans le tableau du niveau"""
	scnAct = logic.getCurrentScene()
	logic.globalDict['folder_save'] = 'save1/'
	lvlStorage = open(str(SaveGame.getPathBloc())+str(SaveGame.getSceneAct())+'.gs','r')
	array = eval(lvlStorage.read())
	lvlStorage.close()
	arrayClims = array['clims']
	for obj in scnAct.objects:
		if "spw" in obj:
			val_58 = obj.name.split(".",1)[1]
			arrayClims[val_58] = obj["spw"]
			SaveGame.save(array,str(SaveGame.getSceneAct())+".gs")
	
	hud.hudSave()	