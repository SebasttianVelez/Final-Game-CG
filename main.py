#Funcion Principal


import pygame
import random
from Objects.Level import *
from Objects.Player import *
from Objects.platform import platform
from Objects.bullets import Ukulele,Paper

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
	create_adds=0 # generador de enemigos

	#Creacion de Grupo

	todos = pygame.sprite.Group()
	Players = pygame.sprite.Group()
	Lvls = pygame.sprite.Group()
	platforms = pygame.sprite.Group()
	balas_personaje  = pygame.sprite.Group()
	all_enemies = pygame.sprite.Group()
	bullets_enemies= pygame.sprite.Group()

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

	#Jugador

	Jugador = Player(100,500)
	Players.add(Jugador)
	todos.add(Jugador)
	#Jugador 2 ()
	# #platforms
	platform1=platform(img3,400,500)
	platforms.add(platform1)
	todos.add(platform1)
	#Nivel 1
	Lvl1 = Level()
	Lvls.add(Lvl1)
	#bullets





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



# platforms
	for p in platforms:
		if p.rect.x <= 0:
			p.vel_x=5
		elif p.rect.x >= ancho-p.rect.x:
			p.vel_x=-5
# colisiones con plataformas
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
