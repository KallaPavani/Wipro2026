from functools import reduce

# 1. range(): To generate numbers from 1 to 20

numbers=list(range(1,20))
print(numbers)

for i in range(1,20):
    print(i)

#2. filter() with a lambda to select only even numbers
even_Numbers=list(filter(lambda x: x%2==0,numbers))
print(even_Numbers)

#3. map() with a lambda to square the filtered even numbers
square_even_Numbers=list(map(lambda x:x*x ,even_Numbers))
print(square_even_Numbers)

#4. reduce() to calculate the sum of squared even numbers
sum_of_square_even_numbers=reduce(lambda x,y: x+y,square_even_Numbers)
print(sum_of_square_even_numbers)

#1. Create a list comprehension to store squares of all numbers
data=[1,2,3,4,5,6,2,4]
square_list=[x * x for x in data]
print(square_list)

#2. Create a set comprehension to store only unique even numbers
even_set={x for x in data if x%2==0}
print(even_set)

#3. Create a dictionary comprehension where the key is the number and the value is its cube
dict_cube={x: x**3 for x in data}
print(dict_cube)