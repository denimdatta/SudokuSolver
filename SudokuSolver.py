import math
from sys import argv

import numpy as np


def get_sudoku(filename):
    _sudoku = []
    with open(filename, "r") as file:
        data = file.readlines()

    lineno = 0
    length = len(data)
    size = math.sqrt(length)
    if not size == (int(size) / 1.0):
        print("File {0} is not correct. Should be of square length."
              "\nColumn count {1} is not a square number".format(filename, length))
        return []
    for line in data:
        lineno += 1
        values = line.rstrip().split(",")
        if not len(values) == length:
            print("File {0} is not correct. Should be of square length. "
                  "\nCheck line {1}: Column count not matching with Row count".format(filename, lineno))
            return []
        _sudoku.append([int(val) for val in values])

    return int(size), _sudoku


def print_sudoku(_sudoku, size):
    sqsize = size*size
    for row in range(sqsize):
        print()
        if (not row == 0) and (row % size == 0):
            print()
        for col in range(sqsize):
            if col % size == 0:
                print("   ", end="")
            print(_sudoku[row][col], end=" ")
    print("\n")


def empty_cell(_sudoku, size):
    sqsize = size*size
    for row in range(sqsize):
        for col in range(sqsize):
            if (_sudoku[row][col] == 0):
                loc = [row, col]
                return loc
    return []


def solver(_sudoku, size):
    cell = empty_cell(_sudoku, size)
    if len(cell) == 0:
        return True

    (row, col) = (cell[0], cell[1])

    complete_row = _sudoku[row]

    temp = np.array(_sudoku)
    temp = temp[:, col, None]
    complete_col = temp.flatten().tolist()
    del temp

    s_row = row - (row % size)
    s_col = col - (col % size)
    temp = np.array([_sudoku[i][s_col:s_col + size] for i in range(s_row, s_row + size)])
    complete_box = temp.flatten().tolist()
    del temp, s_col, s_row

    limit = (size*size)+1
    for entry in range(1, limit):
        if (entry in complete_row) or (entry in complete_col) or (entry in complete_box):
            continue

        _sudoku[row][col] = entry

        if solver(_sudoku, size):
            return True
        else:
            _sudoku[row][col] = 0

    return False


def main():
    problem_files = []
    if len(argv) < 2:
        problem_files.append("problem_16x16.txt")
    else:
        problem_files.append(argv[1])

    (size, sudoku) = get_sudoku(problem_files[0])
    if len(sudoku) == 0:
        return
    print("Problem\n\n")
    print_sudoku(sudoku, size)
    solver(sudoku, size)
    print("\n\n\nSolution\n\n")
    print_sudoku(sudoku, size)


if __name__ == "__main__":
    main()
