import pygame
import random
from functions.cut import CortarImagen

<<<<<<< HEAD
img_plataforma = pygame.image.load('Images/Plataformas/Plataforma11.png')
=======
PL = pygame.image.load('Images/Plataformas/Plataforma11.png')
>>>>>>> 517bf93b0377368c43013b93cca4de10373bd8ab

class Plataforma(pygame.sprite.Sprite):
	def __init__(self, px, py):
		pygame.sprite.Sprite.__init__(self)
<<<<<<< HEAD
		self.cut = CortarImagen(img_plataforma, 0, 0, 1, 1)
=======
		self.cut = CortarImagen(PL, 0, 0, 1, 1)
>>>>>>> 517bf93b0377368c43013b93cca4de10373bd8ab
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
