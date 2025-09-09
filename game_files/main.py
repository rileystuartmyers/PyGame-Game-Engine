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
game.createMap("beach", (width, height), (10, 10), [], [], [portal("port", "default_map", "icons/default_map.png", (width * 2/3, height * 1/3)), portal("port", "2fort", "icons/2fort.png", (width * 1/3, height * 1/3))])
game.createMap("2fort", (width, height), (10, 10), [], [], [portal("port", "default_map", "icons/default_map.png", (width * 2/3, height * 8/9)), portal("port", "beach", "icons/pokBack.png", (width * 1/3, height * 8/9))])

game.maps["beach"].setBackground(r"icons/pokBack.png")
game.maps["2fort"].setBackground(r"icons/2fort.png")

game.createPortal("beach_portal", "beach", "icons/pokBack.png", (width * 1/3, height * 3/5))
game.createPortal("2fort_portal", "2fort", "icons/2fort.png", (width * 2/3, height / 3/5))


game.createPlayer("Fritz", r"icons/frog_art",(width / 2, height / 2), False, "player", (80, 80))

game.createEntity("Rock", r"icons/rock.jpg", (width / 3, height / 3), True, "object", (40, 40))

game.createEntity("Mcgucket", r"icons/mcgucket.png", (width / 5, height / 8), False, "object", (100, 100))


game.init()

while game.running:

    speed = game.player.speedUnit
    keys = pygame.key.get_pressed()

    if (keys[K_LSHIFT]):
        speed *= 2



    if keys[K_s]:
        game.player.rect.y += speed
        game.player.setDirection(0)

    elif keys[K_w]:
        game.player.rect.y -= speed
        game.player.setDirection(1)



    if keys[K_a]:
        game.player.rect.x -= speed
        game.player.setDirection(2)

    elif keys[K_d]:
        game.player.rect.x += speed
        game.player.setDirection(3)

    for event in pygame.event.get():

        if event.type == QUIT:
        
            game.quit()

        

    game.player.boundsCheck((game.width, game.height))
    
    game.playerDraw()
    game.renderMap()
    game.render()

    game.portalCollisionCheck()
    game.collisionCheck()

    pygame.display.update()
    game.fpsTick()

pygame.quit()