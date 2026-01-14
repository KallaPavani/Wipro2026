numbers =[10, 20, 30, 40, 50]
names = ["Pavani", "Sara", "Akki", "Khurma"]
mixed = [10, "Pavan", 3.5, False]

numbers[1] = 100
print(numbers)
print(names)
print(mixed)

for i in numbers:
    print(i)
if 40 in numbers:
    print("found")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])


names.reverse()
print(names)
names.append("lavanya")
print(names)
names.extend(["Manasa","lishanth"])
print(names)
names.remove("Pavani")
print(names)
names.insert(1,"Pavani")
print(names)
