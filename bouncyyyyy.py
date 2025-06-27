import pygame
pygame.init()
pygame.display.set_caption("Hello everybody are you bored I am oooh ball")
screen=pygame.display.set_mode((900,500))


drawcircle=pygame.draw.circle(surface=screen,color=(250,20,105),center=[100,100],radius=50)
speed=[1,1]

while True:
    screen.fill((20,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    drawcircle=drawcircle.move(speed)
    if drawcircle.left==0 or drawcircle.right==900:
        speed[0]=-speed[0]
    if drawcircle.top==0 or drawcircle.bottom==500:
        speed[1]=-speed[1]
    pygame.draw.circle(surface=screen,color=(250,20,105),center=drawcircle.center,radius=50)
    pygame.display.update()