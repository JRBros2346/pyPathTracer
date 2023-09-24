WIDTH=60
HEIGHT=25

import Terminal

screen=Terminal.Screen(WIDTH,HEIGHT)
screen.rect(6,5,1,1,0,0,255)
screen.rect(6,6,1,1,255,255,0)
#screen.pixels[5][6]=[0,255,0]
#screen.pixels[6][6]=[255,0,255]
screen.display()
