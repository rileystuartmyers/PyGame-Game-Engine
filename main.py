import pygame
import os, sys
import random
from pygame.locals import *

def resizeImage(image, scaleX, scaleY):

    if (scaleX > 0) and (scaleY > 0):

        image = pygame.transform.scale(image, (image.get_width() * scaleX, image.get_height() * scaleY))

    return image

def rescaleImage(image, scale):

    if (scale > 0):

        image = pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))
    
    return image

def redimensionImage(image, dimX, dimY):

    if (dimX > 0) and (dimY > 0):

        image = pygame.transform.scale(image, (dimX, dimY))

    return image


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

size = 450, 500
width, height = size
background = RED
caption = ""

pygame.init()
rand = random.randrange(1)
print(rand)
FPS = 60
fpsClock = pygame.time.Clock()
SCREEN = pygame.display.set_mode(size)
running = True

ball = pygame.image.load(r"game/icons/slate.png")
ball = rescaleImage(ball, 0.2)
rect = ball.get_rect()

blah = pygame.image.load(r"game/icons/blah.png")
blah = rescaleImage(ball, 0.2)
rect2 = blah.get_rect()

background = pygame.image.load(r"game/checkered_background.png")
background = redimensionImage(background, width, height)

speedUnit = 3
speed = [speedUnit, speedUnit]
speedBot = [3, 1]

while running:

    for event in pygame.event.get():

        if event.type == QUIT:
        
            running = False

        elif event.type == KEYDOWN and (event.key in key_dict):

            #background = key_dict[event.key]
            #caption = "Background Color: " + str(background)

            if event.key == K_d:
    
                speed[0] = -speed[0]

            elif event.key == K_w:

                speed[1] = -speed[1]    


    rect = rect.move(speed)
    rect2 = rect2.move(speedBot)

    if (rect.left < 0) or (rect.right > width):

        speed[0] = -speed[0]

    if (rect.top < 0) or (rect.bottom > height):

        speed[1] = -speed[1]


    if (rect2.left < 0) or (rect2.right > width):

        speedBot[0] = -speedBot[0]

    if (rect2.top < 0) or (rect2.bottom > height):

        speedBot[1] = -speedBot[1]
    
    pygame.draw.rect(SCREEN, RED, rect, 1)
    pygame.draw.rect(SCREEN, RED, rect2, 1)

    SCREEN.blit(background, (0, 0))
    SCREEN.blit(ball, rect)
    SCREEN.blit(blah, rect2)
        

    pygame.display.set_caption(caption)
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
