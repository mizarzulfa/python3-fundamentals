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
# print(f"Love Score is {Calculation}")

if Calculation < 10 or Calculation > 90:
    print(
        f"Your score is {Calculation}, you go together like coke and mentos.")
elif Calculation >= 40 and Calculation <= 50:
    print(f"Your score is {Calculation}, you are alright together.")
else:
    print(f"Your score is {Calculation}.")
