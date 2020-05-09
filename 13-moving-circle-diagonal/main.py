import pgzrun # Do not edit this line
#Screen Width in pixels
WIDTH=500
#Screen height in pixels
HEIGHT=500
#Circle X and Y positions
circle_posx = 100
circle_posy = 100

#offset
speed = 1

#function that draws
def draw():
    #screen is your window
    #screen.fill(colorname)
    screen.fill('black')

    #screen.draw.circle((posx,posy),radius,color)
    screen.draw.circle((circle_posx,circle_posy),50,'white')

#function called 60 times per second 
def update():
    #scope
    global circle_posx,circle_posy #do not edit this line
    #change in circle_posx
    circle_posx = circle_posx + speed    

    #change in circle_posy
    circle_posy = circle_posy + speed 

pgzrun.go() # Do not edit this line