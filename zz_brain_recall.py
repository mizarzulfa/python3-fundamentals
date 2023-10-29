#### python class - add substract divide minus -- basic structure to understand

class calculator:
    """
    A simple calculator class with basic arithmetic operation
    """
    
    def __init__(self, v1=10) -> None:
    #    self.uhuy = v1
       self.__uhuy = v1 ###protected members
    
    def add(self, n1, n2):
        cek = n1 + self.__uhuy
        return cek + n2
    
    def substract(self, n1, n2):
        return n1 - n2
    
    def divide(self, n1, n2):
        if n2 != 0:
            return n1 / n2
        else:
            return "cannot divide by 0"
        
    def __str__(self) -> str:
        return f'a calcualor with {self.__uhuy}'        
        
calc = calculator()

data = calc.add(2,2)

sata = calc.divide(3,0)


print(calc)