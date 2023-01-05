from board import Board

data=[['.' for i in range(7)] for j in range(6)]

board=Board(data)
board.display()
for i in range(10):
    if i % 2 ==0:
        board.update_data('red')
    else:
        board.update_data('blue')
    board.display()
    

