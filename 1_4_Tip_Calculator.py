welcome_bro = print("Welcome to the tip calculator.")
total_bill_ask = input("What was the total bill? $")
percentage_ask = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")
total_people_split = input("How many people to split the bill? ")


data_total_bill = float(total_bill_ask)
data_percentage = int(percentage_ask) / 100  # example : 12/100 = 0.12
data_people_split = int(total_people_split)

each_person_no_tip = data_total_bill / data_people_split
tip_percentage = (data_total_bill * data_percentage) / data_people_split

each_person_no_tip += tip_percentage
res = each_person_no_tip

final_message = print(F"each person should pay: ${round(res, 2)}")


print('''
---------------
Tip Calculator - Splitting the Bill Fairly

Description:
In this Python program, I have created a tip calculator that helps you
split the bill fairly among a group of people.
By entering the total bill amount, desired tip percentage, and the number of people in the group,
the calculator provides the amount each person should contribute, including the tip.

Learning Focus:
- Basic input/output operations in Python.
- Variables and data types (float, int).
- Mathematical calculations.
- String formatting.
- Code organization and readability.

Code Explanation:
1. We start by printing a welcome message to greet the user and introduce the tip calculator.
2. Using the input() function, we prompt the user to enter the total bill amount, tip percentage, and the number of people splitting the bill. The values entered are stored as strings.
3. We convert the total bill amount (total_bill_ask) to a float using the float() function. This allows us to perform mathematical calculations.
4. The tip percentage (percentage_ask) is converted to an integer and divided by 100 to get the decimal representation (e.g., 12/100 = 0.12). This is stored in the variable data_percentage.
5. The number of people splitting the bill (total_people_split) is converted to an integer using the int() function and stored in data_people_split.
6. We calculate the amount each person would pay without considering the tip by dividing the total bill by the number of people (data_total_bill / data_people_split). This value is stored in each_person_no_tip.
7. The tip amount for each person is calculated by multiplying the total bill (data_total_bill) by the tip percentage (data_percentage) and dividing it by the number of people (data_people_split). The result is stored in tip_percentage.
8. We add the tip amount to the amount each person would pay without the tip (each_person_no_tip) to get the final amount each person should contribute. The result is stored in res.
9. The final amount is rounded to two decimal places using the round() function.
10. We print a message using string formatting (F"") to display the final amount each person should pay (${round(res, 2)}).
''')
