from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name):
        self.name=name
        print("Employee Constructor is called")

    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def salary(self):
        print(self.name,"Salary is 35k")

m=Manager("Vasu")
m.salary()