class TicTacToe:
    """ Clase para manear el tablero, estado y jugador actual """

    def __init__(self):
        self.board: list = [[" "] * 3 for _ in range(3)]
        self.current_player: str = "X"
        self.winner: str = None
    
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

    # Checks status
    def is_empty(self, move: tuple) -> bool:
        """ Verificar que la celda seleccionada este vacía """
        position = move[0]
        row = position // 3
        col = position % 3

        # existe mejor opcion? ternary operator?
        if self.board[row][col] == " ":
            return True
        
        return False
    
    def is_tie(self) -> bool:
        """ Verificar si el juego esta empatado """
        if " " in self.board:
            return False
        
        return True


    # Make Moves

    # Switch Players

    # Bucle principal play game