"""
If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]

We want our function to return:

    -1 if the board is not yet finished AND no one has won yet (there are empty spots),
    1 if "X" won,
    2 if "O" won,
    0 if it's a cat's game (i.e. a draw).

You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
"""
import numpy as np


def is_solved(board):
    b = np.array(board)
    for i in range(3):
        if (b[:,i] == 1).all():
            return 1
        elif (b[i,:] == 1).all():
            return 1
        elif (b[:,i] == 2).all():
            return 2
        elif (b[i,:] == 2).all():
            return 2
    for i in range(1,3):
        if (np.diag(b) == i).all():
            return i
        elif (np.diag(np.fliplr(b)) == i).all():
            return i
    if  (b == 0).any():
        return -1
    return -1 if (b == 0).any() else 0
