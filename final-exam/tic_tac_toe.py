"""
***************
* Tic Tac Toe *
***************
Creates a TicTacToe object and uses the start() method to being the game.
You play against a computer! Have fun.
"""

from random import randint, choice
import os

BOARD_SIZE = 10
BOARD_WIDTH = 3
POSSIBLE_WIN_COMBOS = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1],
                       [8, 5, 2], [9, 6, 3], [7, 5, 3], [9, 5, 1]]


class Board:
    """Represents a tic tac toe board."""
    def __init__(self, board=None):
        if isinstance(board, list) and len(board) == BOARD_SIZE:
            self.board = board
        else:
            self.board = [' '] * BOARD_SIZE

    def draw_board(self):
        """This function prints out the board that it was passed."""
        vertical_lines = '\n   |   |\n'
        middle_lines = f'{vertical_lines}-----------{vertical_lines}'

        str_board = vertical_lines
        for i in range(1, BOARD_SIZE):
            if i % BOARD_WIDTH > 0:
                str_board += f' {self.board[i]} |'
            elif i % BOARD_WIDTH == 0:
                str_board += f' {self.board[i]}'
                if i < BOARD_SIZE - 1:
                    str_board += middle_lines
        str_board += vertical_lines
        print(str_board)

    def is_space_free(self, move):
        """Return true if the passed move is free on the passed board."""
        return self.board[move] == ' '

    def make_move(self, letter, move):
        """Adds a letter X/O to the board at index 'move'."""
        self.board[move] = letter

    def get_board_copy(self):
        """Make a duplicate of the board and return it the duplicate."""
        return Board(self.board.copy())

    def is_board_full(self):
        """Return True if every space on the board has been taken."""
        for i in range(1, BOARD_SIZE):
            if self.is_space_free(i):
                return False
        return True

    def is_winner(self, letter):
        """Given a player’s letter, returns True if that player has won."""
        for combo in POSSIBLE_WIN_COMBOS:
            if self.board[combo[0]] == self.board[combo[1]] == \
                                self.board[combo[2]] == letter:
                return True
        return False

    def choose_random_move_from_list(self, moves_list):
        """Returns a valid move from the passed list on the passed board.
        Returns None if there is no valid move."""
        possible_moves = []
        for i in moves_list:
            if self.is_space_free(i):
                possible_moves.append(i)

        if possible_moves:
            return choice(possible_moves)
        return None

    def wipe_board(self):
        """Empties the board."""
        self.board = [' '] * BOARD_SIZE


class TicTacToe:
    """Represents a tic tac toe game."""
    def __init__(self):
        self.board = Board()
        self.player_letter = None
        self.computer_letter = None

    @staticmethod
    def print_welcome_banner():
        """Clears the terminal and prints a welcome banner."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print('*****************************')
        print('*  Welcome to Tic Tac Toe!  *')
        print('*****************************')

    @staticmethod
    def who_goes_first():
        """Randomly choose the player who goes first."""
        if randint(0, 1) == 0:
            return 'computer'
        return 'player'

    @staticmethod
    def game_over_message(winner):
        """Prints a message with the results of the game."""
        if winner == 'tie':
            print('* The game is a tie! *')
        elif winner == 'player':
            print('* Hooray! You have won the game! *')
        elif winner == 'computer':
            print('* The computer has beaten you! You lose. *')
        else:
            print('Oops, something went wrong! :(')

    @staticmethod
    def play_again():
        """This function returns True if the player wants to play again,
        otherwise it returns False."""
        print('\n* Do you want to play again? (yes or no) *')
        return input().lower().startswith('y')

    def set_player_letter(self):
        """Lets the player type which letter they want to be."""
        letter = ''
        while letter not in ('X', 'O'):
            print('* Do you want to be X or O? *')
            letter = input().upper()
        if letter == 'X':
            self.player_letter, self.computer_letter = 'X', 'O'
        else:
            self.player_letter, self.computer_letter = 'O', 'X'

    def get_computer_move(self):
        """Given a board and the computer's letter,
        determine where to move and return that move."""

        # First, check if we can win in the next move
        for i in range(1, BOARD_SIZE):
            copy_board_comp_win = self.board.get_board_copy()
            if copy_board_comp_win.is_space_free(i):
                copy_board_comp_win.make_move(self.computer_letter, i)
                if copy_board_comp_win.is_winner(self.computer_letter):
                    return i

        # Check if the player could win on their next move, and block them.
        for i in range(1, BOARD_SIZE):
            copy_board_player_win = self.board.get_board_copy()
            if copy_board_player_win.is_space_free(i):
                copy_board_player_win.make_move(self.player_letter, i)
                if copy_board_player_win.is_winner(self.player_letter):
                    return i

        # Try to take one of the corners, if they are free.
        move = self.board.choose_random_move_from_list([1, 3, 7, 9])
        if move is not None:
            return move

        # Try to take the center, if it is free.
        if self.board.is_space_free(5):
            return 5

        # Move on one of the sides.
        return self.board.choose_random_move_from_list([2, 4, 6, 8])

    def get_player_move(self):
        """Let the player type in their move."""
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or \
                not self.board.is_space_free(int(move)):
            print('* What is your next move? (1-9) *')
            move = input()
        return int(move)

    def game_loop(self, turn):
        """This is the main game loop.
        Returns a string containing the winner."""
        if turn == 'player':
            # Player’s turn.
            self.board.draw_board()
            move = self.get_player_move()
            self.board.make_move(self.player_letter, move)
            self.board.draw_board()

            if self.board.is_winner(self.player_letter):
                return 'player'

            if self.board.is_board_full():
                return 'tie'

            next_turn = 'computer'

        elif turn == 'computer':
            # Computer’s turn.
            move = self.get_computer_move()
            self.board.make_move(self.computer_letter, move)

            if self.board.is_winner(self.computer_letter):
                self.board.draw_board()
                return 'computer'

            if self.board.is_board_full():
                self.board.draw_board()
                return 'tie'

            next_turn = 'player'

        if next_turn:
            return self.game_loop(next_turn)
        # Invalid 'turn' arg was given! Something went wrong.
        return 'error'

    def start(self):
        """Starts the game! Resets the board."""
        TicTacToe.print_welcome_banner()
        self.board.wipe_board()
        self.set_player_letter()
        turn = TicTacToe.who_goes_first()
        print(f'The {turn} will go first.')

        # The main game loop
        winner = self.game_loop(turn)

        # Lets the player know who won or if it was a draw
        TicTacToe.game_over_message(winner)

        # If the player wants to play again, run this fxn again.
        if TicTacToe.play_again():
            self.start()


def play_tic_tac_toe():
    """Starts a game of tic tac toe."""
    ttt = TicTacToe()
    ttt.start()


if __name__ == '__main__':
    play_tic_tac_toe()
