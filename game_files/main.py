import pygame
import random
import os, sys
import time
from pygame.locals import *

from renderutils import windowSize

width, height = windowSize
os.environ['SDL_VIDEO_CENTERED'] = '1'

from renderutils import *
from imageutils import *

from entityClass import *
from gameClass import *
from mapClass import *
from dialogueClass import *


gameName = "game"
gameCaption = "Frodadurg"

#width = 1920
#height = 1080
#windowSize = width, height
FPS = 60

game = game(gameName, gameCaption, windowSize, FPS)

game.createMap("beach", windowSize, (10, 10), [], [], [portal("port", "default_map", "icons/default_map.png", (width * 2/3, height * 1/3)), portal("port", "2fort", "icons/2fort.png", (width * 1/3, height * 1/3))])
game.maps["beach"].setBackground(r"icons/pokBack.png")

game.createMap("2fort", windowSize, (10, 10), [], [], [portal("port", "default_map", "icons/default_map.png", (width * 2/3, height * 8/9)), portal("port", "beach", "icons/pokBack.png", (width * 1/3, height * 8/9))])
game.maps["2fort"].setBackground(r"icons/2fort.png")

game.createPortal("beach_portal", "beach", "icons/pokBack.png", (width * 1/3, height * 3/5))
game.createPortal("2fort_portal", "2fort", "icons/2fort.png", (width * 2/3, height / 3/5))


game.createEntity("Rock", r"icons/rock.jpg", (width * 3/5, height / 3), True, "object", (40, 40))

p0 = entity("Froh", r"icons/frog_art",(width / 4, height / 4), False, "player", (110, 110))
p1 = entity("Fritz2", r"icons/frog_art",(width / 2, height / 2), False, "player", (110, 110))


game.addPlayer(p0)
game.addEntity(p1)

d1 = dialogueBox(iconPath = r"icons/frog_art/icon.png", header = "Fritz", body = ["Hello, I'm Frog.",
                "Ribidi Toilet...",
                "Fuck yourself."])

d2 = dialogueBox(iconPath = r"icons/frog_art/icon.png", header = "Fritz", body = ["Go away...",
                  "BLAH BLAH BLAH",
                  "Bye now!"], isRepeatable = True)

p1.addDialogue(d1)
p1.addDialogue(d2)

game.init()

while game.running:

    speed = game.player.speedUnit
    keys_pressed = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == QUIT:
        
            game.quit()

    if (game.player.canMove):
            
        if (keys_pressed[K_LSHIFT]):
    
            speed *= 2

        if keys_pressed[K_s]:
    
            game.player.rect.y += speed
            game.player.setDirection(0)

        elif keys_pressed[K_w]:
    
            game.player.rect.y -= speed
            game.player.setDirection(1)

        if keys_pressed[K_a]:
    
            game.player.rect.x -= speed
            game.player.setDirection(2)

        elif keys_pressed[K_d]:
    
            game.player.rect.x += speed
            game.player.setDirection(3)        

        
    game.player.boundsCheck((game.width, game.height))
    
    game.playerDraw()
    game.renderMap()

    game.render()
    game.playerCollisionProcesses(keys_pressed)

    game.collisionCorrection()

    if (game.player.health == 0):

        game.quit()

    pygame.display.update()
    game.fpsTick()

pygame.quit()