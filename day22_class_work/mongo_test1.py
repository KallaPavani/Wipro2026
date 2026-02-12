from pymongo import MongoClient

#Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

#Create database
db = client["company_db"]
collection = db["employee"]

#New employee document
new_employee={
    "name":"Pavani",
    "department": "IT",
    "salary": 50000
}

#Insert document
insert_result = collection.insert_one(new_employee)
print("\nInserted new employee with ID:", insert_result.inserted_id)

#Fetch inserted document
employee  = collection.find_one({"_id": insert_result.inserted_id})
print("\nDetails of inserted employee", employee)