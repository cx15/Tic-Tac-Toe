import random



#variables to operate the structure of the games

possibleNumbers = [1,2,3,4,5,6,7,8,9]


Board =  [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
colloms = 3

#Functions to print out a game board

def printGameBoard():
  for a in range(rows):
    print("\n+---+---+---+") 
    print("|", end="")
    for b in range(colloms):
      print("", Board[a][b], end=" |")
  print("\n+---+---+---+")

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
def checkForWinner(Board):
  """Returns the winner, if any.

  :param Board - a 3X3 array of "X", "O" or ""
  Returns "X", "O", or "N" depending on who has won.
  """
  # X axis
  if(Board[0][0] == 'X' and Board[0][1] == 'X' and Board[0][2] == 'X'):
    print("X has won!")
    return "X"
  elif(Board[0][0] == 'O' and Board[0][1] == 'O' and Board[0][2] == 'O'):
    print("O has won!")
    return "O"
  elif(Board[1][0] == 'X' and Board[1][1] == 'X' and Board[1][2] == 'X'):
    print("X has won!")
    return "X"
  elif(Board[1][0] == 'O' and Board[1][1] == 'O' and Board[1][2] == 'O'):
    print("O has won!")
    return "O"
  elif(Board[2][0] == 'X' and Board[2][1] == 'X' and Board[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(Board[2][0] == 'O' and Board[2][1] == 'O' and Board[2][2] == 'O'):
    print("O has won!")
    return "O"
  # Y axis
  if(Board[0][0] == 'X' and Board[1][0] == 'X' and Board[2][0] == 'X'):
    print("X has won!")
    return "X"
  elif(Board[0][0] == 'O' and Board[1][0] == 'O' and Board[2][0] == 'O'):
    print("O has won!")
    return "O"
  elif(Board[0][1] == 'X' and Board[1][1] == 'X' and Board[2][1] == 'X'):
    print("X has won!")
    return "X"
  elif(Board[0][1] == 'O' and Board[1][1] == 'O' and Board[2][1] == 'O'):
    print("O has won!")
    return "O"
  elif(Board[0][2] == 'X' and Board[1][2] == 'X' and Board[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(Board[0][2] == 'O' and Board[1][2] == 'O' and Board[2][2] == 'O'):
    print("O has won!")
    return "O"
  # Cross wins
  elif(Board[0][0] == 'X' and Board[1][1] == 'X' and Board[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(Board[0][0] == 'O' and Board[1][1] == 'O' and Board[2][2] == 'O'):
    print("O has won!")  
    return "O"
  elif(Board[0][2] == 'X' and Board[1][1] == 'X' and Board[2][0] == 'X'):
    print("X has won!")  
    return "X"
  elif(Board[0][2] == 'O' and Board[1][1] == 'O' and Board[2][0] == 'O'):
    print("O has won!") 
    return "O" 
  else:
    return "N"

leaveLoop = False
turnCounter = 0

if __name__=="__main__":
    print("welcome to Tic Tac Toe")
    print("----------------------")
    while(leaveLoop == False):
        #the player's turn
        if(turnCounter % 2 == 0):
            printGameBoard()
            numberPicked = int(input("\nChoose a number [1-9]: "))
            if(numberPicked >= 1 or numberPicked <= 9):
                modifyArray(numberPicked, 'X')
                possibleNumbers.remove(numberPicked)
            else:
                print("Invalid input. Please try again.")
                turnCounter += 1
        #the computer's turn
        else:
            while(True):
                cpuChoice = random.choice(possibleNumbers)
                print("\nCpu choice: ", cpuChoice)
                if(cpuChoice in possibleNumbers):
                    modifyArray(cpuChoice, 'O')
                    possibleNumbers.remove(cpuChoice)
                    turnCounter += 1
                    break

        winner = checkForWinner(Board)
        if(winner != "N"):
            print("\nGame over! Thank you for playing :)")
            break
