import random


game_running: bool = True
current_player: str = "X"
winner: str = None


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


# check rows
def check_rows(board: list) -> bool:
    global winner
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != " ":
        winner = board[0][0]
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != " ":
        winner = board[1][0]
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != " ":
        winner = board[2][0]
        return True


def check_columns(board: list) -> bool:
    global winner
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != " ":
        winner = board[0][0]
        return True
    if board[0][1] == board[1][1] == board[2][1] and board[0][1] != " ":
        winner = board[1][0]
        return True
    if board[0][2] == board[1][2] == board[2][2] and board[0][2] != " ":
        winner = board[2][0]
        return True


def check_diagonals(board: list) -> bool:
    global winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        winner = board[0][0]
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[2][0] != " ":
        winner = board[2][0]
        return True
    

# Check Tie
def check_tie(board: list):
    if len(get_empty(board)) <= 0:
        print("It´s a tie!")
        return True


# Game check
def check_status(board: list):
    global game_running, winner
    if check_rows(board) or check_columns(board) or check_diagonals(board):
        print(f"We have a winner: {winner}!")
        game_running = False
    elif check_tie(board):
        game_running = False

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
    print(f"Computer: {c_move[0]+1}")


# Switch player
def switch_player(board):
    global current_player
    if current_player == "X":
        human_move(board)
        check_status(board)
        current_player = "O"
    else:
        computer_move(board)
        check_status(board)
        current_player = "X"


table = create_board()
while game_running:

    switch_player(table)

    show_board(table)