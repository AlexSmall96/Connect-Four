from board import Board
import os
import time
from board import counters


def print_title():
    os.system('cls||clear')
    print('\n') 
    print('               ▄▀▀▀▀'+'\033[1;31m'+'    ▄▀▀▀▄'+'\033[0;0m'+'    ██   █    ██   █   █▀▀▀▀▀    ▄▀▀▀▀   ▀▀▀█▀▀▀')                 
    print('              █'+'\033[1;31m'+'        █     █'+'\033[0;0m'+'   █ █  █    █ █  █   █▄▄▄▄▄   █           █  ')                 
    print('              █'+'\033[1;31m'+'        █     █'+'\033[0;0m'+'   █  █ █    █  █ █   █        █           █   ')                
    print('               ▀▄▄▄▄'+'\033[1;31m'+'    ▀▄▄▄▀'+'\033[0;0m'+'    █   ██    █   ██   █▄▄▄▄▄    ▀▄▄▄▄      █   ')                
    print('\n')                                                                                                              
    print('                           █▀▀▀▀▀'+'\033[1;33m'+'    ▄▀▀▀▄'+'\033[0;0m'+'    █     █   █▀▀▀▀▀█  ') 
    print('                           █▄▄▄▄▄'+'\033[1;33m'+'   █     █'+'\033[0;0m'+'   █     █   █     █ ')   
    print('                           █     '+'\033[1;33m'+'   █     █'+'\033[0;0m'+'   █     █   █▀▀▀█▀▀      ')           
    print('                           █     '+'\033[1;33m'+'    ▀▄▄▄▀ '+'\033[0;0m'+'    ▀▄▄▄▀    █    ▀▄   ') 
    print('\n')

def print_welcome():
    print('Welcome to Connect Four!')
    print('\n')   


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

At the end of the game, press Y to play again, and any other key to exit.

Good Luck!

""")

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
        if usernames[0].lower() != 'computer':
            usernames.append('Computer')
        else: 
            usernames.append('Computer 2')
    user_colors = {}
    correct_input = False
    while not correct_input: 
        choice = input(f"{usernames[0]} Select a color : Red {counters['red']} or Yellow {counters['yellow']} ").lower()
        if choice == 'red':
            user_colors[usernames[0]] = 'red'
            user_colors[usernames[1]] = 'yellow'
            correct_input = True
        elif choice == 'yellow':
            user_colors[usernames[1]] = 'red'
            user_colors[usernames[0]] = 'yellow'
            correct_input = True
    return user_colors,usernames
            
        
            
   

def run_game(no_players,user_colors,usernames):
    data=[['.' for i in range(7)] for j in range(6)]
    board=Board(data)
    board.display()
    user=usernames[0]
    color=user_colors[user]
    user_cycle={usernames[0]:usernames[1],usernames[1]:usernames[0]}
    count=0
    computer_won = False
    while board.running and count < 42:
        if no_players == 1 and count % 2 != 0:
            print('Computer is thinking...')
            time.sleep(1.5)
            column,counter_added=board.update_data_computer(color)
        else:
            column,counter_added=board.update_data_human(color,user)
        if counter_added:
            board.display()
            board.running=board.check_winner(column,color)
            if board.running:
                user = user_cycle[user]
                color= user_colors[user]
                count += 1
            else:
                if no_players == 1 and count % 2 != 0:
                    computer_won = True
    if computer_won:
        print(f"Computer Won ... Better luck next time {usernames[0]}.")
    else:
        print(f"Well Done {user}, you won!" )   
    play_again=input('Would you like to play again? ').lower() == 'y'
    return play_again
