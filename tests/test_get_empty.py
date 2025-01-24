import unittest
from game_fn.tictactoe import TicTacToe

class testGetEmpty(unittest.TestCase):
    def setUp(self):
        """ Prueba de la funcion """
        # Crear instancia del juego para llamar funcion
        # get_empty_spots()

        self.game = TicTacToe()

        # Definicion del tablero de pruebas
        self.game.board = [
            ["X", "O", " "],
            ["X", " ", "O"],
            ["O", "X", " "]
        ]
        self.expected_empty = [2, 4, 8]

    def test_get_empty_spots(self):
        """Ejecutar caso de prueba"""
        results = self.game.get_empty_spots()
        self.assertEqual(results, self.expected_empty)

