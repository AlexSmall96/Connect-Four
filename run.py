import os
import time

def print_board(board_data):
    """
    Prints the game board in its current state to the terminal
    """
    os.system('cls||clear')
    print('-------------------------')
    for row in board_data:
        board_row=''
        for entry in row:
            if entry == 'red':
                board_row +=' '+ '\033[2;31m' + 'o' + '\033[0;0m' ' '
            elif entry == 'blue':
                board_row +=' '+ '\033[2;34m' + 'o' + '\033[0;0m' ' '
            else:
                board_row +=' '+ entry + ' '
        board_row='| ' + board_row + ' |'
        print(board_row)
    print('-------------------------')  
    

board_data=[['.' for i in range(7)] for j in range(6)]
print_board(board_data)


