'''
###########
Lab 5.01
###########

Instructions
------------
Write a program that uses a dictionary to offer users the meanings of common internet abbreviations.
The program, dictionary_lab.py, prompts the user to enter an internet abbreviation they would like explained. 
If the requested abbreviation is in the program's dictionary (use the in keyword with an if statement 
to test this), then it prints out the definition. If the abbreviation is not in the dictionary, the program 
prints an apologetic message saying that it could not find a definition.

Example Output:
---------------
>>> python3 dictionary_lab.py

What word would you like to look up? nbd
nbd: a phrase meaning no big deal

What word would you like to look up? kittens
Sorry, kittens is not defined

What would would you like to look up?

Bonus
------
Extend the program with any of these features:
The user can
update the definitions (values) for existing abbreviations in the dictionary
add new abbreviations (keys) and provide their definitions (values).
delete entries (key, value pairs) from the dictionary.
get the entire dictionary printed to the screen.
Lesson 6.01 did not cover all the techniques for manipulating dictionaries that you will need to program these features. Search for the necessary information in the [Python tutorial about dictionaries][1] and the [advanced Python documentation about dictionaries][2].
'''

abbreviation_dictionary = {
    'lol':"Laugh Out Loud",
    'idk':"I dont know",
    'hbu':"How about you?",
    'idc':'i dont care',
    'nbd':'no big deal',
    'alr':'alright',
    'smh':'shaking my head',
    'ttyl':'talk to you later',
    'gn':'goodnight',
    'bfr':'be for real',
    'acc':'actually',
    'dw':'dont worry'
}

wanted_def = input("What abbreviation would you like yo know? ")
if wanted_def in abbreviation_dictionary:
    print(abbreviation_dictionary[wanted_def])
else:
    print("Sorry, that abbreviation is not in our dictionary...")

# option = input("Would you like to add a definition?")
# if option == 'yes':
#     new_def = input("What abbreviation would you like to add")
