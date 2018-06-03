import pygame
import random

img1 = pygame.image.load('Images/Pjs/PJSebas.png')
img2 = pygame.image.load('Images/Pjs/PJSebas2.png')
def CortarImagen (image, x, y, eX, eY):
	info=image.get_rect()
	an_image = info[2]
	al_image = info[3]
	an_corte = int(an_image/eX)
	al_corte = int(al_image/eY)
	cuadro = image.subsurface(x*an_corte,y*al_corte, an_corte, al_corte)
	return cuadro
gravedad=0.5
class Player(pygame.sprite.Sprite):
	def __init__(self, px, py):
		pygame.sprite.Sprite.__init__(self)
		self.health = 20000
		self.cut = CortarImagen(img1, 1, 1, 7, 4)
		self.image = self.cut
		self.rect = self.image.get_rect()
		self.rect.x = px
		self.rect.y = py
		self.vel_x = 0
		self.vel_y = 0
		self.dir = True
		self.disp = False
		self.saltar	 = False
		self.gravity=gravedad

	def Gravity (self):
		if self.saltar:
			self.rect.y-=self.gravity
			self.gravity-=gravedad
		else:
			if self.rect.y < 500:
				self.rect.y+=self.gravity
				self.gravity+=gravedad
			else:
				self.rect.y=500


	def update(self):

		self.image = self.cut
		self.disp = False
		self.rect.x += self.vel_x
		self.Gravity()
		if self.rect.y<=200:
			self.saltar=False
		
