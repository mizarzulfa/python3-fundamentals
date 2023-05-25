year = int(input("Which year do you want to check? "))

leap_rule_1 = year % 4
leap_rule_2 = year % 100
leap_rule_3 = year % 400

if leap_rule_1 == 0 and leap_rule_2 != 0:
    print("Leap year.")

elif leap_rule_3 == 0:
    print("Leap year.")

else:
    print("Not leap year.")
