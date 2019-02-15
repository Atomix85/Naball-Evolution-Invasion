# -*-coding:utf-8 -*
import bge


def main():
	mySun = bge.logic.getCurrentController().owner
	scn = bge.logic.getCurrentScene()
	myChr = scn.objects[mySun['chr']]

	difX = mySun['x']
	difY = mySun['y']
	difZ = mySun['z']

	mySun.position.x = int(myChr.position.x + difX)
	mySun.position.y = int(myChr.position.y + difY)
	mySun.position.z = int(myChr.position.z + difZ)