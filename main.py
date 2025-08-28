import pygame
import os, sys
import random
from pygame.locals import *
from imageutils import *
from renderutils import *
from entityClass import *

os.environ['SDL_VIDEO_CENTERED'] = '1'






running = True

size = 1000, 600
width, height = size
caption = "Fritz Walking 2 School"
entityList = []

pygame.init()
pygame.display.set_caption(caption)
SCREEN = pygame.display.set_mode(size)

FPS = 120
fpsClock = pygame.time.Clock()


player = entity("Fritz", r"icons/frisk.png",(width / 2, height / 2), False, 60, 60)
entityList.append(player)

entityList.append(entity("Rock", r"icons/rock.jpg", (width / 3, height / 3), True, 40, 40))

entityList.append(entity("Mcgucket", r"icons/mcgucket.png", (width / 5, height / 8), True, 100, 100))

background = pygame.image.load(r"icons/pokBack.png")
background = redimensionImage(background, width, height)


while running:

    for event in pygame.event.get():

        if event.type == QUIT:
        
            running = False

        elif event.type == KEYDOWN:

            if event.key == K_d:
    
                player.speed[0] = player.speedUnit

            elif event.key == K_w:

                player.speed[1] = -player.speedUnit

            elif event.key == K_a:

                player.speed[0] = -player.speedUnit

            elif event.key == K_s:

                player.speed[1] = player.speedUnit

        elif event.type == KEYUP:

            if event.key == K_w or event.key == K_s:
            
                player.speed[1] = 0

            if event.key == K_a or event.key == K_d:
                
                player.speed[0] = 0


    player.move()

    player.boundsCheck(width, height)

    if (player.collisionCheck(entityList)):

        running = False
    
    player.draw(SCREEN)

    renderAll(SCREEN, background, entityList)

    pygame.display.update()
    fpsClock.tick(FPS)

print(player)
pygame.quit()