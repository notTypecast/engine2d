from time import sleep
from os import system

from src.Screen import Screen
from src.Plane import Plane
from src.PointMass import PointMass
from src.Point import Point

if __name__ == "__main__":
	plane = Plane()
	a = PointMass(1, Point(40, 40))
	screen = Screen(plane)

	a.addSpeed(0, 20)
	a.addForce(0, -3)
	plane.addMass(a)

	updateFrequency = 20
	totalTime = 20
	for tick in [.1]*int(totalTime*updateFrequency):
		screen.show()
		sleep(1/updateFrequency)
		plane.update(tick)

	system("clear")