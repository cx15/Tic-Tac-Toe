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
def board_representation():
  representation = ""
  for a in range(board.rows):
    representation += "\n+---+---+---+\n"
    representation += "|"
    for b in range(board.colloms):
      representation += " "
      representation += str(board.Board[a][b])
      representation += " |"
  representation += "\n+---+---+---+\n"
  return representation;

  # Check to see if nobody won and the board is full.


def printGameBoard():
  print(board_representation())


# Define function to check for a winner
def check_for_winner(board):
  """Returns the winner, if any.

  :param board - a 3X3 array of "X", "O" or ""
  Returns "X", "O" depending on who has won or "N" if it's a
  tie or "None" otherwise.
  """
  # Check to see if there's a complete row
  for row in range(0, 3):
    symbol = board[row][0]
    if (symbol in ['X', 'O'] and board[row][1] == symbol
        and board[row][2] == symbol):
      return symbol

  # Check to see if there's a complete column
  for collom in range(0, 3):
    symbol = board[0][collom]
    if (symbol in ['X', 'O'] and board[1][collom] == symbol
        and board[2][collom] == symbol):
      return symbol

  # Cross wins
  symbol = board[1][1]
  if(symbol in ['X', 'O'] and board[0][0] == symbol and board[2][2] == symbol):
    return symbol
  elif(symbol in ['X', 'O'] and board[0][2] == symbol and board[2][0] == symbol):
    return symbol

  # board is full
  for row in range(0, 3):
    for collom in range(0, 3):
      symbol = board[row][collom]
      # print(f"Symbol: {symbol}")
      if symbol not in ['X', 'O']:
        return None
  return "N"

def playerTurn():
  printGameBoard()
  while True:
    number_picked = int(input("\nChoose a number [1-9]: "))
    if (number_picked >= 1 and number_picked <= 9 and
          number_picked in board.possibleNumbers):
      board.modifyArray(number_picked, 'X')
      board.possibleNumbers.remove(number_picked)
      return
    else:
      print("Invalid input. Please try again.")


leave_loop = False
turnCounter = 0

if __name__ == "__main__":
    print("welcome to Tic Tac Toe")
    print("----------------------")
    while not leave_loop:
      #the player's turn
      if(turnCounter % 2 == 0):
        playerTurn()
      else:
        #the computer's turn
        strategies.cpu_turn_random()

      turnCounter += 1

      winner = check_for_winner(board.Board)
      if winner == "O":
        print("O has won!")
        leave_loop = True
      elif winner == "X":
        print("X has won!")
        leave_loop = True
      elif winner == "N":
        leave_loop = True
        print("\nGame over! Thank you for playing :)")

      printGameBoard()

