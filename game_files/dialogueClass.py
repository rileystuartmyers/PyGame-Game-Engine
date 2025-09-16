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

DEFAULT_BOXSIZE = (windowX * 3/5, windowY * 1/4)
DEFAULT_POS = (windowX * 1/5, windowY * 3/5)
DEFAULT_ICONPATH = r"icons/frisk.png"


class dialogueBox:

    def __init__ (self, boxSize = DEFAULT_BOXSIZE, pos = DEFAULT_POS, color = BLACK, text_color = WHITE, iconPath = DEFAULT_ICONPATH, header = "", body = "", subtext = ""):

        self.width, self.height = boxSize
        self.x, self.y = pos
        self.rect = (self.x, self.y, self.width, self.height)
        
        self.color = color
        self.text_color = text_color

        self.icon = loadImage(iconPath)
        self.icon = redimensionImage(self.icon, self.width // 5, self.height * 5/6)

        self.header = header
        self.body = body
        self.subtext = subtext

    def render(self, SCREEN):

        header_render = HEADER_FONT.render(self.header, True, self.text_color)
        #header_rect = header_render.get_rect(center = (self.x + self.width // 4, self.y + self.height // 6))
        header_rect = header_render.get_rect(topleft = (self.x + self.width // 4, self.y + self.height // 8))

        body_render = BODY_FONT.render(self.body, True, self.text_color)
        #body_rect = body_render.get_rect(center = (self.x + self.width // 4, self.y + self.height * 2/5))
        body_rect = body_render.get_rect(topleft = (self.x + self.width // 4, self.y + self.height * 3/8))

        subtext_render = SUBTEXT_FONT.render(self.subtext, True, self.text_color)
        #subtext_rect = subtext_render.get_rect(center = (self.x + self.width // 4, self.y + self.height * 4/5))
        subtext_rect = subtext_render.get_rect(topleft = (self.x + self.width // 4, self.y + self.height * 8/10))
        
        pygame.draw.rect(SCREEN, BLACK, self.rect)

        #pygame.draw.rect(SCREEN, WHITE, (self.x + self.width // 50, self.y + self.height // 12, self.width // 5, self.height * 5/6))
        SCREEN.blit(self.icon, (self.x + self.width // 50, self.y + self.height // 12))
        SCREEN.blit(header_render, header_rect)
        SCREEN.blit(body_render, body_rect)
        SCREEN.blit(subtext_render, subtext_rect)

        return
