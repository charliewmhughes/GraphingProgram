#program to test graphical input for the graphing program.

import time
import pygame
from pygame.locals import*

pygame.font.init()

global input_show
input_show = []

input = []
xvalin = 47
xvaly = 10
yvaltext = 8

#necessaryimages
multiply_button = pygame.image.load('multiply.png')
divide_button = pygame.image.load('divide.png')
add_button = pygame.image.load('add.png')
subtract_button = pygame.image.load('minus.png')
done_button = pygame.image.load('done_button_unclicked.png')

#set the font
myfont = pygame.font.SysFont('Comic Sans MS', 30)

#function to flip the display
def flip():
    pygame.display.flip()
    
def test():
    print('hello_world')
    input_show = ''.join(input)
    keyin = myfont.render(input_show, False, (0, 0, 0))
    screen.blit(keyin, (xvalin,yvaltext))

def GUIInput():
    
    #............setup the display window
    (width, height) = (570,  257)
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
    yequals = myfont.render(('y ='), False, (0, 0, 0))
    #place images
    screen.blit(add_button,  (10, 45))
    screen.blit(subtract_button,  (150, 45))
    screen.blit(divide_button,  (290, 45))
    screen.blit(multiply_button,  (430, 45))
    screen.blit(done_button,  (224, 200))
    #............setup done
    
    screen.blit(yequals,  (xvaly, yvaltext))
    flip()
    
    while running:
       
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print (pygame.key.name(event.key))
                input.append(pygame.key.name(event.key))
                input_show = ''.join(input)
                keyin = myfont.render(input_show, False, (0, 0, 0))
                screen.blit(keyin, (xvalin,yvaltext))
                print(input_show)
                flip()
        
        if done_button.get_rect(x=(224),  y=(200)).collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                running = False

        if add_button.get_rect(x=(10),  y=(45)).collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                input.append('+')
                input_show = ''.join(input)
                time.sleep(0.2)
                keyin = myfont.render(input_show, False, (0, 0, 0))
                screen.blit(keyin, (xvalin,yvaltext))
                flip()
                
        if subtract_button.get_rect(x=(150),  y=(45)).collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                input.append('-')
                input_show = ''.join(input)
                time.sleep(0.2)
                keyin = myfont.render(input_show, False, (0, 0, 0))
                screen.blit(keyin, (xvalin,yvaltext))
                flip()
        
        if divide_button.get_rect(x=(290),  y=(45)).collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                input.append('/')
                input_show = ''.join(input)
                time.sleep(0.2)
                keyin = myfont.render(input_show, False, (0, 0, 0))
                screen.blit(keyin, (xvalin,yvaltext))
                flip()
        
        if multiply_button.get_rect(x=(430),  y=(45)).collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                input.append('*')
                input_show = ''.join(input)
                time.sleep(0.2)
                keyin = myfont.render(input_show, False, (0, 0, 0))
                screen.blit(keyin, (xvalin,yvaltext))
                flip()
         


