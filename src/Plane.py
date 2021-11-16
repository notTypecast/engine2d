

class Plane:

	masses = []

	def __init__(self):
		pass

	def addMass(self, mass):
		self.masses.append(mass)

	def update(self, t):
		for mass in self.masses:
			mass.update(t)