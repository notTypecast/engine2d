import pygame
from src.Mass import Mass
from src.PointMass import PointMass
from src.UniformSquareMass import UniformSquareMass
from src.Point import Point
from math import isclose, sqrt


class Graphics:

	MASS_DRAW_FUNC = {PointMass: None, UniformSquareMass: None}

	C_BLACK = (0, 0, 0)
	C_WHITE = (255, 255, 255)
	C_RED = (255, 0, 0)
	C_GREEN = (0, 255, 0)

	def __init__(self, res, fps, plane, keepMassesOnScreen = False, showForces = False):
		self.width = res[0]
		self.height = res[1]
		self.fps = fps

		self.plane = plane
		self.keepMassesOnScreen = keepMassesOnScreen
		self.showForces = showForces

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
							
				if self.showForces:
					for force in mass.forces:
						startPoint = mass.getForceActPoint(force)
						if startPoint is not None:
							endPoint = Point(startPoint.x + force.x, startPoint.y + force.y)
							pygame.draw.line(self.screen, Graphics.C_RED, startPoint.asTuple(), endPoint.asTuple(), 2)
							pygame.draw.circle(self.screen, Graphics.C_RED, startPoint.asTuple(), 2)


			pygame.display.flip()
			self.clock.tick(self.fps)

		pygame.quit()


	def modPositions(self):
		if self.keepMassesOnScreen:
			for mass in self.plane.masses:
				mass.position.x = mass.position.x % self.width
				mass.position.y = mass.position.y % self.height

	'''
	@staticmethod
	def _getVectorArrowPoints(startPoint, endPoint, arrowLength):
		if isclose(endPoint.x, startPoint.x):
			#see what to do here
			return None

		if isclose(endPoint.y, startPoint.y):
			#and here
			return None

		s1 = (endPoint.y - startPoint.y) / (endPoint.x - startPoint.x)
		c1 = endPoint.y - s1*endPoint.x

		s2 = (startPoint.x - endPoint.x) / (endPoint.y - startPoint.y)

		#see about +- here
		xc_sqrt_term = -16*endPoint.x**2*s1**2+32*endPoint.x*endPoint.y*s1-32*endPoint.x*c1*s1-16*endPoint.y**2+32*endPoint.y*c1-16*c1**2+25*arrowLength**4*s1**2+25*arrowLength**4
		if xc_sqrt_term < 0:
			return None

		xc = (sqrt(xc_sqrt_term) + 4*endPoint.x + 4*endPoint.y*s1 - 4*c1*s1)/(4*(s1**2+1))
		yc = s1*xc + c1

		c2 = yc - s2*xc

		a1_sqrt_term = -4*xc**2*s2**2+8*xc*yc*s2+8*xc*c2*s2-4*yc**2-8*yc*c2-4*c2**2+arrowLength**2*s2**2 + arrowLength**2
		if a1_sqrt_term < 0:
			return None

		a1 = (sqrt(a1_sqrt_term) + 2*xc + 2*yc*s2 + 2*c2*s2)/(2*(s2**2+1))
		a2 = -a1

		b1 = s2*a1 + c2
		b2 = s2*a2 + c2

		return (endPoint.asTuple(), (a1, b1), (a2, b2))
	'''


	@staticmethod
	def drawRotatedRect(surface, color, position, angle):
		max_area = max(position[2], position[3])
		s = pygame.Surface((max_area, max_area))
		s = s.convert_alpha()
		s.fill(Graphics.C_WHITE)
		pygame.draw.rect(s, color, (0, 0, position[2], position[3]))
		s = pygame.transform.rotate(s, angle)
		newRect = s.get_rect(center = (position[0] + position[2]/2, position[1] + position[3]/2))
		surface.blit(s, newRect)
