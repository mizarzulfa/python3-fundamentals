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

print('''
---------------
Description: In this Python program, you embark on an exciting adventure to find the hidden treasure on Treasure Island. 
You will make choices at various points in the game that will determine your fate.
The program utilizes user input and conditional statements to guide you through the game and determine 
whether you succeed or fail.

Learning Focus:
This program provides a beginner-friendly introduction to using user input and conditional statements in Python.
By going through the code and understanding how different choices lead to different outcomes,
you can learn about basic flow control and decision-making in programming.

Code Explanation:
- The program starts with a multiline string that represents a visually appealing ASCII art of a chest.
   It serves as a decorative element to enhance the game's atmosphere.
- The `print` function is used to display a welcome message to the player.
- The `input` function is used to prompt the player for their choice at the first crossroad, which is stored in the variable `crossroad`.
- The `lower` method is applied to the `crossroad` variable to convert the input to lowercase for case-insensitive comparison.
- The program uses conditional statements (`if`, `elif`, and `else`) to handle the different outcomes based on the player's choices.
- If the player chooses to go "left" at the crossroad, they are prompted for another choice at the lake. The input is stored in the variable `lake`.
- Similar to the previous choice, the input is converted to lowercase for comparison.
- Depending on the choice at the lake, the program guides the player through different scenarios using nested conditional statements.
- If the player chooses to wait ("wait"), they are asked to choose a door at the island. Their choice is stored in the variable `doors`.
- Again, the input is converted to lowercase for comparison.
- Based on the door choice, the program determines whether the player has found the treasure or encountered a game-over situation.
- If the player chooses to swim ("swim") at the lake, it results in a game-over.
- If the player chooses to go "right" at the crossroad, it also leads to a game-over.
- If the player enters an invalid input, an error message is displayed.
- The program uses appropriate `print` statements to communicate the outcomes to the player.

Note: This program can be further enhanced by implementing loops and additional choices
to make the gameplay more complex and engaging.

''')
