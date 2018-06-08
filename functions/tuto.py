import pygame
img_tuto=pygame.image.load('Tutorial/Tutorial2.png')
def Tutorial (Screen):
    close = False
    Screen.blit(img_tuto,[200,150])
    pygame.display.flip()
    while not close:
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                close=True
            if events.type == pygame.KEYDOWN:
                if events.key==pygame.K_ESCAPE:
                    close=True
