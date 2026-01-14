#2. Create a generator function that yields the first N Fibonacci numbers
def fib_generator(n):
    a, b = 1, 1
    count=0
    while count < n:
        yield a
        a, b = b, a + b
        count+=1

for fib in fib_generator(10):
      print(fib)