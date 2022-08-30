'''
##################################
Lab 2.02 Booleans & Expressions
##################################
In your Notebook
Predict if each of the following examples will produce a True or False output. Check your answers in interactive mode.
                 
Example 1
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b == "science"       Prediction:  true                   Actual: true
Example 2
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b != "science"       Prediction:  fals                   Actual: false
Example 3
    >>> a = 100
    >>> b = "science"
    >>> a > 75 or b != "science"        Prediction:  true                    Actual: true
Example 4
    >>> a = 100
    >>> b = "science"
    >>> c = True
    >>> not c and a > 75 and b == "science"     Prediction:  error                   Actual: false

In your Console

Complete the following coding challenge
Create a "Can I be President?" program, which determines if the user meets the minimum requirements for becoming the President of the United States. 
Have the user input the information needed.

The minimum requirements to be president of the United States are:

1. Older than 35

2. Resident of US for 14 Years

3. Natural born citizen

Print True if the person could be president and False if they can't be president.

Create a "I can't be President?" program. Print True if the user cannot be President and False if they can be President.

Create a "Can I ride the roller coaster?" program. A roller coaster has the rule that a rider has to be over the height of 50 inches. Because of a legal loophole, if you are over the age of 18 you can ride regardless of your height. If you are allowed to ride, the coaster costs 4 quarters (although the operator accepts tips so more money is appreciated).

Also, the theme park sells frequent rider passes: with a frequent rider pass the roller coaster costs only 2 quarters. Ask the user how tall they are in inches, their age, how many quarters they have, and if they have a frequent rider pass. Print True if the person can ride and False if they can't.


Are the following expressions equivalent? Research DeMorgan's Laws and write why you think they are the same or why they are not the same
not(x or y) == not x and not y

not(x and y) == not x or not y
'''
# can be president (returns true if you can be)
print("hello, do you want to be president? take this short questionnaire to see if you qualify! ")
age = int(input("how old are you? "))
residency = int(input("how long have you lived in the US? "))
born = input("were you born in the US? ")
print(age >= 35 and residency >= 14 and born == 'yes')

# can't be president (returns true if you can't)
# can't be president if under 35, lived less than 14 years in us, or not natural citizen
print("hello, do you want to be president? take this short questionnaire to see if you dont qualify! ")
age = int(input("how old are you? "))
residency = int(input("how long have you lived in the US? "))
born = input("were you born in the US? ")
print(age < 35 or residency < 14 or born != 'yes')

# can ride rollercoaster
print("Hello, it seems you want to ride our rollar coaster, lets see if you can")
age = int(input("How old are you? "))
heigth = int(input("How tall are you? "))
money = int(input("How much money do you have? ")) 
frequentrider = input("do you own our frequent rider pass? ")
print(age >= 18 and money >= 4 or heigth >= 50 and money >= 4 or age >= 18 and money >= 2 and frequentrider == 'yes' or heigth >= 50 and money >= 2 and frequentrider == 'yes')
