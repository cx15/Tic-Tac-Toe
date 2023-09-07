
class Board:
  """Represents a tic tac toe board"""


  def __init__(self):
    print("THe board got created")
    self.ROWS = 3
    self.COLS = 3
    self._board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    self._remaining_positions = {1, 2, 3, 4, 5, 6, 7, 8, 9}


  def modify_board(self, num, turn):
    """
    Modifies the board array when a player takes a turn.

    :param num - a number from 1 to 9 representing a position on the board
    :param turn - either "X" or "O" depending on the turn.
"""
    # num goes from 1 to 9
    # The row number is num / 3
    # The col number is the "remainder when we divide by 3"
    row = (num - 1) // self.ROWS
    col = (num - 1) % self.COLS
    self._board[row][col] = turn
    self._remaining_positions.remove(num)

  def get_symbol(self, row: int, col: int):
    """
    Given the row and column return the symbol at that location
    or the number if the location hasn't been used.
    """
    return self._board[row][col]

  def is_valid_play(self, num):
    """Is the play into an empty space?"""
    return num in self._remaining_positions




