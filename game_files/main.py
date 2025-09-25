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

game = game(name = "game", 
            caption = "Frogburg", 
            size = WINDOWSIZE, 
            FPS = 60, 
            background = r"icons/tempBack.png",
            iconPath = r"icons/frog_art/icon.png")

game.createMap(name = "2fort", 
               size = WINDOWSIZE, 
               block_size = (10, 10), 
               background = r"icons/sball.png",
               portals = [portal("port",
                                 "default_map", 
                                 "icons/default_map.png", 
                                 (WINDOWx * 2/3, WINDOWy * 8/9)), 
                          portal("port", 
                                 "beach", 
                                 DEFAULT_PORTAL_IMG, 
                                 (WINDOWx * 1/3, WINDOWy * 8/9))])
                                 
game.maps["2fort"].setBackground(r"icons/2fort.png")

game.createPortal("2fort_portal", 
                  "2fort", 
                  "icons/2fort.png", 
                  (WINDOWx * 2/3, WINDOWy / 3/5))



p0 = entity("Frog", 
            r"icons/frog_art",
            (WINDOWx / 4, WINDOWy / 4), 
            False, 
            "player", 
            (110, 110))

p1 = entity("Frog2", 
            r"icons/frog_art",
            (WINDOWx / 2, WINDOWy / 2), 
            False, 
            "player", 
            (110, 110))

p2 = entity("Frog2", 
            r"icons/frog_art",
            (WINDOWx / 2, WINDOWy / 2), 
            False, 
            "player", 
            (110, 110))


game.addPlayer(p0)
game.addEntity(p1)
game.addEntityWithMap(entity = p2, 
                      map = "2fort")
                      
game.addEntity(entity("Frog2", 
                      r"icons/frog_art",
                      (WINDOWx * 1/3, WINDOWy * 1/2), 
                      False, 
                      "player", 
                      (110, 110)))



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
            "Bye now!"])

p1.addDialogue(d1)
p1.addDialogue(d2)
p2.addDialogue(d2)

while True:

    if (game.mainMenu.isActive):

        game.menuLoop()

    if (game.running == False):

        break

    game.refreshKeyPresses()
    game.checkForQuitInput()
    speed = game.player.speedUnit

    if (game.player.canMove):
            
        if (game.keys_pressed[K_m]):
            
            game.mainMenu.isActive = True

        if (game.keys_pressed[K_LSHIFT]):
    
            speed *= 2

        if game.keys_pressed[K_s]:
    
            game.player.rect.y += speed
            game.player.setDirection(0)

        elif game.keys_pressed[K_w]:
    
            game.player.rect.y -= speed
            game.player.setDirection(1)

        if game.keys_pressed[K_a]:
    
            game.player.rect.x -= speed
            game.player.setDirection(2)

        elif game.keys_pressed[K_d]:
    
            game.player.rect.x += speed
            game.player.setDirection(3)        

        
    game.player.boundsCheck((game.width, game.height))
    
    game.render()

    game.playerCollisionProcesses(game.keys_pressed)

    game.collisionCorrection()

    if (game.player.health == 0):

        game.quit()

    pygame.display.update()
    game.fpsTick()


pygame.quit()