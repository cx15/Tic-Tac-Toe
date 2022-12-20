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
        

if __name__ == '__main__':
    u.main()
