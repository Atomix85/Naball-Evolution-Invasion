# -*-coding:utf-8 -*
from bge import logic
import random
import scripts.Ressources.Audio as aud
import math

#
#
#
#

def Hit():
	cont = logic.getCurrentController()
	own = cont.owner
	scn = logic.getCurrentScene()
	
	arm = own.children[1]
	
	if own['tic'] >= 1:
		own['life'] -= 1
		own['tic'] = 0
		arm.playAction('Terioriams.001',33,40)

def dropRedClim(to,nb):
	scn = logic.getCurrentScene()
	var1 = nb
	while var1 > 0:
		temp = to.localPosition
		to.localPosition.x += random.randrange(-5, 5, 1)
		to.localPosition.y += random.randrange(-5, 5, 1)
		scn.addObject("Clim_red",to,1000)
		var1 -= 1
		to.localPosition = temp
		