from src.Mass import Mass

class PointMass(Mass):

	charRepr = "•"

	def update(self, t):
		acceleration = self.getForceSumVector()/self.mass

		self.position = self.position + self.velocity*t + acceleration*t**2/2

		self.velocity = self.velocity + acceleration*t