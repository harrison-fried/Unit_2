'''
##############################
User Input Challenge
##############################

Create a program that asks the user to enter their name and their age. Print out a message 
addressed to them that tells them the year that they will turn 100 years old.

Add on to the previous program by asking the user for another number and printing out that 
many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n" is the same as pressing the ENTER button)
'''

name = input("Hello, what is your name? ")
age = int(input("How old are you? "))
turns_100_in = int((2022 - age) + 100)
copies = int(input("How many copies would you like of the resulting message? "))
printamount = ((f"{name}, you turn 100 years old in the year {turns_100_in}!\n") * copies)
print(f"{printamount}")