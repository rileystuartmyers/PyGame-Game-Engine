import pygame
import os, sys
import random
from pygame.locals import *

os.environ['SDL_VIDEO_CENTERED'] = '1'


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

class entity:

    def __init__ (self, name, image, spawnX, spawnY, width = 60, height = 60, speed = [0, 0], randValues = [1, 16]):

        self.name = name
        self.image = redimensionImage(pygame.image.load(image), width, height)
        self.speed = speed
        self.randValues = randValues

        self.rect = image.get_rect()
        self.rect.center = spawnX, spawnY

    def __str__ (self):

        return f"{self.name} {self.rect.x} {self.rect.y} {self.speed}"


running = True

size = 1000, 600
width, height = size
caption = "Fritz Walking 2 School"

pygame.init()
pygame.display.set_caption(caption)
SCREEN = pygame.display.set_mode(size)

FPS = 60
fpsClock = pygame.time.Clock()


playerPath = r"icons/frisk.png"
player = pygame.image.load(playerPath)
player = redimensionImage(player, 60, 60)
playerRect = player.get_rect()
speedUnit = 3
speed = [0, 0]

playerRect.center = width / 2, height / 2


backgroundPath = r"icons/pokBack.png"
background = pygame.image.load(backgroundPath)
background = redimensionImage(background, width, height)


while running:

    for event in pygame.event.get():

        if event.type == QUIT:
        
            running = False

        elif event.type == KEYUP:

            if event.key == K_w or event.key == K_s:
                
                speed[1] = 0

            elif event.key == K_a or event.key == K_d:

                speed[0] = 0

        elif event.type == KEYDOWN:

            if event.key == K_d:
    
                speed[0] = speedUnit

            elif event.key == K_w:

                speed[1] = -speedUnit

            elif event.key == K_a:

                speed[0] = -speedUnit

            elif event.key == K_s:

                speed[1] = speedUnit


    playerRect = playerRect.move(speed)

    if (playerRect.left < 2):
    
        playerRect.left = 3

    elif (playerRect.right > width - 2):

        playerRect.right = width - 3

    if (playerRect.top < 2):

        playerRect.top = 3
    
    elif (playerRect.bottom > height - 2):

        playerRect.bottom = height - 3


    pygame.draw.rect(SCREEN, (0,0,0), playerRect, 1)

    SCREEN.blit(background, (0, 0))
    SCREEN.blit(player, playerRect)

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()