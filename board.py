

POSSIBLE_NUMBERS = {1, 2, 3, 4, 5, 6, 7, 8, 9}


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ROWS = 3
COLS = 3


def modify_array(num, turn):
    """
    Modifies the board array when a player takes a turn.

    :param num - a number from 1 to 9 representing a position on the board
    :param turn - either "X" or "O" depending on the turn.
"""
    # num goes from 1 to 9
    # The row number is num / 3
    # The col number is the "remainder when we divide by 3"
    row = (num - 1) // 3
    col = (num - 1) % 3
    board[row][col] = turn
