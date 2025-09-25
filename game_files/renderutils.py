import pygame
from pygame.locals import *
from screeninfo import get_monitors

def getWindowSize():

    for monitor in get_monitors():

        if (monitor.is_primary == True):

            return (monitor.width, monitor.height)

    return (1920, 1080)
    

def renderBackground(SCREEN, background, pos = (0, 0)):

    SCREEN.blit(background, pos)

def renderAll(SCREEN, background, entities):

    renderBackground(SCREEN, background)

    for entity in entities:

        SCREEN.blit(entity.image, entity.rect)

def loadImage(path):

    img = pygame.image.load(path)

    return img


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIME = (120, 200, 50)
NAVY = (40, 40, 130)
SALMON = (200, 80, 90)
YELLOW = (200, 200, 0)

key_dict = {

    K_r:RED, 
    K_g:GREEN, 
    K_b:BLUE,
    K_w:YELLOW,
    K_a:SALMON, 
    K_s:LIME, 
    K_d:NAVY

}