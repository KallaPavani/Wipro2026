class Calculator:
    def calculate(self,a,b):
       print("Calculator result:",a+b)
class AdvancedCalculator(Calculator):
    def calculate(self,a,b):
        print("Advanced Calculator result:",a*b)

class Box:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return Box(self.value+other.value)

calc1=Calculator()
calc2=AdvancedCalculator()

calc1.calculate(10,2)
calc2.calculate(30,14)

b1=Box(20)
b2=Box(60)
result=b1+b2
print("Box value after addition:",result.value)

