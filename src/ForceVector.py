from src.Point import Point
from src.Vector import Vector

class ForceVector(Vector):
	'''
	Class ForceVector, extends Vector
	Defines a vector that represents a force
	'''

	def __init__(self, endPoint, startPoint = Point(0, 0)):
		'''
		Constructor
		Initializes a new force vector, pointing towards endPoint and acting
		on startPoint on the object
		The coordinates of startPoint represent percentages on the mass
		'''
		self.x = endPoint.x
		self.y = endPoint.y
		self.startXPercentage = startPoint.x
		self.startYPercentage = startPoint.y


	def getComponents(self):
		'''
		Splits force vector into its component vectors on the plane, Fx and Fy, and returns them
		'''
		return (ForceVector(Point(self.x, 0), Point(self.startXPercentage, self.startYPercentage)), 
			ForceVector(Point(0, self.y), Point(self.startXPercentage, self.startYPercentage)))