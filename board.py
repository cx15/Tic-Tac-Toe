

possibleNumbers = {1,2,3,4,5,6,7,8,9}


Board = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
colloms = 3

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
