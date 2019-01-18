"""
Contains everything relevant to a single game of battleship
Author: Emilija Zdilar 6-5-2018
"""
from typing import Union
from strategies import *


class BattleshipGame (object):
    """
    Battleship game. Class that contains all relevant information about players,
    number of hits, moves order (which can be updated depending on the strategy
    that is used), both boards, and a winner.

    """

    def __init__(self, player1_, player2_):

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

    def prepare_boards(self) -> None:
        """
        Method that sets ships on both players boards, from largest ship to smallest.
        Returns: None

        """
        for ship in ALLSHIPS:
            self.place_a_ship(ship, self.board_player1)
            self.place_a_ship(ship, self.board_player2)

    def place_a_ship(self, ship: Tuple[str, int], board: List[List[List[bool]]]) -> None:
        """
        Method that sets a ship in a random horizontal/vertical position to a random chosen
        legal position. In case the chosen position was not legal, another choice is made.
        Args:
            ship: ship to be set on the board
            board: board that ship is set on (1 or 2)

        Returns: None

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

    def game_move_player1(self, field) -> Union[bool, None]:
        """
        Method that checks if the field had already been hit and if not, it reveals it.
        Hit counter for player one is incremented if the newly revealed field contained
        a part of a ship.
        Args:
            field: field chosen by player

        Returns: True in case of hit, False otherwise (miss or hitting already revealed field)

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

    def game_move_player2(self, field) -> Union[bool, None]:
        """
        Method that checks if the field had already been hit and if not, it reveals it.
        Hit counter for player two is incremented if the newly revealed field contained
        a part of a ship.
        Args:
            field: field chosen by player

        Returns: True in case of hit, False otherwise (miss or hitting already revealed field)

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

    def hard_ai_strategy(self, current_move) -> Union[bool, None]:
        """
        Target/Hunt strategy. Moves passed to this function are shuffled legal moves sorted by parity key. They
        are played until there is first hit (Target). After hitting the ship, we look at neighbours od that field
        - left, right, up, down. They get the highest priority and move to the front of the list of remaining
        moves. Since we have 5 ships that take 17 fields, the game is over once the hit counter hits 17, unless
        the opponent has already won.
        Args:
            current_move:

        Returns:

        """

        hit_successful = self.game_move_player1(self.player1_moves_order[current_move])
        if self.player1_hit_counter < 17:
            if hit_successful:
                neighbour_down = (self.player1_moves_order[current_move][0],
                                  self.player1_moves_order[current_move][1] + 1)
                neighbour_up = (self.player1_moves_order[current_move][0],
                                self.player1_moves_order[current_move][1] - 1)
                neighbour_left = (self.player1_moves_order[current_move][0] - 1,
                                  self.player1_moves_order[current_move][1])
                neighbour_right = (self.player1_moves_order[current_move][0] + 1,
                                   self.player1_moves_order[current_move][1])
                neighbourhood = [neighbour_right, neighbour_left, neighbour_down, neighbour_up]
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
        if hit_successful:
            return True

    def random_ai_strategy(self, current_move) -> Union[bool, None]:
        """
        Random moves
        Args:
            current_move:

        Returns: True in case of hit, None otherwise

        """
        hit_successful = self.game_move_player2(self.player2_moves_order[current_move])

        if current_move < len(self.player2_moves_order) - 1:
            current_move += 1
        if hit_successful:
            return True

    def easy_ai_strategy(self, current_move) -> Union[bool, None]:
        """
        Level 1, easiest strategy. AI plays legal moves without a pattern or a plan. (It is
        arguable to call it a strategy).
        Args:
            current_move:

        Returns: True in case of successful hit, None otherwise

        """

        hit_successful = self.game_move_player1(self.player1_moves_order[current_move])
        if current_move < len(self.player1_moves_order) - 1:
            current_move += 1
        if hit_successful:
            return True

    def medium_ai_strategy(self, current_move) -> Union[bool, None]:
        """
        Middle ground between Easy and Hard level. Partial Terget/Hunt strategy. Moves passed to this method
        are shuffled legal moves, not sorted by parity. AI hits random fields until it hits something (Taget).
        After that, it looks at two neighbours - upper and lower, which were not visited (Hunt). Then that two
        fields get the biggest priority, and take the front places in the list of upcoming moves. Since we have
        5 ships that take 17 fields, the game is over once the hit counter hits 17, unless the opponent has
        already won.
        Args:
            current_move:

        Returns: True in case of successful hit, None otherwise

        """

        hit_successful = self.game_move_player1(self.player1_moves_order[current_move])
        if self.player1_hit_counter < 17:
            if hit_successful:
                neighbour_down = (
                    self.player1_moves_order[current_move][0], self.player1_moves_order[current_move][1] + 1)
                neighbour_up = (
                    self.player1_moves_order[current_move][0], self.player1_moves_order[current_move][1] - 1)

                neighbourhood = [neighbour_down, neighbour_up]
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
        if hit_successful:
            return True
