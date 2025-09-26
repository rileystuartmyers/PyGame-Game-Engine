from settings import DEFAULT_TEXTURE, DEFAULT_MENUBACKGROUND
from settings import WINDOWx, WINDOWy, WINDOWSIZE
from settings import DEFAULT_PLAYBUTTON_IMG, DEFAULT_SETTINGSBUTTON_IMG
from imageutils import redimensionImage
from renderutils import getWindowSize
from mapClass import *
import pygame


class mainMenu (map):

    def __init__(self, SCREEN, background = DEFAULT_MENUBACKGROUND):

        map.__init__(self, name = "menu", size = WINDOWSIZE)
    

        self.SCREEN = SCREEN
        self.isActive = True

        self.playbutton_icon = pygame.image.load(DEFAULT_PLAYBUTTON_IMG).convert_alpha()
        self.playbutton_icon = redimensionImage(self.playbutton_icon, 180, 100)

        self.settings_icon = pygame.image.load(DEFAULT_SETTINGSBUTTON_IMG).convert_alpha()
        self.settings_icon = redimensionImage(self.settings_icon, 100, 100)

        self.setBackground(DEFAULT_MENUBACKGROUND)

    def render(self):

        self.renderMap(SCREEN = self.SCREEN)
        
        self.SCREEN.blit(self.settings_icon, pygame.rect.Rect(self.res_width - 150, self.res_height - 150, 100, 100))
