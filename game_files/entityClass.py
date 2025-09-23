import pygame
import os
from pygame.locals import *
from imageutils import redimensionImage

DEFAULT_IMG = r"icons/sball.png"
DEFAULT_PORTAL = r"icons/portal.png"

class entity:

    def __init__ (self, name = "char", imagePath = "", spawnCoords = (0, 0), isEnemy = False, entityType = "object", dims = [60, 60], speedUnit = 3, randValues = [1, 16]):

        self.images = []

        if (os.path.isdir(imagePath)):

            self.images.append(redimensionImage(pygame.image.load(os.path.join(imagePath, "front.png")), dims[0], dims[1]))
            self.images.append(redimensionImage(pygame.image.load(os.path.join(imagePath, "behind.png")), dims[0], dims[1]))
            self.images.append(redimensionImage(pygame.image.load(os.path.join(imagePath, "left.png")), dims[0], dims[1]))
            self.images.append(redimensionImage(pygame.image.load(os.path.join(imagePath, "right.png")), dims[0], dims[1]))

            self.image = self.images[0]

        elif (os.path.isfile(imagePath)):

            self.image = redimensionImage(pygame.image.load(imagePath), dims[0], dims[1])

        else:

            self.image = redimensionImage(pygame.image.load(DEFAULT_IMG), dims[0], dims[1])

        self.name = name
        self.entityType = entityType
        self.health = 3
        self.facing = 0   # (down, up, left, right) => (0, 1, 2, 3)
        self.isEnemy = isEnemy
        self.speedUnit = speedUnit
        self.randValues = randValues
        self.canMove = True

        self.rect = self.image.get_rect()
        self.rect.center = spawnCoords

        self.dialogue = []
        self.dialogueCount = 0
        self.isTalking = False
    
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

    def getType(self):

        return self.entityType
    
    def setType(self, entityType):

        self.entityType = entityType
        
    def getDirection(self):

        return self.facing

    def setDirection(self, direction):

        self.facing = direction
        self.changeDirectionImage()

    def changeDirectionImage(self):

        if (not len(self.images) <= 1):

            self.image = self.images[self.facing]

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

    """
    def addDialogue(self, header, body, subtext, isRepeatable = False):

        if (header == None or header == ""):

            header = self.name

        if (subtext == None or subtext == ""):

            subtext = "Press 'e' to continue"

        dialogue = dialogueBox(header = header, body = body, subtext = subtext, isRepeatable = isRepeatable)
        self.dialogue.append(dialogue)

        return
    """

    def addDialogue(self, dialogue):

        if (len(self.dialogue) == 0):

            dialogue.body.insert(0, "")
            
        self.dialogue.append(dialogue)

    def draw(self, SCREEN, color = (0, 0, 0), width = 0):

        pygame.draw.rect(SCREEN, color, self.rect, width)

    def __str__ (self):

        return f"{self.name} {self.rect.x} {self.rect.y} {self.speedUnit}"

class portal (entity):

    def __init__ (self, name = "port", destination = "", imagePath = "", spawnCoords = (0, 0), isEnemy = False, entityType = "object", dims = [60, 60], speedUnit = 3, randValues = [1, 16]):

        if (imagePath == ""):

            self.image = redimensionImage(pygame.image.load(DEFAULT_IMG), dims[0], dims[1])

        else:

            self.image = redimensionImage(pygame.image.load(imagePath), dims[0], dims[1])

        self.name = name
        self.destination = destination
        self.entityType = entityType
        self.isEnemy = isEnemy
        self.speedUnit = speedUnit
        self.randValues = randValues

        self.rect = self.image.get_rect()
        self.rect.center = spawnCoords