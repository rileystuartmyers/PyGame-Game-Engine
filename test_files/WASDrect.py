import pygame
import os, sys
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

size = 1280, 500
width, height = size
background = RED
caption = ""

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()
SCREEN = pygame.display.set_mode(size)
running = True

ball = pygame.image.load("game/icons/slate.png")
ball = rescaleImage(ball, 0.25)
rect = ball.get_rect()
speed = [0, 0]
speedUnit = 7

while running:

    for event in pygame.event.get():

        if event.type == QUIT:
        
            running = False

        if event.type == KEYUP and (event.key in key_dict):

            if event.key == K_w or event.key == K_s:
                
                speed[1] = 0

            elif event.key == K_a or event.key == K_d:

                speed[0] = 0

        elif event.type == KEYDOWN and (event.key in key_dict):

            background = key_dict[event.key]
            caption = "Background Color: " + str(background)

            if event.key == K_w:
                
                speed[1] -= speedUnit

            elif event.key == K_s:

                speed[1] += speedUnit

            elif event.key == K_a:

                speed[0] -= speedUnit

            elif event.key == K_d:

                speed[0] += speedUnit

    rect = rect.move(speed)

    if (rect.left < 0):

        rect.left = 0

    elif (rect.right > width):

        rect.right = width

    elif (rect.top < 0):

        rect.top = 0

    elif (rect.bottom > height):

        rect.bottom = height



    SCREEN.fill(background)
    pygame.draw.rect(SCREEN, RED, rect, 1)
    SCREEN.blit(ball, rect)
        

    pygame.display.set_caption(caption)
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
