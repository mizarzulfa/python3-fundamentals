# Take input from the user and split it into a list of strings
student_heights = input("Input a list of student heights").split()

# #method 1
# for c in range(0, len(student_heights)):
#     student_heights[c] = int(student_heights[c])

# #method 2
list_str_to_int = [int(j) for j in student_heights]

# method 3
# list_str_int = []
# for appending in student_heights:
#     list_str_int.append(int(appending))

total = 0
for var_numb in list_str_to_int:
    total += var_numb

stud = 0
for student in list_str_to_int:
    stud += 1

avg = total / stud

print(round(avg))
