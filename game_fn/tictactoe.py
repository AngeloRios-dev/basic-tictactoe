import random

class TicTacToe:
    """ Clase para manear el tablero, estado y jugador actual """

    def __init__(self):
        self.board: list = [[" "] * 3 for _ in range(3)]
        self.current_player: str = "X"
        self.winner: str = None

    
    def get_empty_spots(self):
        """
        Retorna las celdas disponibles para ser utilizada
        por la funcion computer() que usa random para
        seleccionar una celda libre
        
        Para comprender como funciona:
        Es una 'List Comprehension' lo que hace es basicamente
        verificar si la celda seleccionada esta vacia, y al estarlo
        usamos la formula 'ROW X 3 + COL' 
        Por ejemplo:
        Celda en FILA [0] COLUMNA [0] -> FILA[0] x 3 + COLUMNA[0] = 0
        Celda en FILA [0] COLUMNA [1] -> FILA[0] x 3 + COLUMNA[1] = 1
        Celda en FILA [0] COLUMNA [2] -> FILA[0] x 3 + COLUMNA[2] = 2

        """
        return [
            row * 3 + col
            for row in range(3)
            for col in range(3)
            if self.board[row][col] == " "
        ]
    
    
    # Show board
    def show_board(self) -> None:
        """ Mostrar el tablero del juego al usuario"""

        print()
        for item in self.board:
            print("\t+---+---+---+")
            for idx, each in enumerate(item):
                if idx == 0:
                    print("\t|", each, end=" | ")
                else:
                    print(each, end=" | ")
            print()
        print("\t+---+---+---+")
        print()
    
    # Checks
    def check_winner(self) -> bool:
        options = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]
        for option in options:
            if all(self.board[row][col] == self.current_player for row, col in option):
                self.winner = self.current_player
                return True
        return False
    
    def is_tie(self) -> bool:
        """ Verificar si el juego esta empatado """
        for row in self.board:
            if " " in row:
                return False
        print("EMPATE!")
        return True
    
    def valid_entry(self, number: int) -> bool:
        """
        Verificar que la entrada del usuario sea correcta.
        Debe ser un numero mayor o igual a 1
        Debe ser un numero menor o igual a 9
        """
        return 0 <= number <= 8

    # Make Moves
    def make_move(self, spot: int, player: str) -> None:
        """
        Verifica si la posicion que le se pasa por tupla 
        se encuentra disponible en el tablero
        """
        row = spot // 3
        col = spot % 3
        if self.board[row][col] == " ":
            self.board[row][col] = player
        else:
            print("CELDA NO DISPONIBLE!")
            self.human()

    def human(self) -> None:
        """
        Pide al usuario seleccionar un numero,
        si el numero se encuentra disponible,
        realiza en movimiento en el tablero
        """
        print("Selecciona un numero entre 1 y 9: ")
        while True:
            try:
                human_move: int = int(input("Numero > ")) -1
                if self.valid_entry(human_move):
                    self.make_move(human_move, "X")
                    break
                else:
                    print("Fuera de rango!")
            except ValueError:
                print("Valores validos del 1 al 9")

    def computer(self) -> None:
        """
        Generar movimiento automatico utilizando random
        """
        computer_move = random.choice(self.get_empty_spots())
        self.make_move(computer_move, "O")
        print("Eleccion de computadora:", computer_move + 1)


    # Switch Players
    def switch_player(self) -> None:
        """ Simplemente cambia el jugador actual"""
        self.current_player = "O" if self.current_player == "X" else "X"

        
    # Bucle principal play game
    def play_game(self) -> None:
        while True:
            self.show_board()
            if self.current_player == "X":
                self.human()
                if self.is_tie():
                    self.show_board()
                    break

            else:
                self.computer()
                if self.is_tie():
                    self.show_board()
                    break

            if self.check_winner():
                self.show_board()
                print(f"El ganador es {self.winner}")
                break
            
            self.switch_player()

            