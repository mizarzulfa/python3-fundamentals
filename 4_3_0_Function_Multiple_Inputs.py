def greet_with(name: str,location: str):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
    
# # POSITIONAL ARGUMENTS
greet_with("Anjay","Indonesia")

# # KEYWORD ARGUMENTS
greet_with(location="Indonesia", name="Bodir")

# # # Multiple Parameters & Returning Function VALUE
# def greet_with(name: str, location: str) -> str:
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
#     return f"{name} {location}"

# print(greet_with("anjay", "Unjuy"))