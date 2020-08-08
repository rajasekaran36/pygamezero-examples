import pgzrun # Do not edit this line
#Screen Width in pixels
WIDTH=800
#Screen height in pixels
HEIGHT=600

background = Actor('background')
alien = Actor('alien')
background.pos = 400,300
alien.pos = 50,450
#function that draws
def draw():

    #draw background
    background.draw()
    alien.draw()

#it will called 60 times per second
def update():
    #increse x value by 3 check for width
    if(alien.x<WIDTH):
        alien.x = alien.x + 3
    else:
        alien.x = 0
pgzrun.go() # Do not edit this line