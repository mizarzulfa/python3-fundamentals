import random

lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                     "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

all_letters = lowercase_letters + uppercase_letters

symbols = ["!", "@", "#", "$", "%", "^", "&", "*",
           "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", "|", ":", ";", ",", ".", "<", ">", "/", "?"]
numbers = []
for all in range(10):
    numbers.append(all)
numbers = [str(i) for i in numbers]

print("PyPassword Generator")
much_Letters = int(
    input("How many letters would you like in your password?\n"))
much_symbols = int(input("How many symbols would you like?\n"))
much_numbers = int(input("How many numbers would you like?\n"))

password = []
for letter in range(1, much_Letters + 1):
    password.append(random.choice(all_letters))

for symbol in range(1, much_symbols + 1):
    password.append(random.choice(symbols))

for number in range(1, much_numbers + 1):
    password.append(random.choice(numbers))

random.shuffle(password)

string_final = ""
for connect in password:
    string_final = string_final + connect
print(string_final)
