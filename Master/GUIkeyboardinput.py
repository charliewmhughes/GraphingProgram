#program to test graphical input for the graphing program.

import time
import pygame
from pygame.locals import*

pygame.font.init()

input = ('GUI input module reporting for duty...')
xvalin = 47
xvaly = 10
yvaltext = 20


#function to flip the display
def flip():
    pygame.display.flip()
    
def test():
    print('hello_world')
    


def GUIInput():
    
    #............setup the display window
    (width, height) = (300,  60)
    screen = pygame.display.set_mode((width, height))
    running = True
    #give the display window a title
    pygame.display.set_caption('GUI_Keyboard-input')
    #set colour variables
    white = (255,  255,  255)
    black = (0,  0,  0)
    #colour the background again to erase whatever is above
    background_colour = (white)
    screen.fill(background_colour)
    flip()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    yequals = myfont.render(('y ='), False, (0, 0, 0))
    #............setup done
    

    screen.blit(yequals,  (xvaly, yvaltext))
    keyin = myfont.render(input, False, (0, 0, 0))
    screen.blit(keyin, (xvalin,yvaltext))
    flip()
