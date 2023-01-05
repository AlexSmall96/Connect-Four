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
max_rows={i:5 for i in range(7)}
print_board(board_data)


for i in range(10):
    column = int(input('Choose Column '))
    if max_rows[column] == -1:
        column = int(input('Column Full. Choose Another Column  '))
    else:  
        if i % 2 == 1:
            board_data[max_rows[column]][column] = 'red'
        else:
            board_data[max_rows[column]][column] = 'blue'
        print_board(board_data)
        max_rows[column] -=1
    

