"""
Runs a monte carlo simulator over tic-tac-toe to evaluate different
strategies.
"""

import strategies
from display import print_game_board
from game import play_game

if __name__ == "__main__":
    print("welcome to Tic Tac Toe Monte Carlo")
    print("----------------------------------")

    player1_human = False
    player2_human = False

    cpu_strat1 = strategies.CpuRandomStrategy()
    cpu_strat2 = strategies.CpuBetterStrategy()

    # TODO: add counters for number of times each strategy wins.
    # Increment them after each game.

    the_game_board, the_winner = play_game(
      player1_human, player2_human, cpu_strat1, cpu_strat2,
      do_print=False)

    print(the_winner)

    #print_game_board(the_game_board)

