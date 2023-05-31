print("Welcome to the Love Calculator V1")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# "TRUE"
count_T = name1.lower().count("t") + name2.lower().count("t")
count_R = name1.lower().count("r") + name2.lower().count("r")
count_U = name1.lower().count("u") + name2.lower().count("u")
count_E = name1.lower().count("e") + name2.lower().count("e")

# "LOVE"
count_L = name1.lower().count("l") + name2.lower().count("l")
count_O = name1.lower().count("o") + name2.lower().count("o")
count_V = name1.lower().count("v") + name2.lower().count("v")
count_EE = name1.lower().count("e") + name2.lower().count("e")

true_Total = count_T + count_R + count_U + count_E
love_Total = count_L + count_O + count_V + count_EE

Calculation = int(str(true_Total) + str(love_Total))

if Calculation < 10 or Calculation > 90:
    print(
        f"Your score is {Calculation}, you go together like coke and mentos.")
elif Calculation >= 40 and Calculation <= 50:
    print(f"Your score is {Calculation}, you are alright together.")
else:
    print(f"Your score is {Calculation}.")


print('''
---------------
Description:
This program is a simple Love Calculator that determines the compatibility
between two people based on their names. It calculates a score by counting the occurrences of specific letters
in both names and then combines them to form a final score.
The program provides different messages based on the calculated score,
indicating the level of compatibility between the individuals.

Learning Focus:
- focusing on basic input/output
- string manipulation
- mathematical operations
- conditional statements
- Logical Operators

Code Explanation:
1. The program starts by printing a welcome message and prompting the user to enter their name and the name of their partner.
2. It then proceeds to count the occurrences of specific letters ("TRUE" and "LOVE") in both names using the `count()` function.
    The counts for each letter are stored in separate variables.
3. The total counts for "TRUE" and "LOVE" are calculated by summing the individual counts.
4. The `true_Total` and `love_Total` variables store the combined counts for "TRUE" and "LOVE", respectively.
5. The `Calculation` variable is created by concatenating the `true_Total` and `love_Total` variables as strings and converting them back to an integer.
6. The program then uses conditional statements (`if`, `elif`, and `else`) to determine the compatibility score and provide an appropriate message based on the calculated score.
    - If the score is less than 10 or greater than 90, it outputs a message indicating a strong incompatibility.
    - If the score is between 40 and 50 (inclusive), it outputs a message indicating moderate compatibility.
    - For all other scores, it simply outputs the calculated score.
7. The program prints the final result along with the calculated score.

This program is a basic implementation and does not consider various factors that influence relationships.
It is purely intended for fun and educational purposes.

''')
