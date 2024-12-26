from functions import create, show, check, moves

table = create.board()
while True:

    moves.human(table)
    show.board(table)
    if check.status(table, "X"):
        print("You are the winner".upper())
        break
    
    if check.is_tie(table):
        break

    moves.computer(table)
    show.board(table)
    if check.status(table, "O"):
        print("You lost! Computer wins.".upper())
        break

    if check.is_tie(table):
        break