from bge import logic
import pickle
import os


folder_save = ""

path = logic.expandPath(os.environ['APPDATA'] + "//Naball/")

def loadInstance(fileInstance):
	path_2 = logic.expandPath("//gameInstance/"+fileInstance+".sii") #Static Instance Initial
	fileInstance = open(path_2,'r',encoding='utf-8')
	tabInstance = eval(fileInstance.read())
	fileInstance.close()
	return tabInstance
	
def getPathBloc():
	try:
		return path+logic.globalDict['folder_save']
	except:
		return path+"save1/"
	
def save(info,file):

	#get save's folder
	try:
		folder_save = logic.globalDict['folder_save']
	except:
		folder_save = "save1/"
	#check the save's folder
	if not os.path.isdir(path+folder_save):
		os.mkdir(path+folder_save) 
	
	cont = logic.getCurrentController()#necessary variable of bge.logic
	own = cont.owner 

    #save the info's setting in file's setting
	file = open(path+folder_save+file, 'w')    
	file.write(str(info))
	file.close()
    
    
def load(file, inSaveBloc=True):
	if inSaveBloc:
		file = open(getPathBloc()+file,'r')
	else:
		file = open(path+file,'r')
	tab = eval(file.read())
	file.close()
	return tab
		
def permuteFolderSave():
	objOnglet = logic.getCurrentScene().objects['Onglet_play_menu.003']
	own = logic.getCurrentController().owner
	logic.globalDict['folder_save'] = str(own['folder'])
		
def getSceneAct():
	scnAct = str(logic.getCurrentScene().name)
	ARRAY_SCN = {"Prison of the Terioriams": "prison","Ger_FieldSwamp":"ger","Prairie_of_the waters":"prairie","Swamp_bug":"swp1","Underground":"und1","Rock_desert":"desert1"}
	return ARRAY_SCN[scnAct]