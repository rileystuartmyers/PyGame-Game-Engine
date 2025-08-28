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

def renderBackground(SCREEN, background, pos = (0, 0)):

    SCREEN.blit(background, pos)

def renderAll(SCREEN, background, entities):

    renderBackground(SCREEN, background)

    for entity in entities:

        SCREEN.blit(entity.image, entity.rect)


class entity:

    def __init__ (self, name, image, spawnCoords, isEnemy, width = 60, height = 60, speed = [0, 0], speedUnit = 3, randValues = [1, 16]):

        self.name = name
        self.image = redimensionImage(pygame.image.load(image), width, height)
        self.speed = speed
        self.isEnemy = isEnemy
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

    def collisionCheck(self, entities):

        for index in self.rect.collidelistall(entities):

            if (entities[index].isEnemy != self.isEnemy):

                return True
        
        return False
    
    def collisionCount(self, entities):

        count = 0

        for index in self.rect.collidelistall(entities):

            if (entities[index].isEnemy != self.isEnemy):

                count += 1

        return count

    def __str__ (self):

        return f"{self.name} {self.rect.x} {self.rect.y} {self.speed}"


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

            if event.key == K_w:
            
                player.speed[1] = 0

            if event.key == K_s:
                
                player.speed[1] = 0

            if event.key == K_a:
                
                player.speed[0] = 0
            
            if event.key == K_d:

                player.speed[0] = 0


    player.move()

    player.boundsCheck(width, height)
    print(player.collisionCount(entityList))

    if (player.collisionCheck(entityList)):

        running = False
    
    pygame.draw.rect(SCREEN, (0,0,0), player.rect, 1)

    renderAll(SCREEN, background, entityList)

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()