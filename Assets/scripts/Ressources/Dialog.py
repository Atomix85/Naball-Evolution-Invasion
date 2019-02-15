import bge
import scripts.GameSave.SaveGame as sv
import scripts.Ressources.I18n as inter

path = bge.logic.expandPath("//lang/")

#DialogsEngine 1.05
#Create By Bretelle Alan

class dlgComponent:
	"""Cette classe permet de charger les dialogues du
	jeu depuis l'adresse dlg vers les composents du fichier
	cible dans \'lang\'"""
	arrColor = {"Default": [1,1,1,1],
	"G1": [0,1,0,1],#vert
	"R": [1,0,0,1],#rouge
	"B1": [0,0,1,1],#Bleu
	"P": [1,0,1,1],#Violet
	"C": [0,1,1,1],#Cyan
	"B2": [0,0,0,1],#Noir
	"G2": [0.1,0.1,0.1,1],#Gris
	"O": [1,0.25,0,1],#Orange
	"Alpha": [0,0,0,0],#Cyan
	"Y": [1,1,0,1]}#Jaune
	def __init__(self,file,id,syntaxeEnabled=True):
		"""Initialise nos constructeurs"""
		self.file = file
		self.id = id
		self.syntaxeEnabled = syntaxeEnabled
		
	def loadDlg(self):
		"""Renvoie les données du fichier"""
		try:
			file = open(path+str(inter.getLang())+"\\"+self.file,'r')
			return eval(file.read().encode("latin-1"))
		except:
			return None
			
	def f_dlg_1(self,i):
		"""Décompose le tableau du fichier dlg"""
		var1 = dlgComponent.loadDlg(self)
		try:
			own = bge.logic.getCurrentController().owner
			if self.syntaxeEnabled == True:
				color = var1["dlg"+str(i)]['color']
				own.color = dlgComponent.arrColor[color]
				txtVar = var1["dlg"+str(i)]["text"]
			return txtVar
		except:
			try:
				if var1["dlg"+str(i)] == "Stop":
					return "Stop"
				else:
					return "Encode error"
			except:
				return None
	def primairy_func_2(self):
		"""Check if the dialog can be open"""
		if bge.logic.getCurrentController().sensors['Keyboard'].positive or bge.logic.getCurrentController().sensors['Msg'].positive:
			if bge.logic.globalDict['dlg.iter'] >= 0:
				dat = sv.load("tmp/__dialogs__.gs")
				if  dat[self.file] == 0:
					bge.logic.globalDict['dlg.iter'] += 1
					bge.logic.getSceneList()[0].suspend()
					var2 = self.syntaxe(bge.logic.globalDict['dlg.iter'])
					if var2 == 1:
						bge.logic.globalDict['dlg.iter'] = -1
						bge.logic.getSceneList()[0].resume()
						dat[self.file] = 1
						sv.save(dat,"tmp/__dialogs__.gs")
	def syntaxe(self,nb=1):
		"""Renvoie la syntaxe du texte"""
		scn = bge.logic.getCurrentScene()
		obj = bge.logic.getCurrentController().owner
		meGraphic = scn.objects['hud.achievement.graphic']
		var1 = dlgComponent.loadDlg(self)
		var2 = dlgComponent.f_dlg_1(self,nb)
		if var1 != None:
			if var2 == "Stop":
				obj['Text'] = ""
				meGraphic.visible = False
				return 1
			else:    
				obj['Text'] = var2
				meGraphic.visible = True
				return 0
		else:
			obj['Text'] = 'Dlg component was not found !'
			obj.color = dlgComponent.arrColor['R']