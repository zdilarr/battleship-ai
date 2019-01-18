from constants import *

def get_field_at_pixel(x, y, left_right_board):
    """
    :param x: koordinata
    :param y: koordinata
    :param left_right_board: lijeva/desna ploca
    konvertuje koorinatu piksela u koordinatu polja kojem pripada, ako
    takvo polje postoji
    :return:
    """
    for fieldx in range(BOARDWIDTH):
        for fieldy in range(BOARDHEIGHT):
            left, top = left_top_field_coordinate(fieldx, fieldy, left_right_board)
            box_rect = pygame.Rect(left, top, FIELDSIZE, FIELDSIZE)
            if box_rect.collidepoint(x, y):
                return (fieldx, fieldy)
    return None, None


def left_top_field_coordinate(fieldx, fieldy,left_right_board):
    """
    pomocna funkcija za iscrtavanje ploce. Nalazi gornji lijevi cosak polja
    :param fieldx:
    :param fieldy:
    :param left_right_board:
    :return:
    """
    if left_right_board == 'left':
        left = fieldx * (FIELDSIZE + SPACESIZE) + 50
        top = fieldy * (FIELDSIZE + SPACESIZE) + YMARGIN + 80
        return left, top
    if left_right_board == 'right':
        left = WINDOWWIDTH - fieldx * (FIELDSIZE + SPACESIZE) - 100
        top = fieldy * (FIELDSIZE + SPACESIZE) + YMARGIN + 80
        return left, top


def draw_board(board, left_right):
    """
    iscrtava lijevu ili desnu plocu za datu konfiguraciju.
    :param board: Trodimenzionalni niz polja (matrica cije svako polje sadrzi niz informacija)
    :param left_right: lijeva ili desna ploca
    :return:
    """
    for fieldx in range(BOARDWIDTH):
        for fieldy in range(BOARDHEIGHT):
            left, top = left_top_field_coordinate(fieldx, fieldy, left_right)
            if board[fieldx][fieldy][0] is not REVEALED:
                pygame.draw.rect(DISPLAYSURF, UNREVEALEDFIELDCOLOR, (left, top, FIELDSIZE, FIELDSIZE))
            elif board[fieldx][fieldy][0] is REVEALED and board[fieldx][fieldy][1] is not HASSHIP:
                pygame.draw.rect(DISPLAYSURF, EMPTYFIELDCOLOR, (left, top, FIELDSIZE, FIELDSIZE))
            elif board[fieldx][fieldy][0] is REVEALED and board[fieldx][fieldy][1] is HASSHIP:
                pygame.draw.rect(DISPLAYSURF, SHIPFIELDCOLOR, (left, top, FIELDSIZE, FIELDSIZE))


def draw_header():
    """
    Crta logo i Naziv Battlesip
    :return:
    """
    font_obj = pygame.font.SysFont('Courier New', 32)
    text_surface_obj = font_obj.render('BattleShip', True, GREY, NAVY)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (100, 30)
    DISPLAYSURF.blit(text_surface_obj, text_rect_obj)
    ship_img =\
        pygame.image.load('.\img\ship.png')
    shipx = 130
    shipy = 10
    DISPLAYSURF.blit(ship_img, (shipx, shipy))


def has_won(player_one_or_two):
    """
    Ispisuje ko je pobjedio
    :param player_one_or_two:
    :return:
    """
    font_obj = pygame.font.SysFont('Courier New', 20)
    text_surface_obj = font_obj.render('Pobjeda!', True, GREY, NAVY)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (300, 140) if player_one_or_two == 'Player One' else (900,140)
    DISPLAYSURF.blit(text_surface_obj, text_rect_obj)


def draw_match_no(match_no, no_of_games):
    """
    Ispisuje redni broj partije za mečeve od više partija
    :param match_no: trenutna igra
    :param no_of_games: ukupan broj igara
    :return:
    """
    font_obj = pygame.font.SysFont('Courier New', 20)
    text_surface_obj = font_obj.render(str(match_no) + ' / ' + str(no_of_games) , True, GREY, NAVY)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (580, 50)
    DISPLAYSURF.blit(text_surface_obj, text_rect_obj)


def draw_score(score):
    """
    Ipisuje rezultat za meć od više partija
    :param score: oblika (broj_bodova_1, broj_bodova2)
    :return:
    """
    font_obj = pygame.font.SysFont('Courier New', 20)
    text_surface_obj = font_obj.render(str(score[0]) + ' : ' + str(score[1]), True, GREY, NAVY)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (580, 80)
    DISPLAYSURF.blit(text_surface_obj, text_rect_obj)


def draw_count_moves(moves_player_one, moves_player_two, player_one, player_two):
    """
    Ispisuje broj poteza, za svakog od AI, kako bi se uporedila brzina
    :param moves_player_one: broj poteza prvog igraca
    :param moves_player_two: broj poteza drugog igraca
    :param player_one: Ime igraca ili Strategije
    :param player_two: Ime igraca ili Strategije
    :return:
    """
    font_obj = pygame.font.SysFont('Courier New', 20)
    text_surface_obj = font_obj.render(player_one, True, GREY, NAVY)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (300, 100)
    DISPLAYSURF.blit(text_surface_obj, text_rect_obj)

    text_surface_obj = font_obj.render('Broj poteza:' + str(moves_player_one), True, GREY, NAVY)
    text_rect_obj.center = (300, 120)
    DISPLAYSURF.blit(text_surface_obj, text_rect_obj)

    text_surface_obj = font_obj.render(player_two, True, GREY, NAVY)
    text_rect_obj.center = (900, 100)
    DISPLAYSURF.blit(text_surface_obj, text_rect_obj)

    text_surface_obj = font_obj.render('Broj poteza:' + str(moves_player_two), True, GREY, NAVY)
    text_rect_obj.center = (900, 120)
    DISPLAYSURF.blit(text_surface_obj, text_rect_obj)


