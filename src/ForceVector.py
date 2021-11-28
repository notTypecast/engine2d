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
		startPoint represents the x and y percentage of the mass' width and height respectively where the force acts
		Both endPoint and startPoint are relative, meaning they consider (0, 0) to be the center of the mass
		'''
		if not (0 <= startPoint.x <= 1 and 0 <= startPoint.y <= 1):
			raise ValueError("Force act point must be a tuple of percentages on the mass")


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