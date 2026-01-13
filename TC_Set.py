myset = {1,2,3,4,5,3,4,1,2}
print(myset)

for x in myset:
    print(x)

myset.add(10)
print(myset)
myset.remove(4)
print(myset)

A = {1,2,3,4}
B = {4,5,6,7}
print(A|B)
print(A&B)
print(A^B)
print(A-B)
print(2 in A)

