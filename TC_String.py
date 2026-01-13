p="""Hello
Welcome 
to 
python learning"""""
print(p)

#Index
print(p[2])
print(p[-3])
print(p[0])
print(p[-1])

#slicing
text="Selenium"
print(text[2:5])
print(text[:4])
print(text[3:])
print(text[::2])
print(text[1::2])
print(text[0])

#concatination
print(p+text)
print(p+"Hello")
#repetition
print("Hello World"*5)

#convert to upper & lower case
print(text.upper())
print(text.lower())


print(text.replace("Selenium","java"))
print(len(p))
print(len(text))

print("a" in "Pavani")
print("v" not in "Pavani")


s1 = "I am {0} and I am {1} years old".format("Pavani", 23)
print(s1)
s2 = p.split()
print(s2)