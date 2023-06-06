import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")  # string into list using split()

people_total = len(names)
random_names = random.randint(1, people_total)

# Alternatives
# var_random = random.choice(names)

person = names[random_names]

print(f"{person} is going to buy the meal today!")
