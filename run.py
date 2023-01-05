from board import Board

data=[['.' for i in range(7)] for j in range(6)]

board=Board(data)
board.display()
color='red'
color_map={'red':'blue','blue':'red'}
game_running=True
count=0
while board.running and count < 42:
    color=color_map[color]
    column=board.update_data(color)
    board.display()
    game_running=board.check_winner(column,color)
    count += 1

print(f"Well Done {color}, you won!" )   
    

