'''
###############
#  Lab 5.03   #
###############
In this lab your job is to create a week-long to-do list using a Python dictionary. 
Each key in the dictionary is a day of the week. Each associated value is a list of items to do that day.

The program repeatedly asks the user what action they wish to take ( add or get).

If the user enters get, the program asks for a day of the week, and then returns the to-do list for that day.

If the user enters add, the program asks for a day of the week, then asks for a new item, then adds it to the 
specified list.

If a user tries to add an item that already exists on the list for that day, the program rejects the request.

At the start of the program the dictionary should be totally empty (containing no keys and no values).

---------
-Example-
---------
Here's an example. The program output is shown in bold text, the user input in regular text. (use your imagination)

>>>python3 daily_to_do_list.py
What would you like to do ('add' or 'get')?
add
What day?
Friday
What would you like to add to Fridays to-do list?
practice clarinet
What would you like to do ('add' or 'get')?
get
What day?
Friday
You have to practice clarinet.
What would you like to do('add' or 'get')?

-------
-Bonus-
-------
It's a bit tedious for the user to have to type in three different lines to add an item to a to-do list. 
Use split() to allow the user to input add Friday watch tv and relax.  Create a variation of the program 
that doesn't allow any duplicates across any of the days. Make sure when you add a to-do item that it 
doesn't exist in the to-do lists of any of the days before adding.
'''

weekly_schedule = {
    'Monday':'',
    'Tuesday':'',
    'Wensday':'',
    'Thursday':'',
    'Friday':'',
    'Saturday':'',
    'Sunday':''
}

# running = True
# while running:
#     user_choice = input("Would you like to 'get' or 'add' ")
#     if user_choice == 'add':
#         chosen_day = input("What day? ")
#         if chosen_day in weekly_schedule:
#             to_do = input("What would you like to add? ")
#             if weekly_schedule[chosen_day] == '':
#                 weekly_schedule[chosen_day] += to_do
#             else:
#                 weekly_schedule[chosen_day] += (' and ') + (to_do)
#         else:
#             print("Sorry that day is not in your weekly schedule")

#     if user_choice == 'get':
#         get_day = input("What day would you like to see your schedule for? ")
#         if get_day in weekly_schedule:
#             print(f"On {get_day} you have to {weekly_schedule[get_day]}")
#         else:
#             print("Sorry that day is not in your weekly schedule")

playing = True
while playing:
    user_choice = input("What would you like to do? ")
    command_list = user_choice.split()
    cycle = 1
    to_do = ''
    for command in command_list:
        if cycle == 1:
            action = command
        if cycle == 2:
            day = command
        elif cycle > 2:
            if to_do != 'add':
                to_do = to_do + command
                to_do = to_do + (' ')
        cycle += 1
    if action == 'add':
        if day in weekly_schedule:
            if weekly_schedule[day] == '':
                    weekly_schedule[day] += to_do
            else:
                weekly_schedule[day] += (' and ') + (to_do)
    elif action == 'get':
        if day in weekly_schedule:
            print(f"On {day} you have to {weekly_schedule[day]}")

