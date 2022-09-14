'''
#################
Lab 2.06
#################
1. In your Notebook
-------------------
Predict what will be printed then type the program in your console to confirm
Example 1
    a = 0
    while a < 10:
        print(a)

prediction: infinite a's
actual: infinite a's

Example 2
    a = 0
    while a < 10:
        a = a + 1
        print(a)

prediction: a a a a a a a a a a 
actual: a a a a a a a a a a

2. In your Notebook
-------------------
Create a set of test cases for the following sample code and predict the behavior
    a = input("Would you like to quit: ")
    while a != "y" and a != "n" :
        a = input("Would you like to quit: ")

test cases: 'y', 'n', 'q', 'cat'

3. Implement the Tic Tac Toe game using a while loop
----------------------------------------------------
Allow users to keep playing (max 9 times).

Use variables to decide whose turn it is, and greet them as Xs or Os.

User picks a location on the board according to the number:
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9


Depending on the position user gave, update the corresponding position of the board to reflect that.

Print the updated board out.

You will not need to determine the winner at this point.
(Copy and paste your previous tic-tac-toe version and modify the code to implement the above)


a = input("Would you like to quit: ")
while a != "y" and a != "n" :
        a = input("Would you like to quit: ")



'''
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # game board
turns = 0 # keeps track of turns
player = 1 # keeps track of whose turn it is
player_symbol = 'X' # keeps track of which symbol to replace w
valid_choice = False

# Starting board
print(f"{board[0][0]} | {board[0][1]} | {board[0][2]} ")
print("---------")
print(f"{board[1][0]} | {board[1][1]} | {board[1][2]} ")
print("---------")
print(f"{board[2][0]} | {board[2][1]} | {board[2][2]} ")

#game loop
while turns < 9:
    chosen_move = int(input(f" Choose where to put your {player_symbol} "))

    #move conditionals
    if chosen_move == 1 and board[0][0] == 1:
        board[0][0] = player_symbol
        valid_choice = True
    elif chosen_move == 2 and board[0][1] == 2:
        board[0][1] = player_symbol
        valid_choice = True
    elif chosen_move == 3 and board[0][2] == 3:
        board[0][2] = player_symbol
        valid_choice = True
    elif chosen_move == 4 and board[1][0] == 4:
        board[1][0] = player_symbol
        valid_choice = True
    elif chosen_move == 5 and board[1][1] == 5:
        board[1][1] = player_symbol
        valid_choice = True
    elif chosen_move == 6 and board[1][2] == 6:
        board[1][2] = player_symbol
        valid_choice = True
    elif chosen_move == 7 and board[2][0] == 7:
        board[2][0] = player_symbol
        valid_choice = True
    elif chosen_move == 8 and board[2][1] == 8:
        board[2][1] = player_symbol
        valid_choice = True
    elif chosen_move == 9 and board[2][2] == 9:
        board[2][2] = player_symbol
        valid_choice = True
    else: print("Invalid choice!")
    # reprint board
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---------")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---------")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]} ")

    #switch players
    if valid_choice:
        turns += 1
        if player == 1:
            player = 2
            player_symbol = 'O'
        elif player == 2:
            player = 1
            player_symbol = 'X'
    valid_choice == False
print("Board is full")