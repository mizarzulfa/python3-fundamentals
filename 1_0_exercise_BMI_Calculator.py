weight = input("Enter your weight in kg: ")
height = input("Enter your height in m: ")

weight = int(weight)
height = float(height)

BMI = weight / pow(height, 2)

print(int(BMI))

# """
# The code calculates the Body Mass Index (BMI) based on the weight and height entered by the user.
# Here's a step-by-step explanation:

#mantappppp

# 1. The user is prompted to enter their weight in kilograms using the `input()` function. The entered value is stored in the `weight` variable.
# 2. The user is prompted to enter their height in meters using the `input()` function. The entered value is stored in the `height` variable.
# 3. The `weight` variable is converted to an integer using `int(weight)` to ensure it is treated as a numerical value.
# 4. The `height` variable is converted to a float using `float(height)` to handle decimal values.
# 5. The BMI is calculated by dividing the weight by the square of the height using the `pow()` function.
# 6. The calculated BMI is stored in the `BMI` variable.
# 7. Finally, the calculated BMI is converted to an integer using `int(BMI)` and printed to the console.

# """
