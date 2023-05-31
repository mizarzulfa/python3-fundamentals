print('''
                        .--------------------------------...
               ,'-------------------------------,'   |
              /                                /     |
             /________________________________/    ,'|
             |               ..               |  ,'  |
             |___________-==/88\==-___________|,' /) |.
             |  \    \     ((  ))     /    /  |  (/  |-. .
             |   \    \     \{}/     /    /   |    .' .  .
          . '|    \    \     )(     / _  /    |    ,   .  .
         . . |\    \    \    \/    _.( ~-.   /|\ ,' .   . .
       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
        .  `    .     .       .  ,'\. ~-  . , .  .  .   .
           .  `   .     ,   .      , ~~-.' .  .    .
      ''')

print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")

crossroad = input(
    'You\'re at a crossroad. Where do you want to go? Type "left" or "right" \n')
crossroad = crossroad.lower()
# print(left_right)

if crossroad == "left":
    lake = input('You\'ve come to a lake. There is an island in the middle of the lake. \n Type "wait" or wait for a boat. Type "swim" to swim accross.\n')
    lake = lake.lower()
    if lake == "wait":
        doors = input(
            "You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which color do you choose?\n")
        doors = doors.lower()
        if doors == "red":
            print("It's a room full of fire. Game Over.")
        elif doors == "blue":
            print("You enter a room of beasts. Game Over.")
        elif doors == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("Error, Please input the correct words!!")

    elif lake == "swim":
        print("Game Over.")
    else:
        print("Error, Please input the correct words!!")

elif crossroad == "right":
    print("Game Over.")
else:
    print("Error, Please input the correct words!!")
