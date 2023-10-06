import board
import strategies
from display import print_game_board

game_mode = int(input("which mode would you like to play:pvp pvc cvp cvc"))
if game_mode = "pvc":
  player_symbol = 'X'
elif game_mode = 'cvp':
  player_symbol = 'O'
# TODOs
# We will:
# 1) Make the game work DONE
# 2) Make it possible to do PvP, PvC, or CvC
# 3) Make it possible to swap in better computer players DONE
# 4) Replace the text interface with a graphical interface.
# 5) Maybe? See if we can get the computer to *learn*.

def player_turn(game_board: board.Board, player_symbol='X'):
  print_game_board(game_board)
  while True:
    number_picked = int(input("\nPlayer " + player_symbol + " pick a number [1-9]: "))
    if (1 <= number_picked <= 9 and
        game_board.is_valid_play(number_picked)):
      game_board.modify_board(number_picked, player_symbol)
      return
    else:
      print("Invalid input. Please try again.")


leave_loop = False
turn_counter = 0


if __name__ == "__main__":
    print("welcome to Tic Tac Toe")
    print("----------------------")

    cpu_strategy = strategies.CpuMirrorStrategy()
    game_board = board.Board()

    while not leave_loop:
      # the player's turn
      if turn_counter % 2 == 0:
        player_turn(game_board, 'X')
      else:
        # the computer's turn
        #cpu_strategy.make_turn(game_board)
        player_turn(game_board, 'O')
      turn_counter += 1

      winner = game_board.check_for_winner()
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

