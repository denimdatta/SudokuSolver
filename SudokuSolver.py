from sys import argv

import numpy as np


def get_sudoku(filename):
    _sudoku = []
    with open(filename, "r") as file:
        data = file.readlines()

    for line in data:
        values = line.rstrip().split(",")
        _sudoku.append([int(val) for val in values])

    return _sudoku


def print_sudoku(_sudoku):
    print()
    for row in range(9):
        print()
        if row % 3 == 0:
            print()
        for col in range(9):
            if col % 3 == 0:
                print("   ", end="")
            print(_sudoku[row][col], end=" ")
    print("\n")


def empty_cell(_sudoku):
    for row in range(9):
        for col in range(9):
            if (_sudoku[row][col] == 0):
                loc = [row, col]
                return loc
    return []


def solver(_sudoku):
    cell = empty_cell(_sudoku)
    if len(cell) == 0:
        return True

    (row, col) = (cell[0], cell[1])

    complete_row = _sudoku[row]

    temp = np.array(_sudoku)
    temp = temp[:, col, None]
    complete_col = temp.flatten().tolist()
    del temp

    s_row = row - (row % 3)
    s_col = col - (col % 3)
    temp = np.array([_sudoku[i][s_col:s_col+3] for i in range(s_row, s_row+3)])
    complete_box = temp.flatten().tolist()
    del temp, s_col, s_row

    print("Row: {}\nCol: {}\nBox: {}".format(complete_row, complete_col, complete_box))

    # for entry in range(1,10):
    #     if
    #
    #
    # solver(_sudoku)


def main():
    problem_files = []
    if len(argv) < 2:
        problem_files.append("problem.txt")
    else:
        problem_files.append(argv[1])

    sudoku = get_sudoku(problem_files[0])
    print_sudoku(sudoku)
    solver(sudoku)
    print_sudoku(sudoku)


if __name__ == "__main__":
    main()
