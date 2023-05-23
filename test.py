"""
These are the tests for Tic Tac Toe
"""


import unittest as u

import board
import main


class BasicFunctionTests(u.TestCase):
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
        board.modifyArray(3, "X")
        self.assertEqual(board.Board[0][2], "X", "First row, 3 element should be X")

        board.modifyArray(8, "O")
        self.assertEqual(board.Board[2][1], "O", "Last row, 2nd element should be O")
        
   
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



        





if __name__ == '__main__':
    u.main()
