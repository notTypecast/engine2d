import pygame
from src.Mass import Mass
from src.PointMass import PointMass
from src.UniformSquareMass import UniformSquareMass


class Graphics:

	MASS_DRAW_FUNC = {PointMass: None, UniformSquareMass: None}

	C_BLACK = (0, 0, 0)
	C_WHITE = (255, 255, 255)

	def __init__(self, res, fps, plane, keepMassesOnScreen = False):
		self.width = res[0]
		self.height = res[1]
		self.fps = fps

		self.plane = plane
		self.keepMassesOnScreen = keepMassesOnScreen

		pygame.init()
		pygame.font.init()
		pygame.display.set_caption("engine2d")
		self.screen = pygame.display.set_mode([self.width, self.height])
		self.clock = pygame.time.Clock()

		Graphics.MASS_DRAW_FUNC[PointMass] = lambda mass: pygame.draw.circle(self.screen, Graphics.C_WHITE, mass.position.asTuple(), 3)
		Graphics.MASS_DRAW_FUNC[UniformSquareMass] = lambda mass: self.drawRotatedRect(self.screen, Graphics.C_WHITE, (*mass.position.asTuple(), mass.side, mass.side), mass.rotationAngle)


	def start(self, updateInterval):
		while True:
			for event in pygame.event.get():
				if event == pygame.QUIT:
					break

			self.plane.update(updateInterval)
			self.modPositions()

			self.screen.fill(Graphics.C_BLACK)

			for mass in self.plane.masses:
				Graphics.MASS_DRAW_FUNC[type(mass)](mass)


			pygame.display.flip()
			self.clock.tick(self.fps)

		pygame.quit()


	def modPositions(self):
		if self.keepMassesOnScreen:
			for mass in self.plane.masses:
				mass.position.x = mass.position.x % self.width
				mass.position.y = mass.position.y % self.height

	@staticmethod
	def drawRotatedRect(surface, color, position, angle):
		max_area = max(position[2],position[3])
		s = pygame.Surface((max_area, max_area))
		s = s.convert_alpha()
		s.fill(Graphics.C_WHITE)
		pygame.draw.rect(s, color, (0, 0, position[2], position[3]))
		s = pygame.transform.rotate(s, angle)
		surface.blit(s, (position[0], position[1]))
