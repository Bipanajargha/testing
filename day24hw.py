# 2. Create a class Shape with a method area(). Create two subclasses Circle and Rectangle that override the area() method. Implement polymorphism to display the area of both shapes.
class Shape:
    def area(self):
        pass

class Circle:
    def area(self,r):
        a = 3.14*r**2
        print(a)
class Rectangle:
    def area(self,l,b):
        self.a = l*b
        print(self.a)
c = Circle()
c.area(3)
r = Rectangle()
r.area(3,4)


# 3. Write a Python function that takes a list of objects of different classes and calls a common method describe() on each. Ensure that the objects print different messages depending on their class.
class Dog:
    def describe(self):
        print("I am a Dog. I bark.")

class Cat:
    def describe(self):
        print("I am a Cat. I meow.")

class Bird:
    def describe(self):
        print("I am a Bird. I chirp.")

def show_descriptions(objects):
    for obj in objects:
        obj.describe()

# Creating objects
d = Dog()
c = Cat()
b = Bird()

# List of objects
animals = [d, c, b]

# Call the function
show_descriptions(animals)


# 4. **Demonstrate method overriding using a base class Employee and a subclass Manager, where both have a method called work()
class Employee:
    def work(self):
        print("Employee is working.")

class Manager(Employee):
    def work(self):
        print("Manager is managing the team.")

# Creating objects
e = Employee()
m = Manager()

# Calling the work method
e.work()  # Calls base class method
m.work() 