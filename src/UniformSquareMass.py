from src.Mass import Mass
from src.Point import Point
from src.Vector import Vector
from src.ForceVector import ForceVector
from src.VerticalToPlaneVector import VerticalToPlaneVector
from math import sin, copysign

class UniformSquareMass(Mass):

	SQUARE = "■"
	SQUARE_ROT = "◆"

	def __init__(self, mass, side, position = Point(0, 0), rotationAngle = 0):
		super().__init__(mass, position)
		self.side = side
		self.momentOfInertia = side**4/12
		self.rotationAngle = rotationAngle
		self.angularSpeed = 0

	def addForce(self, x, y, xPercentageOnMass, yPercentageOnMass):
		forceVector = ForceVector(Point(x, y), Point(xPercentageOnMass, yPercentageOnMass))
		self.forces.append(forceVector)

	def getTorqueSumVector(self):
		torqueSumVector = VerticalToPlaneVector(0)

		for forceVector in self.forces:
			#positionVector: vector starting at the center of the square and ending at the start point of the force
			positionVector = Vector(Point(forceVector.startXPercentage*self.side, forceVector.startYPercentage*self.side), 
				Point(.5*self.side, .5*self.side))
			#assume positive sign means counter-clockwise rotation
			if abs(forceVector.y) > abs(forceVector.x):
				if forceVector.startXPercentage < .5:
					sign = copysign(1, forceVector.y)
				else:
					sign = -copysign(1, forceVector.y)
			else:
				if forceVector.startYPercentage < .5:
					sign = -copysign(1, forceVector.x)
				else:
					sign = copysign(1, forceVector.x)

			torqueSumVector = torqueSumVector + sign*abs(forceVector)*abs(positionVector)*sin(forceVector.getAngleWith(positionVector))

		return torqueSumVector

	def update(self, t):
		acceleration = self.getForceSumVector()/self.mass

		self.position = self.position + self.velocity*t + acceleration*t**2/2

		self.velocity = self.velocity + acceleration*t
		

		angularAccelerationVal = abs(self.getTorqueSumVector())/self.momentOfInertia

		self.rotationAngle = self.rotationAngle + self.angularSpeed*t + angularAccelerationVal*t**2/2

		self.angularSpeed = self.angularSpeed + angularAccelerationVal*t

	def canRotate(self):
		return True