def draw_names(player_one, player_two):
    """
    Ispisuje imena igrača iznad respektivnih ploča
    :param player_one:
    :param player_two:
    :return:
    """
    font_obj = pygame.font.SysFont('Courier New', 28)
    text_surface_obj = font_obj.render(player_one, True, GREY, NAVY)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (300, 100)
    DISPLAYSURF.blit(text_surface_obj, text_rect_obj)
    text_surface_obj = font_obj.render(player_two, True, GREY, NAVY)
    text_rect_obj.center = (900, 100)
    DISPLAYSURF.blit(text_surface_obj, text_rect_obj)


def draw_menu_buttons(on_mouse_over, button_ai_vs_ai, button_ai_vs_player):
    """
    Crta glavni izbornik s dva dugmeta koja mjenjaju boju on hover
    :param on_mouse_over: kad pređe mišem preko dugmeta
    :param button_ai_vs_ai: Mode AI protiv AI
    :param button_ai_vs_player: Mode Human protiv AI
    :return:
    """
    font_obj = pygame.font.SysFont('Courier New', 20)

    if on_mouse_over == 'AIvsPlayer':
        pygame.draw.rect(DISPLAYSURF, [100, 100, 100], button_ai_vs_ai)
        pygame.draw.rect(DISPLAYSURF, [200, 200, 200], button_ai_vs_player)
        text_surface_obj = font_obj.render('AI vs Player', True, (50, 50, 50), (200, 200, 200))
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (WINDOWWIDTH / 2 + 200, 300)
        DISPLAYSURF.blit(text_surface_obj, text_rect_obj)
        text_surface_obj = font_obj.render('AI vs AI', True, (50, 50, 50), (100, 100, 100))
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (WINDOWWIDTH / 2 - 200, 300)
        DISPLAYSURF.blit(text_surface_obj, text_rect_obj)

    elif on_mouse_over == 'AIvsAI':
        pygame.draw.rect(DISPLAYSURF, [200, 200, 200], button_ai_vs_ai)
        pygame.draw.rect(DISPLAYSURF, [100, 100, 100], button_ai_vs_player)
        text_surface_obj = font_obj.render('AI vs AI', True, (50, 50, 50), (200, 200, 200))
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (WINDOWWIDTH / 2 - 200, 300)
        DISPLAYSURF.blit(text_surface_obj, text_rect_obj)
        text_surface_obj = font_obj.render('AI vs Player', True, (50, 50, 50), (100, 100, 100))
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (WINDOWWIDTH / 2 + 200, 300)
        DISPLAYSURF.blit(text_surface_obj, text_rect_obj)

    elif on_mouse_over == 'Neither':
        pygame.draw.rect(DISPLAYSURF, [100, 100, 100], button_ai_vs_ai)
        pygame.draw.rect(DISPLAYSURF, [100, 100, 100], button_ai_vs_player)
        text_surface_obj = font_obj.render('AI vs AI', True, (50, 50, 50), (100, 100, 100))
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (WINDOWWIDTH / 2 - 200, 300)
        DISPLAYSURF.blit(text_surface_obj, text_rect_obj)
        text_surface_obj = font_obj.render('AI vs Player', True, (50, 50, 50), (100, 100, 100))
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (WINDOWWIDTH / 2 + 200, 300)
        DISPLAYSURF.blit(text_surface_obj, text_rect_obj)


def draw_level_buttons(button_easy, button_medium, button_hard):
    """
    Crta Izbornik razina
    :param button_easy: Easy Razina
    :param button_medium: Medium Razina
    :param button_hard: Hard Razina
    :return:
    """
    font_obj = pygame.font.SysFont('Courier New', 20)
    pygame.draw.rect(DISPLAYSURF, [200, 200, 200], button_easy)
    pygame.draw.rect(DISPLAYSURF, [200, 200, 200], button_medium)
    pygame.draw.rect(DISPLAYSURF, [200, 200, 200], button_hard)
    text_surface_obj = font_obj.render('Easy', True, (50, 50, 50), (200, 200, 200))
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (WINDOWWIDTH / 2, 225)
    DISPLAYSURF.blit(text_surface_obj, text_rect_obj)
    text_surface_obj = font_obj.render('Medium', True, (50, 50, 50), (200, 200, 200))
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (WINDOWWIDTH / 2, 325)
    DISPLAYSURF.blit(text_surface_obj, text_rect_obj)
    text_surface_obj = font_obj.render('Hard', True, (50, 50, 50), (200, 200, 200))
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (WINDOWWIDTH / 2, 425)
    DISPLAYSURF.blit(text_surface_obj, text_rect_obj)



