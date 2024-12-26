import unittest
from functions.check import is_tie


class testIsTie(unittest.TestCase):
    def setUp(self):
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
        self.assertFalse(is_tie(self.tie_false))

    def test_is_tie_true(self):
        self.assertTrue(is_tie(self.tie_true))

    def test_empty_board(self):
        self.assertFalse(is_tie(self.empty_board))

