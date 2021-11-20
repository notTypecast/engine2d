from time import sleep
from os import system

from src.Screen import Screen
from src.Plane import Plane
from src.PointMass import PointMass
from src.UniformSquareMass import UniformSquareMass
from src.Point import Point
from src.Vector import Vector

if __name__ == "__main__":
	plane = Plane()
	screen = Screen(plane)

	a = PointMass(2, Point(40, 40))
	#a.addVelocity(20, 20)
	a.addForce(-3, -3)
	plane.addMass(a)

	b = UniformSquareMass(2, 5)
	b.addForce(0, 5, 1, 1)
	b.addForce(0, 5, 0, 1)
	plane.addMass(b)

	updateFrequency = 20
	totalTime = 20
	for tick in [.1]*int(totalTime*updateFrequency):
		screen.show()
		sleep(1/updateFrequency)
		plane.update(tick)

	system("clear")