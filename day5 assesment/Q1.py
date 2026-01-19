class Vehicle:
    vehicle_count = 0

    def __init__(self):
        Vehicle.vehicle_count += 1
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def drive(self):
        print("Car is starting")

class ElectricCar(Car):
    def charge(self):
        print("Electric Car is charging")

v1=Vehicle()
c1=Car()
e1=ElectricCar()

v1.start()
c1.start()
e1.start()

c1.drive()
e1.drive()

e1.charge()

print("Total vehicles created:",Vehicle.vehicle_count)