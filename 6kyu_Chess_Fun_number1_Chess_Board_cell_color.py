"""
Task

Given two cells on the standard chess board, determine whether they have the same color or not.
Example

For cell1 = "A1" and cell2 = "C3", the output should be true.

For cell1 = "A1" and cell2 = "H3", the output should be false.

Input/Output

    [input] string cell1

    [input] string cell2

    [output] a boolean value

    true if both cells have the same color, false otherwise.

"""


def chess_board_cell_color(cell1, cell2):
    c1 = get_color(cell1)
    c2 = get_color(cell2)
    return c1 == c2


def get_color(cell):
    if cell[0] in "ACEG":
        return "w" if int(cell[1]) % 2 == 0 else "b"
    else:
        return "b" if int(cell[1]) % 2 == 0 else "w"
