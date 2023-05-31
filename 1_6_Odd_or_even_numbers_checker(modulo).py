number = int(input("Which number do you want to check? "))

Even_number_check = number % 2

if Even_number_check == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


print('''
---------------
The modulo operator in Python is represented by the percentage sign (%).
It calculates the remainder when one number is divided by another.

Let's take a few examples to explain it in a simpler way:

Example 1:
When we divide 6 by 2, we get the result 3 with no remainder.
This means 6 is evenly divisible by 2. In Python, if we use the modulo operator
6 % 2, the result will be 0 because there is no leftover or remainder.

Example 2:
If we divide 5 by 2, the result is 2 with a remainder of 1.
This means 5 cannot be divided evenly by 2, and there is a leftover of 1.
In Python, if we use the modulo operator, 5 % 2,
the result will be 1 because it represents the leftover or remainder.

Example 3:
When we divide 14 by 4, we get the result 3 with a remainder of 2.
This means 14 is not evenly divisible by 4, and there are 2 leftover.
In Python, if we use the modulo operator, 14 % 4,
the result will be 2 because it represents the remainder.

So, the modulo operator helps us find the remainder when dividing two numbers.
It can be useful in various programming scenarios, such as checking if a number is even or odd, 
or grouping items into equal-sized portions.
''')
