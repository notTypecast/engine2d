from src.Point import Point
from src.VerticalToPlaneVector import VerticalToPlaneVector
from math import sin, acos

class Vector:
	'''
	Class Vector
	Represents a 2D Vector
	'''

	def __init__(self, endPoint, startPoint = Point(0, 0)):
		'''
		Initializes Vector AB, where A: startPoint and B: endPoint
		'''
		self.x = endPoint.x - startPoint.x
		self.y = endPoint.y - startPoint.y

	def update(x, y):
		'''
		Updates the coordinates of the Vector to (x, y)
		'''
		self.x = x
		self.y = y

	def getAngleWith(self, other):
		'''
		Returns angle of vector with vector other
		w = arccos(A * B / (||A||*||B||))
		'''
		return acos(self*other / (abs(self)*abs(other)))

	def __neg__(self):
		'''
		Defines the -v operator
		'''
		return type(self)(Point(-self.x, -self.y))

	def __abs__(self):
		'''
		Defines the abs(v) operator (equivalent to |v|)
		'''
		return (self.x**2 + self.y**2)**.5

	def __add__(self, other):
		'''
		Defines the v+u operator, for u: vector or u: scalar
		'''
		if isinstance(other, Vector):
			return type(self)(Point(self.x + other.x, self.y + other.y))
		else:
			return type(self)(Point(self.x + other, self.y + other))

	def __sub__(self, other):
		'''
		Defines the v-u operator
		'''
		return self + (-other)

	def __mul__(self, other):
		'''
		Defines the v*u operator
		For u: vector, returns dot product of v and u
		For u: scalar, returns uv
		'''
		if isinstance(other, Vector):
			return self.x*other.x + self.y*other.y
		else:
			return type(self)(Point(self.x*other, self.y*other))

	def cross(self, other):
		'''
		Defines the cross product between vectors
		v x u = ||v|| * ||u|| * sin(a) * n, where a: angle between v and u, and n: unit vector vertical to plane
		'''
		return VerticalToPlaneVector(abs(self)*abs(other)*sin(self.getAngleWith(other)))

	def __truediv__(self, other):
		'''
		Defines the vu = (1/u)v operator, where u: scalar

		'''
		return type(self)(Point(self.x/other, self.y/other))

	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"

	def __repr__(self):
		return str(self)


