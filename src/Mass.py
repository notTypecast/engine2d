import abc

from src.Point import Point
from src.Vector import Vector
from src.ForceVector import ForceVector

class Mass(metaclass = abc.ABCMeta):
	'''
	Abstract class
	Defines a new mass
	'''
	charRepr = "m"

	def __init__(self, mass, position = Point(0, 0)):
		self.forces = []
		self.mass = mass
		self.position = position
		self.velocity = Vector(Point(0, 0))

	def addForce(self, x, y):
		forceVector = ForceVector(Point(x, y))
		self.forces.append(forceVector)

	def clearForces(self):
		self.forces.clear()

	def setVelocity(self, x, y):
		self.velocity = Vector(Point(x, y))

	def addVelocity(self, x, y):
		self.velocity = self.velocity + Vector(Point(x, y))

	def getForceSumVector(self):
		forceSumVector = ForceVector(Point(0, 0))

		for forceVector in self.forces:
			forceSumVector = forceSumVector + forceVector

		return forceSumVector

	@abc.abstractmethod
	def update(self, t):
		pass
