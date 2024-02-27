'''Create an inheritance heirarical for vehicles. start with a base class vehicle and then create child classes such as car, motorcycle, bus, truch, cycle etc that inherit commom attributes and methods from base class while adding vehile specific features'''

class Vehicle(): #base class
    def Vehicle_color(self):
        print("Choose the color:\n1. Red\n2. Green\n3. Blue\n4. Yellow\n5. Black")

class Car(Vehicle): #child1 class
    def Average(self):
        print("Average of your car: 20")
    def Power(self):
        print("Power of your car: 746 Horse Power")

class Bike(Vehicle): #child2 class
    def Average(self):
        print("Average of your bike: 50")
    def Power(self):
        print("Power of your bike: 200 hp")

class Truck(Vehicle): #child3 class
    def Average(self):
        print("Average of your truck: 35")
    def Power(self):
        print("Power of your truck: 600 hp")

info_car = Car()
info_car.Vehicle_color()
info_car.Average()
info_car.Power()

info_bike = Bike()
info_bike.Vehicle_color()
info_bike.Average()
info_bike.Power()

info_truck = Truck()
info_truck.Vehicle_color()
info_truck.Average()
info_truck.Power()
