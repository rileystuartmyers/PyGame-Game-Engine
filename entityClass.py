import pygame
from pygame.locals import *
from imageutils import redimensionImage

class entity:

    def __init__ (self, name = "char", image = r"icons/blah.png", spawnCoords = (0, 0), isEnemy = False, dims = (60, 60), speed = [0, 0], speedUnit = 3, randValues = [1, 16]):

        self.name = name
        self.image = redimensionImage(pygame.image.load(image), dims)
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

    def movec(self, speed):

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

    def draw(self, SCREEN, color = (0, 0, 0), width = 0):

        pygame.draw.rect(SCREEN, color, self.rect, width)

    def __str__ (self):

        return f"{self.name} {self.rect.x} {self.rect.y} {self.speed}"
