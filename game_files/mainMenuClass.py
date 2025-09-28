from settings import DEFAULT_TEXTURE, DEFAULT_MENUBACKGROUND
from settings import WINDOWx, WINDOWy, WINDOWSIZE
from settings import DEFAULT_PLAYBUTTON_IMG, DEFAULT_SETTINGSBUTTON_IMG
from settings import DEFAULT_MENUMUSIC
from imageutils import redimensionImage
from renderutils import getWindowSize
from mapClass import *
import pygame


class mainMenu (map):

    def __init__(self, SCREEN, background = DEFAULT_MENUBACKGROUND):

        map.__init__(self, name = "menu", size = WINDOWSIZE, musicPath = DEFAULT_MENUMUSIC)
    
        self.SCREEN = SCREEN
        self.isActive = True

        self.playbutton_width = 350
        self.playbutton_height = 100
        self.settingsbutton_width = 100
        self.settingsbutton_height = 100

        self.playbutton_icon = redimensionImage(
            image = pygame.image.load(DEFAULT_PLAYBUTTON_IMG).convert_alpha(), 
            dimX = self.playbutton_width, 
            dimY = self.playbutton_height)
        self.settingsbutton_icon = redimensionImage(
            image = pygame.image.load(DEFAULT_SETTINGSBUTTON_IMG).convert_alpha(), 
            dimX = self.settingsbutton_width, 
            dimY = self.settingsbutton_height)
        
        self.playbutton_rect = pygame.Rect(
            (self.res_width - self.playbutton_width) / 2, 
            (self.res_height - self.playbutton_height) / 2,
            self.playbutton_width,
            self.playbutton_height)
        self.settingsbutton_rect = pygame.Rect(
            (self.res_width * 16/17) - self.settingsbutton_width,
            (self.res_height * 16/17) - self.settingsbutton_height,
            self.settingsbutton_width,
            self.settingsbutton_height)
        
        self.setBackground(DEFAULT_MENUBACKGROUND)

    def checkForMenuButtonClicks(self, gameInstance):

        hasLeftClicked = pygame.mouse.get_pressed()[0]
        mousePos = pygame.mouse.get_pos()

        if (not hasLeftClicked):

            return
        
        elif (self.playbutton_rect.collidepoint(mousePos)):

            gameInstance.isFading = True

        elif (self.settingsbutton_rect.collidepoint(mousePos)):

            print("Settings screen would pop up now!")

    def playMenuMusic(self):

        pygame.mixer.Sound.play(self.music, loops = -1)
