'''
##########################################
Lab 2.03 - Game Show
##########################################
In your Notebook
Follow the flow of execution in the following programs and predict what will happen for each
one
---------------------------------------
Example 1
---------------------------------------
a = input("What... is your quest")
b = "to seek the holy grail"
if a != b:
    print("Go On. Off you go")
else:
    b = input("What...is the air-speed velocity of an unladen swallow?")
    if b == "What do you mean? An African or European swallow?":
        print("I don't know that...AHHH [Bridgekeeper was thrown over bridge]")
    else:
        print("[you were thrown over bridge]")

Prediction: It will all work as it should
Actual: it does

---------------------------------------
Example 2
---------------------------------------
user_input = input("What is your favorite color")
if user_input == 'blue':
    print("Blueskadoo")
elif user_input == "red":
    print("Roses are red!")
elif user_input == "yellow":
    print("Mellow Yellow")
elif user_input == "green":
    print("Green Machine")
elif user_input == "orange":
    print("Orange you glad I didn't say banana.")
elif user_input == "black":
    print("I see a red door and I want it painted black")
elif user_input == "purple":
    print("And we'll never be royalllssss")
elif user_input == "pink":
    print("Pinky- and the Brain")
else:
    print("I don't recognize that color. Is it even...??")

Prediction: it works correctly
Actual: it does

---------------------------------------
In your Notebook
---------------------------------------
Translate this Snap! program into a Python program
***Refer to the image provided on Moodle located below the Lab 2.03 link***
Write program below:

---------------------------------------
Create a game show program
---------------------------------------
Declare 10 prizes (prize1, prize2, prize 3 at the top of your file)
User picks a number
The prize corresponding with that door is printed for the user.
Write code below the multiline comment
'''

prize1 = '50,000 dollars'
prize2 = 'a new Car!'
prize3 = 'a target giftcard'
prize4 = 'a new cat'
prize5 = 'a box of coal'
prize6 = 'a vacation to a mountain resort'
prize7 = 'pushed into a pit of lava!'
prize8 = 'a mansion'
prize9 = 'a private jet'
prize10 = 'a bucket full of spiders!'

chosen_door = int(input("Pick a door and you will win a mystery prize! \n hint:(say 1-10) \n there are ten doors chose wisely! "))
if chosen_door == 1:
    print(f"Congrats! you got {prize1}")
elif chosen_door == 2:
    print(f"Congrats! you got {prize2}")
elif chosen_door == 3:
    print(f"Congrats! you got {prize3}")
elif chosen_door == 4:
    print(f"Congrats! you got {prize4}")
elif chosen_door == 5:
    print(f"Congrats! you got {prize5}")
elif chosen_door == 6:
    print(f"Congrats! you got {prize6}")
elif chosen_door == 7:
    print(f"Congrats! you got {prize7}")
elif chosen_door == 8:
    print(f"Congrats! you got {prize8}")
elif chosen_door == 9:
    print(f"Congrats! you got {prize9}")
elif chosen_door == 10:
    print(f"Congrats! you got {prize10}")
else: 
    print("Oh No! it seems you did not choose a valid door... we are going to have to kick you out now \n *you get kicked out*")


x = int(input("What is x? "))
y = int(input("What is y? "))
z = int(input("What is z? "))




if x + y > z and x + z > y and y + z > x:
    print("This is a valid triangle! ")

    if x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2:
        print("This is a right triangle! ")

    if x == y and y == z:
        print("This is an equalateral triangle! ") 

    elif (x == y and y != z) or (y == z and z != x) or (x == z and z != y):
        print("This is an icoceles triangle! ")

    else:
        print("This is a scalene triangle")

else:
    print("Sorry the inputs you gave me does not make a valid triangle !")


