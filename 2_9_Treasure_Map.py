row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

data1 = int(position[1]) - 1
data2 = int(position[0]) - 1

treasure = "X"

map[data1][data2] = treasure
print(f"{row1}\n{row2}\n{row3}")
