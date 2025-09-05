import pygame
from entityClass import *
from mapClass import *

#TODO: add object and portal collision for player and other live entities

class game:

    def __init__ (self, name, caption, size, FPS):

        self.running = True

        self.maps = []
        self.maps.append(map("default_map", size, (10, 10)))
        self.activemap = self.maps[0]
        
        self.activemap.setBackground(r"icons/default_map.png")
        self.activemap.addTexture(r"icons/brick.png")


        self.name = name
        self.caption = caption
        self.size = size
        self.width, self.height = size
        self.FPS = FPS
        self.player = entity()

        self.SCREEN = pygame.display.set_mode(size)
        pygame.display.set_caption(self.caption)
        self.fpsClock = pygame.time.Clock()

    def init(self):

        pygame.init()

    def createPlayer(self, name, image, spawnCoords, isEnemy = False, entityType = "object",dims = (60, 60), speed = [0, 0], speedUnit = 3, randValues = [1, 16]):

        self.player = entity(name, image, spawnCoords, isEnemy, entityType, dims, speed, speedUnit, randValues)

    def createEntity(self, name = "char", image = r"icons/", spawnCoords = (0, 0), isEnemy = False, entityType = "object", dims = (60, 60), speed = [0, 0], speedUnit = 3, randValues = [1, 16]):

        self.activemap.entities.append(entity(name, image, spawnCoords, isEnemy, entityType, dims, speed, speedUnit, randValues))

    def changeCaption(self, caption):

        self.caption = caption
        pygame.display.set_caption(caption)
        
    def playerMove(self, speed = None, bounds = None):

        if (speed == None):

            speed = self.player.speed

        if (bounds == None):

            bounds = self.width, self.height

        self.player.move()

        self.player.boundsCheck(bounds)


    def playerDraw(self, SCREEN = None, color = (0, 0, 0), width = 0):

        if (SCREEN == None):

            SCREEN = self.SCREEN

        self.player.draw(SCREEN, color, width)

    def enemyPlayerCollision(self):

        if (self.player.enemyCollisionCheck(self.activemap.entities)):

            return True

    def totalPlayerCollision(self):

        if (self.player.totalCollisionCheck(self.activemap.entities)):

            return True
        
    #def hitboxCollision(self):


    def renderMap(self):

        self.activemap.renderMap(self.SCREEN)

    def render(self):

        #self.renderBackground()

        for entity in self.activemap.entities:

            self.SCREEN.blit(entity.image, entity.rect)

        self.SCREEN.blit(self.player.image, self.player.rect)

    def fpsTick(self):

        self.fpsClock.tick(self.FPS)

    def quit(self):

        self.running = False

    def __str__ (self):

        print(f"{self.name}:   size:{self.size}  entities:{self.entities}  FPS:{self.fps}")