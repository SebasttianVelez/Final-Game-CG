import pygame
import random
from functions.cut import CortarImagen

palomita= pygame.image.load ('Images/Enemies/Paloma.png')


class Paloma(pygame.sprite.Sprite):
	def __init__(self, px):
		pygame.sprite.Sprite.__init__(self)
		self.health = 300
		self.i = 0
		self.cut = CortarImagen(palomita, self.i, 0, 6, 1)
		self.image = self.cut
		self.rect = self.image.get_rect()
		self.rect.x = px
		self.rect.y = 80
		self.vel_x = -10
		self.disp = False

	def update(self):
		self.image = CortarImagen(palomita, self.i, 0, 6, 1)
		self.rect.x += self.vel_x
		if(self.i >=5):
			self.i = 0

	