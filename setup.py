from board import Board
import os
import time



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
            if int(no_players) == 1 or int(no_players) == 2:
                return int(no_players)
                correct_input=True
        else:
            print('Please enter either 1 or 2')

    

def set_usernames(no_players):
    if no_players == 1:
        player_1 = input('Player 1 - Please enter your username ')
        return [player_1]
    else:
        player_1 = input('Player 1 - Please enter your username ')
        player_2 = input('Player 2 - Please enter your username ')
        return [player_1, player_2]

def select_colors(usernames):
    if len(usernames) == 1:
        usernames.append('computer')
    user_colors = {}
    correct_input = False
    while not correct_input: 
        choice = input(f"{usernames[0]} Select a color : Red or Yellow ").lower()
        if choice == 'red':
            user_colors[usernames[0]] = 'red'
            user_colors[usernames[1]] = 'yellow'
            correct_input = True
        elif choice == 'yellow':
            user_colors[usernames[1]] = 'red'
            user_colors[usernames[0]] = 'yellow'
            correct_input = True
    return user_colors
            
        
            
   

def run_game(no_players,usercolors,usernames):
    if no_players == 2:
        play_again=True
        while play_again:
            data=[['.' for i in range(7)] for j in range(6)]
            board=Board(data)
            board.display()
            color='red'
            color_cycle={'red':'yellow','yellow':'red'}
            count=0
            while board.running and count < 42:
                column,counter_added=board.update_data_human(color)
                if counter_added:
                    board.display()
                    board.running=board.check_winner(column,color)
                    count += 1
                    color=color_cycle[color]
            color=color_cycle[color]
            print(f"Well Done {color}, you won!" )   
            play_again=input('Would you like to play again? (y/n) ')=='y'
        print("""
Thank you for playing connect 4. 
This programme was created by Alex Small. 
Please visit my GitHub profile https://github.com/AlexSmall96.
""")