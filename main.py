#Funcion Principal


import pygame
import random
from Objects.Player import *
from Objects.Level import *
img1 = pygame.image.load('Images/Pjs/PJSebas.png')


#Definicion de Variables
ancho = 1200
alto = 650
TIC = 20

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


	#Nivel 1
	Lvl1 = Level()
	Lvls.add(Lvl1)
	todos.add(Lvl1)
	#Jugador 1 (Velez)
	Jugador1 = Player(100, 500)
	Players.add(Jugador1)
	todos.add(Jugador1)
	#Jugador 2 ()





	#inicializar el juego
while not close:
	#Gestion de Eventos
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			close = True		
	Screen.fill([0,0,0])
	todos.draw(Screen	)
	pygame.display.flip()
	reloj.tick(TIC)

