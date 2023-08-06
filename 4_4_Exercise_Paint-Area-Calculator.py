# # Paint Area Calculator Method 1
def paint_calc(height, width, cover):
    calculation = -((-height * width) // cover)
    print(f"You'll need {calculation} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# # Paint Area Calculator Method 2
def paint_calc(height, width, cover):
    return -((-height * width) // cover)

height_ = int(input("Height of wall: "))
wiidth_ = int(input("Width of wall: "))
coverage = 5

value = paint_calc(height=height_,width=wiidth_,cover=coverage)
print(f"You'll need {value} cans of paint.")

