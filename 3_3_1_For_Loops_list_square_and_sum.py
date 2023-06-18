numbers = [1, 2, 3, 4, 5]
mem = 0

for sq in numbers:
    square = pow(sq, 2)
    mem += square
    print(f"square of {sq} is {square}")

print(mem)
