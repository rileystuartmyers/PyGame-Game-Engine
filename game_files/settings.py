#settings.py

import pygame
from renderutils import getWindowSize
pygame.font.init()



WINDOWSIZE = getWindowSize()
WINDOWx, WINDOWy = WINDOWSIZE
HEADER_FONT = pygame.font.Font(None, 30)
BODY_FONT = pygame.font.Font(None, 38)
SUBTEXT_FONT = pygame.font.Font(None, 18)
SUBTEXT_FONT.set_italic(True)
DEFAULT_BOXSIZE = (WINDOWx * 1/2, WINDOWy * 1/4)
DEFAULT_POS = (WINDOWx * 1/4, WINDOWy * 3/5)
DEFAULT_ICONPATH = r"icons/sball.png"
DEFAULT_TEXTURE = r"icons/brick.png"
DEFAULT_BACKGROUND = r"icons/default_map.png"
DEFAULT_MENUBACKGROUND = r"icons/menuback.png"
DEFAULT_CHARACTER_IMG = r"icons/sball.png"
DEFAULT_PORTAL_IMG = r"icons/portal.png"