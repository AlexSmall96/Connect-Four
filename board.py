import os

class Board:
    def __init__(self,data):
        Board.data=data
        Board.max_rows={i:5 for i in range(7)}

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
        if Board.max_rows[column] == -1:
            column = int(input('Column Full. Choose Another Column  '))
        else:  
            Board.data[Board.max_rows[column]][column] = color
        Board.max_rows[column] -=1

