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

gameName = "game"
gameCaption = "Frodadurg"
width = 1000
height = 600
windowSize = width, height
FPS = 60

game = game(gameName, gameCaption, windowSize, FPS)

game.createMap("beach", windowSize, (10, 10), [], [], [portal("port", "default_map", "icons/default_map.png", (width * 2/3, height * 1/3)), portal("port", "2fort", "icons/2fort.png", (width * 1/3, height * 1/3))])
game.createMap("2fort", windowSize, (10, 10), [], [], [portal("port", "default_map", "icons/default_map.png", (width * 2/3, height * 8/9)), portal("port", "beach", "icons/pokBack.png", (width * 1/3, height * 8/9))])

game.maps["beach"].setBackground(r"icons/pokBack.png")
game.maps["2fort"].setBackground(r"icons/2fort.png")

game.createPortal("beach_portal", "beach", "icons/pokBack.png", (width * 1/3, height * 3/5))
game.createPortal("2fort_portal", "2fort", "icons/2fort.png", (width * 2/3, height / 3/5))


game.createEntity("Fritz", r"icons/frog_art",(width / 2, height / 2), False, "player", (110, 110))

game.createEntity("Rock", r"icons/rock.jpg", (width / 3, height / 3), True, "object", (40, 40))

game.createPlayer("Mananda", r"icons/mananda_art", (width / 5, height / 8), False, "object", (140, 140))


game.init()

while game.running:

    speed = game.player.speedUnit
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == QUIT:
        
            game.quit()

    if (keys[K_h]):

        game.initiateScreenFade()
        
    if (game.player.canMove):
            
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


        

    game.player.boundsCheck((game.width, game.height))
    
    game.playerDraw()
    game.renderMap()
    game.portalCollisionCheck()
    game.render()

    game.collisionCorrection()

    pygame.display.update()
    game.fpsTick()

pygame.quit()