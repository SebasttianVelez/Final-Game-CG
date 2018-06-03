import  pygame
img=pygame.image.load ('Images/platform/Platform.png')
class platform (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.x=200
        self.rect.y=300
        self.vel_x=5
    def update (self):
        self.rect.x += self.vel_x
