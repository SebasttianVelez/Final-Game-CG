#Funcion Principal


import pygame
import random
from Objects.Level import *
from Objects.Player import *
from Objects.platform import platform

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



	#CREACION DE OBJETOS



	#Jugador

	Jugador = Player(100,500)
	Players.add(Jugador)
	todos.add(Jugador)
	#Jugador 2 ()
	# #platforms
	platform1=platform()
	platforms.add(platform1)
	todos.add(platform1)
	#Nivel 1
	Lvl1 = Level()
	Lvls.add(Lvl1)


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
			if event.key == pygame.K_RIGHT:
				Jugador.vel_x = 10
				Jugador.vel_y = 0
				mirada = True
				i1 = 0
			elif event.key == pygame.K_LEFT:
				Jugador.vel_x = -10
				Jugador.vel_y = 0
				mirada = False
				i2 = 0
			elif event.key == pygame.K_g:
				Jugador.saltar = True

			if event.key == pygame.K_SPACE:
				Jugador.saltar = True

#------------------------------------------------------------------------------Si el jugador suelta una tecla
		if event.type == pygame.KEYUP:
			if (event.key == pygame.K_RIGHT)or(event.key == pygame.K_LEFT):
				Jugador.vel_y = 0
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
			print "inicio der"
		elif p.rect.x >= ancho-p.rect.x:
			p.vel_x=-5
			print "inicio izq"

#colisiones
	col_platform=pygame.sprite.spritecollide(Jugador,platforms,False)
	for c in col_platform:
		if Jugador.rect.top < c.rect.bottom and Jugador.rect.top > c.rect.top:
			Jugador.rect.top=c.rect.bottom
			Jugador.gravity=0
		elif Jugador.rect.bottom >= c.rect.top:
			Jugador.rect.bottom=c.rect.top
			Jugador.gravity=0
		elif Jugador.rect.left < c.rect.right:
			Jugador.rect.left=c.rect.right
		Jugador.saltar=False



		'''
	if(Jugador.vel_x<0):
		Jugador.cut=CortarImagen(img2, i2, 7, 4)
	'''
	print Jugador.rect.bottom
	Screen.fill([0,0,0])
	Lvls.update()
	todos.update()
	Lvls.draw(Screen)
	todos.draw(Screen)
	pygame.display.flip()
	reloj.tick(TIC)
