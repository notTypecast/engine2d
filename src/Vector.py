from src.Point import Point

class Vector:
	def __init__(self, endPoint, startPoint = Point(0, 0)):
		self.x = endPoint.x - startPoint.x
		self.y = endPoint.y - startPoint.y

	def update(x, y):
		self.x = x
		self.y = y

	def __neg__(self):
		return Vector(Point(-self.x, -self.y))

	def __add__(self, other):
		if type(other) is Vector:
			return Vector(Point(self.x + other.x, self.y + other.y))
		else:
			return Vector(Point(self.x + other, self.y + other))

	def __sub__(self, other):
		return self + (-other)

	def __mul__(self, other):
		if type(other) is Vector:
			return Vector(Point(self.x*other.x, self.y*other.y))
		else:
			return Vector(Point(self.x*other, self.y*other))

	def __truediv__(self, other):
		if type(other) is Vector:
			return Vector(Point(self.x/other.x, self.y/other.y))
		else:
			return Vector(Point(self.x/other, self.y/other))

	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"

	def __repr__(self):
		return str(self)


