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
