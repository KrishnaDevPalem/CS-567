import unittest
from unittest.mock import patch
import tictactoe

class TestTicTacToe(unittest.TestCase):

    def test_winner(self):
        board = [['X', 'O', ' '],
                 ['X', 'O', ' '],
                 ['X', ' ', ' ']]
        self.assertEqual(tictactoe.check_winner(board), 'X')

    def test_tie(self):
        board = [['X', 'O', 'X'],
                 ['X', 'X', 'O'],
                 ['O', 'X', 'O']]
        self.assertTrue(tictactoe.is_board_full(board))

    @patch('builtins.input', side_effect=['0', '0', '1', '1', '2', '2', '0', '1', '2', '0', '1', '2', 'q'])
    def test_gameplay(self, mock_input):
        # Mocking user input for testing gameplay
        with patch('tictactoe.print_board'):  # To avoid actual printing during testing
            with self.assertRaises(SystemExit):  # Ensure the game exits when 'q' is entered
                tictactoe.main()

if __name__ == '__main__':
    unittest.main()
