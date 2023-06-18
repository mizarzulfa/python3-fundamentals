
# method 1
mem = 0  # not include 1 #change to 1 to include 1
for n in range(0, 101, 2):  # using step size
    mem += n
print(mem)


# method 2 - using module operation
mem2 = 0
for data in range(2, 101):
    if data % 2 == 0:
        mem2 += data
print(mem2)
