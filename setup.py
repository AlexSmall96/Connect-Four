def print_title():
    print('               ▄▀▀▀▀'+'\033[1;31m'+'    ▄▀▀▀▄'+'\033[0;0m'+'    ██   █    ██   █   █▀▀▀▀▀    ▄▀▀▀▀   ▀▀▀█▀▀▀')                 
    print('              █'+'\033[1;31m'+'        █     █'+'\033[0;0m'+'   █ █  █    █ █  █   █▄▄▄▄▄   █           █  ')                 
    print('              █'+'\033[1;31m'+'        █     █'+'\033[0;0m'+'   █  █ █    █  █ █   █        █           █   ')                
    print('               ▀▄▄▄▄'+'\033[1;31m'+'    ▀▄▄▄▀'+'\033[0;0m'+'    █   ██    █   ██   █▄▄▄▄▄    ▀▄▄▄▄      █   ')                
    print('\n')
    print('█▀▀▀█')
    print('█▄▄▄█')
    print('█▀▄')
    print('█  ▀▄ ')
                         
def print_weclome():
    print('Welcome to the classic game Connect Four!')   


def print_instructions():
    print("""
Welcome to the classic game Connect Four!

Instructions:

When ready, select the number of players, enter your username(s)
and choose your colour(s) to begin the game!

The aim of the game is to take it in turns to drop counters into
the play area, with the winner being the first to have 4 counters
of their colour next to eachother.
A win can be a vertical, horizontal or diagonal streak of counters.

To play the game, each turn select the columnn you want to add a
counter to, and add the corresponding column number in the input section. 
This will automatically drop a counter to the highest space in the column.

At the end of the game, press Y or Yes to play again, 
or N or No to exit.
Good Luck!""")