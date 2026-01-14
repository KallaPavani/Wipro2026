data=[1,2,3,4]
iterator=iter(data)
print(next(iterator))
print(next(iterator))
#print(next(iterator))
#print(next(iterator))


for x in [10,20,30]:
    print(x)

class CustomIterator:
     def __init__(self,n):
         self.n=n
         self.current=1
     def __iter__(self):
         return self
     def __next__(self):
         if self.current<=self.n:
             value=self.current
             self.current+=1
             return value
         else:
             raise StopIteration

obj=CustomIterator(3)
for num in obj:
    print(num)

