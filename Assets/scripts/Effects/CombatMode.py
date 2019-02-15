# -*-coding:utf-8 -*
from bge import logic
import math


def getTargetInScn(cont):
	objs = logic.getCurrentScene().objects
	canTarget = []
	for obj in objs:
		if "target" in obj:
			if obj['target'] == 1:
				canTarget.append([obj , getDistance(cont.owner, obj)])
			else:
				if obj['target'] == 0:
					logic.sendMessage("unShow","","Target")
					logic.globalDict['targetAlr'] = False
					obj['target'] = -1
	
	canTarget1 = [(dist, obj) for obj , dist in canTarget]
	return [(obj , dist) for dist, obj in sorted(canTarget1, reverse=False)]
	
def End(cont):

	logic.sendMessage("unShow","","Target")
	logic.globalDict['targetAlr'] = False
	
def getDistance(obj, target):

	"Get distance between the 2 arguments type obj"
	
	yDif = obj.position.y - target.position.y
	zDif = obj.position.z - target.position.z
	xDif = obj.position.x - target.position.x
	return math.sqrt( (yDif * yDif) + (xDif * xDif) + (zDif * zDif))
	
def actualTarget():

	scn = logic.getSceneList()[0]
	tar = scn.objects[str(logic.globalDict['actualTarget'])]
	return tar
	
def targetLife(cont):

	try:
		cont.owner['Text'] = str(int(actualTarget()['nb']) - int(actualTarget()['life'])) + '/' + str(actualTarget()['nb'])
	except:
		cont.owner['Text'] = ""
		
def showTarget(cont):
	own = cont.owner
	scn = logic.getCurrentScene()
	if cont.sensors['al'].positive:
		try:
			obj = getTargetInScn(cont)[0]
			if getDistance(own,obj[0]) < 50 and not logic.globalDict['targetAlr']:
				scn.addObject("Target",obj[0])
				logic.globalDict['actualTarget'] = obj[0]
				logic.globalDict['targetAlr'] = True
			elif getDistance(own,obj[0]) > 50 and getDistance(own,obj[0]) < 55:
				logic.globalDict['targetAlr'] = False
				logic.globalDict['actualTarget'] = ""
				logic.sendMessage("unShow","","Target")
		except:
			pass
		try:
			tar = scn.objects['Target']
			tar.position = actualTarget().position
		except:
			pass
			
def Main(cont):
	own = cont.owner
	tracker = cont.actuators['tracker']
	if logic.globalDict['targetAlr'] == True:
		tracker.object = logic.globalDict['actualTarget']
		cont.activate(tracker)