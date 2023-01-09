import setup


setup.print_title()
setup.print_welcome()
input('Press Enter for Instructions ')
setup.print_instructions()
input('Press Enter to set up the game!')

no_players = setup.set_no_players()
usernames = setup.set_usernames(no_players)
user_colors = setup.select_colors(usernames)
setup.run_game(no_players,user_colors,usernames)

    


