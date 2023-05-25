height = float(input("Enter your height in m: "))
weight = float(input("Enter yout weight in kg: "))

# BMI Formula
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
