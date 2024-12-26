import unittest
from functions.check import get_empty

class testGetEmpty(unittest.TestCase):
    def setUp(self):
        self.board = [
            ["X", "O", " "],
            ["X", " ", "O"],
            ["O", "X", " "]
        ]
        self.expected_empty = [3, 5, 9]

    def test_get_empty_cells(self):
        results = get_empty(self.board)
        self.assertEqual(results, self.expected_empty)

