import pygame

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