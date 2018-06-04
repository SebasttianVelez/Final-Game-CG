import pygame
import random
Ancho = 1200
Alto = 650
size = width, height = [Ancho,Alto]
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
gravedad=4.5
limite_salto =300
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

	def gravedad(self,v):
		if self.vel_y == 0:
			self.vel_y=1
		else:
			self.vel_y+=v



	def update(self):
		self.image = self.cut
		self.disp = False

		self.gravedad(0.7)
		self.rect.y += self.vel_y

		if self.rect.y >=( Alto -self.rect.height):
			self.rect.y = (Alto - self.rect.height)
		self.rect.x += self.vel_x
