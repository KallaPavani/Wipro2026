class Animal:
    def sound(self):
        print("Animal makes sounds")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")

obj=[Dog(),Cat()]

for a in obj:
    a.sound()
