class PositiveSalary:
    def __init__(self):
        self._salary = {}

    def __get__(self, instance, owner):
        return self._salary.get(instance, None)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        self._salary[instance] = value


class Employee:
    salary = PositiveSalary()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary



emp1 = Employee("Pavani", 30000)
emp2 = Employee("Teena", 45000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)
