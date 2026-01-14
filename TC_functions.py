def add(a,b):
    print(a+b)
def sub(a,b):
    return(a-b),a,b
def mult(a,b):
    print(a*b)

add(10,40)
print(sub(100,40))
mult(5,3)


def hello(greeting="Hello",name="World"):
    print('%s,%s'%(greeting,name))
hello()
hello("Pavani","kalla")
def print_param(*params):
    print(params)
print_param("Testing")
print_param(1,2,3,4)
def print_param1(**params):
    print(params)

print_param1(x=1,y=2,z=3)