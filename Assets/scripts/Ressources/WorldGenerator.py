import bge
import scripts.GameSave.SaveGame as sg

class WorldGenerator:

	def __init__(self):
		self.own = bge.logic.getCurrentController().owner
		self.scn = bge.logic.getCurrentScene()
		self.createdObjects = []
		self.objects = sg.loadInstance("Generate/und1/part"+self.own['part'])['objects']
		for obj in self.objects:
			temp = self.scn.addObject(obj)
			self.createdObjects.append(temp)
			if "ANI_LESS" in temp:
				temp.state = 1
			if self.objects[obj] != "own":
				temp.position = self.objects[obj]
				
	# def __del__(self):
		# self.createdObjects = []
		# for obj in self.objects:
			# object = self.scn.objects[obj]
			# object.endObject()
def Delete(Part):
	scn = bge.logic.getCurrentScene()
	objects = sg.loadInstance("Generate/und1/part"+Part)['objects']
	for obj in objects:
		objet = scn.objects[obj]
		objet.endObject()
def Main(cont):
	own = cont.owner
	if own["part"] != "0":
		try:
			temp = bge.logic.globalDict["scn.loaded"+own["part"]]
		except:
			bge.logic.globalDict["scn.loaded"+own["part"]] = WorldGenerator()
			print("Partie "+own["part"]+ " créée !")
	if own["partDel"] != "0":
		try:
			Delete(own["partDel"])
			del bge.logic.globalDict["scn.loaded"+own["partDel"]]
			print("Partie "+own["partDel"]+ " supprimée !")
		except:
			pass
