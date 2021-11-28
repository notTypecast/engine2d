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
	g = Graphics((1280, 680), 60, plane, keepMassesOnScreen = True, showForces = True)
	g.start(.5)


if __name__ == "__main__":
	plane = Plane()

	#a = PointMass(2, Point(40, 40))
	#a.addVelocity(20, 20)
	#a.addForce(-3, -3)
	#plane.addMass(a)

	b = UniformSquareMass(50, 50, Point(500, 300))
	b.setAngularSpeed(1)
	#b.addForce(0, 100, 1, 1)
	#b.addForce(0, -200, .5, .5)
	#b.addForce(0, 100, 0, 1)
	b.addForce(-100, -100, 0.3, 0)
	b.addForce(100, 100, 0.7, 0)
	b.addForce(-100, -100, 0, 0.3)
	b.addForce(101, 101, 0, 0.8)
	#b.addForce(100, 100, 0.5, 0.5)
	plane.addMass(b)

	graphics(plane)