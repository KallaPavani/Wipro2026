class A():
    def read(self):
        print("A is reading")

class B():
    def write(self):
        print("B is writing")
    def read(self):
        print("B is reading")

class C(B,A):
    pass

c=C()
c.read()
c.write()

#we can declare same method which we used in parent class but it executes based on what class we extended 1st in child class
#for ex  in class C we passed B and A thatswhy its executed 1st B class methods write and read() and in A also we have same
#method thatswhy it didnt executed ,hence it works in first order like if we passed Class C(A,B) then class A read method and class B write method would have executed