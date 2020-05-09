import pgzrun # Do not edit this line
#Screen Width in pixels
WIDTH=800
#Screen height in pixels
HEIGHT=500

#Actor('image',(xpos,ypos))
background = Actor('background',(400,250))
alien = Actor('alien',(100,250))

#function that draws
def draw():
    #screen is your window
    #screen.fill(colorname)
    screen.fill('black')
    
    #you have to draw your background first
    background.draw()

    #you have draw your actor
    alien.draw()

pgzrun.go() # Do not edit this line