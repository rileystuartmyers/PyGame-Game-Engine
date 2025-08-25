import pygame
import os, sys
import random
from pygame.locals import *

def resizeImage(image, scaleX, scaleY):

    if (scaleX > 0) and (scaleY > 0):

        image = pygame.transform.scale(image, (image.get_width() * scaleX, image.get_height() * scaleY))

    return image

def rescaleImage(image, scale):

    if (scale > 0):

        image = pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))
    
    return image

def redimensionImage(image, dimX, dimY):

    if (dimX > 0) and (dimY > 0):

        image = pygame.transform.scale(image, (dimX, dimY))

    return image

def checkCollision(player, objects):

    for obj in objects:

        if (obj.top == player.bottom) or (obj.bottom == player.top) or (obj.left == player.right) or (obj.right == player.left):

            return True
        
    return False


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIME = (120, 200, 50)
NAVY = (40, 40, 130)
SALMON = (200, 80, 90)
YELLOW = (200, 200, 0)

key_dict = {

    K_r:RED, 
    K_g:GREEN, 
    K_b:BLUE,
    K_w:YELLOW,
    K_a:SALMON, 
    K_s:LIME, 
    K_d:NAVY

}

size = 800, 600
width, height = size
background = RED
caption = ""

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()
SCREEN = pygame.display.set_mode(size)
running = True

randMin = 1
randMax = 8

randSpeedMin = 3
randSpeedMax = 12

playerPath = r"icons/mcguckin.png"
player = pygame.image.load(playerPath)
player = redimensionImage(player, 60, 60)
playerRect = player.get_rect()
speedUnit = 3
speed = [speedUnit, speedUnit]

playerRect.center = width / 2, height / 2

blobPath0 = r"icons/bball.png"
blob0 = pygame.image.load(blobPath0)
blob0 = redimensionImage(blob0, 50, 50)
rect0 = blob0.get_rect()
blob0speed = [3, 0]

blobPath1 = r"icons/sball.png"
blob1 = pygame.image.load(blobPath1)
blob1 = redimensionImage(blob1, 80, 80)
rect1 = blob1.get_rect()
blob1speed = [3, 0]


backgroundPath = r"icons/background.jpgw"
background = pygame.image.load(backgroundPath)
background = redimensionImage(background, width, height)


while running:

    for event in pygame.event.get():

        if event.type == QUIT:
        
            running = False

        elif event.type == KEYDOWN and (event.key in key_dict):

            #background = key_dict[event.key]
            #caption = "Background Color: " + str(background)

            if event.key == K_d:
    
                speed[0] = -speed[0]

            elif event.key == K_w:

                speed[1] = -speed[1]    


    playerRect = playerRect.move(speed)
    rect0 = rect0.move(blob0speed)
    rect1 = rect1.move(blob1speed)

    if (playerRect.left < 2) or (playerRect.right > width - 2):

        speed[0] = -speed[0]

    if (playerRect.top < 2) or (playerRect.bottom > height - 2):

        speed[1] = -speed[1]

    if (rect0.left > width):

        rect0.bottom = width / random.randrange(randMin, randMax)
        blob0speed[0] = random.randrange(randSpeedMin ,randSpeedMax)
        rect0.right = 0

    if (rect1.left > width):

        rect1.bottom = width / random.randrange(randMin, randMax)
        blob1speed[0] = random.randrange(randSpeedMin ,randSpeedMax)
        rect1.right = 0
    
    if (playerRect.collidelistall([rect0, rect1])):

        running = False

    pygame.draw.rect(SCREEN, RED, playerRect, 1)
    pygame.draw.rect(SCREEN, RED, rect0, 1)
    pygame.draw.rect(SCREEN, RED, rect1, 1)

    SCREEN.blit(background, (0, 0))
    SCREEN.blit(player, playerRect)
    SCREEN.blit(blob0, rect0)
    SCREEN.blit(blob1, rect1)

    pygame.display.set_caption(caption)
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()