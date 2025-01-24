import unittest
from game_fn.tictactoe import TicTacToe

class TestStatus(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

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
        self.o_rows = [
            [["O", "O", "O"], [" ", " ", " "], [" ", " ", " "]],
            [[" ", " ", " "], ["O", "O", "O"], [" ", " ", " "]],
            [[" ", " ", " "], [" ", " ", " "], ["O", "O", "O"]],
        ]

    def test_check_winner_rows(self):
        """Verifica filas ganadoras para el jugador X"""
        self.game.current_player = "X"
        for row in self.rows:
            self.game.board = row
            self.assertTrue(
                self.game.check_winner(),
                f"check_winner fallo en el tablero (fila): {row}"
            )

    def test_check_winner_cols(self):
        """Verifica columnas ganadoras para el jugador X"""
        self.game.current_player = "X"
        for col in self.cols:
            self.game.board = col
            self.assertTrue(
                self.game.check_winner(),
                f"check_winner fallo en el tablero (columna): {col}"
            )

    def test_check_winner_diags(self):
        """Verifica diagonales ganadoras para el jugador X"""
        self.game.current_player = "X"
        for diag in self.diags:
            self.game.board = diag
            self.assertTrue(
                self.game.check_winner(),
                f"check_winner fallo en el tablero (diagonal): {diag}"
            )

    def test_check_winners_orows(self):
        """Verifica filas ganadoras para el jugador O"""
        self.game.current_player = "O"
        for o_row in self.o_rows:
            self.game.board = o_row
            self.assertTrue(
                self.game.check_winner(),
                f"check_winner fallo en el tablero (fila jugador O): {o_row}"
            )
