from os import system, get_terminal_size
from sys import stdout

class Screen:
	'''
	Screen class
	Represents the terminal window screen
	'''

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
				self.matrix[normalizedY][X] = mass.charRepr


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


