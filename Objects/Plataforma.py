import pygame
import random
from functions.cut import CortarImagen

PL = pygame.image.load('Images/Plataformas/Plataforma11.png')

class Plataforma(pygame.sprite.Sprite):
	def __init__(self, px, py):
		pygame.sprite.Sprite.__init__(self)
		self.id=0
		self.cut = CortarImagen(PL, 0, 0, 1, 1)
		self.image = self.cut
		self.rect = self.image.get_rect()
		self.rect.x= px
		self.rect.y = py
		self.vel_x = 0
		self.vel_y = 0
	def update(self):
		self.image = self.cut
		self.rect.x += self.vel_x
		self.rect.y += self.vel_y
