import abc

from src.Point import Point
from src.Vector import Vector

class Mass(metaclass = abc.ABCMeta):
	'''
	Abstract class
	Defines a new mass
	'''

	forces = []
	charRepr = "m"

	def __init__(self, mass, position = Point(0, 0)):
		self.mass = mass
		self.position = position
		self.speed = Vector(Point(0, 0))

	def addForce(self, x, y):
		forceVector = Vector(Point(x, y))
		self.forces.append(forceVector)

	def clearForces(self):
		self.forces.clear()

	def setSpeed(self, x, y):
		self.speed = Vector(Point(x, y))

	def addSpeed(self, x, y):
		self.speed = self.speed + Vector(Point(x, y))

	def getForceSumVector(self):
		forceSumVector = Vector(Point(0, 0))

		for forceVector in self.forces:
			forceSumVector = forceSumVector + forceVector

		#print(self.forces)
		#sleep(1)
		return forceSumVector

	@abc.abstractmethod
	def update(self, t):
		pass
