import random
from tic_tac_toe_data import GameDataHandler

class TicTacToeGame:
    def __init__(self):
        self.board = list(" " * 9)
        self.data_handler = GameDataHandler()

    def save(self):
        self.data_handler.save_game(self.board)

    def restore(self):
        try:
            self.board = self.data_handler.restore_game()
            if len(self.board) != 9:
                self.board = list(" " * 9)
            return self.board
        except IOError:
            self.board = list(" " * 9)
            return self.board

    def _generate_move(self):
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        if options:
            return random.choice(options)
        else:
            return -1

    def _is_winning_move(self):
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))
        game = self.board
        for a, b, c in wins:
            chars = game[a] + game[b] + game[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def user_move(self, cell):
        if self.board[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            self.board[cell] = 'X'
        if self._is_winning_move():
            return 'X'
        else:
            return ""

    def computer_move(self):
        cell = self._generate_move()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        if self._is_winning_move():
            return 'O'
        else:
            return ""

def play_game():
    result = ""
    game = TicTacToeGame()
    while not result:
        print(game.board)
        try:
            result = game.user_move(game._generate_move())
        except ValueError:
            print("Oops, that shouldn't happen")
        if not result:
            result = game.computer_move()
            
        if not result:
            continue
        elif result == 'D':
            print("It's a draw")
        else:
            print("Winner is:", result)
        print(game.board)

if __name__ == "__main__":
    play_game()
