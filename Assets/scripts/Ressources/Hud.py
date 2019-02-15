# -*-coding:utf-8 -*
from bge import logic
import pickle
import codecs
import scripts.GameSave.SaveGame as SaveGame
import scripts.Effects.CombatMode as cm
import time

path = logic.expandPath("//lang/")



def life():
	hud = logic.getCurrentScene()
	bac = hud.objects['Hud.Bar_life']
	own = logic.getCurrentController().owner
	
	#init
	if own['lifeDyn'] > bac['lifeMax']:
		own['lifeDyn'] = bac['lifeMax']
	elif own['lifeDyn'] < 0:
		logic.sendMessage("Print","","Hud.GameOver")
	else:
		own.localScale[0] = own['lifeDyn']/bac['lifeMax'] * bac.localScale[0]
def lifeInit():
	hud = logic.getCurrentScene()
	bac = hud.objects['Hud.Bar_life']
	own = logic.getCurrentController().owner
	own['lifeDyn'] = bac['lifeMax']/2
	
def allLife(cont):

	hud = logic.getCurrentScene()
	bac = hud.objects['Hud.Bar_life']
	own = cont.owner
	own['lifeDyn'] = bac['lifeMax']
	
	
def lifeMaxGain():
	own = logic.getCurrentController().owner
	
	#init
	if own['lifeMax'] > 100:
		own['lifeMax'] = 100
	else:
		own.localScale[0] = own['lifeMax']/100 * own.localScale[0]
		own.localScale[0] = own['lifeMax']/100 * 3.5
		
def hudSave():
	hud = logic.getSceneList()[1]
	nbClim = hud.objects['Hud.nbClim']
	nbAto = hud.objects['Hud.nbAto']
	nbCage = hud.objects['Hud.nbCage']
	nbXp = hud.objects['Hud.nbXp']
	life = hud.objects['Hud.Bar_life.dyn']
	lifeMax = hud.objects['Hud.Bar_life']

	array = {"__INIT__":"Hud","nbClim":nbClim['nb'],"nbCage":nbCage['nb'],"nbAto":nbAto['nb'],"nbXp":nbXp['nb'],"lifeDyn":life["lifeDyn"],"lifeMax":lifeMax['lifeMax']}
	SaveGame.save(array,"hud.gs")
	
def hudLoad():
	hud = logic.getCurrentScene()
	nbClim = hud.objects['Hud.nbClim']
	nbAto = hud.objects['Hud.nbAto']
	nbCage = hud.objects['Hud.nbCage']
	nbXp = hud.objects['Hud.nbXp']
	life = hud.objects['Hud.Bar_life.dyn']
	lifeMax = hud.objects['Hud.Bar_life']

	hudFile = open(str(SaveGame.getPathBloc())+'hud.gs','r') #Charge MainPath + NomDuBloc + Hud.gs
	hudTab = eval(hudFile.read())
	hudFile.close()
	nbClim['nb'] = hudTab['nbClim']
	nbAto['nb']  = hudTab['nbAto']
	nbCage['nb'] = hudTab['nbCage']
	nbXp['nb'] = hudTab['nbXp']
	life['lifeDyn'] = hudTab['lifeDyn']
	lifeMax['lifeMax'] = hudTab['lifeMax']

	
def climFormat():
	own = logic.getCurrentController().owner
	own['Text'] = str(own['nb']) + "/161"
def atoFormat():
	own = logic.getCurrentController().owner
	own['Text'] = str(own['nb'])
def cageFormat():
	own = logic.getCurrentController().owner
	own['Text'] = str(own['nb']) + "/7"
def xpFormat():
	own = logic.getCurrentController().owner
	own['Text'] = str(own['nb']) + " XP"

def lifeEnn(cont):
	own = cont.owner
	barDyn = logic.getCurrentScene().objects[own['bar']]
	try:
		own.visible = True
		barDyn.visible = True
		
		actualTarget = cm.actualTarget()
		if actualTarget['life'] <= 0:
			own.visible = False
			barDyn.visible = False
			actualTarget['life'] = 0
			
		else:
			own.localScale[0] = 3.5
	
			barDyn.localScale[0] = actualTarget['life']/actualTarget['nb'] * own.localScale[0]
	except:
		own.visible = False
		barDyn.visible = False
	