from time import sleep
from os import system

from src.Screen import Screen
from src.Graphics import Graphics

from src.Plane import Plane
from src.PointMass import PointMass
from src.UniformSquareMass import UniformSquareMass
from src.Point import Point
from src.Vector import Vector

def cmd(plane):
	screen = Screen(plane)

	updateFrequency = 10
	while True:
		screen.show()
		sleep(1/updateFrequency)
		plane.update(.1)

	system("clear")

def graphics(plane):
	g = Graphics((1280, 680), 60, plane, keepMassesOnScreen = True)
	g.start(.1)


if __name__ == "__main__":
	plane = Plane()

	#a = PointMass(2, Point(40, 40))
	#a.addVelocity(20, 20)
	#a.addForce(-3, -3)
	#plane.addMass(a)

	b = UniformSquareMass(1, 50, Point(50, 50))
	b.addForce(0, 1000, 1, 1)
	b.addForce(0, -1000, 0, 1)
	plane.addMass(b)

	graphics(plane)