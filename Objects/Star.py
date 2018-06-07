import pygame
import random
from functions.cut import CortarImagen
star = pygame.image.load('Images/Lvl-1/Estrellas editar.png')

class Star(pygame.sprite.Sprite):
	def __init__(self, px, py):
		pygame.sprite.Sprite.__init__(self)
		self.i = 0
		self.cut = CortarImagen(star, 0, self.i, 2, 1)
		self.image = self.cut
		self.rect = self.image.get_rect()
		self.rect.x = px
		self.rect.y = py
		self.vel_x = 0
	def update(self):
		self.rect.x += self.vel_x
		self.image = CortarImagen(star, self.i, 0, 2, 1)
		if self.i == 0:
			self.i = 1
		else:
			self.i = 0
