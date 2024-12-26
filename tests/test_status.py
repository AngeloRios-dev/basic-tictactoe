import unittest
from functions.check import status

class TestStatus(unittest.TestCase):
    def setUp(self):
        self.rows = [
            [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]],
            [[" ", " ", " "], ["X", "X", "X"], [" ", " ", " "]],
            [[" ", " ", " "], [" ", " ", " "], ["X", "X", "X"]]
        ]
        self.cols = [
            [["X", " ", " "], ["X", " ", " "], ["X", " ", " "]],
            [[" ", "X", " "], [" ", "X", " "], [" ", "X", " "]],
            [[" ", " ", "X"], [" ", " ", "X"], [" ", " ", "X"]]
        ]
        self.diags = [
            [[" ", " ", "X"], [" ", "X", " "], ["X", " ", " "]],
            [["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]]
        ]

    def test_rows(self):
        for row in self.rows:
            self.assertTrue(status(row, "X"))

    def test_cols(self):
        for col in self.cols:
            self.assertTrue(status(col, "X"))

    def test_diags(self):
        for diag in self.diags:
            self.assertTrue(status(diag, "X"))

    def test_no_win(self):
        no_win_boards = [
            [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]],
            [[" ", "O", "X"], ["X", "O", " "], ["O", " ", "X"]],
            [["X", "O", " "], [" ", "X", "O"], ["O", "X", " "]],
        ]
        for board in no_win_boards:
            self.assertFalse(status(board, "X"))

    def test_player_o(self):
        win_boards = [
            [["O", "O", "O"], [" ", " ", " "], [" ", " ", " "]],
            [[" ", " ", " "], ["O", "O", "O"], [" ", " ", " "]],
            [["O", " ", " "], ["O", " ", " "], ["O", " ", " "]],
        ]
        for board in win_boards:
            self.assertTrue(status(board, "O"))

if __name__ == "__main__":
    unittest.main()
