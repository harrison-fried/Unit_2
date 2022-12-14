'''Lab 4.01

Remove the Vowels
Create a function, de_vowel, which will take a string as input and return a copy of that string with all the vowels removed. Otherwise, the string should be the same. 'Y' does not count as a vowel for the purposes of this function.

Create the function contract for de_vowel.

Write de_vowel using a for loop

Provide a few examples that confirm de_vowel works as expected:

What if the string is all vowels?

What if there are no vowels?

What if there is a mix of vowels and non-vowels and spaces?

What if some vowels are capitalized, e.g., the first letter in a sentence?

Example
Example of the file:

    # contract goes here
    def de_vowel(a_string):
        # your code goes here

    no_vowels = de_vowel("This sentence has no vowels")
    print(no_vowels)
    # examples go here
Example output:

    >>> python3 de_vowel_lab.py
    Ths sntnc hs n vwls
Bonus
Use a counter (variable you define outside of a loop to keep track of a value inside a loop) to create a function count_vowels.

count_vowels takes in a string and returns an int representing the number of vowels in the string.

Can you think of an alternate way to do complete this task without any loop or counter, by making use of your new de_vowel() function instead?'''



def de_vowel(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_sentence = ''
    for letter in sentence:
        if letter not in vowels:
            new_sentence += letter

    return new_sentence

scentence = input("What would you like your scentence to be? ")

print(de_vowel(scentence))

def count_vowel(a_sentence):
    vowel = 'aeiou'
    in_sentence = 0
    for letter in a_sentence:
        if letter in vowel:
            in_sentence += 1

    return in_sentence


print(f"There are {count_vowel(scentence)} vowels in your sentence")

    

