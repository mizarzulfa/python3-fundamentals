print("Welcome to the Pizza Delivery!")
size = input("What size of pizza do you want? S, M, L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N")

# brief
# small pizza --> $15
# medium pizza  --> $20
# large pizza --> $25
# pepperoni for small pizza --> +$2
# pepperoni for medium or large pizza --> +$3
# extra_cheese for all size --> +$1

val = 0

if size == "S":
    val = 15
    if add_pepperoni == "Y":
        val += 2

if size == "M":
    val = 20
    if add_pepperoni == "Y":
        val += 3

if size == "L":
    val = 25
    if add_pepperoni == "Y":
        val += 3

if extra_cheese == "Y":
    val += 1

final = val

print(f"Your final bill is: ${final}")


'''
Pizza Delivery app with Size, Toppings, and Extra Cheese

Description:
In this Python program, I created a simple pizza delivery system.
The program will prompt the user to input the size of the pizza (S for small, M for medium, or L for large),
whether they want pepperoni (Y or N), and whether they want extra cheese (Y or N).
Based on the user's choices, the program will calculate the final bill and display it to the user.

Learning Focus:
1. Handling user input using the `input()` function.
2. Using multiple if statements.
3. Performing calculations and updating variables.
4. Displaying formatted output using f-strings.

Code Explanation:
1. The program starts by printing a welcome message and asking the user for input regarding the pizza's size,
    whether they want pepperoni, and whether they want extra cheese.
2. The variable `val` is initialized to 0, which will hold the initial cost of the pizza.
3. The program checks the size of the pizza selected by the user and updates the `val` variable accordingly.
4. If the pizza size is "S" (small), the cost is set to 15. If the user wants pepperoni, an additional $2 is added to the cost.
5. If the pizza size is "M" (medium), the cost is set to 20. If the user wants pepperoni, an additional $3 is added to the cost.
6. If the pizza size is "L" (large), the cost is set to 25. If the user wants pepperoni, an additional $3 is added to the cost.
7. If the user wants extra cheese, $1 is added to the cost.
8. The final cost of the pizza is stored in the variable `final`.
9. Finally, the program prints the final bill using an f-string to display the cost to the user.

Note: This is a basic example and does not include input validation or error handling.
'''
