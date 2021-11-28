from src.Mass import Mass

class PointMass(Mass):
	'''
	PointMass class, implements Mass
	Defines a point mass
	A point mass can have forces act on it linearly, but cannot rotate
	All the mass is concentrated in one theoretical point on the plane
	'''

	def update(self, t):
		'''
		Implements abstract method update
		Updates the position and velocity of the point mass based on the forces acting on it
		after t time units pass from the current point in time
		'''
		acceleration = self.getForceSumVector()/self.mass

		self.position = self.position + self.velocity*t + acceleration*t**2/2

		self.velocity = self.velocity + acceleration*t

	def getCenterPoint(self):
		return self.position

	def canRotate(self):
		'''
		Implements abstract method canRotate
		'''
		return False

	def getForceActPoint(self, forceVector):
		return None