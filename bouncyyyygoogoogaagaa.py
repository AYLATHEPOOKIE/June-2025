import pgzrun
WIDTH=900
HEIGHT=500
TITLE="oooooh balllllll"

gravity=2000
class ball():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.velx=200
        self.vely=0
        self.radius=50
    def draw(self):
        screen.draw.filled_circle((self.x,self.y),self.radius,(250,20,100))

theball=ball(100,100)

def draw():
    screen.fill((20,0,5))
    theball.draw()

def update(t):
    initvel=theball.vely
    theball.vely+=gravity*t
    theball.y+=(initvel+theball.vely)*0.5*t
    if theball.y>485:
        theball.y=485
        theball.vely=-theball.vely*0.75
    theball.x+=theball.velx*t



pgzrun.go()