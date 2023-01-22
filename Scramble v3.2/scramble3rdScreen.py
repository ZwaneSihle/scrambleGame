## Get modules
import pygame, sys
from pygame.locals import *
import pygame_gui

## Get additional programms
import scramblePlayer as sp
import scrambleGameScreenv32 as sgs


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


## Quit Button
x2, y2 = 370, 500
WIDTH, HEIGHT = 100, 50
font = pygame.font.SysFont(font2, 40, bold=True)
surf1 = font.render('Quit', True, 'white')
BUTTON_quit = pygame.Rect(x2,y2,WIDTH, HEIGHT)


## Press ENTER prompt
x3, y3 = 400, 415
Press_next = 'Press Enter to go to the next page'
Press_nextfont = pygame.font.SysFont(font1, 30).render(Press_next, True, "white")
Press_nextrect = line1font.get_rect(center=(x3 - 100, y3 + 15))


## Textbox
    # Box
def next3(UserManager, DISPLAYSURF, player_name, phrase):

    ## Greet
    x_delta = 20
    y_delta = 30
    greet = 'Hey!'
    x2, y2 = 310 - x_delta, 237 - y_delta
    greetfont = pygame.font.SysFont(font1,25).render(greet, True, "orange")
    greetrect = greetfont.get_rect(center=(x2, y2))
    ## Player name
    player1 = player_name
    x2, y2 = 420 - x_delta, 250 - y_delta
    player1font = pygame.font.SysFont(font1,50).render(player1, True, "white")
    player1rect = player1font.get_rect(center=(x2, y2))
    ## Welcome
    welcome = 'welcome to the best game ever !!! '
    x2, y2 = 470 - x_delta, 275 - y_delta
    welcomefont = pygame.font.SysFont(font1,22).render(welcome, True, "orange")
    welcomerect = welcomefont.get_rect(center=(x2, y2))

    x1, y1 = 320, 350
    WIDTH, HEIGHT = 350, 30
    DIFFICULTY = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((x1, y1), (WIDTH, HEIGHT)), manager=UserManager, object_id="difficulty")

    ## Begin game play
    ## Main game loop
    while True:

        ## Textbox
        # Title
        difficultyLevel = 'Difficulty'
        x1, y1 = 320, 350
        difficultyLevelfont = pygame.font.SysFont(font1, 30).render(difficultyLevel, True, "white")
        difficultyLevelrect = difficultyLevelfont.get_rect(center=(x1 - 100, y1 + 15))

        ## Available level
        select = "Enter 1 (easy), 2 (medium), 3 (hard), 4 (deadly), 5 (Oh you're gone gone!)"
        x1, y1 = 523, 320
        selectfont = pygame.font.SysFont(font1, 20).render(select, True, "white")
        selectrect = selectfont.get_rect(center=(x1 - 100, y1 + 15))

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

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "difficulty":
                DISPLAYSURF = pygame.display.set_mode( screen_size )
                UserManager = pygame_gui.UIManager(screen_size)
                diff = event.text

                sgs.next4(UserManager, DISPLAYSURF, player1, phrase, diff, 3, '')
                
            UserManager.process_events(event)
            
        DISPLAYSURF.blit(line1font, line1rect)
        DISPLAYSURF.blit(line2font, line2rect)
        DISPLAYSURF.blit(line3font, line3rect)
        DISPLAYSURF.blit(surf1, BUTTON_quit)
        DISPLAYSURF.blit(player1font, player1rect)
        DISPLAYSURF.blit(difficultyLevelfont, difficultyLevelrect)
        DISPLAYSURF.blit(selectfont, selectrect)
        DISPLAYSURF.blit(Press_nextfont, Press_nextrect)
        DISPLAYSURF.blit(greetfont, greetrect)
        DISPLAYSURF.blit(welcomefont, welcomerect)
        pygame.display.update()

        ## Updates the game state
        ## draws the Surface object returned by pygame.display.set_mode() to the screen

        CLOCK.tick(60)
