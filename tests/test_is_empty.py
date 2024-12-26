import unittest
from functions.check import is_empty


# Clase de pruebas unitarias
class TestIsEmpty(unittest.TestCase):
    # Variable compartida por todas las pruebas
    board = [
        ["X", "O", " "],
        ["X", " ", "O"],
        ["O", "X", " "]
    ]

    def test_position_is_empty(self):
        move = (2,)  # La posición 2 corresponde a la casilla vacía en la fila 0, columna 2
        self.assertTrue(is_empty(move, self.board))

    def test_position_is_occupied(self):
        move = (1,)  # La posición 1 está ocupada por "O" en la fila 0, columna 1
        self.assertFalse(is_empty(move, self.board))

    def test_position_out_of_range(self):
        move = (9,)  # La posición 9 está fuera del rango de un tablero de 3x3
        with self.assertRaises(IndexError):
            is_empty(move, self.board)

if __name__ == "__main__":
    unittest.main()
