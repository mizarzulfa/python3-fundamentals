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

# Write your code below this line 👇
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
