t1 = (10, 20,40, 30, 40)
t2 = "Pavani", "Sara", "Arjun"
print(t1)
print(t2)

print(t1+t2)
print(t1[1])
print(t2[0])
print(t1[1:3])
print(t2[:1])
print(t2[2:])

print(t1.count(40))
print(t2.count("Pavani"))
print(t2.index("Sara"))
print(t1.index(30))

a=5
b=20
a,b = b,a
print(a,b)

data = 10,20,30
a,b,c = data
print(a,b,c)