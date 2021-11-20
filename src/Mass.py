import abc

from src.Point import Point
from src.Vector import Vector
from src.ForceVector import ForceVector

class Mass(metaclass = abc.ABCMeta):
	'''
	Abstract Mass class
	Defines a new mass
	'''

	def __init__(self, mass, position = Point(0, 0)):
		'''
		Constructor
		Initializes the new object with the given mass, at the given position
		The initial velocity is (0, 0)
		'''
		self.forces = []
		self.mass = mass
		self.position = position
		self.velocity = Vector(Point(0, 0))

	def addForce(self, x, y):
		'''
		Adds a new (constant) force to the mass
		'''
		forceVector = ForceVector(Point(x, y))
		self.forces.append(forceVector)

	def removeForce(self, n):
		'''
		Removes the nth force added to the mass
		Indexing starts at 1
		'''
		self.forces.remove(n - 1)

	def clearForces(self):
		'''
		Removes all existing forces acting on the mass
		'''
		self.forces.clear()

	def setVelocity(self, x, y):
		'''
		Sets the current velocity of the mass to the given value, (x, y)
		'''
		self.velocity = Vector(Point(x, y))

	def addVelocity(self, x, y):
		'''
		Adds the velocity (x, y) to the existing velocity of the mass
		'''
		self.velocity = self.velocity + Vector(Point(x, y))

	def getForceSumVector(self):
		'''
		Returns a vector, representing the sum of all the forces acting on the mass
		'''
		forceSumVector = ForceVector(Point(0, 0))

		for forceVector in self.forces:
			forceSumVector = forceSumVector + forceVector

		return forceSumVector

	@abc.abstractmethod
	def update(self, t):
		'''
		Abstract method update
		Updates the object by t time units, considering all the forces acting on it
		'''
		pass

	@abc.abstractmethod
	def canRotate(self):
		'''
		Abstract method canRotate
		Returns True if the object can rotate, else False
		'''
		pass
