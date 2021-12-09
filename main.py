def check_wins(values):
    if values[0] == "_":
        return 0, ""
    elif len(set(values)) == 1:
        return True, values[0]
    else:
        return False, ""


def print_board(cells):
    print("---------")
    print(f"| {cells[0]} {cells[1]} {cells[2]} |")
    print(f"| {cells[3]} {cells[4]} {cells[5]} |")
    print(f"| {cells[6]} {cells[7]} {cells[8]} |")
    print("---------")


def add_char(cells, char):
    cords = input("Enter the coordinates: ").split(" ")

    if len(cords) == 2 and cords[0].isdigit() and cords[1].isdigit():
        if not 1 <= int(cords[0]) <= 3 or not 1 <= int(cords[1]) <= 3:
            print("Coordinates should be from 1 to 3!")
            return False
        y = int(cords[0]) - 1
        x = int(cords[1]) - 1
        position = y * 3 + x
        if cells[position] != "_":
            print("This cell is occupied! Choose another one!")
            return False
        elif 1 <= int(cords[0]) <= 3 and 1 <= int(cords[1]) <= 3:
            cells[position] = char
            return True

    else:
        print("You should enter numbers!")
        return False


def check_state(cells):

    row1, row2, row3 = [cells[0], cells[1], cells[2]], [cells[3], cells[4], cells[5]], [cells[6], cells[7], cells[8]]
    column1, column2, column3 = [cells[0], cells[3], cells[6]], [cells[1], cells[4], cells[7]], [cells[2], cells[5],
                                                                                                 cells[8]]
    diagonal1, diagonal2 = [cells[0], cells[4], cells[8]], [cells[2], cells[4], cells[6]]

    board = [row1, row2, row3, column1, column2, column3, diagonal1, diagonal2]

    wins, win_symbol = 0, ""
    for i in board:
        temp = check_wins(i)
        wins, win_symbol = wins + temp[0], win_symbol + temp[1]
    if wins > 1 or abs(cells.count("X") - cells.count("O")) > 1:
        print("Impossible")
        return False
    elif wins == 1:
        print(f"{win_symbol} wins")
        return False
    elif cells.count("_") == 0:
        print("Draw")
        return False
    else:
        return True


def play(cells, char):
    while True:
        if add_char(cells, char):
            break
    print_board(cells)
    # python 3.8 solution
    # while (state := add_char(cells, "X")) is False:
    #    pass


def main():
    cells = list("_________")
    print_board(cells)

    play(cells, "X")

    while check_state(cells):
        play(cells, "O")
        if not check_state(cells):
            break
        play(cells, "X")


if __name__ == "__main__":
    main()
