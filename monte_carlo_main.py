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

    cpu_strat1 = strategies.CpuBetterStrategy()
    cpu_strat2 = strategies.CpuBetterStrategy()

    # TODO: add counters for number of times each strategy wins.
    # Increment them after each game.
    N_GAMES = 10000

    p1_wins = 0
    p2_wins = 0
    p1_wins_by_position = {
      1: 0,
      2: 0,
      3: 0,
      4: 0,
      5: 0,
      6: 0,
      7: 0,
      8: 0,
      9: 0
    }

    for i in range(0, N_GAMES):
      the_game_board, the_winner, history = play_game(
        player1_human, player2_human, cpu_strat1, cpu_strat2,
        do_print=False)
      #print(history)
      p1_starting_move = history[0]

      if the_winner == "X":
        p1_wins += 1
        p1_wins_by_position[p1_starting_move] += 1
      elif the_winner == "O":
        p2_wins += 1

    print(f"P1 wins {p1_wins * 100.0 / N_GAMES}%")
    print(f"P2 wins {p2_wins * 100.0 / N_GAMES}%")
    print(f"Draws {(N_GAMES - p1_wins - p2_wins) * 100.0 / N_GAMES}%")
    print(f"p1 wins by position {p1_wins_by_position}")


