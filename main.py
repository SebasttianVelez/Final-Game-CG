#Funcion Principal


import pygame
import random
from Objects.Level import *
from Objects.Player import *
from Objects.bullets import Ukulele,Paper
from Objects.Plataforma import *

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
	close_menu_inicial =False
	opcion_menu_inicial=1
	reloj = pygame.time.Clock()
	create_adds=0 # generador de enemigos

	#Creacion de Grupo

	todos = pygame.sprite.Group()
	Players = pygame.sprite.Group()
	Lvls = pygame.sprite.Group()
	balas_personaje  = pygame.sprite.Group()
	all_enemies = pygame.sprite.Group()
	bullets_enemies= pygame.sprite.Group()
	Plataformas = pygame.sprite.Group()

	#Images
	img=pygame.image.load ('Images/platform/Platform.png')
	img3=pygame.image.load('Images/platform/Car.png')
	img_ukulele=pygame.image.load('Images/Instruments/ukulele1.png')
	img_paper=pygame.image.load('Images/Instruments/paper.png')

	#CREACION DE OBJETOS

	#enemigos
	enemy=Enemies(800,500)
	all_enemies.add(enemy)
	todos.add(enemy)


	#Plataforma

	Plataforma1 = Plataforma(500, 500)
	Plataformas.add(Plataforma1)
	todos.add(Plataforma1)

	#Jugador

	Jugador = Player(100,500)
	Players.add(Jugador)
	todos.add(Jugador)
	#Jugador 2 ()
	#Nivel 1
	Lvl1 = Level()
	Lvls.add(Lvl1)
	#bullets



while not close_menu_inicial:
	for events in pygame.event.get():
		if events.type == pygame.QUIT:
			close_menu_inicial=True
			close=True
		if events.type==pygame.KEYDOWN:
			if events.key==pygame.K_DOWN:
				opcion_menu_inicial=2
			if events.key==pygame.K_UP:
				opcion_menu_inicial=1
			if events.key==pygame.K_SPACE:
				if opcion_menu_inicial==1:
					close_menu_inicial=True
				else:
					close_menu_inicial=True
					close=True
	if opcion_menu_inicial==1:
		menustart=pygame.image.load('menu_inicio/Menu_Start.png')
	else :
		menustart=pygame.image.load('menu_inicio/Menu_Exit.png')
	Screen.blit(menustart,[0,0])
	pygame.display.flip()



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
				mirada = True
				i1 = 0
			elif event.key == pygame.K_LEFT:
				Jugador.vel_x = -10
				mirada = False
				i2 = 0
			elif event.key == pygame.K_g:
				ukulele=Ukulele(img_ukulele,Jugador.rect.right,Jugador.rect.y)
				ukulele.vel_x=20
				balas_personaje.add(ukulele)
				todos.add(ukulele)

			if not Jugador.is_jumping:
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

#comportamiento enemigos
	for e in all_enemies:
		if e.coldown== 40:
			p=Paper(img_paper,enemy.rect.x,enemy.rect.y)
			p.vel_x=-20
			bullets_enemies.add(p)
			todos.add(p)
			e.coldown=0

	if create_adds==100:
		w=wolf(ancho,550)
		w.vel_x=-10
		all_enemies.add(w)
		todos.add(w)
		create_adds=0
	create_adds+=1



#colisiones de balas
	for e in all_enemies:
		col_balas_jugador=pygame.sprite.spritecollide(e,balas_personaje,True)
		for c in col_balas_jugador:
			e.health-=20
			print e.health
		if e.health <=0:
			all_enemies.remove(e)
			todos.remove(e)
			print 'enemigo removido'

# remover elementos
	for b in balas_personaje:
		if b.rect.x>ancho or b.rect.y < 0:
			balas_personaje.remove(b)
			todos.remove(b)
			print 'bala removida'




	if Jugador.saltar:
		Jugador.vel_y = -30
		Jugador.vel_in_platform=0
		Jugador.saltar=False
		Jugador.is_jumping=True

	#Movimiento del Fondo y plataformas

	if(Jugador.vel_x != 0):
		for l in Lvls:
			Lvl1.vel_x = -Jugador.vel_x
		for i in Plataformas:
			i.vel_x = -Jugador.vel_x
	else:
		for l in Lvls:
			Lvl1.vel_x = 0
		for i in Plataformas:
			i.vel_x = 0
#colisiones

	#Colisiones con plataformas




	Screen.fill([0,0,0])
	Lvls.update()
	todos.update()
	Lvls.draw(Screen)
	todos.draw(Screen)
	pygame.display.flip()
	reloj.tick(TIC)
