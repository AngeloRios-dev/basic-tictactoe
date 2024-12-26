import random
from .check import is_empty, get_empty

# Make a move
def make_move(move: tuple, board: list) -> None:
    position = int(move[0])
    value = str(move[1])
    row = position // 3
    col = position % 3
    board[row][col] = value


def human(board: list) -> None:
    print("Select a number between 1 & 9:")
    h_move = int(input("Input > ")) -1, "X"
    
    if is_empty(h_move, board):
        make_move(h_move, board)
    else:
        print("That cell is not empty!")
        human(board)

def computer(board: list) -> None:
    empty_cells: list = get_empty(board)
    c_move: int = int(random.choice(empty_cells)) -1, "O"
    make_move(c_move, board)
    print(f"Computer choose: {c_move[0]+1}")