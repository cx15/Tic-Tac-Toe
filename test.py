import unittest as u

import main


class BasicFunctionTests(u.TestCase):
    def test_is_true(self):
        self.assertTrue(True, "Yup, true is true")

    def test_modify_array(self):
        main.modifyArray(3, "X")
        self.assertEqual(main.Board[0][2], "X", "First row, 3 element should be X")

        main.modifyArray(8, "O")
        self.assertEqual(main.Board[2][1], "O", "Last row, 2nd element should be O")
        
   
    def test_check_for_winner(self):
      # TODO: write a test to confirm this function does what you expect
        board_x_wins = [["X", "X", "X"],
                        ["O", "X", "O"],
                        ["O", "O", ""]]

        result =  main.checkForWinner(board_x_wins)
        # Returns "X", "O" or "N"
        self.assertEqual("X", result)

        board_noone_wins = [["X", "",  "X"],
                            ["O", "X", "O"],
                            ["O", "O", ""]]

        result = main.checkForWinner(board_noone_wins)
        # Returns "X", "O" or "N"
        self.assertEqual("N", result)





if __name__ == '__main__':
    u.main()
