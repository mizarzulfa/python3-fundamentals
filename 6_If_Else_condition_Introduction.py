print("Welcome to the Roller Coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the Roller Coaster!")
# elif: height == 120: (else if)
    # print("Congrats! You can ride the Roller Coaster!")
else:
    print("sorry, you have to grow taller before you can ride ")

'''
The code checks the value of 'height' against three conditions. 
If height is greater than or equals to 120, the statement under the first 'if' block is executed.
If it is not, the condition in the first 'elif' block is evaluated.
If that condition is also False, the code falls back to the else block.

'''
