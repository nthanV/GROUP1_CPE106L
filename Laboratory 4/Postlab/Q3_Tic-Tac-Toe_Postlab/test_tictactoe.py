from unittest import TestCase, mock
import unittest
import oxo_ui

class TestTicTacToe(TestCase):

    @mock.patch('builtins.input', side_effect=['1'])  
    def test_user_move_valid(self, mock_input):
        
        oxo_ui.executeChoice(1)

    @mock.patch('builtins.input', side_effect=['invalid', '1'])  
    def test_user_move_invalid(self, mock_input):
        
        oxo_ui.executeChoice(1)

if __name__ == '__main__':
    unittest.main()
