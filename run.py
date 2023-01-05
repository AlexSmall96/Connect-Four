from board import Board

data=[['.' for i in range(7)] for j in range(6)]

board=Board(data)
board.display()
color='red'
color_map={'red':'blue','blue':'red'}

for i in range(10):
    column=board.update_data(color)
    board.display()
    board.check_winner(column,color)
    color=color_map[color]
    

