import json
import csv
import time
from abc import ABC,abstractmethod
# DECORATORS
def log_execution(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper

def admin_only(func):
    def wrapper(*args,**kwargs):
        role=kwargs.get("role","user")
        if role != "admin":
            raise PermissionError("Access Denied: Admin privileges required")
        return func(*args,**kwargs)
    return wrapper

class Marks:
    def __set_name__(self,owner,name):
        self.name=name
    def __get__(self,obj,objtype=None):
        return obj.__dict__[self.name]
    def __set__(self,obj,value):
        for m in value:
            if m < 0 or m > 100:
                raise ValueError("Invalid Marks\nError: Marks should be between 0 and 100")
            obj.__dict__[self.name]=value

class Salary:
    def __get__(self,obj,objtype=None):
        raise PermissionError("Unauthorized Salary Access\nAccess Denied: Salary is Confidential")
    def __set__(self,obj,value):
        obj.__dict__["_salary"]=value

# Abstract Base Class
class Person(ABC):
    def __init__(self,pid,name,department):
        self.pid=pid
        self.name=name
        self.department=department

    @abstractmethod
    def get_details(self):
        pass

    def __del__(self):
        print(f"Cleaning up records for {self.name}")

#Department Class
class Department:
    def __init__(self,name):
        self.name=name

#Student Class
class Student(Person):
    marks=Marks()
    def __init__(self,sid,name,department,semester,marks):
        super().__init__(sid,name,department)
        self.semester=semester
        self.marks=marks
        self.courses=[]

    def enroll(self,course):
        self.courses.append(course)

    @log_execution
    def calculate_performance(self):
        avg=sum(self.marks)/len(self.marks)
        grade="A" if avg >= 85 else "B" if avg>=70 else "C"
        return avg,grade

    def get_details(self):
        print("Student Details:")
        print(f"Name:  {self.name}")
        print("Role:  Student")
        print(f"Department:  {self.department.name}")

    def __gt__(self,other):
        return sum(self.marks) > sum(other.marks)

#Faculty Class
class Faculty(Person):
    salary = Salary()
    def __init__(self,fid,name,department,salary):
        super().__init__(fid,name,department)
        self.salary=salary

    def get_details(self):
        print("Faculty Details:")
        print(f"Name:  {self.name}")
        print("Role:  Faculty")
        print(f"Department:  {self.department.name}")


#Course Class
class Course:
    def __init__(self,code,name,credits,faculty):
        self.code=code
        self.name=name
        self.credits=credits
        self.faculty=faculty
    def __add__(self,other):
        return self.credits+other.credits

#Iterator
class CourseIterator:
    def __init__(self,courses):
        self.courses=courses
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.courses):
            raise StopIteration
        course=self.courses[self.index]
        self.index+=1
        return course

#Generator
def student_generator(students):
    for student in students:
        print("Student Record Generator")
        print("Fetching Student Records....")
        print("-----------------------------")
        for s in students:
          yield f"{s.pid} - {s.name}"

#File Handling
def save_students_json(students):
    data=[]
    for s in students:
        data.append({
            "id":s.pid,
            "name":s.name,
            "department":s.department.name,
            "semester":s.semester,
            "marks":s.marks
        })
    with open("students.json","w") as f:
        json.dump(data,f,indent=2)
    print("Student data successfully saved to students.json")

