'''
###########
Lab 4.03
###########

Instructions
In this lab we will be drawing images using nested for loops.

For each of the following problems, you will write a function that will draw the desired output. You may use an extra function if you find it helpful.

1.  Write a function, draw_7, to draw the 7x7 square (shown below)

    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
2.  Write a function stars_and_stripes, that will draw a 3 sets of rows. 1st a row of 7 stars followed by a row of 7 dashes (shown below)

    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
3.  Write a function, increasing_triangle that will print out the following:

    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    1 2 3 4 5 6
    1 2 3 4 5 6 7

4. Write a function, vertical_stars_and_stripes that will print out the following:

    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -

5.  Use a function to create your own pattern or drawing. Some possible pattern ideas:

    Write a function that will print a border around a 7x7 square (shown below)

        * * * * * * * *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * * * * * * * *
    Write a function that will print the following balanced_triangle.

        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
        1 2 3 4 5 6
        1 2 3 4 5 6 7
        1 2 3 4 5 6
        1 2 3 4 5
        1 2 3 4
        1 2 3
        1 2
        1
    Write a function that will print the following triangle.

        *
        ***
        *****
    
'''
# Write the code for your custom function below:



def my_function(choice):
    if choice == 1:
        for j in range(0, 7):
            my_string = ''
            for i in range(0, 7):
                my_string += ' *'
            print(my_string)
    elif choice == 2:
        current = '*'
        for j in range(0, 7):
            my_string = ''
            if current == '*':
                for i in range(0, 7):
                    my_string += ' *'
                print(my_string)
                current = '-'
            elif current == '-':
                for i in range(0, 7):
                    my_string += ' -'
                print(my_string)
                current = "*"
    elif choice == 3:
        my_string = ''
        number = 1
        num_for_str = ''
        for j in range(0, 7):
            for i in range(0, 1):
                num_for_str += ' ' + str(number)
                my_string = num_for_str
                number += 1
            print(my_string)    
    elif choice == 4:
        current = '-'
        for j in range(0, 7):
            my_string = ''
            current = '-'
            for i in range (0, 7):
                if current == '-':
                    my_string += ' -'
                    current = '*'
                elif current == '*':
                    my_string += ' *'
                    current = '-'
            print(my_string)
    elif choice == 5:
        current = '*'
        index = 0
        for j in range (0, 9):
            my_string = ''
            if current == '*' or index == 8:
                for i in range (0, 7):
                    my_string += ' *'
                    current = "-"
                index = index + 1
                print(my_string)
            elif current == '-':
                my_string += ' *'
                for v in range (0, 5):
                    my_string += ' -'
                my_string += ' *'
                index = index + 1
                print(my_string)
    




            
              
        
                
        





pattern_choice = int(input("What pattern would you like? (1-5) "))

my_function(pattern_choice)