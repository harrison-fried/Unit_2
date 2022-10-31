
# STARTING VARIABLES

month = 3
day = 1
miles_to_go = 2000
lbs_of_food = 500
health = 5
question = "nothing"

import random
from tkinter.tix import DisplayStyle

Playing = True

#  FUNCTIONS 

def travel():
    global day
    global miles_to_go
    global lbs_of_food
    global health
    day = (day + random.randint(3,7))
    lbs_of_food = lbs_of_food - day * 4
    miles_to_go = (miles_to_go - random.randint(30,60))
    health_loss = random.randint(1,5)
    if health_loss == 2:
        health = health - 1

def rest():
    global health
    global day
    global lbs_of_food
    if health < 5:
        health = (health + 1)
        day = (day + random.randint(2,5))
        lbs_of_food = lbs_of_food - day * 2
    else:
        print("Sorry you have full health, you cannot rest")

def hunt():
    global lbs_of_food
    global day
    global health
    day = (day + random.randint(2,5))
    lbs_of_food = lbs_of_food - day * 5
    lbs_of_food = (lbs_of_food + 200)
    health_loss = random.randint(1,3)
    if health_loss == 2:
        health = health - 1
        
def random_event():
    global health
    global question
    global lbs_of_food
    global day
    global miles_to_go
    event_chance = random.randint(1,70)
    if question == travel or question == hunt:
        if 1 <= event_chance <= 5:
            health = health - 2
            lbs_of_food = lbs_of_food - day * 10
            day = day + 10
            miles_to_go = (miles_to_go - random.randint(10,30))
            print(f"Oh no! you contracted dysantary! It slowed you down a ton and caused you to lose 2 health and consume over twice as much food!")
        elif 20 <= event_chance <= 35:
            day = day + 6
            miles_to_go = (miles_to_go - random.randint(20,35))
            lbs_of_food = lbs_of_food - random.randint(5,200)
            print(f"Oh no! you ran into a river, you were slown down a little bit and you lost some food in the river!")
        elif 50 <= event_chance <= 51:
            day = day + 30
            health = health - 3
            lbs_of_food = lbs_of_food - 200
            print("Oh no! an alien space ship came down and kidnapped you! You were held captive for a month and lost some health!")
            print("You also had some of your earthly food confiscated for testing!")
   

def status():
    print(f"The date is {month}/{day}, you have {miles_to_go} miles to go to reach Oregon City You have {lbs_of_food}lbs of food left And your health is {health}")
    
def help():
    print("travel: (randomly travel a certain amount of miles taking up a random number of days (consumes 4 pounds of food per day))")
    print("rest: (replinishes health and takes up days, consumes 2lbs of food each day)")
    print("hunt: (adds 200lbs of food and takes up days, consumes 5lbs of food each day)")
    print("status: (lists all current statuses)")
    print("quit: (quits game)")

def quit():
    global Playing
    Playing = False

def add_day():
    global day
    global month
    global Playing
    if month == 3 and day >= 31:
        month = month + 1
        day -= 31
    elif month == 4 and day >= 30:
        month = month + 1
        day -= 31
    elif month == 5 and day >= 31:
        month = month + 1
        day -= 31
    elif month == 6 and day >= 30:
        month = month + 1
        day -= 31
    elif month == 7 and day >= 31:
        month = month + 1
        day -= 31
    elif month == 8 and day >= 31:
        month = month + 1
        day -= 31
    elif month == 9 and day >= 30:
        month = month + 1
        day -= 31
    elif month == 10 and day >= 31:
        month = month + 1
        day -= 31
    elif month == 11 and day >= 30:
        month = month + 1
        day -= 31
    elif month == 12 and day >= 31 and miles_to_go != 0:
        print("Sorry, you didnt make it in time...")
        Playing = False

def select_action():
    global question
    question = input(f"{name} what would you like to do? ")
    print("-------------")

    if question == "travel":
        travel()
        global day
        global month
        global lbs_of_food
        global miles_to_go
        global health
        print(f"You traveled for a while... the date is now {month}/{day}, you have {lbs_of_food}lbs of food left and {miles_to_go}mi to go. Health = {health}")
        print("-------------")
    elif question == "rest":
        rest()
        print(f"You rested for a while... The date is now {month}/{day}, your health is now {health}")
        print("-------------")
    elif question == "hunt":
        hunt()
        print(f"You went hunting... the date is now {month}/{day} and you now have {lbs_of_food}lbs of food. Health = {health}")
        print("-------------")
    elif question == "status":
        status()
    elif question == "quit":
        quit()
    elif question == "help":
        help()
    else:
        print("Sorry that is an invalid command...")
        print("-------------")
    

# INTRODUCTION

name = input("Hello! Welcome to the Oregon Trail!... Whats your name, brave traveler? ")
print(f"{name}, Your mission is to traverse the 2000 miles of Oregon trail by the end of the year! Good Luck! (use 'help' if you do not know what to do)")
print("-------------")

# GAME LOOP

while Playing:
    
    select_action()
    random_event()
    add_day()

    if lbs_of_food <= 0:
        print("Sorry, you ran out of food and starved to death while on the Oregon Trail! ")
        Playing = False
    elif health == 0:
        print("Sorry, you ran out of health and died!")
        Playing = False

    if health > 0 and miles_to_go <= 0:
        print("Congrats! You finally made it to Oregon! Your ending stats are:")
        status()
        print("Have fun in your new life in Oregon!")