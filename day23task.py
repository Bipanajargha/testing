# #Create a base class Animal with attributes name and sound. Add a method make_sound() that prints the sound of the animal.

# class Animal:
#     def __init__(self,name,sound):
#         self.name= name
#         self.sound = sound
#     def make_sound(self):
#         print(f"Name:{self.name}\nSound:{self.sound}")
# a = Animal("Dog","Barks")
# a.make_sound()


# # Multi-level Inheritance:

# # Create a base class Vehicle with attributes brand and fuel_type.
# class Vehicle:
#     def vehicle_type(self,brand,fuel_type):
#         self.brand = brand
#         self.fuel_type = fuel_type
#         print(f"{self.brand} {self.fuel_type}")
# class Car(Vehicle):
#     def wheels(self,num_wheels):
#         self.num_wheels= num_wheels
#         print(f"{self.num_wheels}")
# class ElectricCar(Car):
#     def fule(self,fuel_type):
#         self.fuel_type = fuel_type
#         print(f"{self.fuel_type}")
# obj = ElectricCar()
# obj.fule("Charing")
# obj.wheels(4)
# obj.vehicle_type("Toyota","Gasoline")



# # Create a subclass Car that inherits from Vehicle and adds an attribute num_wheels = 4.

# # Create another subclass ElectricCar that inherits from Car and overrides the fuel_type to "Electric".

# # Multiple Inheritance:

# # Create two classes, Swimmer (with a method swim()) and Flyer (with a method fly()).

# # Create a class Duck that inherits from both Swimmer and Flyer. Implement a method quack() in the Duck class
# class Swimmer:
#     def swim(self):
#         print("Swimming...")

# class Flyer:
#     def fly(self):
#         print("Flying...")

# class Duck(Swimmer, Flyer):
#     def quack(self):
#         print("Quack!")

# donald = Duck()
# donald.swim()
# donald.fly()
# donald.quack()


# # Create a base class Shape with a method area() that returns 0.

# # Create subclasses Circle and Rectangle that override the area() method to calculate and return the area of the respective shape.

# # Write a function print_area(shape) that accepts any Shape object and prints its area.
class Shape:
    def area(self):
        pass #return 0 means here nth
class Circle(Shape):
    def area(self,r):
        self.r = 3.14*r**2
        print(f"{self.r}")
    # def _init_(self, radius):
    #     self.radius = radius

    # def area(self,math):
    #     return math.pi * self.radius ** 2
class Rectangle(Shape):
    def area(self,l,b):
        self.a = l*b
        print(self.a)

# #     def area(self):
# #         return self.width * self.height

# # def print_area(shape):
# #     print(f"Area: {shape.area()}")

circle = Circle()
circle.area(4)
rectangle = Rectangle()
rectangle.area(4,3)
# print_area(circle)
# print_area(rectangle)



# Create two classes, Car and Bicycle, each with a method start().

# Write a function start_vehicle(vehicle) that accepts any object with a start() method and calls it.

# Demonstrate duck typing by passing instances of Car and Bicycle to the start_vehicle() function.
# class Car:
#     def start(self):
#         print("Car started.")

# class Bicycle:
#     def start_vehicle(self):
#         print("Bicycle started.")

# def show(vehicle):
#     vehicle.start()

# car = Car()
# bike = Bicycle()
# show(car)
# show(bike)