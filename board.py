import os
import random

counters = {}
counters['red'] = '\033[1;31m' + '●' + '\033[0;0m'
counters['yellow'] = '\033[1;33m' + '●' + '\033[0;0m'


class Board:
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
        os.system('cls||clear')
        print('\n')
        print('\n')
        print('                      ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
        for row in self.data:
            display_row = ''
            for entry in row:
                if entry == '.':
                    display_row += ' ' + entry + ' '
                else:
                    display_row += ' ' + counters[entry] + ' '
            display_row = '                     ▮ ' + display_row + ' ▮'
            print(display_row)
        print('                      ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
        print('                        0  1  2  3  4  5  6  ')
        print('\n')

    def update_data_human(self, color, user):
        """
        Updates the board data based on user input
        """
        counter_added = False
        column = input(f"{user} {counters[color]} Choose a Column (0-6) ")
        if column.isnumeric():
            column = int(column)
            if column >= 0 and column <= 6:
                if self.highest_counter[column] > 0:
                    self.highest_counter[column] -= 1
                    self.data[self.highest_counter[column]][column] = color
                    counter_added = True
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
        row = self.highest_counter[col]
        color_streak = [color for i in range(4)]
        # horizontal left side of board
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
   
        # horizontal right side of board
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

        # vertical
        if self.running:
            if self.highest_counter[col] <= 2:
                rnge = [self.data[row+i][col] for i in range(4)]
                if rnge == color_streak:
                    self.running = False

        # diagonal upwards left to right
        # last counter in 1st position
        if self.running:
            if col <= 3 and row >= 3:
                rnge = [self.data[row-i][col+i] for i in range(4)]
                if rnge == color_streak:
                    self.running = False
     
        # last counter in 2nd position
        if self.running:
            if col >= 1 and col <= 4 and row >= 2 and row <= 4:
                rnge = [self.data[row+1-i][col-1+i] for i in range(4)]
                if rnge == color_streak:
                    self.running = False
     
        # last counter in 3rd position
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

        # diagonal downards left to right
        # last counter in 4th position
        if self.running:
            if col >= 3 and row >= 3:
                rnge = [self.data[row-i][col-i] for i in range(4)]
                if rnge == color_streak:
                    self.running = False

        # last counter in 3rd position
        if self.running:
            if col >= 2 and col <= 5 and row >= 2 and row <= 4:
                rnge = [self.data[row+1-i][col+1-i] for i in range(4)]  
                if rnge == color_streak:
                    self.running = False
    
        # last counter in 2nd position
        if self.running:
            if col >= 1 and col <= 4 and row >= 1 and row <= 3:
                rnge = [self.data[row+2-i][col+2-i] for i in range(4)]
                if rnge == color_streak:
                    self.running = False
       
        # last counter in 1st position
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
        # First check if computer is about to win
        for col in range(7):
            color = user_colors[usernames[1]]
            if self.highest_counter[col] > 0:
                self.highest_counter[col] -= 1
                self.data[self.highest_counter[col]][col] = color
                pot_win_detected = not self.check_winner(col, color)
                self.running = True
                # undo update of data
                self.data[self.highest_counter[col]][col] = '.'
                self.highest_counter[col] += 1
                if pot_win_detected:
                    best_column = col
                    break
                else:
                    # Check if human is about to win
                    color = user_colors[usernames[0]]
                    if self.highest_counter[col] > 0:
                        self.highest_counter[col] -= 1
                        self.data[self.highest_counter[col]][col] = color
                        win_prevented = not self.check_winner(col, color)
                        self.running = True
                        # undo update of data
                        self.data[self.highest_counter[col]][col] = '.'
                        self.highest_counter[col] += 1
                        if win_prevented:
                            best_column = col
                            break
                        else:
                            best_column = random.randint(0, 6)
        return best_column
            
    def update_data_computer(self, color, user_colors, usernames):
        """
        Updates the board data based on user input
        """
        counter_added = False
        column = self.choose_column(user_colors, usernames)
        if self.highest_counter[column] > 0:
            self.highest_counter[column] -= 1
            self.data[self.highest_counter[column]][column] = color
            counter_added = True
        return column, counter_added