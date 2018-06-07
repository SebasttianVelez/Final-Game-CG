import pygame
class item_heal (pygame.sprite.Sprite):
    def __init__ (self,img,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.x=posx
        self.rect.y=posy
        self.vel_x=0
    def update (self):
        self.rect.x+=self.vel_x
class item_weapon (item_heal):
    def __init__ (self,img,px,py):
        item_heal.__init__(self,img,px,py)
        self.type_weapon=0
    def update (self):
        self.rect.x+=self.vel_x
