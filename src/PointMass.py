from src.Mass import Mass

class PointMass(Mass):

	charRepr = "■"

	def update(self, t):
		acceleration = self.getForceSumVector()/self.mass

		self.position = self.position + self.speed*t + acceleration*t/2

		self.speed = self.speed + acceleration*t