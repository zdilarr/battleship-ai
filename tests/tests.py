import os
import sys
import unittest
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from battleship_game import *


class TestBattleshipGame (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.game_one = battleship_game(HARDAI,HUMAN)
        self.game_two = battleship_game(HARDAI,RANDOMAI)
        self.game_one.prepare_boards()
        self.game_two.prepare_boards()

    def tearDown(self):
        pass

    def test_board(self):
        self.assertEqual((len(self.game_one.board_player1), len(self.game_one.board_player1[0])), (10, 10) )
        self.assertEqual((len(self.game_one.board_player2), len(self.game_one.board_player2[0])), (10, 10) )

    def test_move(self):
        self.assertIn(self.game_one.game_move_player1((9, 9)), (False, True), "Nesto nije ok s poljima")

    def test_strategy(self):
        sum1, sum2 = 0, 0
        all_moves = [(x, y) for x in list(range(0, BOARDHEIGHT)) for y in list(range(0, BOARDWIDTH))]
        for move in all_moves:
            sum1 += self.game_one.game_move_player1(move)
            sum2 += self.game_two.game_move_player2(move)
        self.assertEqual((sum1, sum2), (17, 17))


if __name__ == '__main__':
    unittest.main()


