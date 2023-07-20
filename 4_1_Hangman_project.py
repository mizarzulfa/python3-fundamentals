import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"hint for testing: {chosen_word}")

new_words = []

for i in range(len(chosen_word)):
    new_words += "_"

underscore_remain = False
while underscore_remain == False:  # alt : while not underscore_remain:
    guess = input("Guess a letter: ").lower()

    for check in range(len(chosen_word)):
        string_check = chosen_word[check]
        if string_check == guess:
            new_words[check] = string_check

    print(new_words)

    if "_" not in new_words:
        print("You win.")
        underscore_remain = True

## FIRST METHOD ##
# while "_" in new_words:
#     guess = input("Guess a letter: ").lower()

#     for check in range(len(chosen_word)):
#         string_check = chosen_word[check]
#         if string_check == guess:
#             new_words[check] = string_check

#     print(new_words)

# print("You Win.")

# Convert list to string using for loop method
# words_combine = ""
# for i in new_words:
#     words_combine = words_combine + i
# print(words_combine)

# Convert list to string using join function
# res = ' '.join(new_words)
# print(res)
