# Simple Function

# def greet():
#     print("anjay")
#     print("Hello")
#     print("Uhuy")
    
# greet()

# Function With Inputs -- Any data Types

# def greet_with_param(name):
#     print(f"Hello {name}")
#     print(f"Your name is {name}")
    
# greet_with_param("Mizar")

# Funtion With Inputs -- Specific Data Types

# METHOD 1
# def specific_call(intejer):
#     if isinstance(intejer, int):
#         print(f"Hello bro {intejer}")
#     else:
#         print("Wrong data type!")
        
# specific_call(123)

# METHOD 2 -- Specific Data Types RAISE ERROR!
def specific_call(intejer: str):
    if not isinstance(intejer, str):
        raise TypeError("Invalid input! Please provide an integer.")
    print(f"Hello bro {intejer}")
        
specific_call("Mizar")