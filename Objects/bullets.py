import pygame
from functions.cut import CortarImagen
img_ukulele1=pygame.image.load('Images/Instruments/ukulele1.png')
img_ukulele2=pygame.image.load('Images/Instruments/ukulele2.png')
img_ukulele3=pygame.image.load('Images/Instruments/ukulele3.png')
img_ukulele4=pygame.image.load('Images/Instruments/ukulele4.png')
img_ball=pygame.image.load('Images/Instruments/Ball.png')
imgU=[img_ukulele1,img_ukulele2,img_ukulele3,img_ukulele4]
class Ukulele (pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.img=imgU
        self.image=self.img[0]
        self.rect=self.image.get_rect()
        self.rect.x=posx
        self.rect.y=posy
        self.vel_x=0
        self.indice=0
        self.coldown_show=2
    def update (self):
        self.rect.x += self.vel_x

        if self.coldown_show==0:
            self.image=self.img[self.indice]
            self.indice+=1

            if self.indice >=3:
                self.indice=0
            self.coldown_show=5
        self.coldown_show-=1


class Paper (pygame.sprite.Sprite):
    def __init__(self,img,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.x=posx
        self.rect.y=posy
        self.vel_x=0
    def update (self):
        self.rect.x += self.vel_x

class Ball (pygame.sprite.Sprite):
    def __init__ (self,px,py):
        pygame.sprite.Sprite.__init__(self)
        self.cut = CortarImagen(img_ball,0,0,3,1)
        self.image=self.cut
        self.rect=self.image.get_rect()
        self.rect.x=px
        self.rect.y=py
        self.vel_x=20
        self.action=0

    def update (self):
        self.rect.x+=self.vel_x
        if self.action < 3:
            self.cut=CortarImagen(img_ball,self.action,0,3,1)
            self.action+=1
            self.image=self.cut
        else:
            self.action=0
