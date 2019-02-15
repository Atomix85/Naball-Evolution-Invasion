# -*-coding:utf-8 -*
from bge import logic
import bge.texture as VideoTexture
import scripts.GameSave.SaveGame as sv
import random

def applyLvl(cont):
	
	own = cont.owner
	
	lvl = own["lvl"]
	
	logic.globalDict["Ilvl"] = lvl
	
def changeTexture(cont):
	
	obj = cont.owner

	matID = VideoTexture.materialID(obj, "MAlvlBackground")

	texture = VideoTexture.Texture(obj, matID, 0)
	
	imageP = logic.expandPath("//textures/LoadLvl/"+logic.globalDict["Ilvl"]+".png")

	texture.source = VideoTexture.ImageFFmpeg(imageP)

	texture.refresh(False)

	obj["Texture"] = texture