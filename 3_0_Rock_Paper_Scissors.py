import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ask = input(
    "What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors.")

val_rock = val_paper = val_scissors = error_input = 0

if ask == "0":
    print(rock)
    val_rock = 1
elif ask == "1":
    print(paper)
    val_paper = 1
elif ask == "2":
    print(scissors)
    val_scissors = 1
else:
    print("Input errors!")
    error_input = 1

# random pick: computer
if error_input != 1:
    print("Computer Chose:")

list_of_hand = [rock, paper, scissors]
var_random = random.randint(1, 3) - 1

computer_respon = list_of_hand[var_random]

if error_input != 1:
    print(computer_respon)

# conditional
if val_rock == 1 and var_random == 1:
    print("You lose")
elif val_rock == 1 and var_random == 2:
    print("You win")
elif val_rock == 1 and var_random == 0:
    print("Draw")

if val_paper == 1 and var_random == 1:
    print("draw")
elif val_paper == 1 and var_random == 2:
    print("You lose")
elif val_paper == 1 and var_random == 0:
    print("You win")

if val_scissors == 1 and var_random == 1:
    print("You win")
elif val_scissors == 1 and var_random == 2:
    print("draw")
elif val_scissors == 1 and var_random == 0:
    print("You lose")


print('''
---------------

Description: 
This is a simple implementation of the Rock-Paper-Scissors game in Python. 
The program allows the user to choose between rock, paper, and scissors by entering the corresponding number. 
The computer then randomly selects its choice, and the program determines the winner based on the game's rules.

Learning Focus:
 - This program helps someone to learn the basics of programming in Python,
 including user input, conditional statements, random number generation, and string manipulation.

Code Explanation:
1. The code begins by importing the `random` module, which is used to generate random numbers later in the program.
2. Three variables, `rock`, `paper`, and `scissors`, store ASCII art representations of the corresponding hand gestures.
3. The user is prompted to enter their choice by typing '0' for Rock, '1' for Paper, or '2' for Scissors. The input is stored in the `ask` variable.
4. The variables `val_rock`, `val_paper`, and `val_scissors` are initialized to 0 and will be used to determine the user's choice.
5. Based on the user's input, the corresponding hand gesture is printed, and the respective variable is set to 1 (indicating the user's choice).
6. If the user's input is invalid (i.e., not '0', '1', or '2'), an error message is printed, and the variable `error_input` is set to 1.
7. The computer's choice is randomly generated by selecting a number between 1 and 3 and subtracting 1 to get an index for the `list_of_hand` list.
8. If there were no input errors, the computer's hand gesture is printed.
9. The program then checks the combinations of choices to determine the winner using a series of conditional statements.
   The variables `val_rock`, `val_paper`, and `val_scissors` are used to identify the user's choice, while `var_random` represents the computer's choice.
10. Based on the combinations, the program prints the result of the game: "You win," "You lose," or "Draw."
11. The game ends, and the program terminates.

Note: The ASCII art representations are not necessary for the functioning of the game but add a visual element to make it more engaging.
''')
