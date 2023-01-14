import os
import time
from board import Board
from board import counters


def print_title():
    """
    Prints the game title to the terminal
    """
    # Clear terminal
    os.system('cls||clear')
    # Assign lines for connect word to list
    connect = [
        ' ▄▀▀▀▀'+'\033[1;31m'+'    ▄▀▀▀▄'+'\033[0;0m'+'    ██   █',
        '██   █    █▀▀▀▀▀     ▄▀▀▀▀   ▀▀▀█▀▀▀',
        '█'+'\033[1;31m'+'        █     █'+'\033[0;0m'+'   █ █  █',
        '█ █  █    █▄▄▄▄▄    █           █  ',
        '█'+'\033[1;31m'+'        █     █'+'\033[0;0m'+'   █  █ █',
        '█  █ █    █         █           █',
        ' ▀▄▄▄▄'+'\033[1;31m'+'    ▀▄▄▄▀'+'\033[0;0m'+'    █   ██',
        '█   ██    █▄▄▄▄▄     ▀▄▄▄▄      █'
        ]
    # Assign lines for four word to list
    four = [
        '█▀▀▀▀▀'+'\033[1;33m'+'    ▄▀▀▀▄'+'\033[0;0m'+'    █     █   █▀▀▀▀▀█',
        '█▄▄▄▄▄'+'\033[1;33m'+'   █     █'+'\033[0;0m'+'   █     █   █     █',
        '█     '+'\033[1;33m'+'   █     █'+'\033[0;0m'+'   █     █   █▀▀▀█▀▀',
        '█     '+'\033[1;33m'+'    ▀▄▄▄▀ '+'\033[0;0m'+'    ▀▄▄▄▀    █    ▀▄ '
    ]
    # Access lists to print words to terminal
    print('\n')
    for i in range(4):
        print('    '+connect[2*i]+'    '+connect[2*i+1])
    print('\n')
    for i in range(4):
        print('                   '+four[i])
    print('\n')


def print_welcome():
    """
    Prints the welcome message to the terminal
    """
    print('Welcome to Connect Four!')
    print('\n')


def print_instructions():
    """
    Prints the instructions to the terminal
    """
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

At the end of the game, press Y and Enter to play again, or Enter to exit.

Good Luck!

""")


def set_no_players():
    """
    Allows the user to select number of players
    1 : human vs computer
    2: human vs human
    """
    # Use while loop to ensure input is valid
    correct_input = False
    while not correct_input:
        no_players = input("""
Select Number of Players:
Enter 1 to play human vs computer or 2 to play human vs human
        """)
        # Validate input
        if no_players.isnumeric():
            if int(no_players) == 1 or int(no_players) == 2:
                return int(no_players)
                # Set variable to true as validation passed
                correct_input = True
            # Retry input
            else:
                print('Please enter either 1 or 2')
        else:
            print('Please enter either 1 or 2')


def set_usernames(no_players):
    """
    Allows all users to select a username
    """
    if no_players == 1:
        player_1 = input('Player 1 - Please enter your username ')
        return [player_1]
    else:
        # Use while loop to ensure input is valid
        correct_input = False
        while not correct_input:
            player_1 = input('Player 1 - Please enter your username ')
            player_2 = input('Player 2 - Please enter your username ')
            # Validate input
            if player_1.lower() != player_2.lower():
                # Set variable to true as validation passed
                correct_input = True
            else:
                # Retry input
                print('Usernames must be different')
        return [player_1, player_2]


def select_colors(usernames):
    """
    Allows player 1 to select their counter color
    """
    # In single player mode, add computer to list of usernames
    # Deal with case when user enters 'computer'
    if len(usernames) == 1:
        if usernames[0].lower() != 'computer':
            usernames.append('Computer')
        else:
            usernames.append('Computer 2')
    # Create dictionary to map usernames to colors
    user_colors = {}
    # Use while loop to ensure input is valid
    correct_input = False
    while not correct_input:
        # Map words to visual counters
        red = counters['red']
        yellow = counters['yellow']
        # Allow user to select color
        user = usernames[0]
        message = f"{user} Select a color : Red {red} or Yellow {yellow} "
        choice = input(message)
        choice = choice.lower()
        # Validate input
        if choice == 'red':
            # Add usernames to dictionary
            user_colors[usernames[0]] = 'red'
            user_colors[usernames[1]] = 'yellow'
            correct_input = True
        elif choice == 'yellow':
            user_colors[usernames[1]] = 'red'
            user_colors[usernames[0]] = 'yellow'
            correct_input = True
        else:
            # Retry input
            print('Please Select from Available Colors')
    return user_colors, usernames


def run_game(no_players, user_colors, usernames):
    """
    Main function to run game sequence
    """
    # Set the initial data to create a blank game board
    data = [['.' for i in range(7)] for j in range(6)]
    # Create an instance of Board
    board = Board(data)
    # Display initial empty board
    board.display()
    user = usernames[0]
    color = user_colors[user]
    # Create dictionary to cycle between usernames during game
    user_cycle = {usernames[0]: usernames[1], usernames[1]: usernames[0]}
    # Count number of moves played
    count = 0
    # Variable to flag if computer has won
    computer_won = False
    # Main loop to run game
    while board.running and count < 42:
        # Check if computer is playing
        if no_players == 1 and count % 2 != 0:
            print('Computer is thinking...')
            # Pause to allow user to read message
            time.sleep(1.5)
            # Clear last line of terminal
            print("\033[A                             \033[A")
            # Call board.update_data_computer to get choice of column
            output = board.update_data_computer(color, user_colors, usernames)
            column = output[0]
            counter_added = output[1]
        else:
            # If computer isn't currently playing,
            # call board.update_data_human to get choice of column
            column, counter_added = board.update_data_human(color, user)
        # If choice of column accepted
        if counter_added:
            # Displate board
            board.display()
            # Call board.check_winner to see if a win has been played
            board.running = board.check_winner(column, color)
            if board.running:
                # Reassign user and color to other player/computer
                user = user_cycle[user]
                color = user_colors[user]
                # Count number of turns
                count += 1
            else:
                if no_players == 1 and count % 2 != 0:
                    computer_won = True
    # Print message when computer wins
    if computer_won:
        print(f"Computer Won ... Better luck next time {usernames[0]}.")
    else:
        # Print well done message if human wins
        print(f"Well Done {user}, you won!")
    # Give user the option to play again
    play_again = input('Would you like to play again? ').lower() == 'y'
    return play_again
