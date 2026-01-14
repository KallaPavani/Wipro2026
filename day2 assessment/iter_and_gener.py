from TC_Iterator import iterator
from day2.CustomIterator import NumberIterator
from day2.Fib_generator import fib_generator

print("Using Custom Iterator")
iter = NumberIterator(10)
for num in iter:
    print(num)

print("Using Fibonnacci Generator")
Generator = fib_generator(10)
for i in Generator:
    print(i)