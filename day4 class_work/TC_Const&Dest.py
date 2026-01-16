class Employee:
   def __init__(self,name,salary):
       self.name=name
       self.salary=salary
   print("Constructor is called")

   def __del__(self):
       print("Destructor is called")

e=Employee("Khurma",28)
