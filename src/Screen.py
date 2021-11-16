from os import system, get_terminal_size
from sys import stdout

class Screen:

	matrix = []

	def __init__(self, plane):
		self.plane = plane
		self.updateMatrix()

	def updateMatrix(self):
		self.matrix = []
		x, y = get_terminal_size()
		for row in range(y):
			self.matrix.append([" "]*x)

		rowNormalizationFactor = y/x

		for mass in self.plane.masses:
			X = int(mass.position.x)
			normalizedY = int(rowNormalizationFactor * mass.position.y)
			if (0 <= X < len(self.matrix[0])) and (0 <= normalizedY < len(self.matrix)):
				self.matrix[normalizedY][X] = mass.charRepr


	def show(self):
		system("clear")

		self.updateMatrix()

		columns, rows = get_terminal_size()

		for r in range(min(len(self.matrix), rows)):
			for c in range(min(len(self.matrix[0]), columns)):
				print(self.matrix[r][c], end="")

		stdout.flush()


