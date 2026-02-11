from settings import WINDOWx, WINDOWy, WINDOWSIZE
from settings import DEFAULT_CHARACTER_IMG, DEFAULT_PORTAL_IMG
import pygame
import random
import os, sys
import time
from pygame.locals import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

from renderutils import *
from imageutils import *
from entityClass import *
from gameClass import *
from mapClass import *
from dialogueClass import *
from mainMenuClass import *

from game import gameContents
while True:

    if (gameContents.running == False):
        break

    if (gameContents.mainMenu.isActive):
        pygame.mixer.stop()
        gameContents.mainMenu.playMenuMusic()
        gameContents.menuLoop()

    if (gameContents.keys_pressed[K_m]):
        gameContents.mainMenu.isActive = True

    gameContents.refreshKeyPresses()
    gameContents.checkForQuitInput()

    gameContents.movementProcesses()
    #gameContents.player.boundsCheck((gameContents.width, gameContents.height))

    gameContents.render()
    gameContents.playerCollisionProcesses(gameContents.keys_pressed)
    gameContents.collisionCorrection()

    if (gameContents.player.health == 0):
        gameContents.quit()

    pygame.display.update()
    gameContents.fpsTick()


pygame.quit()