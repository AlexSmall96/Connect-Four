import os
import time
class Board:
    def __init__(self,data):
        """
        Creates an instance of Board
        """
        Board.data=data
        Board.highest_counter={i:6 for i in range(7)}

    def display(self):
            """
            Prints the game board in its current state to the terminal
            """
            os.system('cls||clear')
            print('-------------------------')
            for row in Board.data:
                display_row=''
                for entry in row:
                    if entry == 'red':
                        display_row +=' '+ '\033[2;31m' + 'o' + '\033[0;0m' ' '
                    elif entry == 'blue':
                        display_row +=' '+ '\033[2;34m' + 'o' + '\033[0;0m' ' '
                    else:
                        display_row +=' '+ entry + ' '
                display_row='| ' + display_row + ' |'
                print(display_row)
            print('-------------------------')  

    def update_data(self,color):
        """
        Updates the board data based on user input
        """
        column = int(input('Choose Column '))
        if Board.highest_counter[column] == 0:
            column = int(input('Column Full. Choose Another Column  '))
        else: 
            Board.highest_counter[column] -=1 
            Board.data[Board.highest_counter[column]][column] = color
        return column

    def check_winner(self,column,color):
        if column <=3:
            if [Board.data[Board.highest_counter[column]][column+i] for i in range(4)]==[color for i in range(4)]:
                print(color,'won')
        else:
            if [Board.data[Board.highest_counter[column]][column-i] for i in range(4)]==[color for i in range(4)]:
                print(color,'won')
        
        if Board.highest_counter[column]<=2:
            if [Board.data[Board.highest_counter[column]+i][column] for i in range(4)]==[color for i in range(4)]:
                print(color,'won')
        else:
            if [Board.data[Board.highest_counter[column]-i][column] for i in range(4)]==[color for i in range(4)]:
                print(color,'won')

            
                