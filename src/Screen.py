from os import system, get_terminal_size
from sys import stdout
from src.Mass import Mass
from src.PointMass import PointMass
from src.UniformSquareMass import UniformSquareMass

class Screen:
	'''
	Screen class
	Represents the terminal window screen
	'''

	#MASS_REPR: Maps each type of mass to its corresponding character representation
	MASS_REPR = {Mass: "m", PointMass: "•", UniformSquareMass: ("■", "◆")}

	#Matrix: RxC representing the screen, where R: rows and C: columns
	#Each cell is a single character
	matrix = []

	def __init__(self, plane):
		'''
		Constructor
		Initializes a new Screen object with an RxC matrix consisting of cells, each containing a whitespace
		Accepts a 2D plane as an argument
		'''
		self.plane = plane
		self.updateMatrix()

	def updateMatrix(self):
		'''
		Updates the internal matrix representing the screen, placing each mass at its corresponding cell (if it fits within the screen)
		and setting all other cells to whitespaces
		'''
		self.matrix = []
		x, y = get_terminal_size()
		for row in range(y):
			self.matrix.append([" "]*x)

		rowNormalizationFactor = y/x

		for mass in self.plane.masses:
			X = int(mass.position.x)%len(self.matrix[0])
			normalizedY = int(rowNormalizationFactor * mass.position.y%len(self.matrix))
			if (0 <= X < len(self.matrix[0])) and (0 <= normalizedY < len(self.matrix)):
				if mass.canRotate():
					self.matrix[normalizedY][X] = self.MASS_REPR[type(mass)][1 if 22.5 < mass.rotationAngle % 100 < 72.5 else 0]
				else:
					self.matrix[normalizedY][X] = self.MASS_REPR[type(mass)]


	def show(self):
		'''
		Displays the current plane on the screen
		'''
		system("clear")

		self.updateMatrix()

		columns, rows = get_terminal_size()

		for r in range(min(len(self.matrix), rows)):
			for c in range(min(len(self.matrix[0]), columns)):
				print(self.matrix[r][c], end="")

		stdout.flush()


