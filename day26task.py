#12345
#1234
#123
#12
#1

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end ="")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end ="")
    print()
        

    # print(i)
    # for j in i:
    #     print(j)

#1 to 100 prime number

for i in range (2,101):
    for j in range(2,i):
        #print(j)
        if i%j==0:
            break
    else:
        print(i)

#*****
#****
#***
#**
#*
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end ="")
    print()
#*
#**
#***
#****
#*****

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end ="")
    print()


# Create an abstract class Shape with an abstract method area() and a concrete method describe().
# Inherit Shape in Circle and implement area() using radius passed in the constructor.

# Create another subclass Rectangle from Shape with attributes length and width, and implement area().


from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def describe(self):
        print("I am name")
        #class Circle(Shape):
class Circle(Shape):
    def __init__(self,radius):
        self.r= 3.14*radius**2
    def area(self):
        print(f"circle {self.r}")
class Rectangle(Shape):
    def __init__(self,length,breath):
        self.a = length*breath
    def area(self):
        print(f"Rectangle {self.a}")
# s = Shape()
# s.describe()
c = Circle(3)
c.area()
a = Rectangle(4,4)
a.area()


# Create an abstract class Vehicle with an abstract method start_engine() and implement it in Car and Motorbike
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print("I am car")
class Bike(Car):
    def start_engine(self):
        super().start_engine()
        print("I am bike")
obj = Bike()
obj.start_engine()
# obj1 = Car()
# obj1.start_engine()