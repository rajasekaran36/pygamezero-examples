import pgzrun # Do not edit this line
#Screen Width in pixels
WIDTH=500
#Screen height in pixels
HEIGHT=500

#function that draws
def draw():
    #screen is your window
    #screen.fill(colorname)
    screen.fill('black')

    #screen.draw.line((startx,starty),(endx,endy),line_color)
    screen.draw.line((50,50),(100,100),'white')

    #screen.draw.line((startx,starty),(endx,endy),(red,grean,blue))
    screen.draw.line((150,150),(250,250),(255,0,0))
pgzrun.go() # Do not edit this line