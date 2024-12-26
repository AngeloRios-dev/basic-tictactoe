# Check if cell is empty
def is_empty(move: tuple, board: list) -> bool:
    position = move[0]
    row = position // 3
    col = position % 3

    if board[row][col] == " ":
        return True

    return False


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
def is_tie(board: list) -> bool:
    for row in board:
        if " " in row:
            return False
    
    return True

def status(board: list, player: str) -> bool:
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