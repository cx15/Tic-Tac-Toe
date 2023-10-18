import board
import strategies
from display import print_game_board


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
    game_mode = input("which mode would you like to play:pvp pvc cvp cvc")

    player1_human = (game_mode[0] == "p")
    player2_human = (game_mode in ["pvp", "cvp"])

    player1_cpu = (game_mode[0] == "c")
    player2_cpu = (game_mode in ["cvc", "pvc"])

    cpu_strat1 = strategies.CpuRandomStrategy()
    cpu_strat2 = strategies.CpuRandomStrategy()
    game_board = board.Board()

    while not leave_loop:
      # the player's turn
      if turn_counter % 2 == 0:
       # player_turn(game_board, 'X')
        if player1_human:
            player_turn(game_board,'X')
        else:
            cpu_strat1.make_turn(game_board)
      else:
        if player2_human:
            player_turn(game_board,'O')
        else:
            cpu_strat2.make_turn(game_board)
     #""" else:
      #  if player1_cpu:
      #      print()
       # else:
       #     print()"""

        #cpu_strategy.make_turn(game_board)

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

