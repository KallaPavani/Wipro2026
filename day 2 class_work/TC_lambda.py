add=lambda a,b: a+b
print(add(3,4))
multiply=lambda a,b: a*b
print(multiply(3,5))
maxnum=lambda x,y: x if x>y else y
print(maxnum(10,20))

#map(function,iteratble)
numbers=[1,2,3,4,5]
result=map(lambda x:x*2,numbers)
print(list(result))