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


def game_loop():
    player1 = input("Player 1 enter your name ")
    player2 = input("Player 2 enter your name ")
    current_turn = 1
    if current_turn == 1:
        print_board()
        player_1_choice = int(input(f"{player1} where would you like your first move to be?"))
        for row in board:
            for place in row:
                if place == player_1_choice:
                    if row == 0:
                        row[place - 1] = 'X'
                    elif row == 1:
                        row[place - 4] = 'X'
                    elif row == 2:
                        row[place - 7] = 'X'
        current_turn = 2
        print_board()
        if current_turn == 2:
            player_2_choice = int(input(f"{player2} where would you like your first move to be?"))
            for row in board:
                for place in row:
                    if place == player_2_choice:
                        if row == 0:
                            row[place - 1] = 'O'
                        elif row == 1:
                            row[place - 4] = 'O'
                        elif row == 2:
                            row[place - 7] = 'O'
        current_turn = 1
        print_board()

playing = True

while playing:
    game_loop()



