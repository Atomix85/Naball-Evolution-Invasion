# -*-coding:utf-8 -*
from bge import logic
import pickle
import codecs
import scripts.GameSave.SaveGame as SaveGame
import time

path = logic.expandPath("//lang/")

#InterLang 1.02
#Create By Bretelle Alan

def getLang():
	
	lang = SaveGame.load('account.gs', False)['lang']
	return lang
	
def getArrayOfScn():
	own = logic.getCurrentController().owner
	path_2 = logic.expandPath("//lang/"+str(getLang())+"/"+str(own['scn'])+".lg")
	with codecs.open(path_2,encoding='utf-8') as fileInstance: #
		tabInstance = eval(fileInstance.read())
	return tabInstance
	
def translate(cont):
        scnAct = logic.getCurrentScene()
        arrayTranslate = getArrayOfScn()
        for obj in arrayTranslate:
            scnAct.objects[obj]['Text'] = arrayTranslate[obj]
def textCenter():
	if getLang() != 'fr':
		scnAct = logic.getCurrentScene()
		arrayTranslate = getArrayOfScn(scnAct)
		for obj in arrayTranslate:
			tempBotonText = scnAct.objects[obj]
			text = tempBotonText['Text']
			textScaleX = 10/len(text)
			tempBotonText.localScale[0] *= textScaleX
			tempBotonText.localPosition[0] -= len(text)  * 0.008