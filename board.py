
class Board:
  """Represents a tic tac toe board"""

  def __init__(self, initial_data=None):
    self.ROWS = 3
    self.COLS = 3
    self._board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    self._remaining_positions = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    if initial_data:
      self.fill_from_array(initial_data)

  def row_col_from_num(self, num):
    # num goes from 1 to 9
    # The row number is num / 3
    # The col number is the "remainder when we divide by 3"
    row = (num - 1) // self.ROWS
    col = (num - 1) % self.COLS
    return row, col

  def modify_board(self, num, turn):
    """
    Modifies the board array when a player takes a turn.

    :param num - a number from 1 to 9 representing a position on the board
    :param turn - either "X" or "O" depending on the turn.
"""
    row, col = self.row_col_from_num(num)
    self._board[row][col] = turn
    self._remaining_positions.remove(num)

  def get_symbol(self, row: int, col: int):
    """
    Given the row and column return the symbol at that location
    or the number if the location hasn't been used.
    """
    return self._board[row][col]

  def get_symbol_by_pos(self, pos: int):
    """
    Given the play position 1-9 return the symbol at that location
    or the number if the location hasn't been used.
    """
    row, col = self.row_col_from_num(pos)
    return self._board[row][col]

  def is_valid_play(self, num):
    """Is the play into an empty space?"""
    return num in self._remaining_positions

  def get_open_positions(self):
    """Return a list of positions that have not been taken."""
    return list(self._remaining_positions)

  def fill_from_array(self, data):
    """Takes a 2D array of turn symbols in order and
    fills the board"""
    idx = 1
    for row in range(0, 3):
      for col in range(0, 3):
        self.modify_board(idx, data[row][col])
        idx += 1

  def check_for_winner(self):
    """Returns the winner, if any.

    Returns "X", "O" depending on who has won or "N" if it's a
    tie or "None" otherwise.
    """
    # currently only works for 3x3 boards.

    # Check to see if there's a complete row
    for row in range(0, self.ROWS):
      symbol = self.get_symbol(row, 0)
      if (symbol in ['X', 'O'] and self.get_symbol(row, 1) == symbol
          and self.get_symbol(row, 2) == symbol):
        return symbol

    # Check to see if there's a complete column
    for col in range(0, self.COLS):
      symbol = self.get_symbol(0, col)
      if (symbol in ['X', 'O'] and self.get_symbol(1, col) == symbol
          and self.get_symbol(2, col) == symbol):
        return symbol

    # Cross wins
    symbol = self.get_symbol(1, 1)
    if (symbol in ['X', 'O'] and self.get_symbol(0, 0) == symbol and
          self.get_symbol(2, 2) == symbol):
      return symbol
    elif (symbol in ['X', 'O'] and self.get_symbol(0, 2) == symbol and
          self.get_symbol(2, 0) == symbol):
      return symbol

    # board is full
    for row in range(0, self.ROWS):
      for col in range(0, self.COLS):
        symbol = self.get_symbol(row, col)
        # print(f"Symbol: {symbol}")
        if symbol not in ['X', 'O']:
          return None
    return "N"
