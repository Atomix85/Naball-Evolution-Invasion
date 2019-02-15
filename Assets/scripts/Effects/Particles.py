# -*-coding:utf-8 -*
from bge import logic
import scripts.GameSave.SaveBloc as svBl
import random

def Zone3D():
	scn = logic.getCurrentScene()
	own = logic.getCurrentController().owner
	
	initialPos = own.position
	
	x = random.randrange(-5, 5, 1)
	y = random.randrange(-5, 5, 1)
	z = random.randrange(0, 10, 1)
	
	initialPos.x += x
	initialPos.y += y
	initialPos.z += z
	
	own.position = initialPos
	
	scn.addObject("Particle.purple", own, 200)
	
	own.position.x -= x
	own.position.y -= y
	own.position.z -= z
	
	