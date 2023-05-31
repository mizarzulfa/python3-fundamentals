height = float(input("Enter your height in m: "))
weight = float(input("Enter yout weight in kg: "))

# Formula: weight (kg) / [height (m)]^2 or
# Formula: weight (lb) / [height (in)]^2 x 703
BMI = weight / (pow(height, 2))

# if statement
if BMI > 35:
    print(f"Your BMI is {round(BMI)}, you are clinically obese.")
elif BMI > 30:
    print(f"Your BMI is {round(BMI)}, you are obese.")
elif BMI > 25:
    print(f"Your BMI is {round(BMI)}, you are slightly overweight.")
elif BMI > 18.5:
    print(f"Your BMI is {round(BMI)}, you have a normal weight.")
else:
    print(f"Your BMI is {round(BMI)}, you are underweight.")

print('''
---------------
Description:
This Python program calculates and classifies your Body Mass Index (BMI) based on ur height and weight.
It provides a brief assessment of the weight status, ranging from underweight to clinically obese.

Learning Focus:
This program introduces the concept of BMI and demonstrates the use of if-elif-else statements for conditional execution in Python.

Code Explpanation:
1. The user is prompted to enter their height and weight in meters and kilograms, respectively.
2. The BMI is calculated using the formula: weight / (height^2).
3. The BMI value is then compared against a series of thresholds to determine the weight category.
4. The if-elif-else statements are used to check the BMI value against each category and print the corresponding message.
5. The messages include the rounded BMI value and a brief description of the weight status.

Note: This BMI calculator is a good way to practice basic input/output
operations and conditional statements in Python.
Feel free to explore and modify the code as you continue learning!

''')
