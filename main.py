#Funcion Principal


import pygame
import random
from Objects.Level import *
from Objects.Player import *
from Objects.bullets import Ukulele,Paper,Ball
from Objects.Plataforma import *
from Objects.items import item_heal,item_weapon
# rules for programing balls
# 1 = ball
# 2 = ukulele
# 3 = dipstick
#Definicion de Variables
ancho = 1200
alto = 650
TIC = 20
i1 = 0
i2 = 6
"""
Mejorar el movimiento del fondo
"""

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
	is_pause=False
	pause_close=False
	opcion_paause=1
	vidaJugador=pygame.font.Font(None,32)

	#Creacion de Grupo

	todos = pygame.sprite.Group()
	Players = pygame.sprite.Group()
	Lvls = pygame.sprite.Group()
	balas_personaje  = pygame.sprite.Group()
	all_enemies = pygame.sprite.Group()
	bullets_enemies= pygame.sprite.Group()
	Plataformas = pygame.sprite.Group()
	Wolfs = pygame.sprite.Group()
	items_heal=pygame.sprite.Group()
	items_weapon=pygame.sprite.Group()
	#Images
	img=pygame.image.load ('Images/platform/Platform.png')
	img3=pygame.image.load('Images/platform/Car.png')
	img_ukulele=pygame.image.load('Images/Instruments/ukulele1.png')
	img_paper=pygame.image.load('Images/Instruments/paper.png')
	img_item_heal=pygame.image.load('Images/Items/item_heal.png')
	img_item_ukulele=pygame.image.load('Images/Instruments/ukulele1.png')

	#CREACION DE OBJETOS

	#enemigos
	enemy=Enemies(800,500)
	all_enemies.add(enemy)
	todos.add(enemy)


	#Plataforma
	x=100
	y=450
	id_platform=1
	Plataforma1 = Plataforma(500, 460)
	Plataformas.add(Plataforma1)
	todos.add(Plataforma1)

	Plataforma2 = Plataforma(800, 320)
	Plataformas.add(Plataforma2)
	todos.add(Plataforma2)

	for i in range (20):
		p=Plataforma(x,y)
		x+=900
		p.id=id_platform
		id_platform+=1
		Plataformas.add(p)
		todos.add(p)
		p2=Plataforma(x+300,y-140)
		p2.id=id_platform
		Plataformas.add(p2)
		todos.add(p2)
		id_platform+=1

	for p in  Plataformas:
		if (p.id % 2) == 0:
			e=Enemies(0,0)
			e.rect.x=p.rect.x
			e.rect.bottom=p.rect.top
			all_enemies.add(e)
			todos.add(e)
		if p.id == 5 or p.id ==1 or p.id==12:
			i=item_heal(img_item_heal,0,0)
			i.rect.x=p.rect.x+15
			i.rect.bottom=p.rect.top
			items_heal.add(i)
			todos.add(i)
		if p.id == 12 or  p.id == 1:
			i=item_weapon(img_item_ukulele,0,0)
			i.rect.x=p.rect.x+15
			i.rect.bottom=p.rect.top
			i.type_weapon=2
			items_weapon.add(i)
			todos.add(i)

	#Jugador

	Jugador = Player(500,500)
	Players.add(Jugador)
	todos.add(Jugador)
	#Jugador 2 ()
	#Nivel 1
	Lvl1 = Level()
	Lvls.add(Lvl1)
	#bullets


#---------------------------------------menu de inicio-------------------------------
while not close_menu_inicial:
	for events in pygame.event.get():
		if events.type == pygame.QUIT:
			close_menu_inicial=True
			close=True
		if events.type==pygame.KEYDOWN:
			if events.key==pygame.K_DOWN:
				if opcion_menu_inicial==1:
					opcion_menu_inicial=2
				elif opcion_menu_inicial==3:
					opcion_menu_inicial=4
			if events.key==pygame.K_UP:
				if opcion_menu_inicial==2:
					opcion_menu_inicial=1
				elif opcion_menu_inicial==4:
					opcion_menu_inicial=3
			if events.key==pygame.K_LEFT:
				if opcion_menu_inicial==3:
					opcion_menu_inicial=1
				elif opcion_menu_inicial==4:
					opcion_menu_inicial=2
			if events.key==pygame.K_RIGHT:
				if opcion_menu_inicial==1:
					opcion_menu_inicial=3
				elif opcion_menu_inicial==2:
					opcion_menu_inicial=4
			if events.key==pygame.K_RETURN :
				if opcion_menu_inicial==1:
					close_menu_inicial=True
				elif opcion_menu_inicial==4:
					close_menu_inicial=True
					close=True
	if opcion_menu_inicial==1:
		menustart=pygame.image.load('menu_inicio/Menu_inicio_Start.jpeg')
	elif opcion_menu_inicial==2:
		menustart=pygame.image.load('menu_inicio/Menu_inicio_Tutorial.jpeg')
	elif opcion_menu_inicial==3:
		menustart=pygame.image.load('menu_inicio/Menu_inicio_Story.jpeg')
	elif opcion_menu_inicial==4:
		menustart=pygame.image.load('menu_inicio/Menu_inicio_Exit.jpeg')
	Screen.blit(menustart,[0,0])
	pygame.display.flip()

#---------------------------------------------------

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
				if Jugador.type_weapon==1:
					ball=Ball(Jugador.rect.right,Jugador.rect.y)
					ball.vel_x=20
					balas_personaje.add(ball)
					todos.add(ball)
				elif Jugador.type_weapon==2:
					ukulele=Ukulele(Jugador.rect.right,Jugador.rect.y)
					ukulele.vel_x=20
					balas_personaje.add(ukulele)
					todos.add(ukulele)
			if event.key == pygame.K_ESCAPE:
				is_pause=True

			if not Jugador.is_jumping:
				if event.key == pygame.K_SPACE:
					Jugador.saltar = True

