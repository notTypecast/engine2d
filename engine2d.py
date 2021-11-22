from time import sleep
from os import system

from src.Screen import Screen
from src.Graphics import Graphics

from src.Plane import Plane
from src.PointMass import PointMass
from src.UniformSquareMass import UniformSquareMass
from src.Point import Point
from src.Vector import Vector

def cmd():
	plane = Plane()
	screen = Screen(plane)

	a = PointMass(2, Point(40, 40))
	#a.addVelocity(20, 20)
	a.addForce(-3, -3)
	plane.addMass(a)

	b = UniformSquareMass(2, 5, Point(50, 50))
	b.addForce(0, 5, 1, 1)
	b.addForce(0, -5, 0, 1)
	b.addForce(0, 5, 0.5, 1)
	b.addForce(-5, 5, 1, 0)
	plane.addMass(b)

	c = UniformSquareMass(100, 10, Point(10, 10))
	c.addForce(10, 9, 0, 0)
	plane.addMass(c)

	updateFrequency = 10
	totalTime = 20
	#for tick in [.1]*int(totalTime*updateFrequency):
	while True:
		screen.show()
		sleep(1/updateFrequency)
		plane.update(.1)

	system("clear")

def graphics():
	plane = Plane()
	g = Graphics((1280, 680), 60, plane, keepMassesOnScreen = True)

	a = PointMass(2, Point(40, 40))
	#a.addVelocity(20, 20)
	a.addForce(-3, -3)
	plane.addMass(a)

	b = UniformSquareMass(10, 50, Point(50, 50))
	b.addForce(5, 50, 1, 1)
	b.addForce(0, -50, 0, 1)
	plane.addMass(b)

	g.start(.1)


if __name__ == "__main__":
	graphics()