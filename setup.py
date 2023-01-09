def print_title():
    print('               ▄▀▀▀▀'+'\033[1;31m'+'    ▄▀▀▀▄'+'\033[0;0m'+'    ██   █    ██   █   █▀▀▀▀▀    ▄▀▀▀▀   ▀▀▀█▀▀▀')                 
    print('              █'+'\033[1;31m'+'        █     █'+'\033[0;0m'+'   █ █  █    █ █  █   █▄▄▄▄▄   █           █  ')                 
    print('              █'+'\033[1;31m'+'        █     █'+'\033[0;0m'+'   █  █ █    █  █ █   █        █           █   ')                
    print('               ▀▄▄▄▄'+'\033[1;31m'+'    ▀▄▄▄▀'+'\033[0;0m'+'    █   ██    █   ██   █▄▄▄▄▄    ▀▄▄▄▄      █   ')                
    print('\n')                                                                                                              
    print('                           █▀▀▀▀▀'+'\033[1;33m'+'    ▄▀▀▀▄'+'\033[0;0m'+'    █     █   █▀▀▀▀▀█  ') 
    print('                           █▄▄▄▄▄'+'\033[1;33m'+'   █     █'+'\033[0;0m'+'   █     █   █     █ ')   
    print('                           █     '+'\033[1;33m'+'   █     █'+'\033[0;0m'+'   █     █   █▀▀▀█▀▀      ')           
    print('                           █     '+'\033[1;33m'+'    ▀▄▄▄▀ '+'\033[0;0m'+'    ▀▄▄▄▀    █    ▀▄   ') 
                             
def print_welcome():
    print('Welcome to the classic game Connect Four!')   


def print_instructions():
    print("""
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

def set_no_players():
    correct_input = False
    while not correct_input:
        no_players = input("""
        Select Number of Players:
        Enter 1 to play human vs computer or 2 to play human vs human 
        """) 
        if no_players.isnumeric():
            if int(no_players) == 1 or int(no_players) ==2:
                return no_players
                correct_input=True
        else:
            print('Please enter either 1 or 2')

    

def set_usernames(no_players):
    if no_players == 1:
        player_1 = input('Player 1 - Please enter your username ')
        return player_1
    else:
        player_1 = input('Player 1 - Please enter your username ')
        player_2 = input('Player 2 - Please enter your username ')
        return player_1, player_2