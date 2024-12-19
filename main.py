import random

table: list = [
    " ", " ", " ",
    " ", " ", " ",
    " ", " ", " ",
]

game_running: bool = True
current_player = "X"
winner = None
    

# Print board
def show_board(board: list) -> None:
    print(" =============")
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(" -------------")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(" -------------")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")
    print(" =============")

# Check if cell is empty
def is_empty(move: tuple, board: list):
    position = move[0]
    if board[position] == " ":
        return True

# check rows
def check_rows(board: list) -> bool:
    global winner
    if board[0] == board[1] == board[2] and board[0] != " ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[6]
        return True



def check_columns(board: list) -> bool:
    global winner
    if board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    if board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[1]
        return True
    if board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[2]
        return True


def check_diagonals(board: list) -> bool:
    global winner
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != " ":
        winner = board[2]
        return True
    

# Check Tie
def check_tie(board: list):
    if " " not in board:
        print("It´s a tie!")
        return True


# Game check
def check_status(board: list):
    global game_running, winner
    # if check_rows(board) or check_diagonals(board):
    if check_rows(board) or check_columns(board) or check_diagonals(board):
        print(f"We have a winner: {winner}!")
        game_running = False
    elif check_tie(board):
        game_running = False

# Make a move
def make_move(move: tuple, board: list) -> None:
    position = int(move[0])
    value = str(move[1])
    board[position] = value


def human_move(board: list) -> None:
    print("Select a number between 1 & 9:")
    h_move = int(input("Input > ")) -1, "X"
    
    if is_empty(h_move, board):
        make_move(h_move, board)
    else:
        print("That cell is not empty!")
        human_move(board)


def computer_move(board: list) -> None:
    empty_cells: list = []
    for idx, val in enumerate(board):
        if val == " ":
            empty_cells.append(idx)
    c_move: int = int(random.choice(empty_cells)), "O"
    make_move(c_move, board)


# Switch player
def switch_player():
    global current_player
    if current_player == "X":
        human_move(table)
        check_status(table)
        current_player = "O"
    else:
        computer_move(table)
        check_status(table)
        current_player = "X"


while game_running:

    switch_player()

    show_board(table)