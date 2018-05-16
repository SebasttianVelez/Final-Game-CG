#Funcion Principal

import pygame
import random

ancho = 1200
alto = 650
TIC = 20

def main():
	pygame.init()
	Screen = pygame.display.set_mode([ancho, alto]) 
	close = False
	reloj = pygame.time.Clock()

	#inicializar el juego
	while not close:
	#Gestion de Eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				close = True		
		Screen.fill([0,0,0])
		pygame.display.flip()
		reloj.tick(TIC)

main()