from bge import logic as logic
import scripts.EntityComponents.Naball as nab

def colorVar(cont):
	own = cont.owner
	if own["alr"] < own['auto']:
		own.color = [1,0,0,1]