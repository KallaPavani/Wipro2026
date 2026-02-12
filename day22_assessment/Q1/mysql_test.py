import mysql.connector

#connect to MySQL
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "company_db",
)
cursor=conn.cursor()

#1. Fetch employees with salary > 50000
print("\nEmployees with salary > 50000")
query1 = "SELECT * FROM employee WHERE salary > 50000"
cursor.execute(query1)

for row in cursor.fetchall():
    print(row)

#2. Insert new employee
print("\nInserting new employee")
insert_query = """INSERT INTO employee (name, department, salary) VALUES (%s, %s, %s)"""

values = ("Lavanya", "Management", 80000)
cursor.execute(insert_query, values)
conn.commit()
print("Employee inserted successfully")

#3. Update salary by 10%
print("\nUpdating salary by 10%")

update_query = """
UPDATE employee
SET salary = salary * 1.10
WHERE name = %s
"""

cursor.execute(update_query, ("Lavanya",))
conn.commit()
print("Salary updated successfully")

cursor.close()
conn.close()

