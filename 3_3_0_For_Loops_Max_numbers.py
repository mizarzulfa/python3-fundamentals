# RULES
# NOT ALLOWED TO USE FUNCTION:
# max() or min()
# use FOR LOOPS Instead!

student_score = input("Input a list of student scores: ").split()
# string to int ( list )
student_score = [int(k) for k in student_score]
max_numbers = 0

for z in student_score:
    if z > max_numbers:
        max_numbers = z

print(f"The highest score in the class is: {max_numbers}")
