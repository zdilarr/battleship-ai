"""
Contains methods for battleship game match.
Author: Emilija Zdilar 06-05-2018
"""
import time
from pygame.locals import *
from battleship_game import *
from drawings import *


def main_menu() -> Union[bool, None]:
    """
    Method that initializes the game and handles quiting game, Mode and Level choices
    Returns:

    """

    pygame.init()
    pygame.display.set_caption(BATTLESHIP_CAPTION)
    button_ai_vs_ai = pygame.Rect(WINDOW_WIDTH / 2 - 300, 200, 200, 200)
    button_ai_vs_player = pygame.Rect(WINDOW_WIDTH / 2 + 100, 200, 200, 200)

    DISPLAY_SURF.fill(NAVY)
    draw_header()

    while True:
        s = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT - 150))
        pygame.time.delay(20)
        s.set_alpha(8)
        s.fill(NAVY)
        DISPLAY_SURF.blit(s, (0, 150))

        if button_ai_vs_player.collidepoint(pygame.mouse.get_pos()):
            draw_menu_buttons('AIvsPlayer', button_ai_vs_ai, button_ai_vs_player)
        elif button_ai_vs_ai.collidepoint(pygame.mouse.get_pos()):
            draw_menu_buttons('AIvsAI', button_ai_vs_ai, button_ai_vs_player)
        else:
            draw_menu_buttons('Neither', button_ai_vs_ai, button_ai_vs_player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button_ai_vs_ai.collidepoint(mouse_pos):
                    DISPLAY_SURF.fill(NAVY)
                    draw_header()
                    time.sleep(0.5)
                    no_of_games = 5
                    score = [0, 0]
                    for i in range(1, no_of_games + 1):
                        draw_match_no(i, no_of_games)
                        result = game_ai_vs_ai()
                        if result == False:
                            DISPLAY_SURF.fill(NAVY)
                            draw_header()
                            break
                        score[result - 1] += 1
                        draw_score(score)
                        time.sleep(1)

                if button_ai_vs_player.collidepoint(mouse_pos):
                    level = level_choice()
                    DISPLAY_SURF.fill(NAVY)
                    draw_header()
                    if level == False:
                        break
                    result = game_ai_vs_human(level)
                    if result == False:
                        DISPLAY_SURF.fill(NAVY)
                        draw_header()
                        break
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def level_choice() -> Union[bool, str]:
    """
    Method that handles the difficulty level choice.
    Returns: Chosen difficulty level or False in case of quitting the game.

    """
    DISPLAY_SURF.fill(NAVY)
    draw_header()
    button_easy = pygame.Rect(WINDOW_WIDTH / 2 - 100, 200, 200, 50)
    button_medium = pygame.Rect(WINDOW_WIDTH / 2 - 100, 300, 200, 50)
    button_hard = pygame.Rect(WINDOW_WIDTH / 2 - 100, 400, 200, 50)

    draw_level_buttons(button_easy, button_medium, button_hard)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if button_easy.collidepoint(mouse_pos):
                    DISPLAY_SURF.fill(NAVY)
                    draw_header()
                    return EASY_DIFFICULTY

                if button_medium.collidepoint(mouse_pos):
                    DISPLAY_SURF.fill(NAVY)
                    draw_header()
                    return MEDIUM_DIFFICULTY

                if button_hard.collidepoint(mouse_pos):
                    DISPLAY_SURF.fill(NAVY)
                    draw_header()
                    return HARD_DIFFICULTY

        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def game_ai_vs_human(level: str) -> bool:
    """
    Method that handles ai versus human game mode.
    Args:
        level: string that represents difficulty level - Easy, Medium, Hard

    Returns:
    """

    current_battleship_game = BattleshipGame(HARD_AI, HUMAN)
    current_battleship_game.prepare_boards()
    current_move = 0
    move_ = HUMAN_MOVE

    while current_battleship_game.player1_hit_counter < MAX_NO_OF_HITS and \
            current_battleship_game.player2_hit_counter < MAX_NO_OF_HITS:
        draw_board(current_battleship_game.board_player2, 'right')
        draw_board(current_battleship_game.board_player1, 'left')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == MOUSEBUTTONDOWN and move_ == HUMAN_MOVE:
                field = get_field_at_pixel(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 'right')
                if field != (None, None) and current_battleship_game.board_player2[field[0]][field[1]][0] != REVEALED:
                    if current_battleship_game.game_move_player2(field) != True:
                        pygame.display.update()
                        FPS_CLOCK.tick(FPS)
                        move_ = AI_MOVE

        if current_battleship_game.player2_hit_counter == MAX_NO_OF_HITS:
            draw_board(current_battleship_game.board_player1, 'left')
            draw_board(current_battleship_game.board_player2, 'right')
            has_won('Player Two')

        while move_ == AI_MOVE:
            if current_battleship_game.player1_hit_counter == MAX_NO_OF_HITS:
                draw_board(current_battleship_game.board_player1, 'left')
                draw_board(current_battleship_game.board_player2, 'right')
                has_won('Player One')
            if level == HARD_DIFFICULTY:
                if current_battleship_game.hard_ai_strategy(current_move) != True:
                    move_ = HUMAN_MOVE
            elif level == EASY_DIFFICULTY:
                if current_battleship_game.easy_ai_strategy(current_move) != True:
                    move_ = HUMAN_MOVE
            elif level == MEDIUM_DIFFICULTY:
                if current_battleship_game.medium_ai_strategy(current_move) != True:
                    move_ = HUMAN_MOVE

            current_move += 1

        draw_names('Ai', 'Human')
        pygame.display.update()
        FPS_CLOCK.tick(FPS)
    return True


def game_ai_vs_ai() -> Union[bool, int]:
    """
    Match between two AI using different strategies.
    Returns: False in case of quitting the game, and 1 or 2 depending on the winner

    """
    current_battleship_game = BattleshipGame(HARD_AI, RANDOM_AI)
    current_battleship_game.prepare_boards()
    current_move = 0
    current_move2 = 0

    while current_battleship_game.player1_hit_counter < MAX_NO_OF_HITS or \
            current_battleship_game.player2_hit_counter < MAX_NO_OF_HITS:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        current_battleship_game.hard_ai_strategy(current_move)
        draw_board(current_battleship_game.board_player1, 'left')
        current_battleship_game.random_ai_strategy(current_move2)
        draw_board(current_battleship_game.board_player2, 'right')
        if current_battleship_game.player1_hit_counter < MAX_NO_OF_HITS:
            current_move += 1
        if current_battleship_game.player2_hit_counter < MAX_NO_OF_HITS:
            current_move2 += 1
        draw_count_moves(current_move, current_move2, ADVANCED_STRATEGY, NAIVE_STRATEGY)
        pygame.display.update()
        FPS_CLOCK.tick(FPS)
    if current_move <= current_move2:
        current_battleship_game.winner = 0
        return 1
    else:
        current_battleship_game.winner = 1
        return 2


if __name__ == "__main__":
    main_menu()
