
import pygame
from pygame.locals import *


pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))


bg = pygame.image.load("resources/images/space.png")

#INSIDE OF THE GAME LOOP
gameDisplay.blit(bg, (0, 0))

#REST OF ITEMS ARE BLIT'D TO SCREEN.

player = pygame.image.load("resources/images/dude.png")


while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(player, (100,100))
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)