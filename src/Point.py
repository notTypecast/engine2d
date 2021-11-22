from numbers import Number

class Point:
	'''
	Defines a new point on the 2D plane
	'''

	def __init__(self, x, y):
		'''
		Constructor
		Initializes a new Point (x, y)
		'''
		self.x = x
		self.y = y

	def asTuple(self):
		return (self.x, self.y)

	def __neg__(self):
		'''
		Defines the -P operator: (-x, -y)
		'''
		return type(self)(-self.x, -self.y)

	def __add__(self, other):
		'''
		Defines the P+Q operator:
		(x1+x2, y1+y2) for Q: Point
		(x1+Q, y1+Q) for Q: scalar
		'''
		if isinstance(other, Number):
			return type(self)(self.x + other, self.y + other)
		else:
			return type(self)(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		'''
		Defines the P-Q operator
		'''
		return self + (-other)

	def __mul__(self, other):
		'''
		Defines the P*Q operator:
		(x1*x2, y1*y2) for Q: Point
		(x1*Q, y1*Q) for Q: scalar
		'''
		if isinstance(other, Number):
			return type(self)(self.x*other, self.y*other)
		else:
			return type(self)(self.x*other.x, self.y*other.y)

	def __truediv__(self, other):
		'''
		Defines the P/Q operator (same as P*Q)
		'''
		if isinstance(other, Number):
			return type(self)(self.x/other, self.y/other)
		else:
			return type(self)(self.x/other.x, self.y/other.y)

	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"

	def __repr__(self):
		return str(self)
			