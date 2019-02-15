from bge import logic as logic
import scripts.EntityComponents.Naball as nab

def Main(cont):
	scn = logic.getCurrentScene()
	naball = scn.objects[nab.getNaball()]
	own = cont.owner
	
	naball.setParent(own)
	naball.state = 2
	own.position.z += 2

def Eta(cont):

	if logic.globalDict['pw'] == 0:
		cont.owner.applyForce([0,50,0],True)
	
def End(cont):

	scn = logic.getCurrentScene()
	naball = scn.objects[nab.getNaball()]
	own = cont.owner
	
	naball.removeParent()
	naball.state = 1
	own.endObject()