# Simulated user data (replace this with your actual authentication logic)
# users = {
#     "user1": {"username": "user1", "password": "password1"},
#     "user2": {"username": "user2", "password": "password2"}
# }

# def password_auth(username, password):
#     user = users.get(username)
#     # return user and user["password"] == password
#     if user and user.get("password") == password:
#         return True
    
#     return False

# def authentication(function):
#     def wrapper(username, password):
#         if password_auth(username, password):
#             return function(username)
#         else:
#             return "failed"
#     return wrapper


# @authentication
# def anjay(username):
#     return f'welcome back {username}'



# data = anjay("user2", "password2")
# print(data)

##################################

# def validate_input(func):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if not isinstance(arg, int):
#                 raise ValueError("Input parameter must be an integer")
#         return func(*args, **kwargs)
#     return wrapper

# @validate_input
# def add(x, y):
#     return x + y

# result = add(3, 5)  # This will work
# print(result)

# result = add(3, "5")  # This will raise a ValueError

######################################

def my_level_decorator(x):
    def wrapper(z):
        # x(z)
        cek = x(z)
        return cek
        # print("kocak")
    return wrapper

@my_level_decorator
def analyze_level(level):
    cek = level + 12
    return cek

data = analyze_level(3)
print(data)

################################

# # Authentication decorator
# def authenticate(func):
#     def wrapper(username, password):
#         if is_authenticated(username, password):
#             return func(username)
#         else:
#             return "Authentication failed"
#     return wrapper


# def is_authenticated(username, password):
#     user = users.get(username)
#     return user and user["password"] == password

# # Function protected by authentication
# @authenticate
# def protected_function(username):
#     return f"Welcome, {username}!"
#     pass

# # Testing the protected function
# result = protected_function("user4", "password1")
# print(result)  # Output: Welcome, user1!

# result = protected_function("user1", "wrong_password")
# print(result)  # Output: Authentication failed
