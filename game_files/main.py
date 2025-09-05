import pygame
import random
import os, sys
import time
from pygame.locals import *

from imageutils import *
from renderutils import *

from entityClass import *
from gameClass import *
from mapClass import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

width = 1000
height = 600

game = game("game", "Frodadurg", (width, height), 60)
game.createPortal("port", "alternate", "", (width / 4, height / 3))

game.createMap("alternate", (width, height), (10, 10), [loadImage("icons/rock.jpg")], [], [portal("port", "default_map")])

game.createPlayer("Fritz", r"icons/frog_art",(width / 2, height / 2), False, "player", (90, 90))

game.createEntity("Rock", r"icons/rock.jpg", (width / 3, height / 3), True, "object", (40, 40))

game.createEntity("Mcgucket", r"icons/mcgucket.png", (width / 5, height / 8), False, "object", (100, 100))



game.init()

while game.running:

    for event in pygame.event.get():

        if event.type == QUIT:
        
            game.quit()

        elif event.type == KEYDOWN:

            if event.key == K_d:
    
                game.player.speed[0] = game.player.speedUnit

            elif event.key == K_w:

                game.player.speed[1] = -game.player.speedUnit

            elif event.key == K_a:

                game.player.speed[0] = -game.player.speedUnit

            elif event.key == K_s:

                game.player.speed[1] = game.player.speedUnit

        elif event.type == KEYUP:

            if event.key == K_w or event.key == K_s:
            
                game.player.speed[1] = 0

            if event.key == K_a or event.key == K_d:
                
                game.player.speed[0] = 0

    game.playerMove()

    if (game.enemyPlayerCollision()):

        game.quit()
    
    game.playerDraw()
    game.renderMap()
    game.render()

    game.portalCollisionCheck()

    pygame.display.update()
    game.fpsTick()

pygame.quit()