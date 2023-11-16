import board
from display import print_game_board

def play_game(player1_human, player2_human, cpu_strat1, cpu_strat2):
  leave_loop = False
  turn_counter = 0

  game_board = board.Board()

  while not leave_loop:
    # the player's turn
    if turn_counter % 2 == 0:
      # player_turn(game_board, 'X')
      if player1_human:
        player_turn(game_board, 'X')
      else:
        cpu_strat1.make_turn(game_board=game_board, cpu_x="X")
    else:
      if player2_human:
        player_turn(game_board, 'O')
      else:
        cpu_strat2.make_turn(game_board=game_board, cpu_x="O")

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

  return game_board


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
