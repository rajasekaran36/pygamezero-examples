import pgzrun # Do not edit this line
#Screen Width in pixels
WIDTH=800
#Screen height in pixels
HEIGHT=600

background = Actor('background')
background.pos = 400,300

#function that draws
def draw():

    #draw background
    background.draw()

pgzrun.go() # Do not edit this line