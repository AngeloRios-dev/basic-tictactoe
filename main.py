import random

# Create a new board
def create_board():
    board = [([" "] * 3) for _ in range(3)]
    return board

# Print board
def show_board(board: list) -> None:
    print()
    for item in board:
        print("\t+---+---+---+")
        for idx, each in enumerate(item):
            if idx == 0:
                print("\t|", each, end=" | ")
            else:
                print(each, end=" | ")
        print()
    print("\t+---+---+---+")
    print()
    

# Check if cell is empty
def is_empty(move: tuple, board: list):
    position = move[0]
    row = position // 3
    col = position % 3
    if board[row][col] == " ":
        return True


# Get empty cells
def get_empty(board: list) -> list:
    empty_cells: list = []
    num: int = 1
    for items in board:
        for each in items:
            if each == " ":
                empty_cells.append(num)
            num += 1
    return empty_cells
    

# Check Tie
def check_tie(board: list):
    if len(get_empty(board)) <= 0:
        print("It´s a tie!")
        return True


# Check for winn
def check_status(board: list, player: str) -> True:
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
        win = True
        for each in option:
            row, col = each
            if board[row][col] != player:
                win = False
                break
        if win:
            return True
    return False


# Make a move
def make_move(move: tuple, board: list) -> None:
    position = int(move[0])
    value = str(move[1])
    row = position // 3
    col = position % 3
    board[row][col] = value


def human_move(board: list) -> None:
    print("Select a number between 1 & 9:")
    h_move = int(input("Input > ")) -1, "X"
    
    if is_empty(h_move, board):
        make_move(h_move, board)
    else:
        print("That cell is not empty!")
        human_move(board)


def computer_move(board: list) -> None:
    empty_cells: list = get_empty(board)
    c_move: int = int(random.choice(empty_cells)) -1, "O"
    make_move(c_move, board)
    print(f"Computer choose: {c_move[0]+1}")


table = create_board()
while True:

    human_move(table)
    show_board(table)
    if check_status(table, "X"):
        print("You are the winner".upper())
        break
    
    if check_tie(table):
        break

    computer_move(table)
    show_board(table)
    if check_status(table, "O"):
        print("You lost! Computer wins.".upper())
        break

    if check_tie(table):
        break