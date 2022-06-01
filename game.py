# Create the TicTacToe game
from player import HumanPlayer, RandomComputerPlayer
import time


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # using a single list for 3x3 board
        self.current_winner = None

    def print_board(self):
        # prints the board
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + " |")

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 3 ect (tells us what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + " |")

    def available_spaces(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return len(self.available_spaces())

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return True. if invalid return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row. Need to check everywhere
        if self.board[0:3] == [letter] * 3 or self.board[3:6] == [letter] * 3 or self.board[6:9] == [letter] * 3 or \
                self.board[0:9:3] == [letter] * 3 or self.board[1:9:3] == [letter] * 3 or  \
                self.board[2:9:3] == [letter] * 3 or self.board[0:9:4] == [letter] * 3 or \
                self.board[2:7:2] == [letter] * 3:
            return True
        return False




def play(game, x_player, o_player, print_game=True):

    letter = 'X' # starting letter

    # iterate while the game still has empty squares
    # we don't have to worry about winner because we'll just return that
    # which breaks the loop
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # let's define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # print empty line

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                    return letter

            # after we make our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(2)



    print("It's a tie.")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
