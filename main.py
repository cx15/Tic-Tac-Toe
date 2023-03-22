import random

# TODOs
# We will:
# 1) Make the game work
# 2) Make it possible to do PvP, PvC, or CvC
# 3) Make it possible to swap in better computer players
# 4) Replace the text interface with a graphical interface.
# 5) Maybe? See if we can get the computer to *learn*.

#variables to operate the structure of the games

possibleNumbers = {1,2,3,4,5,6,7,8,9}


Board =  [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
colloms = 3

#Functions to print out a game board
def board_representation():
  representation = ""
  for a in range(rows):
    representation += "\n+---+---+---+\n"
    representation += "|"
    for b in range(colloms):
      representation += " "
      representation += str(Board[a][b])
      representation += " |"
  representation += "\n+---+---+---+\n"
  return representation;

  # Check to see if nobody won and the board is full.


def printGameBoard():
  print(board_representation())


#in charge of how many times the board needs to be modified
def modifyArray(num,turn):
    """
  num -= 1
  if(num == 0):
    Board[0][0] = turn
  elif(num == 1):
    Board[0][1] = turn
  elif(num == 2):
    Board[0][2] = turn
  elif(num == 3):
    Board[1][0] = turn
  elif(num == 4):
    Board[1][1] = turn
  elif(num == 5):
    Board[1][2] = turn
  elif(num == 6):
    Board[2][0] = turn
  elif(num == 7):
    Board[2][1] = turn
  elif(num == 8):
    Board[2][2] = turn
    """
    # num goes from 1 to 9
    # The row number is num / 3
    # The col number is the "remainder when we divide by 3"
    row = (num - 1) // 3
    col = (num - 1) % 3
    Board[row][col] = turn


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
    for collom in range(0,3 ):
      symbol = board[row][collom]
      if not symbol:
        return None
  return "N"

def playerTurn():
  printGameBoard()
  while True:
    number_picked = int(input("\nChoose a number [1-9]: "))
    if (number_picked >= 1 and number_picked <= 9 and
          number_picked in possibleNumbers):
      modifyArray(number_picked, 'X')
      possibleNumbers.remove(number_picked)
      return
    else:
      print("Invalid input. Please try again.")

def cpuTurn():
  cpuChoice = random.choice(list(possibleNumbers))
  print("\nCpu choice: ", cpuChoice)
  if(cpuChoice in possibleNumbers):
    modifyArray(cpuChoice, 'O')
    possibleNumbers.remove(cpuChoice)


leave_loop = False  # TODO(ahmed): are you using this?
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
        cpuTurn()

      turnCounter += 1

      winner = check_for_winner(Board)
      if winner == "O":
        print("O has won!")
        leave_loop = True
      elif winner == "X":
        print("X has won!")
        leave_loop = True
      elif(winner != "N"):
        leave_loop = True
        print("\nGame over! Thank you for playing :)")

      printGameBoard()

