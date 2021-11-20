from src.Point import Point
from src.Vector import Vector

class ForceVector(Vector):

	def __init__(self, endPoint, startPoint = Point(0, 0)):
		self.x = endPoint.x
		self.y = endPoint.y
		self.startXPercentage = startPoint.x
		self.startYPercentage = startPoint.y


	def getComponents(self):
		return (ForceVector(Point(self.x, 0), Point(self.startXPercentage, self.startYPercentage)), 
			ForceVector(Point(0, self.y), Point(self.startXPercentage, self.startYPercentage)))