# Player2.py
#
# author: Stephen Adams
# date  : 2024-10-19
import random

def getMove(board):
    """
    Determines the next move for Player 1. Player 1 will always be 'X'.
    
    Since studnets will not have yet learned lists, we will use indicies 1-9 to represent the Tic-Tac-Toe board as follows:

        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9


    Parameters:
    board (list of list of str): The current state of the Tic-Tac-Toe board.

    Returns:
    integer: The index of the next move between 1 and 9.
    """
    
    return random.randint(1, 9) # This is a placeholder. Replace this line with your code.