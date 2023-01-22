## Get modules
import pygame, sys
from pygame.locals import *
import pygame_gui

## Get additional programms
import scramblePlayer as sp
import scramble2ndScreen as s2s


## Intitiate game
pygame.init()


font1 = "bahnschrift"
font2 = "Georgia"


## Set window name
WIDTH, HEIGHT= 850, 600
screen_size = (WIDTH, HEIGHT)
DISPLAYSURF = pygame.display.set_mode( screen_size )
pygame.display.set_caption( 'Death scramble' )

## User interface manager
CLOCK = pygame.time.Clock()
UserManager = pygame_gui.UIManager(screen_size)


## Game name
line1 = 'Welcome to'
line2 = 'Deadly scrammble'
line3 = 'Where fun meets terror !!!!! :| ' 
## Rules
line4 = 'Rule 1: You will get random scrambled words to guess'
line5 = 'Rule 2: Your task is to get each word correctly to gain points. Failure to do so will result in the loss off points'
line6 = 'Rule 3: If you gain enough point you advance to harder levels, and if you lose all points you die !!!!'
line7 = 'Rule 4: Try to have fun ;-) '


## Game name
line1 = 'Welcome to'
line2 = 'Deadly scrammble'
line3 = 'Where fun meets terror !!!!! :| ' 
## Rules
line4 = 'Rule 1: You will get random scrambled words to guess'
line5 = 'Rule 2: Your task is to get each word correctly to gain points. Failure to do so will result in the loss off points'
line6 = 'Rule 3: If you gain enough point you advance to harder levels, and if you lose all points you die !!!!'
line7 = 'Rule 4: Try to have fun ;-) '

## Show game details line 
x2, y2 = 185, 83
line1font = pygame.font.SysFont(font1, 30).render(line1, True, "green")
line1rect = line1font.get_rect(center=(x2, y2))
x2, y2 = 140, 88
line2font = pygame.font.SysFont(font1, 110).render(line2, True, "red")
line2rect = line1font.get_rect(center=(x2, y2))
x2, y2 = 530, 150
line3font = pygame.font.SysFont(font1, 30).render(line3, True, "white")
line3rect = line1font.get_rect(center=(x2, y2))
## Show game rules
x_delta = 17
x2, y2 = 270, 210
line4font = pygame.font.SysFont(font1, 20).render(line4, True, "white")
line4rect = line4font.get_rect(center=(x2 - x_delta, y2))
x2, y2 = 440, 230
line5font = pygame.font.SysFont(font1, 20).render(line5, True, "white")
line5rect = line5font.get_rect(center=(x2 - x_delta, y2))
x2, y2 = 155, 250
line6font = pygame.font.SysFont(font1, 20).render(line6, True, "white")
line6rect = line1font.get_rect(center=(x2 - x_delta, y2))
x2, y2 = 178, 265
line7font = pygame.font.SysFont(font1, 20).render(line7, True, "white")
line7rect = line7font.get_rect(center=(x2 - x_delta, y2))


## Quit Button
x2, y2 = 370, 500
WIDTH, HEIGHT = 100, 50
font = pygame.font.SysFont(font2, 40, bold=True)
surf1 = font.render('Quit', True, 'white')
BUTTON_quit = pygame.Rect(x2,y2,WIDTH, HEIGHT)
## Next Button
#x2, y2 = 450, 510
#WIDTH, HEIGHT = 100, 50
#font = pygame.font.SysFont(font2, 40, bold=True)
#surf2 = font.render('Next', True, 'white')
#BUTTON_next = pygame.Rect(x2,y2,WIDTH, HEIGHT)


## Press ENTER prompt

x3, y3 = 400, 415
Press_next = 'Press Enter to go to the next page'
Press_nextfont = pygame.font.SysFont(font1, 30).render(Press_next, True, "white")
Press_nextrect = line1font.get_rect(center=(x3 - 100, y3 + 15))


## Textbox
    # Box
def textbox(objectID):
    x1, y1 = 320, 350
    WIDTH, HEIGHT = 350, 30
    PLAYER_NAME = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((x1, y1), (WIDTH, HEIGHT)), manager=UserManager, object_id=objectID)

textbox("player_name")


## Begin game play
## Main game loop
while True:

    ## Textbox
     # Title
    Player_name = 'Player name'
    x1, y1 = 320, 350
    namefont = pygame.font.SysFont(font1, 30).render(Player_name, True, "white")
    namerect = line1font.get_rect(center=(x1 - 100, y1 + 15))

    DISPLAYSURF.fill("black")               ## Set screen background to white

    UI_REFRESH_RATE = CLOCK.tick(60)/1000               ## Frames per second: To allow for reasonable cursor blink time
    
    UserManager.update(UI_REFRESH_RATE)                 ## Update user interface object

    UserManager.draw_ui(DISPLAYSURF)         # Pass into screen

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if BUTTON_quit.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "player_name":
            DISPLAYSURF = pygame.display.set_mode( screen_size )
            UserManager = pygame_gui.UIManager(screen_size)
            name1 = event.text
            name1font = pygame.font.SysFont(font1, 30).render(name1, True, "white")
            name1rect = line1font.get_rect(center=(400, 250))
            DISPLAYSURF.blit(name1font, name1rect)
            s2s.next1(UserManager, DISPLAYSURF, name1)
            

        UserManager.process_events(event)
		
    DISPLAYSURF.blit(line1font, line1rect)
    DISPLAYSURF.blit(line2font, line2rect)
    DISPLAYSURF.blit(line3font, line3rect)
    DISPLAYSURF.blit(line4font, line4rect)
    DISPLAYSURF.blit(line5font, line5rect)
    DISPLAYSURF.blit(line6font, line6rect)
    DISPLAYSURF.blit(line7font, line7rect)
    DISPLAYSURF.blit(surf1, BUTTON_quit)
    #DISPLAYSURF.blit(surf2, BUTTON_next)
    DISPLAYSURF.blit(namefont, namerect)
    DISPLAYSURF.blit(Press_nextfont, Press_nextrect)
    pygame.display.update()

    ## Updates the game state
    ## draws the Surface object returned by pygame.display.set_mode() to the screen

    CLOCK.tick(60)
