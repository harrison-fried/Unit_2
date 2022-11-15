'''
##########
Lab 4.05
##########

1. Read through the following code
    def print_numbers(list):
        for i in range(1, len(list)+1):
            print(list[i])

    num_list = [1, 2, 3, 4, 5, 6]
    print_numbers(num_list)

you cant do the plus one because there is not a number there


In your notebook
Write down any bugs that you see in the program

2. Read through the following code
    def swapping_stars():
    line_str = ""
        for line in range(0, 6):
            for char in range(0,6):
                if line % 2 == char % 2:
                    line_str += "*"
                else:
                    line_str += "-"
    print(line_str)

move the print tabbed in one and add a "line_str = "" " after the first for loop

Continue in your notebook
Write down any bugs that you see in the program

3. In script mode
Fix the 2 programs above.
Create a program that asks the user which function they would like to run.
'''


def print_numbers(list):
        for i in range(1, len(list)):
            print(list[i])


playing = True
num_list = [1, 2, 3, 4, 5, 6]
# print_numbers(num_list)


def swapping_stars():
    line_str = ""
    for line in range(0, 6):
        line_str = ""
        for char in range(0,6):
            if line % 2 == char % 2:
                line_str += "*"
            else:
                line_str += "-"
        print(line_str)


# swapping_stars()


def chose_function():
    global playing
    chosen = input("What function would you like to do? 1. print numbers, 2. swapping stars, 3. quit ")
    if chosen == '1' or chosen == 'print numbers':
        print_numbers(num_list)
    elif chosen == '2' or chosen == 'swapping stars':
        swapping_stars()
    elif chosen == '3' or chosen == 'quit':
        playing = False


while playing:
    chose_function()
