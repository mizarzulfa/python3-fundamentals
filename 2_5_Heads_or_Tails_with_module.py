import random
# print("Welcome to Virtual Coin toss program")

# Heads or Tails
# RULE :
#  First letter should be Capitalised ex. Heads not heads
# random the number between 0 - 1 --> 1 = Heads, 0 = Tails

var_data = random.randint(0, 1)
if var_data == 0:
    print("Tails")
if var_data == 1:
    print("Heads")
