import random

var_random_score = random.randint(10, 100)

if var_random_score < 10 or var_random_score > 90:
    print(
        f"Your score is {var_random_score}, you go together like coke and mentos.")
elif var_random_score >= 40 and var_random_score <= 50:
    print(f"Your score is {var_random_score}, you are alright together.")
else:
    print(f"Your score is {var_random_score}.")
