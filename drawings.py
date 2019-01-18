"""
Contains all methods related to GUI.
Author: Emilija Zdilar 03-05-2018
"""
from typing import Any, Tuple, List

from constants import *


def get_field_at_pixel(x: int, y: int, left_right_board: str) -> Tuple[Any, Any]:
    """
    Method that converts pixel coordinate to board field coordinate, if such field exists.
    Args:
        x: x coordinate
        y: y coordinate
        left_right_board: board one or two

    Returns: returns fields coordinates if used click on a field on the screen,
             empty coordinates otherwise.

    """

    for field_x in range(BOARD_WIDTH):
        for field_y in range(BOARD_HEIGHT):
            left, top = left_top_field_coordinate(field_x, field_y, left_right_board)
            box_rect = pygame.Rect(left, top, FIELD_SIZE, FIELD_SIZE)
            if box_rect.collidepoint(x, y):
                return field_x, field_y
    return None, None


def left_top_field_coordinate(field_x: int, field_y: int, left_right_board: str) -> Tuple[int, int]:
    """
    Helper method for drawing board
    Args:
        field_x: x coordinate
        field_y: y coordinate
        left_right_board: specified board

    Returns: top left field coordinates

    """
    if left_right_board == 'left':
        left = field_x * (FIELD_SIZE + SPACE_SIZE) + 50
        top = field_y * (FIELD_SIZE + SPACE_SIZE) + Y_MARGIN + 80
        return left, top
    if left_right_board == 'right':
        left = WINDOW_WIDTH - field_x * (FIELD_SIZE + SPACE_SIZE) - 100
        top = field_y * (FIELD_SIZE + SPACE_SIZE) + Y_MARGIN + 80
        return left, top


def draw_board(board: List[List[List[bool]]], left_right: str) -> None:
    """
    Method that draws one of the specified boards, for a given configuration.
    Args:
        board:
        left_right:

    Returns:

    """
    for field_x in range(BOARD_WIDTH):
        for field_y in range(BOARD_HEIGHT):
            left, top = left_top_field_coordinate(field_x, field_y, left_right)
            if board[field_x][field_y][0] is not REVEALED:
                pygame.draw.rect(DISPLAY_SURF, UNREVEALED_FIELD_COLOR, (left, top, FIELD_SIZE, FIELD_SIZE))
            elif board[field_x][field_y][0] is REVEALED and board[field_x][field_y][1] is not HAS_SHIP:
                pygame.draw.rect(DISPLAY_SURF, EMPTY_FIELD_COLOR, (left, top, FIELD_SIZE, FIELD_SIZE))
            elif board[field_x][field_y][0] is REVEALED and board[field_x][field_y][1] is HAS_SHIP:
                pygame.draw.rect(DISPLAY_SURF, SHIP_FIELD_COLOR, (left, top, FIELD_SIZE, FIELD_SIZE))


def draw_header() -> None:
    """
    Helper method that draws Battleship sign and Logo
    Returns: None

    """
    font_obj = pygame.font.SysFont('Courier New', 32)
    text_surface_obj = font_obj.render('BattleShip', True, GREY, NAVY)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (100, 30)
    DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)
    ship_img =\
        pygame.image.load('.\img\ship.png')
    ship_x = 130
    ship_y = 10
    DISPLAY_SURF.blit(ship_img, (ship_x, ship_y))


def has_won(player_one_or_two: str) -> None:
    """
    Method that displays the winner
    Args:
        player_one_or_two: Player that won

    Returns:

    """
    font_obj = pygame.font.SysFont('Courier New', 20)
    text_surface_obj = font_obj.render(YOU_WON, True, GREY, NAVY)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (300, 140) if player_one_or_two == 'Player One' else (920, 140)
    DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)


def draw_match_no(match_no: int, no_of_games: int) -> None:
    """
    Method that draws current match number for multi-match
    games.
    Args:
        match_no:
        no_of_games:

    Returns:

    """

    font_obj = pygame.font.SysFont('Courier New', 20)
    text_surface_obj = font_obj.render(str(match_no) + ' / ' + str(no_of_games), True, GREY, NAVY)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (620, 50)
    DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)


def draw_score(score: List[int]) -> None:
    """
    Method that draws the score for multiple-match games.
    Args:
        score: first players score, second players score

    Returns: None

    """

    font_obj = pygame.font.SysFont('Courier New', 20)
    text_surface_obj = font_obj.render(str(score[0]) + ' : ' + str(score[1]), True, GREY, NAVY)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (620, 80)
    DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)


