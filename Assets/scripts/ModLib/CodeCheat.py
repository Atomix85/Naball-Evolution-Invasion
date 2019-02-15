#List of imported modules
import bge.logic as logic
import scripts.EntityComponents.Naball as nab

	
def MoonJump(cont):
	myScn = logic.getSceneList()[0]
	key = cont.sensors["Space"]
	if logic.globalDict['chFly'] == 1:
		naball = myScn.objects[nab.getArrayNaball()[myScn.name]]
		if key.positive:
			
			myScn.gravity = [0,0,0]
			naball.applyMovement([0,0,0.1])
			naball.suspendDynamics()
		else:
			myScn.gravity = [0,0,-10]
			naball.restoreDynamics()