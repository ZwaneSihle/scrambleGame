## Get modules
import pygame, sys
from pygame.locals import *
import pygame_gui

## Get additional programms
import scramblePlayer as sp
import scrambleWords as wrds
import scrambleFunctions as actn
import scramblePlayer as plyr


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
line2 = 'Deadly scrammble'

## Show game details line
y_delta = 50
size_delta = 15
x2, y2 = 220, 88
line2font = pygame.font.SysFont(font1, 50).render(line2, True, "red")
line2rect = line2font.get_rect(center=(x2, y2 - y_delta))


## Quit Button
x2, y2 = 370, 500
WIDTH, HEIGHT = 100, 50
font = pygame.font.SysFont(font2, 40, bold=True)
surf1 = font.render('Quit', True, 'white')
BUTTON_quit = pygame.Rect(x2,y2,WIDTH, HEIGHT)


## Press ENTER prompt
x3, y3 = 425, 430
Press_next = 'Press Enter to check your answer'
Press_nextfont = pygame.font.SysFont(font1, 30).render(Press_next, True, "white")
Press_nextrect = Press_nextfont.get_rect(center=(x3, y3))


## Textbox
    # Box
def next4(UserManager, DISPLAYSURF, player_name, phrase, diff, life, SkippedWord):

    ## Greet
    x_delta = -225
    y_delta = 215
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
    catch_phrase = phrase
    x2, y2 = 470 - x_delta, 265 - y_delta
    phrasefont = pygame.font.SysFont(font1,25).render(catch_phrase, True, "blue")
    phraserect = phrasefont.get_rect(center=(x2, y2))

    x1, y1 = 100, 350
    WIDTH, HEIGHT = 600, 40
    TEXTINPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((x1, y1), (WIDTH, HEIGHT)), manager=UserManager, object_id="main_text_entry")

    ## Measure game time
    start_time = pygame.time.get_ticks()

    points = 0
    health = life

    word = str( actn.game_word( diff , wrds.words ))
    scrambled = str( actn.scrumble(word) )
    text1 = f""                         ## Text line 1
    text2 = f"{scrambled}"              ## Text line 2

    ## Begin game play
    ## Main game loop
    while True:

        if points > 10:
            diff += 1
            health += 1
            points = 0
            

        ## Game stats
        ## Skipped words
        if start_time and len(SkippedWord) > 1:

            ## Title 
            skipped_word = "Skipped word:"
            x1, y1 = 290, 130
            skippedfont = pygame.font.SysFont(font1, 30).render(skipped_word, True, "orange")
            skippedrect = skippedfont.get_rect(center=(x1, y1))
            ## Word
            skipped = SkippedWord
            x1, y1 = 380, 120
            skippedwordfont = pygame.font.SysFont(font1, 30).render(skipped, True, "white")
            skippedwordrect = skippedwordfont.get_rect(topleft=(x1, y1))

            x1, y1 = 80, 130
            healthfont = pygame.font.SysFont(font1, 30).render(f"{health}", True, "white")
            healthrect = healthfont.get_rect(center=(x1 + 50, y1))
            Life = "Life:"
            lifefont = pygame.font.SysFont(font1, 30).render(Life, True, "white")
            liferect = lifefont.get_rect(center=(x1, y1))

            ## Start time
            time_since_enter = round((pygame.time.get_ticks() - start_time)/1000)

            ## Time value
            if time_since_enter > 60:
                start_time = pygame.time.get_ticks()
            elif time_since_enter >= 20 and time_since_enter < 30:
                timeValue = pygame.font.SysFont(font1, 30).render(f"{time_since_enter}s", True, "yellow")
            elif time_since_enter >= 30 and time_since_enter < 50:
                timeValue = pygame.font.SysFont(font1, 30).render(f"{time_since_enter}s", True, "orange")
            elif time_since_enter >= 50 and time_since_enter <= 60:
                timeValue = pygame.font.SysFont(font1, 30).render(f"{time_since_enter}s", True, "red")
            else:
                timeValue = pygame.font.SysFont(font1, 30).render(f"{time_since_enter}s", True, "white") 
            ## Time value rect
            time_rect = timeValue.get_rect(bottomleft = (730, 140))
                
            time = "Time:"
            x1, y1 = 690, 130
            timefont = pygame.font.SysFont(font1, 30).render(time, True, "white")
            timerect = timefont.get_rect(center=(x1, y1))

        elif start_time:

            x1, y1 = 160, 130
            health = life
            healthfont = pygame.font.SysFont(font1, 30).render(f"{health}", True, "white")
            healthrect = healthfont.get_rect(center=(x1 + 50, y1))
            Life = "Life:"
            lifefont = pygame.font.SysFont(font1, 30).render(Life, True, "white")
            liferect = lifefont.get_rect(center=(x1, y1))


            ## Start time
            time_since_enter = round((pygame.time.get_ticks() - start_time)/1000)

            ## Time value
            if time_since_enter > 60:
                start_time = pygame.time.get_ticks()
            elif time_since_enter >= 20 and time_since_enter < 30:
                timeValue = pygame.font.SysFont(font1, 30).render(f"{time_since_enter}s", True, "yellow")
            elif time_since_enter >= 30 and time_since_enter < 50:
                timeValue = pygame.font.SysFont(font1, 30).render(f"{time_since_enter}s", True, "orange")
            elif time_since_enter >= 50 and time_since_enter <= 60:
                timeValue = pygame.font.SysFont(font1, 30).render(f"{time_since_enter}s", True, "red")
            else:
                timeValue = pygame.font.SysFont(font1, 30).render(f"{time_since_enter}s", True, "white") 
            ## Time value rect
            time_rect = timeValue.get_rect(bottomleft = (600, 140))

            time = "Time:"
            x1, y1 = 550, 130
            timefont = pygame.font.SysFont(font1, 30).render(time, True, "white")
            timerect = timefont.get_rect(center=(x1, y1))


        DISPLAYSURF.fill("black")               ## Set screen background to white

        UI_REFRESH_RATE = CLOCK.tick(60)/1000               ## Frames per second: To allow for reasonable cursor blink time
        
        UserManager.update(UI_REFRESH_RATE)                 ## Update user interface object

        UserManager.draw_ui(DISPLAYSURF)         # Pass into screen

        if len(SkippedWord) > 1:
            DISPLAYSURF.blit(skippedfont, skippedrect)
            DISPLAYSURF.blit(skippedwordfont, skippedwordrect)

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
            

            ## Player death
            if health == 0:
                UserManager = pygame_gui.UIManager(screen_size)
                text1 = f"Sorry you died :'-( "     ## Text
                text2 = ""
                Press_next = ""
            
            ## Game events
            elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "main_text_entry" and event.text == word:

                word = str( actn.game_word( diff , wrds.words ))
                scrambled = str( actn.scrumble(word) )
                text1 = f"Well done, now try"    ## Text line 1
                text2 = f"{scrambled}"           ## Text line 2

                points += 1
                start_time = pygame.time.get_ticks()
            
            # User want to try another word
            elif ( event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "main_text_entry" and event.text == '-q' ):
                # Skipped word
                SkippedWord = f"{word}"
                # Generate another word
                word = str( actn.game_word( diff , wrds.words ))
                scrambled = str( actn.scrumble(word) )
                text2 = f"{scrambled}"           ## Text line 2

                health -= 1
                time_since_enter = 0
                start_time = pygame.time.get_ticks()

            elif time_since_enter >= 55 or ( event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "main_text_entry" and event.text != word ) :
                text1 = f"Try again:"           ## Text line 1
                text2 = f"{scrambled}"          ## Text line 2

                health -= 1
            
            ## Show user input
            msg = pygame.font.SysFont("bahnschrift", 70).render(text1, True, "white")    ## Text line 1
            scrabled_word = pygame.font.SysFont("bahnschrift", 100).render(text2, True, "white")    ## Text line 2

            ## Scrambled word text Reactangle
            ## And, game play output
            x1, y1 = 400, 230
            msg_rect = msg.get_rect(center=(x1, y1))

            x2, y2 = 400, 300
            scrabled_word_rect = scrabled_word.get_rect(center=(x2, y2))
                
            UserManager.process_events(event)
            
        
        DISPLAYSURF.blit(msg, msg_rect)  
        DISPLAYSURF.blit(scrabled_word, scrabled_word_rect)   
        DISPLAYSURF.blit(line2font, line2rect)
        DISPLAYSURF.blit(surf1, BUTTON_quit)
        DISPLAYSURF.blit(player1font, player1rect)
        DISPLAYSURF.blit(lifefont, liferect)
        DISPLAYSURF.blit(healthfont, healthrect)
        DISPLAYSURF.blit(timefont, timerect)
        DISPLAYSURF.blit(timeValue, time_rect)
        if health > 0:
            DISPLAYSURF.blit(Press_nextfont, Press_nextrect)
        DISPLAYSURF.blit(greetfont, greetrect)
        DISPLAYSURF.blit(phrasefont, phraserect)

        pygame.display.update()

        ## Updates the game state
        ## draws the Surface object returned by pygame.display.set_mode() to the screen

        CLOCK.tick(60)
