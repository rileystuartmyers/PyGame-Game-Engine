import pygame
from renderutils import BLACK, WHITE, windowSize, loadImage
from imageutils import redimensionImage
from gameClass import *

pygame.font.init()

HEADER_FONT = pygame.font.Font(None, 30)
BODY_FONT = pygame.font.Font(None, 38)
SUBTEXT_FONT = pygame.font.Font(None, 18)

SUBTEXT_FONT.set_italic(True)

windowX, windowY = windowSize

#DEFAULT_BOXSIZE = (windowX * 3/5, windowY * 1/4)
DEFAULT_BOXSIZE = (windowX * 1/2, windowY * 1/4)
DEFAULT_POS = (windowX * 1/4, windowY * 3/5)
DEFAULT_ICONPATH = r"icons/sball.png"


class dialogueBox:

    def __init__ (self, boxSize = DEFAULT_BOXSIZE, pos = DEFAULT_POS, color = BLACK, border_color = WHITE, text_color = WHITE, iconPath = DEFAULT_ICONPATH, header = "", body = "", subtext = "", isRepeatable = False):

        self.width, self.height = boxSize
        self.x, self.y = pos
        self.rect = (self.x, self.y, self.width, self.height)
        self.border_rect = (self.x - (self.width * 0.015), self.y - (self.height * 0.05), self.width * 1.03, self.height * 1.1)

        self.color = color
        self.border_color = border_color
        self.text_color = text_color

        self.icon = loadImage(iconPath)
        self.icon = redimensionImage(self.icon, self.width // 5, self.height * 5/6)

        self.header = header
        self.body = body
        self.subtext = subtext

        self.bodyCount = 0
        self.isRepeatable = isRepeatable

    def hasMoreLines(self):

        if (len(self.body) == self.bodyCount + 1):

            return False
        
        return True
    

    def render(self, SCREEN):

        if (len(self.body) == 0):

            return
        
        header_render = HEADER_FONT.render(self.header, True, self.text_color)
        header_rect = header_render.get_rect(topleft = (self.x + self.width // 4, self.y + self.height // 8))

        body_render = BODY_FONT.render(self.body[self.bodyCount], True, self.text_color)
        body_rect = body_render.get_rect(topleft = (self.x + self.width // 4, self.y + self.height * 3/8))

        subtext_render = SUBTEXT_FONT.render(self.subtext, True, self.text_color)
        subtext_rect = subtext_render.get_rect(topleft = (self.x + self.width // 4, self.y + self.height * 8/10))

        pygame.draw.rect(SCREEN, self.border_color, self.border_rect)        
        pygame.draw.rect(SCREEN, self.color, self.rect)

        SCREEN.blit(self.icon, (self.x + self.width // 50, self.y + self.height // 12))
        SCREEN.blit(header_render, header_rect)
        SCREEN.blit(body_render, body_rect)
        SCREEN.blit(subtext_render, subtext_rect)

        return
