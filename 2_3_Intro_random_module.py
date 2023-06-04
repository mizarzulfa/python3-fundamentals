import random  # This is a python built-in module
import example_of_my_own_module  # import my own module

var_random = random.randint(100, 422)
print(var_random)
# print(random.randint(100, 400)) # Without assigning variable

var_float_random = random.random()  # float random 0.0000 - 0.999999999
print(var_float_random)

print(example_of_my_own_module.hello)
print(example_of_my_own_module.callme())
