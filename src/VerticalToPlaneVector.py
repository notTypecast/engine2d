
class VerticalToPlaneVector:

	def __init__(self, val):
		self.update(val)

	def update(self, val):
		self.val = val

	def __neg__(self):
		return type(self)(-self.val)

	def __abs__(self):
		return self.val

	def __add__(self, other):
		if isinstance(other, VerticalToPlaneVector):
			return type(self)(self.val + other.val)
		else:
			return type(self)(self.val + other)

	def __sub__(self, other):
		return self + (-other)

	def __mul__(self, other):
		if isinstance(other, VerticalToPlaneVector):
			return self.val*other.val
		else:
			return self.val*other

	def __truediv__(self, other):
		if isinstance(other, Vector):
			return type(self)(self.val/other.val)
		else:
			return type(self)(self.val/other)

	def __str__(self):
		return str(self.val)

	def __repr__(self):
		return str(self)
