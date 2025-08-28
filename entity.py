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

    def __init__ (self, name, image, spawnCoords, width = 60, height = 60, speed = [0, 0], speedUnit = 3, randValues = [1, 16]):

        self.name = name
        self.image = redimensionImage(pygame.image.load(image), width, height)
        self.speed = speed
        self.speedUnit = speedUnit
        self.randValues = randValues

        self.rect = self.image.get_rect()
        self.rect.center = spawnCoords

    def getSpeed(self):

        return self.speed

    def setSpeed(self, speed):

        self.speed = speed

    def getLeft(self):

        return self.rect.left
    
    def getRight(self):

        return self.rect.right

    def getTop(self):

        return self.rect.top

    def getBottom(self):

        return self.rect.bottom
    
    def getX(self):

        return self.rect.x
    
    def getY(self):

        return self.rect.y

    def move(self, speed):

        self.rect = self.rect.move(speed)

    def move(self):

        self.rect = self.rect.move(self.speed)

    def boundsCheck(self, width, height):

        if (self.rect.left < 2):

            self.rect.left = 3

        elif (self.rect.right > width - 2):

            self.rect.right = width - 3


        if (self.rect.top < 2):

            self.rect.top = 3

        elif (self.rect.bottom > height - 2):

            self.rect.bottom = height - 3



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
player = entity("Fritz", playerPath,(width / 2, height / 2), 60, 60)


backgroundPath = r"icons/pokBack.png"
background = pygame.image.load(backgroundPath)
background = redimensionImage(background, width, height)


while running:

    for event in pygame.event.get():

        if event.type == QUIT:
        
            running = False

        elif event.type == KEYUP:

            if event.key == K_w or event.key == K_s:
                
                player.speed[1] = 0

            elif event.key == K_a or event.key == K_d:

                player.speed[0] = 0

        elif event.type == KEYDOWN:

            if event.key == K_d:
    
                player.speed[0] = player.speedUnit

            elif event.key == K_w:

                player.speed[1] = -player.speedUnit

            elif event.key == K_a:

                player.speed[0] = -player.speedUnit

            elif event.key == K_s:

                player.speed[1] = player.speedUnit


    player.move()

    player.boundsCheck(width, height)

    pygame.draw.rect(SCREEN, (0,0,0), player.rect, 1)

    SCREEN.blit(background, (0, 0))
    SCREEN.blit(player.image, player.rect)

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()