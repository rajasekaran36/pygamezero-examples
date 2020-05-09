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

    #screen.draw.text(text_to_display,position,fontname="fontname.ext", fontsize=size,ccolor='color_name')
    screen.draw.text("Hello PygameZero",(200,100),fontname="boogaloo.otf", fontsize=30,color='white')


pgzrun.go() # Do not edit this line