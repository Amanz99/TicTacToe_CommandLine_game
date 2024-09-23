import unittest
import TTT_Python_command_line_game

class Test_TTT(unittest.TestCase):
    def clearBoard(self):
        global count
        count = 0
        i = 1
        while i < 10:
            Board[i] = " "
            i += 1

    def test_clearBoard(self):
        # Set up initial board state
        global Board
        Board = {
            1: "X", 2: "O", 3: "X",
            4: "O", 5: "X", 6: "O",
            7: "X", 8: "O", 9: "X"
        }
        global count
        count = 9

        # Call the clearBoard() function
        self.clearBoard()

        # Check if board is cleared
        expected_board = {
            1: " ", 2: " ", 3: " ",
            4: " ", 5: " ", 6: " ",
            7: " ", 8: " ", 9: " "
        }
        expected_count = 0
        self.assertEqual(Board, expected_board)
        self.assertEqual(count, expected_count)

if __name__ == "__main__":
    unittest.main()