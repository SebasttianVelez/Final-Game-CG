import pygame
def CortarImagen (image, x, y, eX, eY):
	info=image.get_rect()
	an_image = info[2]
	al_image = info[3]
	an_corte = int(an_image/eX)
	al_corte = int(al_image/eY)
	cuadro = image.subsurface(x*an_corte,y*al_corte, an_corte, al_corte)
	return cuadro
