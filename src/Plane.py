class Plane:
	'''
	Plane class
	Represents a 2D plane which can contain masses
	'''

	masses = []

	def addMass(self, mass):
		'''
		Adds a mass to the plane
		'''
		self.masses.append(mass)

	def update(self, t):
		'''
		Updates each existing mass on the plane by t units of time
		'''
		for mass in self.masses:
			mass.update(t)