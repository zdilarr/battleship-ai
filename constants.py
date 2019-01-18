import pygame
import os

"""
Pozicioniranje prozora
"""
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 30)

"""
FPS - frames per secons (brzina)
"""
FPS = 30
FPSCLOCK = pygame.time.Clock()

"""
veličina prozora
"""
WINDOWWIDTH = 1250
WINDOWHEIGHT = 680
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

"""
konstante za ploču
"""
FIELDSIZE = 40
SPACESIZE = 10
BOARDWIDTH = 10
BOARDHEIGHT = 10
assert BOARDWIDTH == 10 and BOARDHEIGHT == 10, 'Ploca nije ok'

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (FIELDSIZE + SPACESIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (FIELDSIZE + SPACESIZE))) / 2)

"""
boje  (Red, Green, Blue)
"""
NAVY = (10, 15, 68)
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
RED = (255, 0, 0)

BGCOLOR=NAVY
UNREVEALEDFIELDCOLOR = GREY
EMPTYFIELDCOLOR = WHITE
SHIPFIELDCOLOR = RED

"""
Igraci
"""
HARDAI = 'HardAI'
MEDIUMAI = 'MediumAI'
RANDOMAI = 'RandomAI'
HUMAN = 'Human'

"""
Brodovi
"""
CARRIER = 'Carrier'
BATTLESHIP = 'Battleship'
CRUISER = 'Cruiser'
SUBMARINE = 'Submarine'
DESTROYER = 'Destroyer'

REVEALED = True
HASSHIP = True
ALLSHIPS = ((CARRIER, 5), (BATTLESHIP, 4), (CRUISER, 3), (SUBMARINE, 3), (DESTROYER, 2))
