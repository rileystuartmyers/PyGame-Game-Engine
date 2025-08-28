import pygame

def renderBackground(SCREEN, background, pos = (0, 0)):

    SCREEN.blit(background, pos)

def renderAll(SCREEN, background, entities):

    renderBackground(SCREEN, background)

    for entity in entities:

        SCREEN.blit(entity.image, entity.rect)