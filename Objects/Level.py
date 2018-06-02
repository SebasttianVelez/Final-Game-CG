import pygame
import random

screen = pygame.image.load('Images/Lvl-1/Mapa.png')

def CortarImagen (image, x, y, eX, eY):
	info=image.get_rect()
	an_image = info[2]	
	al_image = info[3]
	an_corte = int(an_image/eX) 
	al_corte = int(al_image/eY)
	cuadro = image.subsurface(x*an_corte,y*al_corte, an_corte, al_corte)
	return cuadro

class Level(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.cut = CortarImagen(screen, 0, 0, 1, 1)
		self.image = self.cut
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
	def update(self):
		self.image = self.cut
				