#------------------------------------------------------------------------------Si el jugador suelta una tecla

		if event.type == pygame.KEYUP:
			if (event.key == pygame.K_RIGHT)or(event.key == pygame.K_LEFT):
				Jugador.vel_x = 0
				i0 = 0
#------------------------------------------------------------------------------
# pausa
	if is_pause:
		while not pause_close:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pause_close=True
					close=True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						opcion_paause-=1
					if event.key == pygame.K_DOWN:
						opcion_paause+=1
					if event.key == pygame.K_RETURN :
						if opcion_paause == 1:
							pause_close=True
						if opcion_paause == 3:
							pause_close=True
							close = True

			if opcion_paause > 3:
				opcion_paause=3
			if opcion_paause < 1:
				opcion_paause=1
			if opcion_paause==1:
				pause=pygame.image.load('menu_pause/Pause_continue.png')
			elif opcion_paause==2:
				pause=pygame.image.load('menu_pause/Pause_restart.png')
			elif opcion_paause==3:
				pause=pygame.image.load('menu_pause/Pause_exit.png')
			Screen.fill([0,0,0])
			todos.draw(Screen)
			Lvls.draw(Screen)
			Screen.blit(pause,[150,0])
			pygame.display.flip()

#Movimiento de sprites
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
		if e.coldown==40:
			if e.rect.x > 0 and e.rect.x < 1200:
				p=Paper(img_paper,e.rect.x,e.rect.y)
				p.vel_x=-20
				bullets_enemies.add(p)
				todos.add(p)
			e.coldown=0


	# if create_adds==100:
	# 	w=wolf(ancho,550)
	# 	w.vel_x=-10
	# 	Wolfs.add(w)
	# 	todos.add(w)
	# 	create_adds=0
	# create_adds+=1



#colisiones de balas Jugador y enemigos
	for e in all_enemies:
		col_balas_jugador=pygame.sprite.spritecollide(e,balas_personaje,True)
		for c in col_balas_jugador:
			if Jugador.type_weapon==1:
				e.health-=20
			elif Jugador.type_weapon==2:
				e.health-=200
		if e.health <=0:
			all_enemies.remove(e)
			todos.remove(e)
			print 'enemigo removido'
# colisones de balas enemigos Jugador
	col_balas_enemigos=pygame.sprite.spritecollide(Jugador,bullets_enemies,True)
	for c in col_balas_enemigos:
		Jugador.health-=10
		if Jugador.health <= 0:
			close=True
#clolisiones Jugador vs enemigos
	col_Jugador_enemigos=pygame.sprite.spritecollide(Jugador,all_enemies,True)
	for c in col_Jugador_enemigos:
		Jugador.health-=100

# remover elementos
	for b in balas_personaje:
		if b.rect.x>ancho or b.rect.y < 0:
			balas_personaje.remove(b)
			todos.remove(b)
			print 'bala removida'
#balas de enemigos
	for b in bullets_enemies:
		if b.rect.x <= 0:
			bullets_enemies.remove(b)
			todos.remove(b)
			print 'Bala enemigo removida'

# recoleccion de items
	col_Jugador_item_heal=pygame.sprite.spritecollide(Jugador,items_heal,True)
	for c in col_Jugador_item_heal:
		if Jugador.health < 300:
			Jugador.health+=20
		if Jugador.health > 300:
			Jugador.health=300
	col_Jugador_item_weapon=pygame.sprite.spritecollide(Jugador,items_weapon,True)
	for c in col_Jugador_item_weapon:
		Jugador.type_weapon=c.type_weapon



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
		for e in all_enemies:
			e.vel_x= -Jugador.vel_x
		for i in items_heal:
			i.vel_x=-Jugador.vel_x
		for i in items_weapon:
			i.vel_x=-Jugador.vel_x


	else:
		for l in Lvls:
			Lvl1.vel_x = 0
		for i in Plataformas:
			i.vel_x = 0
		for e in all_enemies:
			e.vel_x=0
		for i in items_heal:
			i.vel_x=0
		for i in items_weapon:
			i.vel_x=0


#colisiones

	#Colisiones con plataformas
	col_plataformas = pygame.sprite.spritecollide(Jugador,Plataformas,False)
	for c in col_plataformas:
		if Jugador.rect.bottom >= c.rect.top and Jugador.vel_y > 0 :
			Jugador.rect.bottom=c.rect.top
			Jugador.is_jumping=False
			Jugador.vel_y=1
		# elif Jugador.rect.top < c.rect.bottom :
		# 	Jugador.rect.top = c.rect.bottom
		# 	Jugador.vel_y=1



		# elif Jugador.rect.right > c.rect.left:
		# 	Jugador.rect.right=c.rect.left
		# elif Jugador.rect.left < c.rect.right :
		# 	Jugador.rect.left=c.rect.right






	is_pause=False
	pause_close=False
	text=vidaJugador.render('Sebastian Velez (el de instagram)',False,[0,0,255])
	Screen.fill([0,0,0])
	Lvls.update()
	todos.update()
	Lvls.draw(Screen)
	todos.draw(Screen)
	Screen.blit(text,[0,0])
	pygame.draw.line(Screen,[255,0,0],[0,30],[Jugador.health,30],10)
	pygame.display.flip()
	reloj.tick(TIC)
