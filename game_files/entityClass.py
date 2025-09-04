import pygame
import os
from pygame.locals import *
from imageutils import redimensionImage

DEFAULT_IMG = r"icons/blah.png"

class entity:

    def __init__ (self, name = "char", imagePath = "", spawnCoords = (0, 0), isEnemy = False, dims = [60, 60], speed = [0, 0], speedUnit = 3, randValues = [1, 16]):

        self.images = []
        self.facing = 0   # (front, back, left, right) => (0, 1, 2, 3)

        if (os.path.isdir(imagePath)):

            self.images.append(redimensionImage(pygame.image.load(os.path.join(imagePath, "front.png")), dims[0], dims[1]))
            self.images.append(redimensionImage(pygame.image.load(os.path.join(imagePath, "behind.png")), dims[0], dims[1]))
            self.images.append(redimensionImage(pygame.image.load(os.path.join(imagePath, "left.png")), dims[0], dims[1]))
            self.images.append(redimensionImage(pygame.image.load(os.path.join(imagePath, "right.png")), dims[0], dims[1]))

            self.image = self.images[self.facing]

        elif (os.path.isfile(imagePath)):

            self.image = redimensionImage(pygame.image.load(imagePath), dims[0], dims[1])

        else:

            #raise Exception("Provided invalid path for entity image(s)!")        
            self.image = redimensionImage(pygame.image.load(DEFAULT_IMG), dims[0], dims[1])

        self.name = name
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

    def getDirection(self):

        if (self.speed[1] < 0):

            self.facing = 1

        elif (self.speed[1] > 0):

            self.facing = 0

        if (self.speed[0] < 0):

            self.facing = 2

        elif (self.speed[0] > 0):

            self.facing = 3

    def changeDirectionImage(self):

        if (not len(self.images) <= 1):

            self.image = self.images[self.facing]
        
    def movec(self, speed):

        self.rect = self.rect.move(speed)
        self.getDirection()
        self.changeDirectionImage()

    def move(self):

        self.rect = self.rect.move(self.speed)
        self.getDirection()
        self.changeDirectionImage()

    def boundsCheck(self, dims):

        width, height = dims

        if (self.rect.left < 2):

            self.rect.left = 2

        elif (self.rect.right > width - 2):

            self.rect.right = width - 2


        if (self.rect.top < 2):

            self.rect.top = 2

        elif (self.rect.bottom > height - 2):

            self.rect.bottom = height - 2

    def enemyCollisionCheck(self, entities):

        for index in self.rect.collidelistall(entities):

            if (entities[index].isEnemy != self.isEnemy):

                return True
        
        return False
    
    def totalCollisionCheck(self, entities):

        if (self.rect.collidelistall(entities) != -1):

            return True
        
        return False
    
    def collisionCount(self, entities):

        count = 0

        for index in self.rect.collidelistall(entities):

            if (entities[index].isEnemy != self.isEnemy):

                count += 1

        return count

    def draw(self, SCREEN, color = (0, 0, 0), width = 0):

        pygame.draw.rect(SCREEN, color, self.rect, width)

    def __str__ (self):

        return f"{self.name} {self.rect.x} {self.rect.y} {self.speed}"
