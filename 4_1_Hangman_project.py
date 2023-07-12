# 2
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"hint for testing: {chosen_word}")

guess = input("Guess a letter: ").lower()

new_words = []

for check in chosen_word:
    # print(check)
    if check == guess:
        new_words.append(check)
        # print("right")
    else:
        new_words.append("_")

# Convert list to string using for loop method
    # words_combine = ""
    # for i in new_words:
    #     words_combine = words_combine + i
    # print(words_combine)

# Convert list to string using join function
res = ' '.join(new_words)
print(res)
