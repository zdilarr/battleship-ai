"""
    Application constants should be listed here.
    Author: Emilija Zdilar 6-5-2018
"""
import pygame
import os

# Positioning the window
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 30)

# Frames per second (speed)
FPS = 30
FPSCLOCK = pygame.time.Clock()

# Window size
WINDOWWIDTH = 1250
WINDOWHEIGHT = 680
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

# Board constants
FIELDSIZE = 40
SPACESIZE = 10
BOARDWIDTH = 10
BOARDHEIGHT = 10
assert BOARDWIDTH == 10 and BOARDHEIGHT == 10, 'Board is not okay.'

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (FIELDSIZE + SPACESIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (FIELDSIZE + SPACESIZE))) / 2)

# Colors (rgb space)
NAVY = (10, 15, 68)
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
RED = (255, 0, 0)

BGCOLOR = NAVY
UNREVEALEDFIELDCOLOR = GREY
EMPTYFIELDCOLOR = WHITE
SHIPFIELDCOLOR = RED

# Players
HARDAI = 'HardAI'
MEDIUMAI = 'MediumAI'
RANDOMAI = 'RandomAI'
HUMAN = 'Human'

# Ships
CARRIER = 'Carrier'
BATTLESHIP = 'Battleship'
CRUISER = 'Cruiser'
SUBMARINE = 'Submarine'
DESTROYER = 'Destroyer'

REVEALED = True
HASSHIP = True
ALLSHIPS = ((CARRIER, 5), (BATTLESHIP, 4), (CRUISER, 3), (SUBMARINE, 3), (DESTROYER, 2))
