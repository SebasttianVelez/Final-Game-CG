#Funcion Principal


import pygame
import random
from Objects.Level import *
from Objects.Player import *
from Objects.platform import platform
from Objects.bullets import Ukulele

#Definicion de Variables
ancho = 1200
alto = 650
TIC = 20
i1 = 0
i2 = 6


if __name__ == '__main__':
#Inicializacion de Pygame
	pygame.init()

	#Crear variables locales
	Screen = pygame.display.set_mode([ancho, alto])
	close = False
	reloj = pygame.time.Clock()

	#Creacion de Grupo

	todos = pygame.sprite.Group()
	Players = pygame.sprite.Group()
	Lvls = pygame.sprite.Group()
	platforms = pygame.sprite.Group()
	balas_personaje  = pygame.sprite.Group()

	#Images
	img=pygame.image.load ('Images/platform/Platform.png')
	img3=pygame.image.load('Images/platform/Car.png')
	img_ukulele=pygame.image.load('Images/Instruments/ukulele1.png')

	#CREACION DE OBJETOS



	#Jugador

	Jugador = Player(100,500)
	Players.add(Jugador)
	todos.add(Jugador)
	#Jugador 2 ()
	# #platforms
	platform1=platform(img3,ancho,500)
	platforms.add(platform1)
	todos.add(platform1)
	#Nivel 1
	Lvl1 = Level()
	Lvls.add(Lvl1)
	#bullets


"""
Hay que modificar la forma en la que se mueve el personaje

Mejorar salto

"""




	#inicializar el juego
while not close:
	#Gestion de Eventos
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			close = True
		if event.type == pygame.KEYDOWN:
#---------------------------------------------------------------------Presionar teclas
			if not Jugador.is_jumping:
				if event.key == pygame.K_RIGHT:
					Jugador.vel_x = 10
					mirada = True
					i1 = 0
				elif event.key == pygame.K_LEFT:
					Jugador.vel_x = -10
					mirada = False
					i2 = 0
				elif event.key == pygame.K_g:
					ukulele=Ukulele(img_ukulele,Jugador.rect.x,Jugador.rect.y)
					ukulele.vel_x=20
					balas_personaje.add(ukulele)
					todos.add(ukulele)

				if event.key == pygame.K_SPACE:
					Jugador.saltar = True

#------------------------------------------------------------------------------Si el jugador suelta una tecla

		if event.type == pygame.KEYUP:
			if (event.key == pygame.K_RIGHT)or(event.key == pygame.K_LEFT):
				Jugador.vel_x = 0
				i0 = 0
#------------------------------------------------------------------------------ Movimiento de sprites
	if(Jugador.vel_x>0):#movimiento a la derecha
		Jugador.cut=CortarImagen(img1,i1,1,7,4)
		Jugador.dir = True
		if i1 >=6:
			i1 = 0
		else:
			i1 +=1
	if(Jugador.vel_x<0):#movimiento a la izquierda
		Jugador.cut=CortarImagen(img2, i2,1, 7, 4)
		Jugador.dir = False
		if i2<=0:
			i2 = 6
		else:
			i2 -=1

	if(Jugador.vel_x==0):#Sin movimiento
		#Evaluar direccion
		if Jugador.dir:
			Jugador.cut = CortarImagen(img1, 6, 2, 7, 4)
		else:
			Jugador.cut = CortarImagen(img2, 0, 2, 7, 4)


# platforms
	for p in platforms:
		if p.rect.x <= 0:
			p.vel_x=5
		elif p.rect.x >= ancho-p.rect.x:
			p.vel_x=-5
# colisiones con layaformas
	col_platform=pygame.sprite.spritecollide(Jugador,platforms,False)
	for c in col_platform:
		if Jugador.rect.top < c.rect.bottom and Jugador.vel_y < 0:
			Jugador.rect.top=c.rect.bottom
			Jugador.vel_y=0
		elif Jugador.rect.bottom >= c.rect.top and Jugador.vel_y > 0:
			Jugador.rect.bottom=c.rect.top
			Jugador.vel_y=0
			Jugador.vel_in_platform=c.vel_x
		elif Jugador.rect.right > c.rect.left  :
			Jugador.rect.right = c.rect.left
			Jugador.vel_in_platform=c.vel_x






	if Jugador.saltar:
		Jugador.vel_y = -15
		Jugador.vel_in_platform=0
		Jugador.saltar=False
		Jugador.is_jumping=True
#colisiones


		'''
	if(Jugador.vel_x<0):
		Jugador.cut=CortarImagen(img2, i2, 7, 4)
	'''
	Screen.fill([0,0,0])
	Lvls.update()
	todos.update()
	Lvls.draw(Screen)
	todos.draw(Screen)
	pygame.display.flip()
	reloj.tick(TIC)
