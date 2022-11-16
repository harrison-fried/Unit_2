board = [
    [ 1, 2, 3],
    [ 4, 5, 6],
    [ 7, 8, 9]
]

def print_board():
    row_count = 1
    for row in range(len(board)):
        row_string = ""
        for i in range(3):
            if i < 2:
                row_string += str(board[row][i]) + " | "
            else:
                row_string += str(board[row][i])
        if row < 2:
            print(row_string)
            print("---------")
        else:
            print(row_string)




print_board()