def generate_csv_report(students):
    with open("students_report.csv","w",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
        for s in students:
            avg,grade = s.calculate_performance()
            writer.writerow([s.pid,s.name,s.department.name, round(avg ,1),grade])
        print("CSV Report (students_report.csv) generated")


#Main Function
def main():
    students = []
    faculty_list = []
    courses = []

    while True:
        print("Smart University Management System")
        print("\n1  -> Add Student")
        print("2  -> Add Faculty")
        print("3  -> Add Course")
        print("4  -> Enroll Student to Course")
        print("5  -> Calculate Student Performance")
        print("6  -> Compare Two Students")
        print("7  -> Show Person Details (Polymorphism)")
        print("8  -> Merge Course Credits (+ Operator Overloading)")
        print("9  -> Descriptor Validation Demo")
        print("10 -> Decorator Access Control Demo")
        print("11 -> Generate Reports (Generator + CSV + JSON)")
        print("12 -> Exit")

        choice = input("Enter choice: ")

        try:
            if choice=="1":
                sid = input("Enter Student ID:")
                name = input("Enter Student Name:")
                dept= Department(input("Enter Student Department:"))
                sem = int(input("Enter Student Semester:"))
                marks = list(map(int,input("Enter Student Marks:").split()))

                if any (s.pid == sid for s in students):
                    raise ValueError("Error: Student ID already exists")

                s= Student(sid,name,dept,sem,marks)
                students.append(s)

                print("Student Created Successfully")
                print("----------------------------")
                print(f"ID        :   {sid}")
                print(f"Name      :   {name}")
                print(f"Department:   {dept.name}")
                print(f"Semester  :   {sem}")
                print(f"Marks     :   {marks}")

            elif choice=="2":
                fid = input("Enter Faculty ID:")
                name = input("Enter Faculty Name:")
                dept = Department(input("Enter Department:"))
                salary = int(input("Enter Monthly Salary:"))

                f=Faculty(fid,name,dept,salary)
                faculty_list.append(f)

                print("Faculty Created Successfully")
                print("----------------------------")
                print(f"ID        :   {fid}")
                print(f"Name      :   {name}")
                print(f"Department:   {dept.name}")
                print(f"Salary    :   {salary}")

            elif choice=="3":
                code = input("Enter Course code:")
                cname = input("Enter Course Name:")
                credits = int(input("Enter Credits:"))
                fid = input("Enter Faculty ID:")

                fac = next(f for f in faculty_list if f.pid == fid)
                c = Course(code,cname,credits,fac)
                courses.append(c)

                print("Course Added Successfully")
                print("-------------------------")
                print(f"Course Code   :   {code}")
                print(f"Course Name   :   {cname}")
                print(f"Credits       :   {credits}")
                print(f"Faculty       :   {fac.name}")

            elif choice=="4":
                sid = input("Enter Student ID:")
                code = input("Enter Course Code:")
                s = next(s for s in students if s.pid == sid)
                c = next(c for c in courses if c.code == code)
                s.enroll(c)

                print("Enrollment Successful")
                print("---------------------")
                print(f"Student Name  :   {s.name}")
                print(f"Course        :   {c.name}")

            elif choice=="5":
                s = students[0]
                avg,grade = s.calculate_performance()
                print("Student Performance Report")
                print("--------------------------")
                print(f"Student Name    :{s.name}")
                print(f"Marks           :{s.marks}")
                print(f"Average         :{round(avg,1)}")
                print(f"Grade           :{grade}")

            elif choice=="6":
                s1,s2 = students[0],students[1]
                print("Comparing Students Performance")
                print(f"{s1.name} > {s2.name} : {s1>s2}")


            elif choice=="7":
                print("Student Details:")
                print("----------------------")
                students[0].get_details()

                print("Faculty Details:")
                print("----------------------")
                faculty_list[0].get_details()

            elif choice=="8":
                if len(courses) < 2:
                    print("Error: Add at least 2 Courses")
                else:
                    total=courses[0]+courses[1]
                    print("Merge Course Credits:")
                    print("---------------------------------")
                    print(f"Total Credits After merge : {total}")

            elif choice=="9":
                print("Descriptor Validation Demo")
                try:
                    students[0].marks = [120,90]
                except Exception as e:
                    print(e)

                try:
                    print(faculty_list[0].salary)
                except Exception as e:
                    print(e)

            elif choice=="10":
                try:
                    students[0].calculate_performance()(role="user")
                except Exception as e:
                    print(e)


            elif choice=="11":
                for record in student_generator(students):
                    print(record)
                generate_csv_report(students)
                save_students_json(students)

            elif choice=="12":
                print("Thank you for using Smart University Management System")
                break
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()







