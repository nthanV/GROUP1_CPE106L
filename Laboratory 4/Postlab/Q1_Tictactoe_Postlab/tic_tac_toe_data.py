'''tic_tac_toe_data.py: Data module for a tic-tac-toe game. 
   It saves and restores a game board. The functions are:
        save_game(game) -> None
        restore_game() -> game
   Note that no limits are placed on the size of the data.
   The game implementation is responsible for validating
   all data in and out.'''

import os.path

class GameDataHandler:
    def __init__(self):
        self.game_file = "tic_tac_toe_game.dat"

    def _get_path(self):
        try:
            game_path = os.environ['HOMEPATH'] or os.environ['HOME']
            if not os.path.exists(game_path):
                game_path = os.getcwd()
        except (KeyError, TypeError):
            game_path = os.getcwd()
        return game_path

    def save_game(self, game):
        path = os.path.join(self._get_path(), self.game_file)
        try:
            with open(path, 'w') as game_file:
                game_str = ''.join(game)
                game_file.write(game_str)
        except FileNotFoundError:
            print("Failed to save file")

    def restore_game(self):
        path = os.path.join(self._get_path(), self.game_file)
        with open(path) as game_file:
            game_str = game_file.read()
            return list(game_str)

if __name__ == "__main__":
    handler = GameDataHandler()
    print("Path = ", handler._get_path())
    handler.save_game(list("XO XO XO "))
    print(handler.restore_game())
