import pygame
import random

img1 = pygame.image.load('/images/img1.png')
img2 = pygame.image.load('/images/img2.png')

def CortarImagen (image, x, y, eX, eY):
	info=image.get_rect()
	an_image = info[2]	
	al_image = info[3]
	an_corte = int(an_image/eX) 
	al_corte = int(al_image/eY)
	cuadro = image.subsurface(x*an_corte,y*al_corte, an_corte, al_corte)
	return cuadro

class Player(pygame.sprite.Sprite):
	def __init__(self, px, py):
		pygame.sprite.Sprite.__init__(self)
		self.health = 20000
		self.cut = CortarImagen(img, 0, 0, 1, 1)
		self.image = self.cut
		self.rect = self.image.get_rect()
		self.rect.x = px
		self.rect.y = py
		self.vel_x = 0
		self.vel_y = 0
		self.gravity = 4
		self.disp = False
	def update(self):
		self.disp = False
		self.rect.x += self.vel_x
				
