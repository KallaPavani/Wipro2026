from pymongo import MongoClient

#Connect to MongoDB
client=MongoClient('localhost',27017)

db=client["company_db1"]
collection=db["employees"]

#1. Insert new Employee
print("\nInserting new Employee")

new_employee = {
    "name": "Akki",
    "department": "IT",
    "salary": 75000
}
insert_result = collection.insert_one(new_employee)
print("Inserted ID:", insert_result.inserted_id)

#2. Find all employees in IT department
print("\nemployees in IT department")

for emp in collection.find({"department": "IT"}):
    print(emp)

#3. Update salary of given employee
print("\nUpdtating salary")

collection.update_one(
      {"name": "Akki"},
    {"$set": {"salary": 80000}}
)

print("Salary Updated successfully")