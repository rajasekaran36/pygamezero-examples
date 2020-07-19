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

    #screen.draw.rect(Rect((poxx,posy),(width,height)),color)
    screen.draw.rect(Rect((100,100),(100,50)),'white')
        
pgzrun.go() # Do not edit this line