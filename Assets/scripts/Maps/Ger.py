import bge
import scripts.GameSave.SaveGame as SaveGame



def lightVariation(cont):
	scn = bge.logic.getCurrentScene()
	sun = cont.owner
	world = scn.world
	spe = scn.objects["ger.spectr"]
	ger = SaveGame.load("ger.gs")
	alr = ger["alr"]
	
	if alr == 1:
		sun.energy = 0.1
		spe.color = [1,1,1,0]
		#world.mistEnable = True
		#world.mistStart = 40.0
		#world.mistDistance = 60.0
	elif alr == 2:
		spe.color = [1,1,1,0.1]
		sun.energy = 0.2
	elif alr == 3:
		spe.color = [1,1,1,1]
		sun.energy = 1.5
	
	
def situationVariation(cont): 
	#Cette fonction gère à partir du 'niveau maximal atteint' la position de spawn des objets
	#dynamiques(caméras, naball...), du spawn exclusif de certains personnages et aussi des
	#différents dialogues interprétés
	scn = bge.logic.getCurrentScene()
	ger = SaveGame.load("ger.gs")
	alr = ger["alr"]
	
	array1 = SaveGame.loadInstance("Cont/ger")["cond" + str(alr)]
	for objAssign in array1:

		if len(array1[objAssign]) == 2:
			objScn = scn.objects[objAssign]
			objScn[array1[objAssign][0]] = array1[objAssign][1]
		elif len(array1[objAssign]) == 3:
			objScn = scn.objects[objAssign]
			objScn.position = array1[objAssign]
	for obj in scn.objects:
		if "alr" in obj:
			obj["alr"] = alr