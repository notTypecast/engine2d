from numbers import Number

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __neg__(self):
		return Point(-self.x, -self.y)

	def __add__(self, other):
		if isinstance(other, Number):
			return Point(self.x + other, self.y + other)
		else:
			return Point(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return self + (-other)

	def __mul__(self, other):
		if isinstance(other, Number):
			return Point(self.x*other, self.y*other)
		else:
			return Point(self.x*other.x, self.y*other.y)

	def __truediv__(self, other):
		if isinstance(other, Number):
			return Point(self.x/other, self.y/other)
		else:
			return Point(self.x/other.x, self.y/other.y)

	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"

	def __repr__(self):
		return str(self)
			