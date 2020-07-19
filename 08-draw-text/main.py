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

    #screen.draw.text(text_to_display,position,color='color_name')
    screen.draw.text("Hello PygameZero",(100,100),color='white')



pgzrun.go() # Do not edit this line