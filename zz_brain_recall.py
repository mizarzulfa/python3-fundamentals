list_a = ["📦","📦","X","📦"]
list_b = ["⏺️","⏺️","⏺️","⏺️"]
list_c = ["🏀","🏀","🏀","🏀"]

combine_list = [list_a,list_b,list_c]

overwrite = "💩"
combine_list[0][0] = overwrite

print(list_a)
