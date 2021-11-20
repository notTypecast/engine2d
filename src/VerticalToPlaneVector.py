
class VerticalToPlaneVector:
	'''
	Class VerticalToPlaneVector
	Represents a vector vertical to the 2D plane
	Since the direction can only be vertical to the plane, the only thing that needs to be specified
	is which direction the vector points towards
	This is done using the sign of the magnitude of the vector
	Therefore, only a single value, the magnitude, needs to be saved
	'''

	def __init__(self, val):
		'''
		Constructor
		Initializes a new vector vertical to the plane with magnitude val
		'''
		self.update(val)

	def update(self, val):
		'''
		Updates the magnitude of the vector
		'''
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
