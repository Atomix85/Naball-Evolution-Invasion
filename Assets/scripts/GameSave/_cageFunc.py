from bge import logic
import os
import scripts.GameSave.SaveGame as SaveGame


def main():
	"""Fonction qui initialise l'entitée de chaques Cages depuis le tableau du niveau"""
	scnAct = logic.getCurrentScene()#Obtient le nom de la scène actuelle
	lvlStorage = open(str(SaveGame.getPathBloc())+str(SaveGame.getSceneAct())+'.gs','r') #Charge NomDuBloc + NomDeLaScene + .gs
	tabClims = eval(lvlStorage.read())['cages'] #Obtient le tableau des cages du niveau
	for obj in tabClims: 
		try: #Cage trouvé et associé
			nameObj = str(SaveGame.getSceneAct()+"."+str(obj)) #Initialise le nom de la cage dans le niveau : NomDeLaScène + . + NomDuCageDansLeTableau
			clim = scnAct.objects[nameObj] #Ouvre l'instance de la cage
			if tabClims[obj] == 1: #Supprime l'initialisateur si le Cage a déjà été brissé
				clim.endObject() #Fonction de suppression
				print(obj+" removed !")
		except: #Erreur : Cage introuvable sur la scène
			print("A cage isn't identified : "+ obj)
	lvlStorage.close()		
			
def finalSave():
	"""Fonction qui sauvegarde l'entitée de chaques Cages dans le tableau du niveau"""
	scnAct = logic.getCurrentScene()
	logic.globalDict['folder_save'] = 'save1/'
	lvlStorage = open(str(SaveGame.getPathBloc())+str(SaveGame.getSceneAct())+'.gs','r')
	array = eval(lvlStorage.read())
	lvlStorage.close()
	arrayClims = array['cages']
	for obj in scnAct.objects:
		if "spwCag" in obj:
			val_58 = obj.name.split(".",1)[1]
			arrayClims[val_58] = obj["spwCag"]
			SaveGame.save(array,str(SaveGame.getSceneAct())+".gs")
		