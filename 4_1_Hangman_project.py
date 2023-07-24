import random
from Extras.hangman_art import stages, logo
from Extras.hangwan_words import word_list

print(logo)
# word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"hint for testing: {chosen_word}")
stages_data = 6
new_words = []

for i in range(len(chosen_word)):
    new_words += "_"

## FIRST METHOD ##

underscore_remain = False
while not underscore_remain:  # alt : while not underscore_remain:
    guess = input("Guess a letter: ").lower()

    # updates the 'new_words' list by replacing the correct occurrences of the 'guess' character
    # in the 'chosen_word'. The updated 'new_words' list contains the guessed characters at their correct positions.
    for check in range(len(chosen_word)):
        if chosen_word[check] == guess:
            new_words[check] = chosen_word[check]

    print(new_words)

    if guess in chosen_word:
        print(stages[stages_data])

    if guess not in chosen_word:
        stages_data -= 1
        print(stages[stages_data])
        if stages_data == 0:
            underscore_remain = True
            print("You lose.")

    if "_" not in new_words:
        print("You win.")
        underscore_remain = True


## Second METHOD ##

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
