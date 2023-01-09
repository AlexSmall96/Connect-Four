import os
import time

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
            print('_________________________')
            for row in self.data:
                display_row=''
                for entry in row:
                    if entry == '.':
                        display_row +=' '+ entry + ' '
                    else:
                        display_row +=' '+ counters[entry] +' '   
                display_row='| ' + display_row + ' |'
                print(display_row)
            print('_________________________')
            print('   0  1  2  3  4  5  6  ')  

    def update_data(self,color):
        """
        Updates the board data based on user input
        """
        counter_added=False
        column = input(counters[color] + ' Choose a Column (0-6) ')
        if column.isnumeric():
            column=int(column)
            if column >=0 and column <=6:
                if self.highest_counter[column] > 0:
                    self.highest_counter[column] -=1 
                    self.data[self.highest_counter[column]][column] = color
                    counter_added=True
                else:
                    print(' Column ' + str(column) +' Full. Choose another column. ')
            else:
                print('Please choose a whole number between 0 and 6.')
        else:
            print('Please choose a whole number between 0 and 6.')
        return column, counter_added
        

    def check_winner(self,column,color):
        """
        Checks the most recent counter played for any 4 surrounding it
        """
        if column <=3:
            if [self.data[self.highest_counter[column]][column+i] for i in range(4)]==[color for i in range(4)]:
                self.running=False
                
        else:
            if [self.data[self.highest_counter[column]][column-i] for i in range(4)]==[color for i in range(4)]:
                self.running=False
        
        if self.highest_counter[column]<=2:
            if [self.data[self.highest_counter[column]+i][column] for i in range(4)]==[color for i in range(4)]:
                self.running=False
        else:
            if [self.data[self.highest_counter[column]-i][column] for i in range(4)]==[color for i in range(4)]:
                self.running=False

        if column <=3 and self.highest_counter[column]<=2:
            if [self.data[self.highest_counter[column]+i][column+i] for i in range(4)]==[color for i in range(4)]:
                self.running=False
        elif column <=3:
            if [self.data[self.highest_counter[column]-i][column+i] for i in range(4)]==[color for i in range(4)]:
                self.running=False
        elif self.highest_counter[column]<=2:
            if [self.data[self.highest_counter[column]+i][column-i] for i in range(4)]==[color for i in range(4)]:
                self.running=False
        else:
             if [self.data[self.highest_counter[column]-i][column-i] for i in range(4)]==[color for i in range(4)]:
                self.running=False
        return self.running