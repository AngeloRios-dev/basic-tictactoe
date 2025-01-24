import unittest
from game_fn.tictactoe import TicTacToe


class testIsTie(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

        self.tie_false = [
            ["X", "O", " "],
            ["X", " ", "O"],
            ["O", "X", " "]
        ]

        self.tie_true = [
            ["X", "O", "X"],
            ["X", "X", "O"],
            ["O", "X", "O"]
        ]

        self.empty_board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def test_is_tie_false(self):
        """Verifica que no hay empate"""
        self.game.board = self.tie_false
        self.assertFalse(self.game.is_tie())

    def test_is_tie_true(self):
        """Verifica que hay empate"""
        self.game.board = self.tie_true
        self.assertTrue(self.game.is_tie())

    def test_empty_board(self):
        """Verifica que no hay empate (tablero vacio)"""
        self.game.board = self.empty_board
        self.assertFalse(self.game.is_tie())

