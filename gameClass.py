import pygame
from entityClass import *

class game:

    # def __init__ (self, name, image, spawnCoords, isEnemy, 
    # dims = (60, 60), speed = [0, 0], speedUnit = 3, randValues = [1, 16]):

    def __init (self, name, caption, size, FPS, backgroundPath, entities = []):

        self.running = True

        self.name = name
        self.caption = caption
        self.size = size
        self.FPS = FPS
        self.entities = entities

        pygame.init()

        self.background = pygame.image.load(backgroundPath)
        self.SCREEN = pygame.display.set_mode(size)
        self.fpsClock = pygame.time.Clock()

    def createEntity(self, name, image, spawnCoords, isEnemy, dims = (60, 60), speed = [0, 0], speedUnit = 3, randValues = [1, 16]):

        self.entities.append(entity(name, image, spawnCoords, isEnemy, dims, speed, speedUnit, randValues))
        
    def __str__ (self):

        print(f"{self.name}:   size:{self.size}  entities:{self.entities}  FPS:{self.fps}")
        