import pygame
pygame.init()

screen=pygame.display.set_mode((700,700))

class rectanglesss:
    def __init__(self,colour,dimensions):
        self.colour=colour
        self.dimensions=dimensions
        self.screen=screen

    def shapefactorie(self):
        self.rect=pygame.draw.rect(self.screen,self.colour,self.dimensions)

rectred=rectanglesss((200,90,90),(50,50,200,200))
rectblue=rectanglesss((90,90,200),(250,250,200,200))
rectgreen=rectanglesss((90,200,90),(500,500,200,200))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.fill((240,240,255))
    rectred.shapefactorie()
    rectblue.shapefactorie()
    rectgreen.shapefactorie()
    pygame.display.update()