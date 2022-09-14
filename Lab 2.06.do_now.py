great_pets = ['cat', 'dog']
while True: 
    animal = input("WHat is your favorite pet")
    if animal == 'quit': 
        print("Bye! ")
        break
    else:
        if animal in great_pets:
            print("A Great Pet!")
        else:
            print(f"{animal}, a fine pet! ")
