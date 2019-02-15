import bge
import scripts.EntityComponents.Naball as nab

def Update(cont):
	scn = bge.logic.getSceneList()[0]
	naball = scn.objects[nab.getArrayNaball()[scn.name]]
	skin = naball.children[0].children[0]
	own = cont.owner
		

	skin.color = [1,1,1,1]
	own.state = 3
	
def Init(cont):
	scn = bge.logic.getSceneList()[0]
	naball = scn.objects[nab.getArrayNaball()[scn.name]]
	skin = naball.children[0].children[0]
	own = cont.owner
	if own["tic"] > 2:
		skin.color = [1,1,1,0.4]
		own["tic"] = 0
		own.state = 2