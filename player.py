import math
import random


class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_spaces())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        game.print_board_nums()

        while not valid_square:
            square = input(self.letter + "'s turn. Choose a square using (0-8): ")

            try:
                val = int(square)
                if val not in game.available_spaces():
                    raise ValueError
                valid_square = True

            except ValueError:
                print("Invalid square. Please try again.")

        return val
