import pygame
import numpy as np
import math
import os
from imageutils import redimensionImage

DEFAULT_TEXTURE = r"icons/brick.png"

class map:

    def __init__ (self, name, size, block_size = (10, 10), textures = [], entities = [], portals = []):

        self.name = name
        self.width, self.height = block_size
        self.res_width, self.res_height = size
        self.textures = textures
        self.entities = entities
        self.portals = portals
        self.background = None

        if (len(self.textures) == 0):

            self.addTexture(DEFAULT_TEXTURE)    

        for texture in textures:

            texture = redimensionImage(texture, round(self.res_width / self.width), round(self.res_height / self.height))

        self.grid = np.zeros(block_size, dtype=int)

    def saveMap(self, SCREEN):

        pygame.image.save(SCREEN, f"icons/{self.name}.png")
        self.background = pygame.image.load(f"icons/{self.name}.png")

    def createCustomMap(self, SCREEN):
        
        for y in range(self.width):

            for x in range(self.height):

                ind = self.grid[y, x]
                texture = self.textures[ind]

                SCREEN.blit(texture, (math.floor(self.res_width * (y / self.width)), math.floor(self.res_height * (x / self.height))))

        self.saveMap(SCREEN)

    def renderMap(self, SCREEN):

        if (self.background):

            SCREEN.blit(self.background, (0, 0))

        else:

            self.createCustomMap(SCREEN)

    def setBackground(self, path):

        self.background = pygame.image.load(path)
        self.background = redimensionImage(self.background, self.res_width, self.res_height)

    def addTexture(self, path):

        img = pygame.image.load(path)
        img = redimensionImage(img, round(self.res_width / self.width), round(self.res_height / self.height))

        self.textures.append(img)

    
    def __str__ (self):

        pass