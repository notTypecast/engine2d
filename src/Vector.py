from src.Point import Point

class Vector:
	def __init__(self, endPoint, startPoint = Point(0, 0)):
		self.x = endPoint.x - startPoint.x
		self.y = endPoint.y - startPoint.y

	def update(x, y):
		self.x = x
		self.y = y

	@classmethod
	def __neg__(self):
		return type(self)(Point(-self.x, -self.y))

	def __abs__(self):
		return (self.x**2 + self.y**2)**.5

	def __add__(self, other):
		if isinstance(other, Vector):
			return type(self)(Point(self.x + other.x, self.y + other.y))
		else:
			return type(self)(Point(self.x + other, self.y + other))

	def __sub__(self, other):
		return self + (-other)

	def __mul__(self, other):
		if isinstance(other, Vector):
			return type(self)(Point(self.x*other.x, self.y*other.y))
		else:
			return type(self)(Point(self.x*other, self.y*other))

	def __truediv__(self, other):
		if isinstance(other, Vector):
			return type(self)(Point(self.x/other.x, self.y/other.y))
		else:
			return type(self)(Point(self.x/other, self.y/other))

	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"

	def __repr__(self):
		return str(self)


