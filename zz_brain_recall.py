def data(num1, num2):
    jum = num1 + num2
    return jum

# Class definition
class koplak:
    def __init__(self, name="add your name here"):
        self.name = name

    def data(self, nilai1, nilai2):
        res = data(nilai1, nilai2)
        return res



# Instantiate the class without providing a name
ahay = koplak()

print(ahay.name)  # This will print: default_name

# Call the data method
final = ahay.data(19, 19)  # This will print: kocak

print(final)
