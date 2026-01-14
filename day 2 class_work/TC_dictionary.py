student={
    "name":"John",
    "age":25,
    "Course": "Python"
}
print(student)
print(student.get("name"))
print(student["age"])

student["Marks"]=85
print(student)
student["age"]=30
print(student)
student.pop("age")
print(student)
student.popitem()
print(student)

print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key, student.get(key))

if "name" in student:
    print("Key Exists")
    print(student.get("name"))

employee = {
    101:{
        "name":"John","age":25, "Course":"Python"},
    102:{
        "name":"Siri","age":45, "Course":"C++"
    }
}
print(employee)
print(employee[101],["name"])