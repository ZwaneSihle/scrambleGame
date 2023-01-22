## Get game modules
import pygame, sys
from pygame.locals import *
import pygame_gui

## Make a player object
 # Get the player's name
 # Winning pop up massage
 # Level of difficulty (very easy [3], easy [5], moderate [7], hard [9], very hard [])

class player:
    def __init__(self, player_name, catch_phrase, life, skippedWord = '', difficulty = 1, played_words = [] ):
        self.player_name = player_name
        self.catch_phrase = catch_phrase
        self.life = life
        self.skippedWord = skippedWord
        self.difficulty = difficulty
        self.played_words = played_words

    class progress:
        def __init__(self):
            pass

def player_bio(playerx):
    print( 'Player name:        ' + str(playerx.player_name))
    print( 'Catch phrase:       ' + str(playerx.catch_phrase))
    print( 'Difficulty level:   ' + str(playerx.difficulty ))