import pygame
from entityClass import *

class game:

    def __init__ (self, name, caption, size, FPS, backgroundPath, entities = []):

        self.running = True

        self.name = name
        self.caption = caption
        self.size = size
        self.width, self.height = size
        self.FPS = FPS
        self.entities = entities
        self.player = entity()

        self.background = pygame.image.load(backgroundPath)
        self.background = redimensionImage(self.background, self.width, self.height)
        self.SCREEN = pygame.display.set_mode(size)
        pygame.display.set_caption(self.caption)
        self.fpsClock = pygame.time.Clock()

    def init(self):

        pygame.init()

    def createPlayer(self, name, image, spawnCoords, isEnemy = False, dims = (60, 60), speed = [0, 0], speedUnit = 3, randValues = [1, 16]):

        self.player = entity(name, image, spawnCoords, isEnemy, dims, speed, speedUnit, randValues)

    def createEntity(self, name = "char", image = r"icons/", spawnCoords = (0, 0), isEnemy = False, dims = (60, 60), speed = [0, 0], speedUnit = 3, randValues = [1, 16]):

        self.entities.append(entity(name, image, spawnCoords, isEnemy, dims, speed, speedUnit, randValues))

    def changeBackground(self, backgroundPath):

        self.background = pygame.image.load(backgroundPath, self.size) # self.size might need to be replaced by
                                                                       # individual size values

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

        if (self.player.enemyCollisionCheck(self.entities)):

            return True

    def totalPlayerCollision(self):

        if (self.player.totalCollisionCheck(self.entities)):

            return True
        
    def renderBackground(self, pos = (0, 0)):

        self.SCREEN.blit(self.background, pos)

    def render(self):

        self.renderBackground()

        for entity in self.entities:

            self.SCREEN.blit(entity.image, entity.rect)

        self.SCREEN.blit(self.player.image, self.player.rect)

    def fpsTick(self):

        self.fpsClock.tick(self.FPS)

    def quit(self):

        self.running = False

    def __str__ (self):

        print(f"{self.name}:   size:{self.size}  entities:{self.entities}  FPS:{self.fps}")