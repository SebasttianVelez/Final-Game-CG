import pygame
class Ukulele (pygame.sprite.Sprite):
    def __init__(self,img,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.x=posx
        self.rect.y=posy
        self.vel_x=0
    def update (self):
        self.rect.x += self.vel_x

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
