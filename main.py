import board
import strategies

# TODOs
# We will:
# 1) Make the game work
# 2) Make it possible to do PvP, PvC, or CvC
# 3) Make it possible to swap in better computer players
# 4) Replace the text interface with a graphical interface.
# 5) Maybe? See if we can get the computer to *learn*.

#variables to operate the structure of the games


#Functions to print out a game board
def board_representation(game_board: board.Board):
  representation = ""
  for a in range(board.ROWS):
    representation += "\n+---+---+---+\n"
    representation += "|"
    for b in range(board.COLS):
      representation += " "
      representation += str(game_board.board[a][b])
      representation += " |"
  representation += "\n+---+---+---+\n"
  return representation;

  # Check to see if nobody won and the board is full.


def print_game_board(game_board: board.Board):
  print(board_representation(game_board))


# Define function to check for a winner
def check_for_winner(the_board):
  """Returns the winner, if any.

  :param the_board - a 3X3 array of "X", "O" or ""
  Returns "X", "O" depending on who has won or "N" if it's a
  tie or "None" otherwise.
  """
  # Check to see if there's a complete row
  for row in range(0, 3):
    symbol = the_board[row][0]
    if (symbol in ['X', 'O'] and the_board[row][1] == symbol
        and the_board[row][2] == symbol):
      return symbol

  # Check to see if there's a complete column
  for col in range(0, 3):
    symbol = the_board[0][col]
    if (symbol in ['X', 'O'] and the_board[1][col] == symbol
        and the_board[2][col] == symbol):
      return symbol

  # Cross wins
  symbol = the_board[1][1]
  if (symbol in ['X', 'O'] and the_board[0][0] == symbol and
        the_board[2][2] == symbol):
    return symbol
  elif (symbol in ['X', 'O'] and the_board[0][2] == symbol and
        the_board[2][0] == symbol):
    return symbol

  # board is full
  for row in range(0, 3):
    for col in range(0, 3):
      symbol = the_board[row][col]
      # print(f"Symbol: {symbol}")
      if symbol not in ['X', 'O']:
        return None
  return "N"


def player_turn(game_board: board.Board):
  print_game_board(game_board)
  while True:
    number_picked = int(input("\nChoose a number [1-9]: "))
    if (1 <= number_picked <= 9 and
          number_picked in board.POSSIBLE_NUMBERS):
      game_board.modify_foo(number_picked, 'X')
      board.POSSIBLE_NUMBERS.remove(number_picked)
      return
    else:
      print("Invalid input. Please try again.")


leave_loop = False
turn_counter = 0


if __name__ == "__main__":
    print("welcome to Tic Tac Toe")
    print("----------------------")

    our_strategy = strategies.CpuBetterStrategy()
    game_board = board.Board()

    while not leave_loop:
      # the player's turn
      if(turn_counter % 2 == 0):
        player_turn(game_board)
      else:
        # the computer's turn
        our_strategy.make_turn(game_board)

      turn_counter += 1

      winner = check_for_winner(game_board.board)
      if winner == "O":
        print("O has won!")
        leave_loop = True
      elif winner == "X":
        print("X has won!")
        leave_loop = True
      elif winner == "N":
        leave_loop = True
        print("\nGame over! Thank you for playing :)")

      print_game_board(game_board)

