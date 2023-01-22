## Get modules
import pygame, sys
from pygame.locals import *
import pygame_gui

## Get other programs
import scrambleWords as sw
import scrambleFunctions as sf
import scramblePlayer as sp
import scrambleWelcomeScreen as sws

## https://pygame-gui.readthedocs.io/en/v_040/pygame_gui.elements.html


## Intitiate game
pygame.init()

## Set window name
WIDTH, HEIGHT= 850, 600
screen_size = (WIDTH, HEIGHT)
DISPLAYSURF = pygame.display.set_mode( screen_size )
pygame.display.set_caption( 'Death scramble' )

## User interface manager
CLOCK = pygame.time.Clock()
UserManager = pygame_gui.UIManager(screen_size)

## Text input components
    ## Make text input function
x1, y1 = 100, 450
WIDTH, HEIGHT = 600, 50
TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((x1, y1), (WIDTH, HEIGHT)), manager=UserManager, object_id="main_text_entry")


## Begin game play
## Main game loop
while True :

    DISPLAYSURF.fill("black")               ## Set screen background to white

    UI_REFRESH_RATE = CLOCK.tick(60)/1000               ## Frames per second: To allow for reasonable cursor blink time
    ##
        ## Make text update components
    UserManager.update(UI_REFRESH_RATE)                 ## Update user interface object

    for event in pygame.event.get():
    ## for loop that will iterate over the list of Event objects that was returned by pygame.event.get()
    ## a variable named event will be assigned the value of the next event object in this list
    ## If no events have happened, then pygame.event.get() will return a blank list
        if event.type == QUIT:
            ## Remember that since we used the from pygame.locals import * form of the import statement, we only have to type QUIT instead of pygame.locals.QUIT
            pygame.quit()
            ## The pygame.quit() it runs code that deactivates the Pygame library
            sys.exit()
            ## sys.exit() to terminate the program

        ## Event action


        UserManager.process_events(event)

    
    UserManager.draw_ui(DISPLAYSURF)         # Pass into screen

    pygame.display.update()
    ## Updates the game state
    ## draws the Surface object returned by pygame.display.set_mode() to the screen

    CLOCK.tick(60)/1000