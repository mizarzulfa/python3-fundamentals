height = int(input("How tall are you in centimeters?"))

if height > 120:
    # print("You're able to ride!")
    age = int(input("How old are you?"))
    if age > 18:
        print("You should pay $12.")
    elif age >= 12:
        print("You should pay $7")
    else:
        print("You should pay $5.")
else:
    print("Sorry, Come back later!")


print('''
---------------
Description:
This Python program calculates the admission fee for an amusement park ride based on the user's height and age.
It demonstrates the use of nested if statements to determine the appropriate price based on the conditions.

Learning Focus:
 - Understanding nested if statements in Python
 - Taking user input and performing conditional checks
 - Executing different code blocks based on multiple conditions
 
Code Explanation:

1. The user is prompted to enter their height in centimeters.
2. The program checks if the height is greater than 120 centimeters, indicating the person is tall enough to ride the attraction.
3. If the height requirement is met, the program proceeds to ask the user's age.
4. Depending on the age, different admission prices are displayed using nested if statements.
5. If the age is greater than 18, the price is set to $12.
6. If the age is between 12 and 18 (inclusive), the price is set to $7.
7. If the age is less than 12, the price is set to $5.
8. If the user's height is below 120 centimeters, the program displays a message indicating that they cannot ride the attraction.
9. The program terminates after displaying the appropriate admission fee based on the user's input.

Note: The line commented out, "# print("You're able to ride!")", is unnecessary and can be removed since it does not affect the program's functionality.

''')
