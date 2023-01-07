from board import Board
import os

play_again = True
while play_again:
    data=[['.' for i in range(7)] for j in range(6)]
    board=Board(data)
    board.display()
    color='red'
    color_cycle={'red':'blue','blue':'red'}
    count=0
    while board.running and count < 42:
        column,counter_added=board.update_data(color)
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
    


