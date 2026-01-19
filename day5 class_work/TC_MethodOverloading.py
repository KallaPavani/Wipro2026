class calc:
    def add(self,a,b=2,c=5):
        return a+b+c

c=calc()
print(c.add(30))
print(c.add(20,40))
print(c.add(10,40,60))
