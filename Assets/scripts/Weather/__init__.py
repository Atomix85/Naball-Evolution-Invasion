import time
import bge
import random

weather = ["rain","storm"]
p_52_hy = ""
lumen = 1.0
def Intensity():
	print("Mod : Weather ++")
	cont = bge.logic.getCurrentController()
	own = cont.owner
	timeNow = int(time.strftime("%H"))
	print(timeNow)
    
	if timeNow > 10 and timeNow <= 17: #Main hour
		own.energy = 1.0
	elif timeNow >= 9 and timeNow <= 10: #Morning
		own.energy = 0.5
		own.color = [1.0,0.4,0.4]
	elif timeNow >= 7 and timeNow < 9: #Sun rises
		own.energy = 0.25
		own.color = [1.0,0.2,0]
	elif timeNow > 0 and timeNow < 7: #Night-Morning
		own.energy = 0.0
	elif timeNow >= 22 and timeNow < 0: #Night-Evening
		own.energy = 0.0
	elif timeNow >= 20 and timeNow < 22: #Night-Morning
		own.energy = 0.25
		own.color = [1.0,0.2,0]
	elif timeNow >= 17 and timeNow <= 20: #Morning
		own.energy = 0.5
		own.color = [1.0,0.4,0.4]
	else:
		own.energy = 0.0
	return Weather(timeNow)
def Weather(timeNow):
	cont = bge.logic.getCurrentController()
	own = cont.owner
	scene = bge.logic.getCurrentScene()
	Rainer = scene.objects[own['Rainer']]
	p_52_hy = random.choice(weather)
	if p_52_hy == "sun":
		Rainer['act'] = False
		own['act'] = False
	elif p_52_hy == "rain":
		Rainer['act'] = True
		own['act'] = False
	elif p_52_hy == "storm":
		Rainer['act'] = True
		own['act'] = True
	return Background(timeNow,p_52_hy)
def Clouds(temps):
	cont = bge.logic.getCurrentController()
	own = cont.owner
	
	if temps == "sun":
		own.energy *= 2
	else:
		own.energy *= 0.5
	own["Light"] = own.energy
def Background(time,temps):
	own = bge.logic.getCurrentController().owner
	scene = bge.logic.getCurrentScene()
	if temps == "storm" or temps == "rain":
		#scene.world.mistColor = [0.1,0.1,0.1]
		scene.world.backgroundColor = [0.1,0.1,0.1]
		#scene.world.mistEnable = True
	
	return Clouds(temps)