import os
import time
import random

counters={'red':'\033[1;31m' + '●' + '\033[0;0m','yellow':'\033[1;33m' + '●' + '\033[0;0m'}

class Board:
    def __init__(self,data):
        """
        Creates an instance of Board
        """
        self.data=data
        self.highest_counter={i:6 for i in range(7)}
        self.running=True
    def display(self):
            """
            Prints the game board in its current state to the terminal
            """
            os.system('cls||clear')
            print('\n')
            print('\n')
            print('                      ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
            for row in self.data:
                display_row=''
                for entry in row:
                    if entry == '.':
                        display_row +=' '+ entry + ' '
                    else:
                        display_row +=' '+ counters[entry] +' '   
                display_row='                     ▮ ' + display_row + ' ▮'
                print(display_row)
            print('                      ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
            print('                        0  1  2  3  4  5  6  ') 
            print('\n')

    def update_data_human(self,color,user):
        """
        Updates the board data based on user input
        """
        counter_added=False
        column = input('                     '+user + ' ' + counters[color] + ' Choose a Column (0-6) ')
        if column.isnumeric():
            column=int(column)
            if column >=0 and column <=6:
                if self.highest_counter[column] > 0:
                    self.highest_counter[column] -=1 
                    self.data[self.highest_counter[column]][column] = color
                    counter_added=True
                else:
                    print('                     Column ' + str(column) +' Full. Choose another column. ')
            else:
                print('                    Please choose a whole number between 0 and 6.')
        else:
            print('                    Please choose a whole number between 0 and 6.')
        return column, counter_added

    def check_winner(self,column,color):
        """
        Checks the most recent counter played for any 4 surrounding it
        """
        #horizontal left to right
        if column <=3:
            if [self.data[self.highest_counter[column]][column+i] for i in range(4)]==[color for i in range(4)]:
                self.running=False
        #horizontal right to left
        if column >= 3:
            if [self.data[self.highest_counter[column]][column-i] for i in range(4)]==[color for i in range(4)]:
                self.running=False
        #vertical up to down
        if self.highest_counter[column]<=2:
            if [self.data[self.highest_counter[column]+i][column] for i in range(4)]==[color for i in range(4)]:
                self.running=False
        #vertical down to up
        if self.highest_counter[column]>=2:
            if [self.data[self.highest_counter[column]-i][column] for i in range(4)]==[color for i in range(4)]:
                self.running=False
        #diagonal
        if column <=3 and self.highest_counter[column]<=2:
            if [self.data[self.highest_counter[column]+i][column+i] for i in range(4)]==[color for i in range(4)]:
                self.running=False
        if column <=3 and self.highest_counter[column]>=2:
            if [self.data[self.highest_counter[column]-i][column+i] for i in range(4)]==[color for i in range(4)]:
                self.running=False
        if column >=3 and self.highest_counter[column]<=2:
            if [self.data[self.highest_counter[column]+i][column-i] for i in range(4)]==[color for i in range(4)]:
                self.running=False
        if column >=3 and self.highest_counter[column]>=2:
             if [self.data[self.highest_counter[column]-i][column-i] for i in range(4)]==[color for i in range(4)]:
                self.running=False
        return self.running

    def choose_column(self,user_colors,usernames):
        """
        Uses the current board state to pick the best column 
        when computer is playing
        """
        #First check if human is about to win
        for col in range(7):
            if self.highest_counter[col] > 0:
                self.highest_counter[col] -=1 
                self.data[self.highest_counter[col]][col] = user_colors[usernames[0]]
                win_prevented = not self.check_winner(col,user_colors[usernames[0]])
                self.running = True
                #undo update of data
                self.data[self.highest_counter[col]][col] = '.'
                self.highest_counter[col] +=1
                if win_prevented:
                    best_column = col
                    break
                else:
                    if self.highest_counter[col] > 0:
                        self.highest_counter[col] -=1 
                        self.data[self.highest_counter[col]][col] = user_colors[usernames[1]]
                        pot_win_detected = not self.check_winner(col,user_colors[usernames[1]])
                        self.running = True
                        #undo update of data
                        self.data[self.highest_counter[col]][col] = '.'
                        self.highest_counter[col] +=1
                        if pot_win_detected:
                            best_column = col
                            break
                        else:
                            best_column = random.randint(0,6)
        return best_column
                




    

   

    def update_data_computer(self,color,user_colors,usernames):
        """
        Updates the board data based on user input
        """
        counter_added=False
        column = self.choose_column(user_colors,usernames)
        if self.highest_counter[column] > 0:
            self.highest_counter[column] -=1 
            self.data[self.highest_counter[column]][column] = color
            counter_added=True
        return column, counter_added        
    
    

 