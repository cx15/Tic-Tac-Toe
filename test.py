"""
These are the tests for Tic Tac Toe
"""


import unittest as u

import board
import display
import main
import strategies


class BasicFunctionTests(u.TestCase):
    def setUp(self) -> None:
      # Reset the board between tests
      # TODO Remove this once board has been refactored
      self.test_board = board.Board()


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
        self.assertEqual(golden_board, display.board_representation(self.test_board))

    def test_modify_board(self):
        self.test_board.modify_board(3, "X")
        self.assertEqual(self.test_board.get_symbol(0, 2), "X", "First row, 3 element should be X")

        self.test_board.modify_board(8, "O")
        self.assertEqual(self.test_board.get_symbol(2, 1), "O", "Last row, 2nd element should be O")
        
   
    def test_check_for_winner(self):
        board_x_wins = board.Board([["X", "X", "X"],
                        ["O", "X", "O"],
                        ["O", "O", ""]])

        result = board_x_wins.check_for_winner()
        # Returns "X", "O" or "N"
        self.assertEqual("X", result)

        result = board_x_wins.check_for_winner()
        self.assertEqual("X", result)

        board_noone_wins = board.Board(
                           [["X", "",  "X"],
                            ["O", "X", "O"],
                            ["O", "O", ""]])

        result = board_noone_wins.check_for_winner()
        self.assertEqual(None, result,
                         msg="In this case noone should have won")

        board_O_wins = board.Board(
                       [["X", "",  "X"],
                        ["O", "X", "O"],
                        ["O", "O", "O"]])

        result = board_O_wins.check_for_winner()
        self.assertEqual("O", result)

        board_O_wins_diag = board.Board(
                            [["X", "",  "O"],
                             ["O", "O", "O"],
                             ["O", "O", ""]])

        result = board_O_wins_diag.check_for_winner()
        self.assertEqual("O", result)

        board_X_wins_vert = board.Board(
                            [["X", "X", ""],
                             ["O", "X", "O"],
                             ["O", "X", ""]])

        result = board_X_wins_vert.check_for_winner()
        self.assertEqual("X", result)


    def test_check_for_gameover(self):
      """Calls check_for_winner when the board is full"""
      board_game_over = board.Board(initial_data =
                        [["X", "X", "O"],
                         ["O", "X", "X"],
                         ["X", "O", "O"]])

      result = board_game_over.check_for_winner()
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
      myboard = self.test_board
      myboard.modify_board(1, "X")
      myboard.modify_board(2, "X")
      self.assertEqual(3, strategy.check_for_winning_move(self.test_board, "X"))
      self.assertEqual(None, strategy.check_for_winning_move(self.test_board, "O"))

    #
    #  Some additional notes to explain what we're changing.
    #  We have a file called board.py
    #  Before we started making changed that contained as array
    #  called board (actually it was an array of arrays:
    #     board = [[1, 2, 3], ....
    #  When you see "board.board" in the older code...it's
    #  referring to that array.  The first "board" means the file
    # board.py.  The second means the variable board that lives in that file.
    #
    # Now...when we refactored the code we removed that variable...
    # .... so any references to board.board won't work any more and will
    # cause an error.
    #
    # Instead...we created a class called Board.
    # When we refer to board.Board (like on line 17 above) that's
    # what we mean.  Again...the first board means "the file board.py"
    # and the second Board means "the class called Board".
    # To complicate things....we introduced a 'member variable' to the class Board
    # and also called *it* board.  It's the array that we had earlier...
    # but we moved it inside the class.  When we have an *instance* of that class
    # like my_board = Board()
    # then we can refer to the member variable inside it as
    # my_board.board
    #
    # So in most cases in the tests...when we used to say board.board
    # (meaning the variable board that lives in the board.py file)
    # we instead need to say
    # self.test_board.board
    # (meaning, the variable test_board, which set to be an instance
    # of the class board.Board on line 17, and the 'board' variable inside
    # of that.
    # Phew.

    def test_CpuBetterStrategy_finds_winning_move_col(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = self.test_board
      myboard.modify_board(2, "O")
      myboard.modify_board(5, "O")
      self.assertEqual(None, strategy.check_for_winning_move(myboard, "X"))
      self.assertEqual(8, strategy.check_for_winning_move(myboard, "O"))

    def test_CpuBetterStrategy_no_winning_move_col(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = self.test_board
      myboard.modify_board(2,"O")
      self.assertEqual(None, strategy.check_for_winning_move(self.test_board, "X"))
      self.assertEqual(None, strategy.check_for_winning_move(self.test_board, "O"))

    def test_CpuBetterStrategy_blocked_winning_move_row(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = self.test_board
      myboard.modify_board(1, "X")
      myboard.modify_board(2, "X")
      myboard.modify_board(3, "O")
      self.assertEqual(None, strategy.check_for_winning_move(self.test_board, "X"))
      self.assertEqual(None, strategy.check_for_winning_move(self.test_board, "O"))

    def test_CpuBetterStrategy_blocked_winning_move_col(self):
      strategy = strategies.CpuBetterStrategy()
      self.test_board.modify_board(1, "O")
      self.test_board.modify_board(5, "X")
      self.test_board.modify_board(8, "O")

      self.assertEqual(None, strategy.check_for_winning_move(self.test_board, "X"))
      self.assertEqual(None, strategy.check_for_winning_move(self.test_board, "O"))

    def test_CpuBetterStrategy_finds_winning_move_diag1(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = self.test_board
      myboard.modify_board(1, "O")
      myboard.modify_board(9, "O")
      self.assertEqual(None, strategy.check_for_winning_move(self.test_board, "X"))
      self.assertEqual(5, strategy.check_for_winning_move(self.test_board, "O"))

    def test_CpuBetterStrategy_finds_winning_move_diag2(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = self.test_board
      myboard.modify_board(3, "X")
      myboard.modify_board(5, "X")
      self.assertEqual(7, strategy.check_for_winning_move(self.test_board, "X"))
      self.assertEqual(None, strategy.check_for_winning_move(self.test_board, "O"))

    def test_CpuBetterStrategy_blocked_winning_move_diag2(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = self.test_board
      myboard.modify_board(3, "X")
      myboard.modify_board(5, "X")
      myboard.modify_board(7, "O")
      self.assertEqual(None, strategy.check_for_winning_move(self.test_board, "X"))
      self.assertEqual(None, strategy.check_for_winning_move(self.test_board, "O"))

    def test_CpuBetterStrategy_plays_winning_move(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = self.test_board
      myboard.modify_board(1, "O")
      # This should already be true: myboard[1][1] = 5
      myboard.modify_board(9, "O")
      self.assertEqual(5, myboard.get_symbol(1, 1))
      strategy.make_turn(myboard, "O")
      self.assertEqual("O", myboard.get_symbol(1, 1))

    def test_CpuBetterStrategy_plays_blocking_move(self):
      strategy = strategies.CpuBetterStrategy()
      myboard = self.test_board
      myboard.modify_board(1, "X")
      myboard.modify_board(2, "X")
      # This should already be true: myboard[0][2] = 3

      self.assertEqual(3, myboard.get_symbol(0, 2))
      strategy.make_turn(myboard, "O")
      self.assertEqual("O", myboard.get_symbol(0, 2))



#

if __name__ == '__main__':
    u.main()
