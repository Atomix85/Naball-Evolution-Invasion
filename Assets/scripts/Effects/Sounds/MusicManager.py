import bge

def PauseCont(cont):

	if cont.sensors["msg1"].positive:
		misc = cont.actuators["music"]
		misc.pauseSound()
	if cont.sensors["msg2"].positive:
		misc = cont.actuators["music"]
		misc.startSound()