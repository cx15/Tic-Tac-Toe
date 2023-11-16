import strategies
from display import print_game_board
from game import play_game


# TODOs
# We will:
# 1) Make the game work DONE
# 2) Make it possible to do PvP, PvC, or CvC
# 3) Make it possible to swap in better computer players DONE
# 4) Replace the text interface with a graphical interface.
# 5) Maybe? See if we can get the computer to *learn*.


if __name__ == "__main__":
    print("welcome to Tic Tac Toe")
    print("----------------------")
    game_mode = input("which mode would you like to play:pvp pvc cvp cvc")

    player1_human = (game_mode[0] == "p")
    player2_human = (game_mode in ["pvp", "cvp"])

    player1_cpu = (game_mode[0] == "c")
    player2_cpu = (game_mode in ["cvc", "pvc"])

    cpu_strat1 = strategies.CpuBetterStrategy()
    cpu_strat2 = strategies.CpuBetterStrategy()

    the_game_board = play_game(
      player1_human, player2_human, cpu_strat1, cpu_strat2,
      do_print=True)

    print_game_board(the_game_board)

