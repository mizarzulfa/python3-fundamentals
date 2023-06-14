# Take input from the user and split it into a list of strings
student_heights = input("Input a list of student heights").split()

# Iterate over the range of indices from 0 to the length of student_heights
for n in range(0, len(student_heights)):
    # Convert each element in student_heights to an integer
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

total = 0

for var_numb in student_heights:
    c_integer = int(var_numb)
    total += c_integer

total /= (n+1)
print(round(total))
