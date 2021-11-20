from src.Mass import Mass
from src.Point import Point
from src.Vector import Vector
from src.ForceVector import ForceVector

class UniformSquareMass(Mass):

	SQUARE = "■"
	SQUARE_ROT = "◆"

	def __init__(self, mass, side, position = Point(0, 0), rotationAngle = 0):
		super().__init__(mass, position)
		self.side = side
		self.momentOfInertia = side**4/12
		self.rotationAngle = rotationAngle
		self.angularVelocity = Vector(Point(0, 0))

		self._updateCharRepr()

	def addForce(self, x, y, xPercentageOnMass, yPercentageOnMass):
		forceVector = ForceVector(Point(x, y), Point(xPercentageOnMass, yPercentageOnMass))
		self.forces.append(forceVector)

	def getTorqueSumVector(self):
		torqueSumVector = Vector(Point(0, 0))

		for forceVector in self.forces:
			#TODO: this is incorrect
			#instead force must be split into x and y component and each must take distance from x and y center respectively
			#also figure out way to represent only two directions for angular acceleration (clockwise and counter-clockwise)
			#and cancel out the torque of two vectors with the opposite direction and the same ||
			distanceFromCenter = (((forceVector.startXPercentage - .5)*self.side)**2 + ((forceVector.startYPercentage - .5)*self.side)**2)**.5
			torqueSumVector = torqueSumVector + forceVector*distanceFromCenter

		return torqueSumVector

	def update(self, t):
		acceleration = self.getForceSumVector()/self.mass

		self.position = self.position + self.velocity*t + acceleration*t**2/2

		self.velocity = self.velocity + acceleration*t


		angularAcceleration = self.getTorqueSumVector()/self.momentOfInertia

		self.rotationAngle = self.rotationAngle + abs(self.angularVelocity*t) + abs(angularAcceleration*t**2/2)

		self.angularVelocity = self.angularVelocity + angularAcceleration*t


		with open("test.txt", "a+") as f:
			f.write(str(angularAcceleration) + "\n")

		self._updateCharRepr()

	def _updateCharRepr(self):
		if 22.5 < abs(self.rotationAngle) % 100 < 72.5:
			self.charRepr = self.SQUARE_ROT
		else:
			self.charRepr = self.SQUARE




