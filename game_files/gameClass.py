import pygame
from entityClass import *
from mapClass import *

#TODO: add object and portal collision for player and other live entities

class game:

    def __init__ (self, name, caption, size, FPS):

        self.running = True
        
        self.maps = {"default_map" : map("default_map", size, (10, 10))}
        self.activemap = self.maps["default_map"]
        self.activemap.setBackground(r"icons/default_map.png")
        self.activemap.addTexture(r"icons/brick.png")

        self.transitionmap = None

        self.name = name
        self.caption = caption
        self.size = size
        self.width, self.height = size
        self.FPS = FPS
        self.player = entity()

        self.fadeScreen = pygame.Surface(size)
        self.fadeScreen.fill((0, 0, 0))

        self.isFading = False
        self.fadeIncrement = 3
        self.fadeAlpha = 0

        self.SCREEN = pygame.display.set_mode(size)
        pygame.display.set_caption(self.caption)
        self.fpsClock = pygame.time.Clock()


    def init(self):

        pygame.init()

    def createPlayer(self, name, image, spawnCoords, isEnemy = False, entityType = "player",dims = (60, 60), speedUnit = 3, randValues = [1, 16]):

        self.player = entity(name, image, spawnCoords, isEnemy, entityType, dims, speedUnit, randValues)

    def createEntity(self, name = "char", image = DEFAULT_IMG, spawnCoords = (0, 0), isEnemy = False, entityType = "object", dims = (60, 60), speedUnit = 3, randValues = [1, 16]):

        self.activemap.entities.append(entity(name, image, spawnCoords, isEnemy, entityType, dims, speedUnit, randValues))

    def createPortal(self, name, destination, imagePath, spawnCoords, isEnemy = False, entityType = "portal", dims = [60, 60], speedUnit = 3, randValues = [1, 16]):

        self.activemap.portals.append(portal(name, destination, imagePath, spawnCoords, isEnemy, entityType, dims, speedUnit, randValues))

    def createMap(self, name, size, block_size = (10, 10), textures = [], entities = [], portals = []):

        self.maps[name] = map(name, size, block_size, textures, entities, portals)

    def changeCaption(self, caption):

        self.caption = caption
        pygame.display.set_caption(caption)
        
    def playerMove(self, speed = None, bounds = None):

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
    


    def initiateScreenFade(self):

        self.isFadingOut = True
        self.player.canMove = False

        return


    def portalCollisionCheck(self):

        for portal in self.activemap.portals:

            if self.player.rect.colliderect(portal.rect):

                self.isFading = True
                self.player.canMove = False

                if (not portal.destination in self.maps):
    
                    self.transitionmap = self.maps["default_map"]

                else:

                    self.transitionmap = self.maps[portal.destination]

            
    def collisionCorrection(self):

        objects = self.activemap.entities

        for obj in objects:

            colliding = self.player.rect.colliderect(obj.rect)

            if (colliding):

                ObjectTopPlayerBottomDifference = abs(self.player.rect.bottom - obj.rect.top)
                ObjectBottomPlayerTopDifference = abs(self.player.rect.top - obj.rect.bottom)
                ObjectLeftPlayerRightDifference = abs(self.player.rect.right - obj.rect.left)
                ObjectRightPlayerLeftDifference = abs(self.player.rect.left - obj.rect.right)

                objectPlayerFaceDifferences = [ObjectTopPlayerBottomDifference,
                                               ObjectBottomPlayerTopDifference,
                                               ObjectLeftPlayerRightDifference,
                                               ObjectRightPlayerLeftDifference]
                
                objectPlayerFaceDifferencesMin = min(objectPlayerFaceDifferences)

                if (objectPlayerFaceDifferencesMin == ObjectTopPlayerBottomDifference):

                    self.player.rect.bottom = obj.rect.top

                elif (objectPlayerFaceDifferencesMin == ObjectBottomPlayerTopDifference):

                    self.player.rect.top = obj.rect.bottom

                elif (objectPlayerFaceDifferencesMin == ObjectLeftPlayerRightDifference):

                    self.player.rect.right = obj.rect.left

                else:

                    self.player.rect.left = obj.rect.right

                return
            
    
            
    def renderMap(self):

        self.activemap.renderMap(self.SCREEN)

    def render(self):

        for entity in self.activemap.entities:

            self.SCREEN.blit(entity.image, entity.rect)

        for portal in self.activemap.portals:

            self.SCREEN.blit(portal.image, portal.rect)

        self.SCREEN.blit(self.player.image, self.player.rect)

        if (self.isFading):

            self.renderFadeScreen()


    def renderFadeScreen(self):

        MAX_ALPHA = 254

        if (self.fadeAlpha < MAX_ALPHA):

            self.fadeScreen.set_alpha(self.fadeAlpha)

        elif (self.fadeAlpha < (MAX_ALPHA * 2)):

            self.fadeScreen.set_alpha(MAX_ALPHA - (self.fadeAlpha % MAX_ALPHA))

        else:

            self.isFading = False
            self.player.canMove = True
            self.fadeAlpha = 0
            
            return
        
        self.fadeAlpha += self.fadeIncrement
        self.SCREEN.blit(self.fadeScreen, (0, 0))

        if ( (self.fadeAlpha // self.fadeIncrement) == (MAX_ALPHA // self.fadeIncrement) ) and (self.transitionmap != None):

            self.activemap = self.transitionmap


    def fpsTick(self):

        self.fpsClock.tick(self.FPS)

    def quit(self):

        self.running = False

    def __str__ (self):

        print(f"{self.name}:   size:{self.size}  entities:{self.entities}  FPS:{self.fps}")