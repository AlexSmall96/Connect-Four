"""
Contains the class Board and counters,
to allow the game to be played and visualised
"""

# Import to os to allow the terminal to be cleared
import os

# Import random for the case when computer
# column choice is random
import random

# Create dictionary to map color to visual counter
# The counter symbols were inspired by
# https://www.alt-codes.net
counters = {}
counters['red'] = '\033[1;31m' + '●' + '\033[0;0m'
counters['yellow'] = '\033[1;33m' + '●' + '\033[0;0m'


class Board:
    """
    Contains data to represent the game,
    along with methods to display the game board
    and update it with players moves
    """
    def __init__(self, data):
        """
        Creates an instance of Board
        """
        self.data = data
        self.highest_counter = {i: 6 for i in range(7)}
        self.running = True

    def display(self):
        """
        Prints the game board in its current state to the terminal
        """
        # Clear terminal - the code used to clear the terminal was taken from
        # https://stackoverflow.com/questions/44565704/how-to-clear-only-last-one-line-in-python-output-console
        os.system('cls||clear')
        # Print board outline
        print('\n')
        print('\n')
        print('                      ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
        # Print game data
        for row in self.data:
            display_row = ''
            for entry in row:
                if entry == '.':
                    display_row += ' ' + entry + ' '
                else:
                    display_row += ' ' + counters[entry] + ' '
            display_row = '                     ▮ ' + display_row + ' ▮'
            print(display_row)
        # Print board outline
        print('                      ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
        # Column guides
        print('                        0  1  2  3  4  5  6  ')
        print('\n')

    def update_data_human(self, color, user):
        """
        Updates the board data based on user input
        """
        # Variable to indicate wether input is valid
        counter_added = False
        # Input message to user
        column = input(f"{user} {counters[color]} Choose a Column (0-6) ")
        # Validate input
        if column.isnumeric():
            column = int(column)
            if column >= 0 and column <= 6:
                if self.highest_counter[column] > 0:
                    self.highest_counter[column] -= 1
                    self.data[self.highest_counter[column]][column] = color
                    # Validation passed so set varibale to True
                    counter_added = True
                # Retry input
                else:
                    print(f"Column {str(column)} Full. Choose Another.")
            else:
                print('Please choose a whole number between 0 and 6.')
        else:
            print('Please choose a whole number between 0 and 6.')
        return column, counter_added

    def check_winner(self, col, color):
        """
        Checks the most recent counter played for any 4 surrounding it
        """
        # Identify the row that counter was added to
        row = self.highest_counter[col]
        # Create list containing current players color x 4
        color_streak = [color for i in range(4)]
        # Check all cases for streak of 4 depending on col and row range
        # Horizontal left side of board
        if self.running:
            if col <= 3:
                rnge = [self.data[row][col+i] for i in range(4)]
                if rnge == color_streak:
                    self.running = False
                elif col >= 1:
                    rnge = [self.data[row][col-1+i] for i in range(4)]
                    if rnge == color_streak:
                        self.running = False
                    elif col >= 2:
                        rnge = [self.data[row][col-2+i] for i in range(4)]
                        if rnge == color_streak:
                            self.running = False
                        elif col == 3:
                            rnge = [self.data[row][col-3+i] for i in range(4)]
                            if rnge == color_streak:
                                self.running = False

        # Horizontal right side of board
        if self.running:
            if col >= 3:
                rnge = [self.data[row][col-i] for i in range(4)]
                if rnge == color_streak:
                    self.running = False
                elif col <= 5:
                    rnge = [self.data[row][col+1-i] for i in range(4)]
                    if rnge == color_streak:
                        self.running = False
                    elif col <= 4:
                        rnge = [self.data[row][col+2-i] for i in range(4)]
                        if rnge == color_streak:
                            self.running = False
                        elif col == 3:
                            rnge = [self.data[row][col+3-i] for i in range(4)]
                            if rnge == color_streak:
                                self.running = False

        # Vertical
        if self.running:
            if self.highest_counter[col] <= 2:
                rnge = [self.data[row+i][col] for i in range(4)]
                if rnge == color_streak:
                    self.running = False

        # Diagonal upwards left to right
        # Last counter in 1st position
        if self.running:
            if col <= 3 and row >= 3:
                rnge = [self.data[row-i][col+i] for i in range(4)]
                if rnge == color_streak:
                    self.running = False

        # Last counter in 2nd position
        if self.running:
            if col >= 1 and col <= 4 and row >= 2 and row <= 4:
                rnge = [self.data[row+1-i][col-1+i] for i in range(4)]
                if rnge == color_streak:
                    self.running = False

        # Last counter in 3rd position
        if self.running:
            if col >= 2 and col <= 5 and row >= 1 and row <= 3:
                rnge = [self.data[row+2-i][col-2+i] for i in range(4)]
                if rnge == color_streak:
                    self.running = False

        # last counter in 4th position
        if self.running:
            if col >= 3 and row <= 2:
                rnge = [self.data[row+3-i][col-3+i] for i in range(4)]
                if rnge == color_streak:
                    self.running = False

        # Diagonal downards left to right
        # Last counter in 4th position
        if self.running:
            if col >= 3 and row >= 3:
                rnge = [self.data[row-i][col-i] for i in range(4)]
                if rnge == color_streak:
                    self.running = False

        # Last counter in 3rd position
        if self.running:
            if col >= 2 and col <= 5 and row >= 2 and row <= 4:
                rnge = [self.data[row+1-i][col+1-i] for i in range(4)]
                if rnge == color_streak:
                    self.running = False

        # Last counter in 2nd position
        if self.running:
            if col >= 1 and col <= 4 and row >= 1 and row <= 3:
                rnge = [self.data[row+2-i][col+2-i] for i in range(4)]
                if rnge == color_streak:
                    self.running = False

        # Last counter in 1st position
        if self.running:
            if col <= 3 and row <= 2:
                rnge = [self.data[row+3-i][col+3-i] for i in range(4)]
                if rnge == color_streak:
                    self.running = False

        return self.running

    def choose_column(self, user_colors, usernames):
        """
        Uses the current board state to pick the best column
        when computer is playing
        """
        # Scan columns to check if computer or human can play a winning move,
        # by calling check_winner function
        for col in range(7):
            color = user_colors[usernames[1]]
            if self.highest_counter[col] > 0:
                self.highest_counter[col] -= 1
                self.data[self.highest_counter[col]][col] = color
                pot_win_detected = not self.check_winner(col, color)
                self.running = True
                # Undo update of data to reset game to current state
                self.data[self.highest_counter[col]][col] = '.'
                self.highest_counter[col] += 1
                # If selecting column results in computer win, choose column
                if pot_win_detected:
                    best_column = col
                    break
                else:
                    # If no computer win detected,
                    # check if human win can be blocked
                    color = user_colors[usernames[0]]
                    if self.highest_counter[col] > 0:
                        self.highest_counter[col] -= 1
                        self.data[self.highest_counter[col]][col] = color
                        win_prevented = not self.check_winner(col, color)
                        self.running = True
                        # Undo update of data to reset game to current state
                        self.data[self.highest_counter[col]][col] = '.'
                        self.highest_counter[col] += 1
                        # If selecting column blocks a human win, choose column
                        if win_prevented:
                            best_column = col
                            break
                        else:
                            # If neither win is detected,
                            # make column choice random
                            best_column = random.randint(0, 6)
        return best_column

    def update_data_computer(self, color, user_colors, usernames):
        """
        Updates the board data based on user input
        """
        # Variable to indicate wether input is valid
        counter_added = False
        # Call choose_column function
        column = self.choose_column(user_colors, usernames)
        # Validate input
        if self.highest_counter[column] > 0:
            self.highest_counter[column] -= 1
            self.data[self.highest_counter[column]][column] = color
            # Validation passed so set varibale to True
            counter_added = True
        return column, counter_added
