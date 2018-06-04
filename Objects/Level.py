import pygame
import random
from functions.cut import CortarImagen
screen = pygame.image.load('Images/Lvl-1/Mapa.png')


class Level(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.cut = CortarImagen(screen, 0, 0, 1, 1)
		self.image = self.cut
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
