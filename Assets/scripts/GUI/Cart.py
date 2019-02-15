# -*-coding:utf-8 -*
from bge import logic


def Main(cont):

	own = cont.owner
	
	if own.position.x <= -10:
		own.position.x = -10
		
	elif own.position.x >= 45:
		own.position.x = 45
		
	if own.position.z >= 10:
		own.position.z = 10
		
	elif own.position.z <= 2:
		own.position.z = 2
		
	if own.position.y <= -10:
		own.position.y = -10
		
	elif own.position.y >= 10:
		own.position.y = 10