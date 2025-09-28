from settings import DEFAULT_TEXTURE, DEFAULT_MUSIC
import pygame
import numpy as np
import math
import os
from imageutils import redimensionImage

class map:

    def __init__ (self, name, size, musicPath = DEFAULT_MUSIC, block_size = (10, 10), textures = [], entities = [], portals = []):

        self.name = name
        self.blockWidth, self.blockHeight = block_size
        self.res_width, self.res_height = size
        self.textures = textures
        self.entities = entities
        self.portals = portals
        self.background = None
        self.musicPath = musicPath 
        self.music = pygame.mixer.Sound(file = self.musicPath)

        if (len(self.textures) == 0):

            self.addTexture(DEFAULT_TEXTURE)    
            
        self.grid = np.zeros(block_size, dtype=int)

    def saveMap(self, SCREEN):

        pygame.image.save(SCREEN, f"icons/{self.name}.png")

        img = pygame.image.load(f"icons/{self.name}.png")
        self.background = pygame.image.load(img)
        
    def createCustomMap(self, SCREEN):
        
        for y in range(self.blockWidth):

            for x in range(self.blockHeight):

                ind = self.grid[y, x]
                texture = self.textures[ind]

                SCREEN.blit(texture, (math.floor(self.res_width * (y / self.blockWidth)), math.floor(self.res_height * (x / self.blockHeight))))

        self.saveMap(SCREEN)

    def renderMap(self, SCREEN):

        if (self.background):

            SCREEN.blit(self.background, (0, 0))

        else:

            self.createCustomMap(SCREEN)

    def setBackground(self, path):

        self.background = pygame.image.load(path).convert_alpha()
        self.background = redimensionImage(self.background, self.res_width, self.res_height)

    def addTexture(self, path):

        img = pygame.image.load(path)
        img = redimensionImage(img, round(self.res_width / self.blockWidth), round(self.res_height / self.blockHeight))

        self.textures.append(img)

    def getEntityByName(self, name):

        for entity in self.entities:

            if (entity.name == name):

                return entity
            
    def getPortalByname(self, name):

        for portal in self.portals:

            if (portal.name == name):

                return portal
    

    def __str__ (self):

        pass