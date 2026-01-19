class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

c=Cat()
c.speak()
c.meow()
#c.bark() throws error

d=Dog()
d.speak()
d.bark()
#d.meow() throws error