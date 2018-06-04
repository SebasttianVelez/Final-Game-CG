import pygame
import random
from functions.cut import CortarImagen
Ancho = 1200
Alto = 650
size = width, height = [Ancho,Alto]
img1 = pygame.image.load('Images/Pjs/PJSebas.png')
img2 = pygame.image.load('Images/Pjs/PJSebas2.png')
img_enemy= pygame.image.load ('Images/Enemies/enemy.png')

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
		self.is_jumping = False
		self.vel_in_platform=0

	def gravedad(self,v):
		if self.vel_y == 0:
			self.vel_y=1
		else:
			self.vel_y+=v



	def update(self):
		self.image = self.cut
		self.disp = False

		self.gravedad(3)
		self.rect.y += self.vel_y

		if self.rect.y >=500:
			self.rect.y =500
			self.is_jumping=False
			self.vel_in_platform=0
		if self.vel_in_platform != 0:
			self.is_jumping=False
		self.rect.x += self.vel_x
		self.rect.x+=self.vel_in_platform

class Enemies (pygame.sprite.Sprite):
	def __init__(self, px, py):
		pygame.sprite.Sprite.__init__(self)
		self.health = 500
		self.cut = CortarImagen(img_enemy, 0, 0, 3, 1)
		self.image = self.cut
		self.rect = self.image.get_rect()
		self.rect.x = px
		self.rect.y = py
		self.vel_x = 0
		self.vel_y = 0
		self.dir = True
		self.disp = False
		self.saltar	 = False
		self.is_jumping = False
		self.vel_in_platform=0
		self.action=0
		self.coldown=40
	def update (self):
		if self.action < 3:
			self.cut=CortarImagen(img_enemy,self.action,0,3,1)
			self.action+=1
			self.image=self.cut
		else:
			self.action=0
		self.coldown+=1