def draw_count_moves(moves_player_one: int, moves_player_two: int, player_one: str, player_two: str) -> None:
    """
    Method that draws number of moves for both AI playes, for speed comparison.
    Args:
        moves_player_one:
        moves_player_two:
        player_one:
        player_two:

    Returns:

    """

    font_obj = pygame.font.SysFont('Courier New', 20)
    text_surface_obj = font_obj.render(player_one, True, GREY, NAVY)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (300, 100)
    DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)

    text_surface_obj = font_obj.render(NO_OF_MOVES + str(moves_player_one), True, GREY, NAVY)
    text_rect_obj.center = (300, 120)
    DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)

    text_surface_obj = font_obj.render(player_two, True, GREY, NAVY)
    text_rect_obj.center = (900, 100)
    DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)

    text_surface_obj = font_obj.render(NO_OF_MOVES + str(moves_player_two), True, GREY, NAVY)
    text_rect_obj.center = (900, 120)
    DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)


def draw_names(player_one: str, player_two: str) -> None:
    """
    Draws player names above their respective boards
    Args:
        player_one: AI
        player_two: AI or Human

    Returns: None

    """

    font_obj = pygame.font.SysFont('Courier New', 28)
    text_surface_obj = font_obj.render(player_one, True, GREY, NAVY)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (300, 100)
    DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)
    text_surface_obj = font_obj.render(player_two, True, GREY, NAVY)
    text_rect_obj.center = (900, 100)
    DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)


def draw_menu_buttons(on_mouse_over: str, button_ai_vs_ai, button_ai_vs_player) -> None:
    """
    Method that Draws Main Menu with two buttons, that change color on hover.
    Player gets to pick game mode.
    Args:
        on_mouse_over:
        button_ai_vs_ai: Mode AI vs AI
        button_ai_vs_player: Mode Human vs AI

    Returns:

    """

    font_obj = pygame.font.SysFont('Courier New', 20)

    if on_mouse_over == 'AIvsPlayer':
        pygame.draw.rect(DISPLAY_SURF, [100, 100, 100], button_ai_vs_ai)
        pygame.draw.rect(DISPLAY_SURF, [200, 200, 200], button_ai_vs_player)
        text_surface_obj = font_obj.render(AI_VS_PLAYER, True, (50, 50, 50), (200, 200, 200))
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (WINDOW_WIDTH / 2 + 200, 300)
        DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)
        text_surface_obj = font_obj.render(AI_VS_AI, True, (50, 50, 50), (100, 100, 100))
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (WINDOW_WIDTH / 2 - 200, 300)
        DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)

    elif on_mouse_over == 'AIvsAI':
        pygame.draw.rect(DISPLAY_SURF, [200, 200, 200], button_ai_vs_ai)
        pygame.draw.rect(DISPLAY_SURF, [100, 100, 100], button_ai_vs_player)
        text_surface_obj = font_obj.render(AI_VS_AI, True, (50, 50, 50), (200, 200, 200))
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (WINDOW_WIDTH / 2 - 200, 300)
        DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)
        text_surface_obj = font_obj.render(AI_VS_PLAYER, True, (50, 50, 50), (100, 100, 100))
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (WINDOW_WIDTH / 2 + 200, 300)
        DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)

    elif on_mouse_over == 'Neither':
        pygame.draw.rect(DISPLAY_SURF, [100, 100, 100], button_ai_vs_ai)
        pygame.draw.rect(DISPLAY_SURF, [100, 100, 100], button_ai_vs_player)
        text_surface_obj = font_obj.render(AI_VS_AI, True, (50, 50, 50), (100, 100, 100))
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (WINDOW_WIDTH / 2 - 200, 300)
        DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)
        text_surface_obj = font_obj.render(AI_VS_PLAYER, True, (50, 50, 50), (100, 100, 100))
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (WINDOW_WIDTH / 2 + 200, 300)
        DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)


def draw_level_buttons(button_easy, button_medium, button_hard) -> None:
    """
    Method that draws Difficulty level Menu.
    Args:
        button_easy: easy opponent (Random)
        button_medium: medium opponent (partial Target/Hunt)
        button_hard: hard opponent (TargetHunt + Parity)

    Returns: None

    """

    font_obj = pygame.font.SysFont('Courier New', 20)
    pygame.draw.rect(DISPLAY_SURF, [200, 200, 200], button_easy)
    pygame.draw.rect(DISPLAY_SURF, [200, 200, 200], button_medium)
    pygame.draw.rect(DISPLAY_SURF, [200, 200, 200], button_hard)
    text_surface_obj = font_obj.render('Easy', True, (50, 50, 50), (200, 200, 200))
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (WINDOW_WIDTH / 2, 225)
    DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)
    text_surface_obj = font_obj.render('Medium', True, (50, 50, 50), (200, 200, 200))
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (WINDOW_WIDTH / 2, 325)
    DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)
    text_surface_obj = font_obj.render('Hard', True, (50, 50, 50), (200, 200, 200))
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (WINDOW_WIDTH / 2, 425)
    DISPLAY_SURF.blit(text_surface_obj, text_rect_obj)
