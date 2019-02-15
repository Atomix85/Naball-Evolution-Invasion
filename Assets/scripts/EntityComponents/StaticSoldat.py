# -*-coding:utf-8 -*
from bge import logic
import random
import scripts.Ressources.Audio as aud
import scripts.EntityComponents.Naball as nab
import scripts.EntityComponents.Commons as com
import math

#TerioriamsType=1
#CreateBy=Atomix
#Interact=Hostile
#Please don't rage

REDCLIM = 1

def AttackShoot():
	
	cont = logic.getCurrentController()
	own = cont.owner
	scn = logic.getCurrentScene()
	
	if own['lvl'] == 1 and own['raf'] <= -10:
		own['raf'] = random.randint(2,5)
		
	if own['raf'] >= 1:
		scn.addObject("Eclair.002",own,100)
		
		aud.audio.play("Attack_Terioriams.ogg", own)#Son tire
		
		own['raf'] -= 1
	else:
		own['raf'] -= 1
	
def getDistance(obj, target):

	"Get distance between the 2 arguments type obj"
	
	yDif = obj.position.y - target.position.y
	xDif = obj.position.x - target.position.x
	return math.sqrt( (yDif * yDif) + (xDif * xDif) )
	
def IAController():

	cont = logic.getCurrentController()
	own = cont.owner
	path = logic.expandPath("//sounds/")
	scn = logic.getCurrentScene()
	for obj in own.children:
		if obj.name[0] == "S":
			objShot = obj
		elif obj.name[0] == "A":
			arm = obj
	target = scn.objects[nab.getNaball()]
	mesh = own.childrenRecursive[0]
	
	print("arm" + arm.name)
	
	lvl = own['lvl']
	
	dis = int(getDistance(own, target))
	
	snd = cont.actuators['Sound']
	
	if own['tic'] <= 1:
		
		if own['life'] <= 0:
			scn.addObject("Explode.001",own,30)
			
			com.dropRedClim(objShot,REDCLIM)
			
			logic.sendMessage("Music1")
			logic.sendMessage("unShow","","Target")
			logic.globalDict['targetAlr'] = False
			logic.sendMessage('terDead')
			arm.endObject()
			objShot.endObject()
			mesh.endObject()
			own.endObject()
	else:
		mesh.color = [1,1,1,1]

	
	if own['life'] > 0:
		if dis > 60:
			own['lvl'] = 0
		elif dis <= 60 and dis > 40:
			own['lvl'] = 1
			logic.sendMessage('terCombat')
			objShot['lvl'] = 1
		elif dis <= 40 and dis > 20:
			own['lvl'] = 2
			objShot['lvl'] = 1
		elif dis <= 20 and dis > 3:
			own['lvl'] = 3
			objShot['lvl'] = 1

	
		elif dis <= 3:
			own['lvl'] = 4
			objShot['lvl'] = 0
			scn.addObject("Explosion_ani",own,5)
			arm.playAction('Terioriams.001',26,32,logic.KX_ACTION_MODE_PING_PONG)