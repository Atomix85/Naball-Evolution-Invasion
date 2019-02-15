from bge import logic as logic
import scripts.EntityComponents.Naball as nab
from mathutils import Vector, Matrix
import math

def getDistance(obj, target):

	"Get distance between the 2 arguments type obj"
	
	yDif = obj.position.y - target.position.y
	xDif = obj.position.x - target.position.x
	return math.sqrt( (yDif * yDif) + (xDif * xDif) )

def Init(cont):

	scn = logic.getCurrentScene()
	
	naball = scn.objects[nab.getNaball()]
	myRay = cont.owner
	if getDistance(naball, myRay) <= 10:
		if naball.state == 1:
		
			naball.state = 2
			logic.globalDict["nabInitRot"] = naball.worldOrientation
			naball.position = myRay.position
			naball.position.z += 1
		
			naball.orientation = myRay.orientation
		
	
def end(cont):

	naball = cont.owner
	naball.playAction("initRot",0,0)
	naball.state = 1
	
def alignNormal(cont):

	own = cont.owner
	
	rayon = own['rayon']
	rayon = logic.getCurrentScene().objects[rayon]
	logic.sendMessage("partx25")
	own.position.y = rayon.position.y
	own.applyMovement([0.5,0,0])
	
	# if ray.positive:
		# own.alignAxisToVect(Vector(ray.hitNormal)*1,2,.24)
	
	# else:
		# own.alignAxisToVect(Vector([0,0,1]),2,.25)
