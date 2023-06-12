import random

# ex. John, Jonna, lina, kezi
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")  # string into list using split()

people_total = len(names)
random_names = random.randint(0, people_total - 1)

# Alternatives
# var_random = random.choice(names)

person = names[random_names]

print(f"{person} is going to buy the meal today!")

print('''
---------------

Description:
Randomly Selecting a Person to Buy the Meal

In this code, you'll learn how to randomly select a person from a list to determine who will buy the meal.
The program prompts the user to input a list of names separated by commas and randomly selects a person from the list.
The selected person is then announced as the one responsible for buying the meal.

Learning Focus:
- Basic input/output in Python.
- Working with lists and string manipulation.
- Random number generation using the `random` module.
- Formatting output using f-strings.

Code Explanation:
1. The program starts by importing the `random` module, which will be used to generate random numbers.
2. The user is prompted to input a list of names separated by commas using the `input()` function. The input is stored in the variable `names_string`.
3. The `split(", ")` method is used to split the input string at each comma followed by a space, creating a list of individual names stored in the `names` variable.
4. The variable `people_total` is assigned the length of the `names` list, which represents the total number of people.
5. A random number is generated using `random.randint(0, people_total - 1)`, where `people_total - 1` ensures that the generated number is within the valid index range of the `names` list.
6. The random number is used as an index to access a person's name from the `names` list, which is then stored in the variable `person`.
7. The selected person is announced as the one responsible for buying the meal using an f-string formatted output statement.
8. The program terminates.

Note: Make sure to properly indent the code for syntax correctness and execution in Python.

''')
