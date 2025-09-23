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
gameCaption = "Frogburg"

FPS = 60

game = game(gameName, gameCaption, windowSize, FPS, background = r"icons/tempBack.png")
game.init()
game.createMap("2fort", windowSize, (10, 10), [], [], [portal("port", "default_map", "icons/default_map.png", (width * 2/3, height * 8/9)), portal("port", "beach", DEFAULT_PORTAL, (width * 1/3, height * 8/9))], background = r"icons/sball.png")

game.maps["2fort"].setBackground(r"icons/2fort.png")

game.createPortal("2fort_portal", "2fort", "icons/2fort.png", (width * 2/3, height / 3/5))



p0 = entity("Frog", r"icons/frog_art",(width / 4, height / 4), False, "player", (110, 110))
p1 = entity("Frog2", r"icons/frog_art",(width / 2, height / 2), False, "player", (110, 110))
p2 = entity("Frog2", r"icons/frog_art",(width / 2, height / 2), False, "player", (110, 110))


game.addPlayer(p0)
game.addEntity(p1)
game.addEntityWithMap(entity = p2, map = "2fort")

mult1, mult2, mult3 = 1/3, 2/3, 1/2

game.addEntity(entity("Frog2", r"icons/frog_art",(width * 1/3, height * 1/2), False, "player", (110, 110)))



d1 = dialogueBox(
    iconPath = r"icons/frog_art/icon.png",
    header = "Frog", 
    body = ["Hello, I'm Frog.",
            "Blah",
            "Blahb",
            "Ribidi Toilet..."])

d2 = dialogueBox(
    iconPath = r"icons/frog_art/icon.png", 
    header = "Frog", 
    body = ["BLAH BLAH BLAH",
            "Bye now!"],
    #isRepeatable = True)
)

p1.addDialogue(d1)
p1.addDialogue(d2)
p2.addDialogue(d2)


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