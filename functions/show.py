# Print board
def board(table: list) -> None:
    print()
    for item in table:
        print("\t+---+---+---+")
        for idx, each in enumerate(item):
            if idx == 0:
                print("\t|", each, end=" | ")
            else:
                print(each, end=" | ")
        print()
    print("\t+---+---+---+")
    print()