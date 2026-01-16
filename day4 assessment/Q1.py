class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display_details(self):
        print("Name:",self.name)
        print("Rollno:",self.rollno)

s1=Student("Vasu",23)
s2=Student("Pavan",21)

s1.display_details()
s2.display_details()
