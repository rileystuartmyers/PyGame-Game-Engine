from settings import DEFAULT_BACKGROUND, DEFAULT_TEXTURE, DEFAULT_MENUBACKGROUND, DEFAULT_MUSIC
from settings import DEFAULT_CHARACTER_IMG, DEFAULT_PROJECTILE_IMG
import pygame
from entityClass import *
from mapClass import *
from dialogueClass import dialogueBox
from mainMenuClass import *

DEFAULT_DIALOGUE = dialogueBox()


class game:

    def __init__ (self, name, caption, size, FPS, background = DEFAULT_BACKGROUND, texture = DEFAULT_TEXTURE, iconPath = None):

        self.running = True
                
        self.maps = {"default_map" : map(name = "default_map", 
                                         size = size,
                                          block_size = (10, 10))}
        self.activemap = self.maps["default_map"]
        self.transitionmap = self.maps["default_map"]
        self.currentMusic = self.activemap.music

        self.name = name
        self.caption = caption
        self.size = size
        self.width, self.height = size
        self.FPS = FPS
        self.player = entity()
        
        self.fadeScreen = pygame.Surface(size)
        self.fadeScreen.fill((0, 0, 0))

        self.isFading = False
        self.fadeIncrement = 5
        self.fadeAlpha = 0

        self.fpsClock = pygame.time.Clock()
        self.currentDialogue = DEFAULT_DIALOGUE
        self.SCREEN = pygame.display.set_mode(size, pygame.FULLSCREEN)

        self.activemap.setBackground(background)
        self.activemap.addTexture(texture)

        self.mainMenu = mainMenu(SCREEN = self.SCREEN)

        self.keys_pressed = pygame.key.get_pressed()

        if (iconPath):

            icon = pygame.image.load(iconPath)
            pygame.display.set_icon(icon)

        pygame.display.set_caption(self.caption)

        self.init()

    def init(self):

        pygame.init()

    def createPlayer(self, name, image, spawnCoords, isEnemy = False, entityType = "player",dims = (60, 60), speedUnit = 3, randValues = [1, 16]):

        self.player = entity(name, image, spawnCoords, isEnemy, entityType, dims, speedUnit, randValues)

    def addPlayer(self, player):
        
        self.player = player

    def createEntity(self, name = "char", image = DEFAULT_CHARACTER_IMG, spawnCoords = (0, 0), isEnemy = False, entityType = "object", dims = (60, 60), speedUnit = 3, randValues = [1, 16]):

        self.activemap.entities.append(entity(name, image, spawnCoords, isEnemy, entityType, dims, speedUnit, randValues))

    def createEntityWithMap(self, name = "char", map = "default_map", image = DEFAULT_CHARACTER_IMG, spawnCoords = (0, 0), isEnemy = False, entityType = "object", dims = (60, 60), speedUnit = 3, randValues = [1, 16]):

        self.maps[map].entities.append(entity(name, image, spawnCoords, isEnemy, entityType, dims, speedUnit, randValues))
    
    def addEntity(self, entity):

        self.activemap.entities.append(entity)

    def addEntityWithMap(self, entity, map = "default_map"):

        self.maps[map].entities.append(entity)

    def createPortal(self, name, destination, imagePath, spawnCoords, isEnemy = False, entityType = "portal", dims = [60, 60], speedUnit = 3, randValues = [1, 16]):

        self.activemap.portals.append(portal(name, destination, imagePath, spawnCoords, isEnemy, entityType, dims, speedUnit, randValues))

    def addPortal(self, portal):

        self.activemap.portals.append(portal)

    def createMap(self, name, size, musicPath = DEFAULT_MUSIC, block_size = (10, 10), textures = [], entities = [], portals = [], background = None):

        self.maps[name] = map(name, size, musicPath, block_size, textures, entities, portals)

        if (background):

            self.maps[name].setBackground(background)

    def addMap(self, map):

        self.maps[map.name] = map

    def createProjectile(self, name = "projectile", imagePath = "", spawnCoords = (0, 0), direction = 0, isEnemy = True, ownerEntity = None, entityType = "object", dims = [30, 30], speedUnit = 5, randValues = [1, 16]):

        self.activemap.projectiles.append(projectile(name, imagePath, spawnCoords, direction, isEnemy, ownerEntity, entityType, dims, speedUnit, randValues))

    def addProjectile(self, projectile):

        self.activemap.projectiles.append(projectile)

    def changeCaption(self, caption):

        self.caption = caption
        pygame.display.set_caption(caption)
        
    def playerMovement(self):
            
        speed = self.player.speedUnit
        if (self.player.canMove):
                
            if (self.keys_pressed[K_LSHIFT]):
        
                speed *= 2

            if self.keys_pressed[K_s]:
        
                self.player.rect.y += speed
                self.player.setDirection(0)

            elif self.keys_pressed[K_w]:
        
                self.player.rect.y -= speed
                self.player.setDirection(1)

            if self.keys_pressed[K_a]:
        
                self.player.rect.x -= speed
                self.player.setDirection(2)

            elif self.keys_pressed[K_d]:
        
                self.player.rect.x += speed
                self.player.setDirection(3)

        self.player.boundsCheck((self.width, self.height))

    def projectileMovement(self):

        print(type(self.activemap.projectiles))
        for projectile in self.activemap.projectiles:

            speed = projectile.speedUnit
            direction = projectile.facing

            if (direction == 0):

                projectile.rect.y += speed

            elif (direction == 1):

                projectile.rect.y -= speed

            elif (direction == 2):

                projectile.rect.x -= speed
                
            elif (direction == 3):

                projectile.rect.x += speed

            if (projectile.boundsCheck((self.width, self.height))):
                self.activemap.projectiles.remove(projectile)

            #print(f"x = {projectile.rect.x}, y = {projectile.rect.y}\n")

    def movementProcesses(self):

        self.playerMovement()
        self.projectileMovement()

    def playerDraw(self, color = (0, 0, 0), width = 0):

        self.player.draw(self.SCREEN, color, width)
    
    def enemyPlayerCollision(self):

        if (self.player.enemyCollisionCheck(self.activemap.entities)):

            return True

    def totalPlayerCollision(self):

        if (self.player.totalCollisionCheck(self.activemap.entities)):

            return True
    
    def playerHit(self):

        self.player.health -= 1
            
        
    def playerCollisionProcesses(self, keys):

        offset = 3
        self.portalCollisionCheck()

        for projectile in self.activemap.projectiles:

            if (self.player.rect.colliderect(projectile.rect)):

                self.playerHit()

        for entity in self.activemap.entities:

            if (self.player.rect.colliderect(entity.rect)):
                
                if (entity.isEnemy == True):

                    self.playerHit()                

                if (len(entity.dialogue) - entity.dialogueCount <= 0):

                    return
                
                remainingDialogueLineCount = len(entity.dialogue[entity.dialogueCount].body) - entity.dialogue[entity.dialogueCount].bodyCount  - 1
                
                if (keys[K_e]) and (remainingDialogueLineCount > 0) and (entity.isTalking == False):

                    entity.isTalking = True
                    self.player.canMove = False
                    self.currentDialogue = entity.dialogue[entity.dialogueCount]
                    entity.dialogue[entity.dialogueCount].bodyCount += 1

                elif (keys[K_e]) and (remainingDialogueLineCount <= 0) and (entity.isTalking == False):

                    entity.isTalking = False
                    self.player.canMove = True
                    self.currentDialogue = DEFAULT_DIALOGUE
                    offset = -1

                    entity.dialogue[entity.dialogueCount].bodyCount = 0
                    
                    if (entity.dialogue[entity.dialogueCount].isRepeatable == False):

                        entity.dialogueCount += 1


                elif (not keys[K_e]):

                    entity.isTalking = False


        self.collisionCorrection(offset)
        self.currentDialogue.render(self.SCREEN)


    def portalCollisionCheck(self):

        for portal in self.activemap.portals:

            if self.player.rect.colliderect(portal.rect):

                self.isFading = True
                self.player.canMove = False

                if (not portal.destination in self.maps):
    
                    self.transitionmap = self.maps["default_map"]

                else:

                    self.transitionmap = self.maps[portal.destination]

                

    def collisionCorrection(self, offset = 3):

        objects = self.activemap.entities

        for obj in objects:

            colliding = self.player.rect.colliderect(obj.rect)

            if (colliding):

                ObjectTopPlayerBottomDistance = abs(self.player.rect.bottom - obj.rect.top)
                ObjectBottomPlayerTopDistance = abs(self.player.rect.top - obj.rect.bottom)
                ObjectLeftPlayerRightDistance = abs(self.player.rect.right - obj.rect.left)
                ObjectRightPlayerLeftDistance = abs(self.player.rect.left - obj.rect.right)

                ObjectPlayerFaceDistances = [ObjectTopPlayerBottomDistance,
                                               ObjectBottomPlayerTopDistance,
                                               ObjectLeftPlayerRightDistance,
                                               ObjectRightPlayerLeftDistance]
                
                ObjectPlayerFaceDistancesMin = min(ObjectPlayerFaceDistances)

                if (ObjectPlayerFaceDistancesMin == ObjectTopPlayerBottomDistance):

                    self.player.rect.bottom = obj.rect.top + offset

                elif (ObjectPlayerFaceDistancesMin == ObjectBottomPlayerTopDistance):

                    self.player.rect.top = obj.rect.bottom - offset

                elif (ObjectPlayerFaceDistancesMin == ObjectLeftPlayerRightDistance):

                    self.player.rect.right = obj.rect.left + offset

                else:

                    self.player.rect.left = obj.rect.right - offset

                return

    def initiateScreenFade(self):

        self.isFadingOut = True
        self.player.canMove = False

        return
    

    def renderMap(self):

        self.activemap.renderMap(self.SCREEN)

    def render(self):

        self.playerDraw()
        self.activemap.renderMap(self.SCREEN)

        for entity in self.activemap.entities:

            self.SCREEN.blit(entity.image, entity.rect)

        for portal in self.activemap.portals:

            self.SCREEN.blit(portal.image, portal.rect)

        for projectile in self.activemap.projectiles:

            self.SCREEN.blit(projectile.image, projectile.rect)

        self.SCREEN.blit(self.player.image, self.player.rect)

        if (self.isFading):

            self.renderFadeScreen()


    def renderMenu(self):

        self.mainMenu.renderMap(SCREEN = self.SCREEN)
        
        self.SCREEN.blit(self.mainMenu.playbutton_icon, self.mainMenu.playbutton_rect)
        self.SCREEN.blit(self.mainMenu.settingsbutton_icon, self.mainMenu.settingsbutton_rect)

        if (self.isFading):

            self.renderFadeScreen(fadeIncrement = 1)


    def renderFadeScreen(self, fadeIncrement = None):
        
        if (fadeIncrement == None):
            
            fadeIncrement = self.fadeIncrement

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
        
        self.fadeAlpha += fadeIncrement
        self.SCREEN.blit(self.fadeScreen, (0, 0))

        if ( (self.fadeAlpha // fadeIncrement) == (MAX_ALPHA // fadeIncrement) ) and (self.transitionmap != None):

            if (self.activemap.musicPath != self.transitionmap.musicPath):
                
                self.currentMusic = self.transitionmap.music
                self.activemap.musicPath = self.transitionmap.musicPath

                pygame.mixer.fadeout(600)
                pygame.mixer.Sound.play(self.currentMusic, loops = -1)

            self.activemap = self.transitionmap
            self.transitionmap = None
            self.mainMenu.isActive = False


    def fpsTick(self):

        self.fpsClock.tick(self.FPS)

    def checkForQuitInput(self):

        for event in pygame.event.get():

            if (event.type == QUIT or self.keys_pressed[K_ESCAPE]):

                self.quit()

    def refreshKeyPresses(self):

        self.keys_pressed = pygame.key.get_pressed()

    def menuLoop(self):

        while (self.mainMenu.isActive):

            if (self.running == False):

                pygame.mixer.stop()
                self.currentMusic.play()

                break


            self.refreshKeyPresses()
            self.mainMenu.checkForMenuButtonClicks(self)
            self.checkForQuitInput()

            self.renderMenu()

            pygame.display.update()
            self.fpsTick()

            if (self.mainMenu.isActive == False):

                pygame.mixer.fadeout(100)
                self.currentMusic.play()

    def quit(self):

        self.running = False
        pygame.mixer.quit()

    def __str__ (self):

        print(f"{self.name}:   size:{self.size}  entities:{self.entities}  FPS:{self.fps}")