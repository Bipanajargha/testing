#class method = only one variable file for all object 
# it is define and initialize using cls parameter
#acessing variable outside the class
#classname.Varible

class Person:
    school = "Ismt"
    def __init__(self):
        self.name = "bipana"
        self.age = 67
    def show(self):
        print(f"my name is {self.name} and age {self.age}")
    @classmethod
    def display(cls,ab):
        cls.school = ab
        print(f"my school name is {cls.school}")
ram = Person()
ram.display("lec")

syam = Person()
print(Person.school)

a = Person()
print(Person.school)

#static method

class A:
    @staticmethod
    def show(a,b):
        print(a+b)
a= A()
a.show(2,3)



#oop - main concept to real world entity lai map garni ho

#fundamentals of oop(four pillar pf oop) main aim to implement real world cocept or entity
#1 inheritance = parents and child
#child class le parents lai inherite garcha means parents ko all features child use garcha
#2 polymorphism
#yeutai le different kam garna payo
#mache ta manche ho tara aarko aarko properties huncha
#3 enccapsulation
#bind garni so that other unauthorized person cannot access

#4 abstraction
#user le j majecha tei garni extra features nadini



#inheritance  one class that inherit another class and share all attributes and methods 
#parent child relationship
#base class = parents class
#derived class - child class

#1 single inheritance

class Parent: # base class
    def first(self):
        print("i am parent class")
class Child(Parent):#derived class
    def second(self):
        print("i am child class")

ch = Child()
ch.first()
ch.second()


