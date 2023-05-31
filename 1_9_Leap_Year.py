year = int(input("Which year do you want to check? "))

# rule says:
# on every year that is evenly divisible by 4
#  except every year that is divisible by 100
#   unless the year is also evenly divisible by 400

# Method 1
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")

# Method 2

# leap_rule_1 = year % 4
# leap_rule_2 = year % 100
# leap_rule_3 = year % 400

# if leap_rule_1 == 0 and leap_rule_2 != 0:
#     print("Leap year.")

# elif leap_rule_3 == 0:
#     print("Leap year.")

# else:
#     print("Not leap year.")
print('''
---------------
Leap Year Checker in Python

Description:
In this Python code snippet, we implement a program to check whether a given year is a leap year or not.
Leap years have an extra day, February 29th, and occur every four years.
However, there are exceptions to this rule.
Years that are divisible by 100 are not leap years, unless they are also divisible by 400.

Learning Focus:

- Conditional statements in Python (if-else).
- Modulo operator (%).
- Nested if statements.

Code Explanation:

1. The program prompts the user to enter a year to be checked using the input() function,
    and the entered value is stored in the variable year as an integer using the int() function.
2. The code uses conditional statements to determine whether the year is a leap year or not.
3. The first condition checks if the year is divisible by 4 using the modulo operator %. If the remainder is 0, it proceeds to the next condition.
    Otherwise, it directly goes to the last else statement.
4. The second condition checks if the year is divisible by 100. If it is, the code moves to the innermost if-else block.
5. The innermost if-else block checks if the year is divisible by 400. If it is, it prints "Leap year." If not, it prints "Not a leap year."
6. If the year is not divisible by 100, it means it is divisible by 4 but not by 100. In this case, the code directly prints "Leap year."
7. If the year is not divisible by 4, it skips all the inner conditions and directly prints "Not a leap year."

Note: The code assumes the user enters a valid integer as input. No error handling is implemented for invalid inputs in this code snippet.

''')
