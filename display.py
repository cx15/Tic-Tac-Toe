import board


def board_representation(game_board: board.Board):
  representation = ""
  for a in range(game_board.ROWS):
    representation += "\n+---+---+---+\n"
    representation += "|"
    for b in range(game_board.COLS):
      representation += " "
      representation += str(game_board.get_symbol(row=a, col=b))
      representation += " |"
  representation += "\n+---+---+---+\n"
  return representation;

  # Check to see if nobody won and the board is full.


def print_game_board(game_board: board.Board):
  print(board_representation(game_board))
