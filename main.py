from pygame.locals import *
from constants import *
from drawings import *
import time
from battleship_game import *


def main_menu():
    """
    Glavni izbornik
    :return:
    """
    pygame.init()
    pygame.display.set_caption('BattleShip')
    button_ai_vs_ai = pygame.Rect(WINDOWWIDTH/2 - 300, 200, 200, 200)
    button_ai_vs_player = pygame.Rect(WINDOWWIDTH/2 + 100, 200, 200, 200)

    DISPLAYSURF.fill(NAVY)
    draw_header()

    while True:
        s = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT-150))
        pygame.time.delay(20)
        s.set_alpha(8)
        s.fill(NAVY)
        DISPLAYSURF.blit(s, (0, 150))

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
                    DISPLAYSURF.fill(NAVY)
                    draw_header()
                    time.sleep(0.5)
                    no_of_games = 5
                    score = [0, 0]
                    for i in range(1, no_of_games+1):
                        draw_match_no(i, no_of_games)
                        result = game_ai_vs_ai()
                        if result == False:
                            DISPLAYSURF.fill(NAVY)
                            draw_header()
                            break
                        score[result - 1] += 1
                        draw_score(score)
                        time.sleep(1)

                if button_ai_vs_player.collidepoint(mouse_pos):
                    level = level_choice()
                    DISPLAYSURF.fill(NAVY)
                    draw_header()
                    if level == False:
                        break
                    result = game_ai_vs_human(level)
                    if result == False:
                        DISPLAYSURF.fill(NAVY)
                        draw_header()
                        break
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def level_choice():
    """
    Izbor razine Easy / Medium / Hard
    :return: Tag izabrane razine
    """
    DISPLAYSURF.fill(NAVY)
    draw_header()
    button_easy = pygame.Rect(WINDOWWIDTH/2-100, 200, 200, 50)
    button_medium = pygame.Rect(WINDOWWIDTH/2-100, 300, 200, 50)
    button_hard = pygame.Rect(WINDOWWIDTH/2-100, 400, 200, 50)

    draw_level_buttons(button_easy, button_medium, button_hard)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if button_easy.collidepoint(mouse_pos):
                    DISPLAYSURF.fill(NAVY)
                    draw_header()
                    return 'Easy'

                if button_medium.collidepoint(mouse_pos):
                    DISPLAYSURF.fill(NAVY)
                    draw_header()
                    return 'Medium'

                if button_hard.collidepoint(mouse_pos):
                    DISPLAYSURF.fill(NAVY)
                    draw_header()
                    return 'Hard'

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def game_ai_vs_human(level):
    """
    AI protiv Igraca
    :param level: Razina o kojoj ovisi strategija AI
    :return:
    """

    current_battleship_game = BattleshipGame(HARDAI, HUMAN)
    current_battleship_game.prepare_boards()
    current_move = 0
    potez = 'human'

    while current_battleship_game.player1_hit_counter < 17 and current_battleship_game.player2_hit_counter < 17:
        draw_board(current_battleship_game.board_player2, 'right')
        draw_board(current_battleship_game.board_player1, 'left')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == MOUSEBUTTONDOWN and potez == 'human':
                field = get_field_at_pixel(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 'right')
                if field != (None, None) and current_battleship_game.board_player2[field[0]][field[1]][0] != REVEALED:
                    if current_battleship_game.game_move_player2(field) != True:
                        pygame.display.update()
                        FPSCLOCK.tick(FPS)
                        potez = 'ai'

        if current_battleship_game.player2_hit_counter == 17:
            draw_board(current_battleship_game.board_player1, 'left')
            draw_board(current_battleship_game.board_player2, 'right')
            has_won('Player Two')

        while potez == 'ai':
            if current_battleship_game.player1_hit_counter == 17:
                draw_board(current_battleship_game.board_player1, 'left')
                draw_board(current_battleship_game.board_player2, 'right')
                has_won('Player One')
            if level == 'Hard':
                if current_battleship_game.hard_ai_strategy(current_move) != True:
                    potez = 'human'
            elif level == 'Easy':
                if current_battleship_game.easy_ai_strategy(current_move) != True:
                    potez = 'human'
            elif level == 'Medium':
                if current_battleship_game.medium_ai_strategy(current_move) != True:
                    potez = 'human'

            current_move += 1

        draw_names('Ai', 'Human')
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    return True


def game_ai_vs_ai():
    """
    Meč između 2 AI-a s različitim strategijama
    :return:
    """
    current_battleship_game = BattleshipGame(HARDAI, RANDOMAI)
    current_battleship_game.prepare_boards()
    current_move = 0
    current_move2 = 0

    while current_battleship_game.player1_hit_counter < 17 or current_battleship_game.player2_hit_counter < 17:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        current_battleship_game.hard_ai_strategy(current_move)
        draw_board(current_battleship_game.board_player1, 'left')
        current_battleship_game.random_ai_strategy(current_move2)
        draw_board(current_battleship_game.board_player2, 'right')
        if current_battleship_game.player1_hit_counter < 17:
            current_move += 1
        if current_battleship_game.player2_hit_counter < 17:
            current_move2 += 1
        draw_count_moves(current_move, current_move2, 'Target/Hunt+Parity Strategija', 'Nasumicni potezi')
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    if current_move <= current_move2:
        current_battleship_game.winner = 0
        return 1
    else:
        current_battleship_game.winner = 1
        return 2


if __name__ == "__main__":
    main_menu()