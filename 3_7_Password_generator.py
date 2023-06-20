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

print("PyPassword Generator")
much_Letters = int(
    input("How many letters would you like in your password?\n"))
much_symbols = int(input("How many symbols would you like?\n"))
much_numbers = int(input("How many numbers would you like?\n"))

save_letters = ""
for letter in all_letters:
    save_letters += letter
    random_letters = random.choices(save_letters, k=much_Letters)

save_symbols = ""
for symbol in symbols:
    save_symbols += symbol
    random_symbols = random.choices(save_symbols, k=much_symbols)

save_numbers = []
for number in numbers:
    save_numbers.append(str(number))
    random_numbers = random.choices(save_numbers, k=much_numbers)


combine_all_data = random_letters + random_symbols + random_numbers
# random all data
random_final = random.sample(combine_all_data, k=len(combine_all_data))

# String Inside List joined
string_join = ''.join(random_final)

print(string_join)
