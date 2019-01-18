from constants import *
from strategies import *
import random

class battleship_game (object):

    def __init__(self, player1_, player2_):
        """
        BattleShip Partija. Klasa cuva bitne informacije za igrace, broj pogodaka,
        redoslijed poteza (koji se moze mjenjati sukladno strategiji), pobjednika
        i obje ploce
        :param player1_: prvi igrac
        :param player2_: drugi igrax
        """
        self.board_player1 = [[[not REVEALED, not HASSHIP] for _ in range(BOARDHEIGHT)] for _ in range(BOARDWIDTH)]
        self.board_player2 = [[[not REVEALED, not HASSHIP] for _ in range(BOARDHEIGHT)] for _ in range(BOARDWIDTH)]
        self.player1 = player1_
        self.player2 = player2_
        self.player1_hit_counter = 0
        self.player2_hit_counter = 0
        self.player1_move_counter = 0
        self.player2_move_counter = 0
        self.player1_moves_order = []
        self.player2_moves_order = []
        self.winner = -1
        self.player1_moves_order = smart_ai_moves_order() if self.player1 == HARDAI else not_so_smart_ai_moves_order()
        self.player2_moves_order = smart_ai_moves_order() if self.player2 == HARDAI else not_so_smart_ai_moves_order()

    def __str__(self):
        return str(self.board_player1)

    def prepare_boards(self):
        """
        postavlja brodove na ploce oba igraca, od najveceg prema najmanjem
        :return:
        """
        for ship in ALLSHIPS:
            self.place_a_ship(ship, self.board_player1)
            self.place_a_ship(ship, self.board_player2)

    def place_a_ship(self, ship, board):
        """
        postavlja brod slucajno okrenut vodoravno ili okomito
        na slucajno odabranu legalnu poziciju.
        (ako pozicija nije legalna, izabere se neka druga)
        :param ship: brod koji se postavlja
        :param board: ploca na koju se postavlja (player 1 ili 2)
        :return:
        """
        ship_orientation = ['Horizontal', 'Vertical']
        orientation = random.choice(ship_orientation)

        if orientation == 'Horizontal':
            chosen_position = (random.randrange(0, BOARDHEIGHT - 1), random.randrange(0, BOARDWIDTH - ship[1] - 1))
            for i in range(0, ship[1]):
                if board[chosen_position[0]][chosen_position[1] + i][1] == HASSHIP:
                    self.place_a_ship(ship, board)
                    return
            for i in range(0, ship[1]):
                board[chosen_position[0]][chosen_position[1] + i] = [not REVEALED, HASSHIP]

        if orientation == 'Vertical':
            chosen_position = (random.randrange(0, BOARDHEIGHT - ship[1] - 1), random.randrange(0, BOARDWIDTH - 1))
            for i in range(0, ship[1]):
                if board[chosen_position[0] + i][chosen_position[1]][1] == HASSHIP:
                    self.place_a_ship(ship, board)
                    return
            for i in range(0, ship[1]):
                board[chosen_position[0] + i][chosen_position[1]] = [not REVEALED, HASSHIP]

    def game_move_player1(self, field):
        """
        provjerava je li polje vec otkriveno, i ako nije otkrije ga.
        Poveca brojac pogodaka prvom igracu ako je na novootkrivenom polju brod
        :param field: odabrano polje
        :return:
        """

        if field == (None, None):
            return False

        x = field[0]
        y = field[1]

        if self.board_player1[x][y][0] != REVEALED:
            self.board_player1[x][y][0] = REVEALED
            if self.board_player1[x][y][1] is HASSHIP:
                self.player1_hit_counter += 1
                return True
            return False

    def game_move_player2(self, field):
        """
        provjerava je li polje vec otkriveno, i ako nije otkrije ga.
        Poveca brojac pogodaka drugom igracu ako je na novootkrivenom polju brod
        :param field: odabrano polje
        :return:
        """
        if field == (None, None):
            return False

        x = field[0]
        y = field[1]

        if self.board_player2[x][y][0] != REVEALED:
            self.board_player2[x][y][0] = REVEALED

            if self.board_player2[x][y][1] is HASSHIP:
                self.player2_hit_counter += 1
                return True
            return False

    def hard_ai_strategy(self, current_move):
        """
        Target/Hunt strategija. Potezi koji se proslijeđuju ovoj funkciji su nasumično izmješani legalni potezi,
        sortirani po paritetu. Oni se redom igraju sve dok nema pogotka (Target). Nakon pogotka, posmatraju se
        susjedi tog polja - lijevo, desno, gore, dole, koji već nisu posjećeni (Hunt). Oni dobivaju najveći prioritet,
        i prelaze na pocetak liste preostalih poteza. Budući da imamo 5 brodova, koji zauzimaju 17 polja, igra je
        gotova kad broj pogodaka dostigne 17, ako protivnik prije toga ne pobjedi.
        :param current_move: trenutni potez
        :return:
        """
        hit_sucessful = self.game_move_player1(self.player1_moves_order[current_move])
        if self.player1_hit_counter < 17:
            if hit_sucessful:
                neighbourdown = (self.player1_moves_order[current_move][0], self.player1_moves_order[current_move][1] + 1)
                neighbourup = (self.player1_moves_order[current_move][0], self.player1_moves_order[current_move][1] - 1)
                neighbourleft = (self.player1_moves_order[current_move][0] - 1, self.player1_moves_order[current_move][1])
                neighbourright = (self.player1_moves_order[current_move][0] + 1, self.player1_moves_order[current_move][1])
                neighbourhood = [neighbourright, neighbourleft, neighbourdown, neighbourup]
                next_available = 1

                for neighbour in neighbourhood:
                    if neighbour in self.player1_moves_order:
                        if current_move + next_available < self.player1_moves_order.index(neighbour):
                            temp = self.player1_moves_order[self.player1_moves_order.index(neighbour)]
                            del self.player1_moves_order[self.player1_moves_order.index(neighbour)]
                            self.player1_moves_order.insert(current_move + next_available, temp)
                            next_available += 1

        if current_move < len(self.player1_moves_order) - 1:
            current_move += 1
        if hit_sucessful:
            return True

    def random_ai_strategy(self, current_move):

        """
        Nasumicni potezi
        :param current_move: treunutni potez
        :return:
        """
        hit_sucessful = self.game_move_player2(self.player2_moves_order[current_move])

        if current_move < len(self.player2_moves_order) - 1:
            current_move += 1
        if hit_sucessful:
            return True

    def easy_ai_strategy (self, current_move):

        """
        Najlaksi nivo. Igra poteze koji su legalni, ali bez nekog uzorka ili plana
        :param current_move: treunutni potez
        :return:
        """
        hit_sucessful = self.game_move_player1(self.player1_moves_order[current_move])
        if current_move < len(self.player1_moves_order) - 1:
            current_move += 1
        if hit_sucessful:
            return True

    def medium_ai_strategy(self, current_move):

        """
        Razina između Easy i Hard. Potezi koji se proslijeđuju ovoj funkciji su nasumično izmješani legalni potezi,
        ali nisu sortirani po paritetu. Oni se redom igraju sve dok nema pogotka (Target). Nakon pogotka, posmatraju
        se dva susjeda tog polja - gore, dole , koji već nisu posjećeni (Hunt). Oni dobivaju najveći prioritet,
        i prelaze na pocetak liste preostalih poteza. Budući da imamo 5 brodova, koji zauzimaju 17 polja, igra je
        gotova kad broj pogodaka dostigne 17, ako protivnik prije toga ne pobjedi.
        :param current_move: trenutni potez
        :return:
        """

        hit_sucessful = self.game_move_player1(self.player1_moves_order[current_move])
        if self.player1_hit_counter < 17:
            if hit_sucessful:
                neighbourdown = (
                    self.player1_moves_order[current_move][0], self.player1_moves_order[current_move][1] + 1)
                neighbourup = (
                    self.player1_moves_order[current_move][0], self.player1_moves_order[current_move][1] - 1)

                neighbourhood = [neighbourdown, neighbourup]
                next_available = 1

                for neighbour in neighbourhood:
                    if neighbour in self.player1_moves_order:
                        if current_move + next_available < self.player1_moves_order.index(neighbour):
                            temp = self.player1_moves_order[self.player1_moves_order.index(neighbour)]
                            del self.player1_moves_order[self.player1_moves_order.index(neighbour)]
                            self.player1_moves_order.insert(current_move + next_available, temp)
                            next_available += 1

        if current_move < len(self.player1_moves_order) - 1:
            current_move += 1
        if hit_sucessful:
            return True

