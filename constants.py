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
FPS_CLOCK = pygame.time.Clock()

# Window size
WINDOW_WIDTH = 1250
WINDOW_HEIGHT = 680
DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Board constants
FIELD_SIZE = 40
SPACE_SIZE = 10
BOARD_WIDTH = 10
BOARD_HEIGHT = 10
assert BOARD_WIDTH == 10 and BOARD_HEIGHT == 10, 'Board is not okay.'

X_MARGIN = int((WINDOW_WIDTH - (BOARD_WIDTH * (FIELD_SIZE + SPACE_SIZE))) / 2)
Y_MARGIN = int((WINDOW_HEIGHT - (BOARD_HEIGHT * (FIELD_SIZE + SPACE_SIZE))) / 2)

# Colors (rgb space)
NAVY = (10, 15, 68)
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
RED = (255, 0, 0)

BG_COLOR = NAVY
UNREVEALED_FIELD_COLOR = GREY
EMPTY_FIELD_COLOR = WHITE
SHIP_FIELD_COLOR = RED

# Players
HARD_AI = 'HardAI'
MEDIUM_AI = 'MediumAI'
RANDOM_AI = 'RandomAI'
HUMAN = 'Human'

# Ships
CARRIER = 'Carrier'
BATTLESHIP = 'Battleship'
CRUISER = 'Cruiser'
SUBMARINE = 'Submarine'
DESTROYER = 'Destroyer'

REVEALED = True
HAS_SHIP = True
ALL_SHIPS = ((CARRIER, 5), (BATTLESHIP, 4), (CRUISER, 3), (SUBMARINE, 3), (DESTROYER, 2))
MAX_NO_OF_HITS = 17

# Messages
YOU_WON = 'Congratulations!'
NO_OF_MOVES = 'Number of moves: '
AI_VS_PLAYER = 'AI vs Player'
AI_VS_AI = 'AI vs AI'
BATTLESHIP_CAPTION = 'BattleShip'
EASY_DIFFICULTY = 'Easy'
MEDIUM_DIFFICULTY = 'Medium'
HARD_DIFFICULTY = 'Hard'
HUMAN_MOVE = 'human'
AI_MOVE = 'ai'
NAIVE_STRATEGY = 'Random moves'
ADVANCED_STRATEGY = 'Parity + Target/Hunt Strategy'
