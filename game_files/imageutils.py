import pygame

def resizeImage(image, dimX, dimY):

    if (dimX > 0) and (dimY > 0):

        image = pygame.transform.scale(image, (image.get_width() * dimX, image.get_height() * dimY))

    return image

def rescaleImage(image, scale):

    if (scale > 0):

        image = pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))
    
    return image

def redimensionImage(image, dimX, dimY):

    if (dimX > 0) and (dimY > 0):

        image = pygame.transform.scale(image, (dimX, dimY))

    return image