import random

var_random_score = random.randint(10, 100)

if var_random_score < 10 or var_random_score > 90:
    print(
        f"Your score is {var_random_score}, you go together like coke and mentos.")
elif var_random_score >= 40 and var_random_score <= 50:
    print(f"Your score is {var_random_score}, you are alright together.")
else:
    print(f"Your score is {var_random_score}.")

print('''
---------------
Description:
The code generates a random score between 10 - 100 and evaluates
the compatibility of two individuals based on that score. It provides a humorous
response for extreme scores and a neutral response for scores within a specific range.

Learning Focus:
- introduces the use of random number generation
- conditional statements (if-elif-else)
- string formatting, and code execution flow

Code Explanation:
1. Importing the random module:
   - The `random` module is imported to access the `randint` function,
     which generates a random integer.

2. Generating a random score:
   - The `random.randint(10, 100)` function generates a random integer between 10 and 100 (inclusive)
     and assigns it to the variable `var_random_score`.

3. Evaluating the score:
   - The program uses conditional statements (`if`, `elif`, and `else`) to evaluate
     the value of `var_random_score` and print an appropriate message.

4. Handling extreme scores:
   - The condition `var_random_score < 10 or var_random_score > 90` checks if the score is less than 10 or greater than 90.
   If true, it prints a message indicating that the individuals' compatibility is like
   "coke and mentos," a reference to an explosive reaction.

5. Checking a specific score range:
   - The condition `var_random_score >= 40 and var_random_score <= 50` checks if the score is between 40 and 50 (inclusive).
   If true, it prints a message stating that the individuals are "alright together."

6. Handling other scores:
   - If none of the above conditions are met, it means the score is within a normal range.
   The `else` block is executed, printing the score without any specific comment.

7. String formatting:
   - The `f"Your score is {var_random_score}..."` syntax is used to format the output message.
   The value of `var_random_score` is inserted into the string using curly braces `{}`.

8. Execution flow:
   - The program executes sequentially from top to bottom.
   After printing the appropriate message, it reaches the end and terminates.

''')
