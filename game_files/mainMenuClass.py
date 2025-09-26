from settings import DEFAULT_TEXTURE, DEFAULT_MENUBACKGROUND
from settings import WINDOWx, WINDOWy, WINDOWSIZE
from imageutils import redimensionImage
from renderutils import getWindowSize
from mapClass import *
import pygame


class mainMenu (map):

    def __init__(self, SCREEN, background = DEFAULT_MENUBACKGROUND):

        map.__init__(self, name = "menu", size = WINDOWSIZE)
    
        self.SCREEN = SCREEN
        self.isActive = True

        self.newgame_icon = pygame.image.load().convert_alpha()
        self.continuegame_icon = pygame.image.load().convert_alpha()
        self.options_icon = pygame.image.load().convert_alpha()
        
        self.setBackground(DEFAULT_MENUBACKGROUND)

    def render(self):

        self.renderMap(SCREEN = self.SCREEN)
        pygame.draw.rect(self.SCREEN, (240, 240, 240), (0, 0, 100, 100))

