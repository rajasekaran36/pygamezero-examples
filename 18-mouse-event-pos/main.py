import pgzrun # Do not edit this line
#Screen Width in pixels
WIDTH=500
#Screen height in pixels
HEIGHT=500

circle_color = 'white'
circle_posx = 250
circle_posy = 250

#function that draws
def draw():
    #screen is your window
    #screen.fill(colorname)
    screen.fill('black')

    #screen.draw.circle((posx,posy),radius,color)
    screen.draw.circle((circle_posx,circle_posy),50,circle_color)

#function triggered when mouse cliked
#pos tupple (x,y) clicked position
def on_mouse_down(pos):
    global circle_posx,circle_posy
    circle_posx = pos[0]
    circle_posy = pos[1]

pgzrun.go() # Do not edit this line