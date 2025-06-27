import pygame
pygame.init()

screen=pygame.display.set_mode((700,700))

"""class rectanglesss:
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
    pygame.display.update()"""

class drawcircles():
    def __init__(self,colour,position,radius):
        self.colour=colour
        self.position=position
        self.radius=radius
        self.screen=screen
    def drawingonscreen(self):
        pygame.draw.circle(self.screen,self.colour,self.position,self.radius)

    def increaseradius(self):
        self.radius+=50
        pygame.draw.circle(self.screen,self.colour,self.position,self.radius)

circlegreen=drawcircles((40,180,40),(40,200),100)
circlered=drawcircles((180,40,40),(40,200),200)
circleblue=drawcircles((40,40,180),(40,200),300)

screen.fill((240,240,255))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            circlered.drawingonscreen()
            circleblue.drawingonscreen()
            circlegreen.drawingonscreen()
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            circlered.increaseradius()
            circleblue.increaseradius()
            circlegreen.increaseradius()
            pygame.display.update()
        elif event.type==pygame.MOUSEMOTION:
            mousepos=pygame.mouse.get_pos()
            circleblack=drawcircles((0,0,0),mousepos,10)
            circleblack.drawingonscreen()
            pygame.display.update()