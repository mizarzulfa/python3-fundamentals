height = int(input("How tall are you in centimeters?"))
price = 0

if height > 120:
    # print("You're able to ride!")
    age = int(input("How old are you?"))
    if age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
        price = 0
    elif age > 18:
        print("Adults tickets are $12.")
        price = 12
    elif age >= 12:
        print("Youth tickets are $7")
        price = 12
    else:
        print("Childs tickets are $5.")
        price = 12

    photos = input("Do you want a photo taken? Y or N.")
    if photos == "Y":
        price += 3
    print(f"Your final bill is ${price}")

else:
    print("Sorry, Come back later!")
