from src.Mass import Mass
from src.Point import Point
from src.Vector import Vector
from src.ForceVector import ForceVector
from src.VerticalToPlaneVector import VerticalToPlaneVector
from math import sin, cos, copysign, radians


#TODO: forces should keep their place on square when it rotates instead of staying stationary
class UniformSquareMass(Mass):
	'''
	UniformSquareMass class, implements Mass
	Defines a square on the plane with a given side and mass, whose mass is uniformly distributed
	Forces being added to the square can cause torque and rotate the object
	'''

	def __init__(self, mass, side, position = Point(0, 0), rotationAngle = 0):
		'''
		Constructor
		Initializes a new uniform mass square with a given mass and side
		position and rotationAngle represent initial values
		'''
		super().__init__(mass, position)
		self.side = side
		self.momentOfInertia = side**4/12
		self.rotationAngle = rotationAngle
		self.angularSpeed = 0

	def addForce(self, x, y, xPercentageOnMass, yPercentageOnMass):
		'''
		Adds a new force on the object
		The force vector is (x, y), while xPercentageOnMass and yPercentageOnMass represent the
		point on the square, where the force acts (actual point can be calculated as such:
		(side*xPercentageOnMass, side*yPercentageOnMass))
		'''
		forceVector = ForceVector(Point(x, y), Point(xPercentageOnMass, yPercentageOnMass))
		self.forces.append(forceVector)

	def updateForces(self, byAngle):
		angleSin = -sin(radians(byAngle))
		angleCos = cos(radians(byAngle))

		for force in self.forces:
			force.update(force.x*angleCos - force.y*angleSin, force.x*angleSin + force.y*angleCos)

	def getForceActPoint(self, forceVector):
		for force in self.forces:
			if force is forceVector:
				rotationAngleSin = sin(radians(-self.rotationAngle))
				rotationAngleCos = cos(radians(-self.rotationAngle))

				x = self.position.x + force.startXPercentage*self.side
				y = self.position.y + force.startYPercentage*self.side

				pivotX = self.position.x + .5*self.side
				pivotY = self.position.y + .5*self.side

				x -= pivotX
				y -= pivotY

				rotatedX = x*rotationAngleCos - y*rotationAngleSin
				rotatedY = x*rotationAngleSin + y*rotationAngleCos

				rotatedX += pivotX
				rotatedY += pivotY

				return Point(rotatedX, rotatedY)

		return None



	def getTorqueSumVector(self):
		'''
		Returns a vector, representing the sum of all torques caused by forces on this object
		The vector is vertical to the 2D plane, therefore VerticalToPlaneVector represents it
		'''
		torqueSumVector = VerticalToPlaneVector(0)

		rotationAngleSin = sin(radians(self.rotationAngle))
		rotationAngleCos = cos(radians(self.rotationAngle))

		for forceVector in self.forces:
			#positionVector: vector starting at the center of the square and ending at the start point of the force
			forceActPoint = self.getForceActPoint(forceVector)
			positionVector = Vector(forceActPoint - Point(self.position.x, self.position.y), Point(.5*self.side, .5*self.side))
			#assume positive sign means counter-clockwise rotation
			if abs(forceVector.y) > abs(forceVector.x):
				if forceActPoint.x - self.position.x < self.side/2:
					sign = copysign(1, forceVector.y)
				else:
					sign = -copysign(1, forceVector.y)
			else:
				if forceActPoint.y - self.position.y < self.side/2:
					sign = -copysign(1, forceVector.x)
				else:
					sign = copysign(1, forceVector.x)

			torqueSumVector = torqueSumVector + sign*abs(forceVector)*abs(positionVector)*sin(forceVector.getAngleWith(positionVector))

		return torqueSumVector

	def update(self, t):
		'''
		Implements abstract method update
		Updates the position and linear velocity, as well as rotation angle and angular speed of the object
		after t time units pass from the current point in time
		'''
		acceleration = self.getForceSumVector()/self.mass

		self.position = self.position + self.velocity*t + acceleration*t**2/2

		self.velocity = self.velocity + acceleration*t


		angularAccelerationVal = abs(self.getTorqueSumVector())/self.momentOfInertia

		angleToAdd = self.angularSpeed*t + angularAccelerationVal*t**2/2

		self.rotationAngle = self.rotationAngle + angleToAdd

		self.angularSpeed = self.angularSpeed + angularAccelerationVal*t

		self.updateForces(angleToAdd)

		#print(self.getTorqueSumVector())

	def canRotate(self):
		'''
		Implements abstract method canRotate
		'''
		return True



