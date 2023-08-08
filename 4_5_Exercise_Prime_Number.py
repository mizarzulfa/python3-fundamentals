
# #NO LOOP V1
# def prime_checker(number):
#     if number < 2:
#         print("Not a prime number")
#         return
    
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             print("Not a prime number")
#             return

#     print("Prime number")

# n = int(input("Check this number: "))
# prime_checker(number=n)


# NO LOOP V2
def prime_checker(number):
    is_prime = True
    if number < 2:
        return
    
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            
    if is_prime:
        print("Prime")
    else:
        print("not prime")
        
n = int(input("Check this number: "))
prime_checker(number=n)


# # LOOP

# def prime_checker(number):
#     if number < 2:
#         print("Not a prime number")
#         return

#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             print("Not a prime number")
#             return
        
#     print("Prime number")


# while True:        

#     n = input("Check this number: ")
    
#     if n.lower() == "c":
#         break
    
#     numberss = int(n)
#     prime_checker(number=numberss)
