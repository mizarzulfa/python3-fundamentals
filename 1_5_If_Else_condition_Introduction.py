print("Welcome to the Roller Coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the Roller Coaster!")
# elif: height == 120: (else if)
    # print("Congrats! You can ride the Roller Coaster!")
else:
    print("sorry, you have to grow taller before you can ride ")

print('''
---------------
The code checks the value of 'height' against three conditions. 
If height is greater than or equals to 120, the statement under the first 'if' block is executed.
If it is not, the condition in the first 'elif' block is evaluated.
If that condition is also False, the code falls back to the else block.

Note:
 I used to code in C#, and the formatting of if/else conditions differs between C# and Python.
 Here's a comparison of the syntax in both languages:

In C#, the syntax for an if/else condition looks like this:
 if (condition)
     { // Code to execute if the condition is true }
  else
    { // Code to execute if the condition is false }
    
On the other hand, in Python, the syntax is as follows:
if condition:
    # Code to execute if the condition is true
else:
    # Code to execute if the condition is false

in C#, the if and else blocks are enclosed within curly braces {}, whereas in Python,
indentation is used to define the blocks of code.
This difference in formatting is important to keep in mind when transitioning between the two languages.

''')
