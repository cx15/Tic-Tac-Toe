"""
These are the tests for Tic Tac Toe
"""


import unittest as u

import board
import main
import strategies


class BasicFunctionTests(u.TestCase):
    def setUp(self) -> None:
      # Reset the board between tests
      # TODO Remove this once board has been refactored
      board.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


    def test_board_representation(self):
        golden_board = """
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
"""
        self.assertEqual(golden_board, main.board_representation())

    def test_modify_array(self):
        board.modify_array(3, "X")
        self.assertEqual(board.board[0][2], "X", "First row, 3 element should be X")

        board.modify_array(8, "O")
        self.assertEqual(board.board[2][1], "O", "Last row, 2nd element should be O")
        
   
    def test_check_for_winner(self):
        board_x_wins = [["X", "X", "X"],
                        ["O", "X", "O"],
                        ["O", "O", ""]]

        result = main.check_for_winner(board_x_wins)
        # Returns "X", "O" or "N"
        self.assertEqual("X", result)

        result = main.check_for_winner(
          [board_x_wins[2],
           board_x_wins[0],
           board_x_wins[1]])
        self.assertEqual("X", result)

        board_noone_wins = [["X", "",  "X"],
                            ["O", "X", "O"],
                            ["O", "O", ""]]

        result = main.check_for_winner(board_noone_wins)
        self.assertEqual(None, result,
                         msg="In this case noone should have won")

        board_O_wins = [["X", "",  "X"],
                        ["O", "X", "O"],
                        ["O", "O", "O"]]

        result = main.check_for_winner(board_O_wins)
        self.assertEqual("O", result)

        board_O_wins_diag = [["X", "",  "O"],
                             ["O", "O", "O"],
                             ["O", "O", ""]]

        result = main.check_for_winner(board_O_wins_diag)
        self.assertEqual("O", result)

        board_X_wins_vert = [["X", "X", ""],
                             ["O", "X", "O"],
                             ["O", "X", ""]]

        result = main.check_for_winner(board_X_wins_vert)
        self.assertEqual("X", result)


    def test_check_for_gameover(self):
      """Calls check_for_winner when the board is full"""
      board_game_over = [["X", "X", "O"],
                         ["O", "X", "X"],
                         ["X", "O", "O"]]
      result = main.check_for_winner(board_game_over)
      self.assertEqual("N", result)


    def test_cpu_choice(self):
      # TODO(ahmed): Refactor your code so that
      # the computer's choice comes from a function
      # instead of being inside the main loop.
      # Add a simple test for it.
      pass


    def test_player_choice(self):
      # TODO(ahmed): Refactor your code so that
      # the human's choice comes from a function.
      pass


    def test_CpuBetterStrategy_finds_winning_move_row(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = board.board
      myboard[0][0] = "X"
      myboard[0][1] = "X"
      self.assertEqual(3, strategy.check_for_winning_move("X"))
      self.assertEqual(None, strategy.check_for_winning_move("O"))

    def test_CpuBetterStrategy_finds_winning_move_col(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = board.board
      myboard[0][1] = "O"
      myboard[2][1] = "O"
      self.assertEqual(None, strategy.check_for_winning_move("X"))
      self.assertEqual(5, strategy.check_for_winning_move("O"))

    def test_CpuBetterStrategy_no_winning_move_col(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = board.board
      myboard[0][1] = "O"
      self.assertEqual(None, strategy.check_for_winning_move("X"))
      self.assertEqual(None, strategy.check_for_winning_move("O"))

    def test_CpuBetterStrategy_blocked_winning_move_row(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = board.board
      myboard[0][0] = "X"
      myboard[0][1] = "X"
      myboard[0][2] = "O"
      self.assertEqual(None, strategy.check_for_winning_move("X"))
      self.assertEqual(None, strategy.check_for_winning_move("O"))

    def test_CpuBetterStrategy_blocked_winning_move_col(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = board.board
      myboard[0][1] = "O"
      myboard[1][1] = "X"
      myboard[2][1] = "O"
      self.assertEqual(None, strategy.check_for_winning_move("X"))
      self.assertEqual(None, strategy.check_for_winning_move("O"))

    def test_CpuBetterStrategy_finds_winning_move_diag1(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = board.board
      myboard[0][0] = "O"
      myboard[2][2] = "O"
      self.assertEqual(None, strategy.check_for_winning_move("X"))
      self.assertEqual(5, strategy.check_for_winning_move("O"))

    def test_CpuBetterStrategy_finds_winning_move_diag2(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = board.board
      myboard[0][2] = "X"
      myboard[1][1] = "X"
      self.assertEqual(7, strategy.check_for_winning_move("X"))
      self.assertEqual(None, strategy.check_for_winning_move("O"))

    def test_CpuBetterStrategy_blocked_winning_move_diag2(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = board.board
      myboard[0][2] = "X"
      myboard[1][1] = "X"
      myboard[2][0] = "O"
      self.assertEqual(None, strategy.check_for_winning_move("X"))
      self.assertEqual(None, strategy.check_for_winning_move("O"))

    def test_CpuBetterStrategy_plays_winning_move(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = board.board
      myboard[0][0] = "O"
      # This should already be true: myboard[1][1] = 5
      myboard[2][2] = "O"
      self.assertEqual(5, myboard[1][1])
      strategy.make_turn()
      self.assertEqual("O", myboard[1][1])

    def test_CpuBetterStrategy_plays_blocking_move(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = board.board
      myboard[0][0] = "X"
      myboard[0][1] = "X"
      # This should already be true: myboard[0][2] = 3

      self.assertEqual(3, myboard[0][2])
      strategy.make_turn()
      self.assertEqual("O", myboard[0][2])



#

if __name__ == '__main__':
    u.main()
