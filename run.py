import setup

setup.print_title()
setup.print_welcome()
input('Press Enter for Instructions ')
PLAY_AGAIN = True
while PLAY_AGAIN:
    setup.print_instructions()
    input('Press Enter to set up the game!')
    no_players = setup.set_no_players()
    usernames = setup.set_usernames(no_players)
    user_colors, usernames = setup.select_colors(usernames)
    PLAY_AGAIN = setup.run_game(no_players, user_colors, usernames)

print("""
Thank you for playing Connect Four.
This programme was created by Alex Small.
Please visit my GitHub profile https://github.com/AlexSmall96.
""")