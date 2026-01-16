from abc import ABC, abstractmethod

class Shape(ABC):
    def display(self):
        print("display method implemented")
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        print("area method implemented")

r=Rectangle()
r.area()
r.display()

