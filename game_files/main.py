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

game = game("game", "Walking Fritz", (width, height), 60, r"icons/pokBack.png")
gamemap = map("default_map", (width, height), (30, 30))
#gamemap.setBackground("icons/background.jpg")
gamemap.addTexture(r"icons/blah.png")

game.createPlayer("Fritz", r"icons/frisk.png",(width / 2, height / 2), False, (60, 60))
s
game.createEntity("Rock", r"icons/rock.jpg", (width / 3, height / 3), True, (40, 40))

game.createEntity("Mcgucket", r"icons/mcgucket.png", (width / 5, height / 8), False, (100, 100))



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
    
    gamemap.renderMap(game.SCREEN)    
    game.render()

    game.playerDraw()
    pygame.display.update()
    game.fpsTick()

pygame.quit()