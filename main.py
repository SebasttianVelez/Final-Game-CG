#Funcion Principal


import pygame
import random
from Objects.Level import *
from Objects.Player import *

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

	#Creacion de Gripos
	todos = pygame.sprite.Group()
	Players = pygame.sprite.Group()
	Lvls = pygame.sprite.Group()

	#CREACION DE OBJETOS

	#Jugador
	Jugador = Player(100, 500)
	Players.add(Jugador)
	todos.add(Jugador)
	#Jugador 2 ()

	#Nivel 1
	Lvl1 = Level()
	Lvls.add(Lvl1)
	todos.add(Lvl1)






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
			
			if event.key == pygame.K_s:
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


		'''
	if(Jugador.vel_x<0):
		Jugador.cut=CortarImagen(img2, i2, 7, 4)
	'''
	todos.draw(Screen)
	todos.update()
	pygame.display.flip()
	reloj.tick(TIC)

