
age = input("What is your current age")

# day = 365
# weeks = 52
# month = 12

current_age = 90 - int(age)  # assume human lifespan --> 90y/0
remain_day = current_age * 365
remain_weeks = current_age * 52
remain_months = current_age * 12

x = remain_day
y = remain_weeks
z = remain_months

print(f"You have {x} days, {y} weeks, and {z} months left.")


print('''
---------------
Description:
In this project, I created a simple Life Tracker to help gain a better understanding of the limited time we have in our lives.
the program calculates the remaining time you have in days, weeks, and months based on your current age.
By visualizing the time you have left, the result encourages you to reflect on your priorities and make the most of each day.

Learning Focus:
- Basic input and output in Python.
- Converting data types from strings to integers.
- Performing arithmetic calculations.
- Formatting strings using f-strings.

Code Explanation:
- The program starts by prompting the user to enter their current age using the input() function and storing it in the age variable.
- The age is then converted from a string to an integer using the int() function.
- The variables day, weeks, and month are calculated by multiplying the age by the respective number of days, weeks, and months in a year.
- The program sets the age limit to 90 years and calculates the remaining time by subtracting the current age from the age limit for days, weeks, and months.
- The remaining time variables are assigned to x, y, and z respectively.
- Finally, the program uses an f-string to display the remaining time in days, weeks, and months with a message.

Note: This is a simple implementation that assumes a year has 365 days, 52 weeks, and 12 months. It does not take into account leap years or different month lengths.

''')
