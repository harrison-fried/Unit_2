'''
##########
Lab 4.02
##########

Part 1
----------
Write a function pluralize_words that takes in a list of words and updates the values of the list 
to make each one plural. It returns nothing.

Making plurals in English has a number of special cases, but for this lab we'll use a simple rule: 
if the word ends in a y remove the y and add ies; otherwise add an 's'.

We'll exercise the function on a list of words.

Create the function contract for pluralize_words.

Provide a few examples that confirm pluralize_words works as expected:

    Include examples with 'berry'

    What if the list is empty?

Example 1
----------
    # contract goes here
    def pluralize_words(word_list):
        # your code goes here

    word_list = ['apple', 'berry', 'melon']
    print(f"Singular words: {word_list}")
    pluralize_words(word_list)
    print(f"No longer singular words: {word_list}")
    # more examples go here

#######################################################
Here is what it should look like when you run your code:
#######################################################
Singular words: ['apple', 'berry', 'melon']
No longer singular words: ['apples', 'berries', 'melons']

Hint
-----
Remember that you can index into the string and get the length of a string. Use that to get the last letter of each word.

Part 2
------
Create a function my_reverse, which will return a reversed string.

Create the function contract for my_reverse.

Provide a few examples to confirm that my_reverse works:

    An empty string

    A string of even length

    A string of odd length greater than 1

    A string of length 1

Example 2
---------
    # contract goes here
    def my_reverse(string_to_reverse):
        # your code goes here

    reversed = my_reverse("apples")
    print(reversed)
    # examples go here

##############################################################
Here is what example 2 should look like when you run your code:
##############################################################
    selppa

Hint 2
------
To get the last element:(len(my_list) -1) - 0 
To get the second to last element: (len(my_list)-1 ) - 1 
To get the third to last element: (len(my_list)-1) - 2

Extension
---------
Create a function reverse_strings_in_list. This function will input a list of strings you want to reverse. 
The function will reverse the strings in the list by calling the my_reverse function in a loop.
'''


def pluralize(a_list):
    index = 0
    for word in a_list:
        if word[-1] != 'y':
            a_list[index] = word + 's'
        else:
            a_list[index] = word[:-1] + 'ies'
        index += 1

singular = ['apple', 'banana', 'grape', 'pineapple','strawberry', 'blackberry']
pluralize(singular)

print(f"no longer singular: {singular}")

def reverse(a_word):
    new_word = ''
    index = 1
    for letter in a_word:
        new_word += a_word[-index]
        index = index + 1
    return new_word


word = 'apple'

print(reverse(word))
        
def reverse_strings_in_list(c_list):
    for word in c_list:
        reverse(word)
        c_list += word
    
    print(c_list)
        




print(reverse_strings_in_list(singular))
print(f"No longer plural: {singular}")