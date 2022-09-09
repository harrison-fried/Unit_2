'''
###########################
Lab 2.04
###########################
1. In your notebook
For each example below, predict what will be printed. Run the program and write down the output in your notebook.

Example 1
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[0])
    print(a[3])

    prediction:  a d                                          
    actual: a d

Example 2
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 3])

    prediction: d
    actual: c

Example 3
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 6])

    prediction: error
    actual: e

Example 4
    a = ['a', 'b', 'c', 'd', 'e']
    a[3] = 'haha'
    print(a)

    prediction: a b c haha e
    actual: error

2. Create this game again using lists and indexes
--------------------------------------------------
Declare 10 prizes (prize0, prize1, prize2 at the top of your file), but store them all in a list.

User picks a number.

Print prize associated with the door user picked.

3. Create a quiz
--------------------------------------------------
Create a food quiz using lists and indexes.

List of 6 different foods.

Ask the user 8 vague questions to find out what their favorite food is using the list.

Update the score and print their top 2 favorite foods.

Hint: Use a search engine to find the largest number in a python list.

----------------------
​Starter code here​:
----------------------
food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','baggles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1

##############################
Together in class:
##############################
Research nested lists and work through the following Examples:

Bonus Example 1
a = ['a', 'b', 'c', ['d', 'e']]
print(len(a))
Bonus Example 2
a = ['a', 'b', 'c', ['d', 'e']]
b = a[3]
print(b)
Bonus - In your Notebook
How would you access d from the list a?
'''

prizes = ['trip to disneyworld', 'brand new phone', 'free concert of your chosing', 'new puppy', 'new car', 'new house', 'stack of 100,000 dollars', 'free pass for free movies for life ', 'kitten', 'bunny']

chosen_prize = int(input("Please chose a number from 0 - 9 "))

if chosen_prize == 0:
    print("Congrats! you won a " + (prizes[0]))
elif chosen_prize == 1:
    print("Congrats! you won a " + (prizes[1]))
elif chosen_prize == 2:
    print("Congrats! you won a " + (prizes[2]))
elif chosen_prize == 3:
    print("Congrats! you won a " + (prizes[3]))
elif chosen_prize == 4:
    print("Congrats! you won a " + (prizes[4]))
elif chosen_prize == 5:
    print("Congrats! you won a " + (prizes[5]))
elif chosen_prize == 6:
    print("Congrats! you won a " + (prizes[6]))
elif chosen_prize == 7:
    print("Congrats! you won a " + (prizes[7]))
elif chosen_prize == 8:
    print("Congrats! you won a " + (prizes[8]))
elif chosen_prize == 9:
    print("Congrats! you won a " + (prizes[9]))
else: print("Since you dont wanna play the game right you dont get to play at all!")


food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','baggles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1

user_input = input('Do you like to put toppings on your food? ')
if user_input == 'y':
  score[1] = score[1] + 1
  score[3] = score[3] + 1
  score[5] = score[5] + 1

user_input = input('Do you like foods that you fry? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[2] += 1
  

user_input = input('Do you like food you eat with a fork? ')
if user_input == 'y':
  score[1] = score[1] + 1
  score[3] = score[3] + 1
  score[4] += 1

user_input = input('Do you like foods that are sometimes sides? ')
if user_input == 'y':
  score[4] = score[4] + 1
  score[2] = score[2] + 1

user_input = input('Do you like hot foods? ')
if user_input == 'y':
  score[1] = score[1] + 1
  score[2] = score[2] + 1
  score[3] += 1
  score[4] += 1

print("I think that your favorite food is " + (food[score.index(max(score))]))

(score.remove[score.index(max(score))])

print("I think that your second favorite food is " + (food[score.index(max(score))]))