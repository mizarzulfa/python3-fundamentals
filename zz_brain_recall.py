def else_if_try(simple):
    if simple < 2:
        print("halo")
        return False
    else:
        return False
    
if else_if_try(3):
    print(f" is prime.")
else:
    print(f"is not prime.")