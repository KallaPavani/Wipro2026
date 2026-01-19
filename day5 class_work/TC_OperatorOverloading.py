class Box:
    def __init__(self,value):
        self.value=value
    def __add__(self, other):
        return self.value + other.value
    def __sub__(self,other):
        return self.value-other.value
      #  return Box(self.value + other.value)


b1=Box(20)
b2=Box(50)
print(b1+b2)

c1=Box(50)
c2=Box(30)
print(c1-c2)
#result=b1+b2
#print(result.value)