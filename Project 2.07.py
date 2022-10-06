



#dungeon map
level1 = ['empty', 'sword', 'empty', 'monster', 'stairs up', 'empty']
level2 = ['stairs up', 'empty', 'sword', 'monster', 'stairs down', 'sword']
level3 = ['stairs down', 'empty', 'magic stones', 'stairs up', 'empty', 'sword']
level4 = ['stairs up', 'sword', 'empty', 'empty', 'stairs down', 'magic stones']
level5 = ['stairs down', 'empty', 'monster', 'sword', 'empty', 'Boss Monster','prize']

current_level = level1
current_room = 0
invintory = []
current_location = current_level[current_room]
movement_room = 5
#Game Loop
playing = True
while playing: 
    # umpdate current location
    current_location = current_level[current_room]

    #describe location
    if current_location == 'empty':
        print("\n \n ---------- \n You are in a empty room")
    elif current_location == 'sword':
        print("\n \n ---------- \n You walk into a room and find a sword!")
    elif current_location == 'magic stones':
        print("\n \n ---------- \n You walk into a room and notice something glowing in the corner, they are magic stones!")
    elif current_location == 'stairs up':
        print("\n \n ---------- \n You walk into a room and see a set of stairs going up... they lead somewhere")
    elif current_location == 'monster':
        print("\n \n ---------- \n You walk into a room and the doors slam shut you see something in the corner, \n you hear a terrifying screech and a monstrous creature lurches at you!")
    elif current_location == 'stairs down':
        print("\n \n ---------- \n You walk into a room and see a set of stairs heading back down... they lead to where you just were")
    elif current_location == 'Boss Monster':
        print("\n \n ---------- \n You walk into the final room you have yet to explore, you expect to see your prize \n instead you see a massive, swirling dark mass \n this is the boss monster")
    elif current_location == 'prize':
        print("\n \n ---------- \n You walk into a room and see a glowing monster egg on a pedestal, this is your prize")
    elif current_location == 'empty prize':
        print("Now the room is dark, but a door opens revealing your escape, the pedestal is empty.")

    print(f"current location: {current_location}")

    #player choice
    #get the user choice, left, right, up, down, attack, retreat, grab, or invintory
    player_choice = input("What would you like to do? left, right, up, down, attack, grab, quit, or invintory ")

    if player_choice == 'right':
        if current_location == level5[5]:
            movement_room = 6
            current_room += 1
        elif current_room < movement_room and current_location != 'monster' and current_location != 'Boss Monster':
            current_room += 1
        
        
        
        
        
            
        else:
            print("There is a wall you cannot move on")
    elif player_choice == 'left' and current_location != 'monster' and current_location != 'Boss Monster':
        if current_room > 0:
            current_room -= 1
            
        else:
            print("There is a wall you cannot move on")
        
    elif player_choice == 'up':
        if current_location == 'stairs up':
            if current_level == level1:
                current_level = level2
            elif current_level == level2:
                current_level = level3
            elif current_level == level3:
                current_level = level4
            elif current_level == level4:
                current_level = level5
        else: 
            print("Sorry you can not move up")

    elif player_choice == 'down':
        if current_location == 'stairs down':
            if current_level == level5:
                current_level = level4
            elif current_level == level4:
                current_level = level3
            elif current_level == level3:
                current_level = level2
            elif current_level == level2:
                current_level = level1
        else: 
            print("Sorry you can not move down")

    elif player_choice == 'attack':
        if 'sword' in invintory and current_location == 'monster':
            invintory.remove('sword')
            current_level[current_room] = 'empty'
            print("Whew! you succesfully drove your sword through the monster and the doors have re opened, but sadly your sword has broken!")
            # if current_location == 'monster' and current_level == level1:
            #     level1[3] = 'empty'
            # elif current_location == 'monster' and current_level == level2:
            #     level2[3] = 'empty'
            # elif current_location == 'monster' and current_level == level5:
            #     level5[2] = 'empty'
        elif 'sword' in invintory and 'magic stones' in invintory and current_location == 'Boss Monster':
            invintory.remove('sword')
            invintory.remove('magic stones')
            print("You drive your sword through the heart of the monster, \n it flinches but doesnt seem affected, just then u look down at your bag and see something glowing, \n you pull out the magic stones and shove them in the monsters wound,\n the monster screaches as it starts to glow, it then explodes, \n you see a door on the other side, something is glowing in there!.")
            current_level[current_room] = 'empty'
        elif 'sword' not in invintory and current_location == 'monster' or 'sword' not in invintory and 'magic stones' not in invintory and current_location == 'Boss Monster':
            print("You go to reach for your sword but.. oh no! you dont have a sword!\n The creature stabs you with one of its arms and throws you against the wall\n you see the light fade...\n GAME OVER")
            playing = False

    elif player_choice == 'grab':
        if current_location == 'sword':
            print("You grab the sword before you and add it to your invintory")
            invintory.append('sword')
            if current_location == 'sword' and current_level == level1:
                level1[1] = 'empty'
            elif current_location == 'sword' and current_level == level2:
                level2[2] = 'empty'
            elif current_location == 'sword' and current_level == level2:
                level2[5] = 'empty'
            elif current_location == 'sword' and current_level == level3:
                level3[5] = 'empty'
            elif current_location == 'sword' and current_level == level4:
                level4[1] = 'empty'
            elif current_location == 'sword' and current_level == level5:
                level5[3] = 'empty'
        elif current_location == 'magic stones':
            print("You grab the glowing stones before you")
            invintory.append('magic stones')
            if current_location == 'magic stones' and current_level == level3:
                level3[2] = 'empty'
            elif current_location == 'magic stones' and current_level == level4:
                level4[5] = 'empty'
        elif current_location == 'prize':
            print("You walk up to the pedestal and grab your prize")
            level5[6] = 'empty prize'
            invintory.append("prize")

    elif player_choice == 'Boss Teleport':
        current_level = level5
        current_room = 5
        invintory = ['sword', 'magic stones']

    elif player_choice == 'invintory':
        print(f"You pull out your pack and look inside: {invintory}")
    
    elif player_choice == 'quit':
        playing = False
        

    else: print("Sorry, invalid choice... choose again")


