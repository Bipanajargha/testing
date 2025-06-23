#poloy=
#operator overloading
a= 3
b = 6
print(a+b)

#int = add
#string = concadenate
#list = merge

#dunder function __init__
#__add__ 
print(int.__add__(1,2))
print(str.__add__("3","4"))

#multiple = mul, div,sub
#greater than = __gt__ ,__lt__

class A:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        return self.a+other.b
class B:
    def __init__(self,b):
        self.b = b 
a = A(9)
b = B(7)
print(a+b)

#encapsulation =data lai binding attributes and methods inside a class so that no one can acess it from outside
#public = default
#private= attributes and methods can only acess within class
#protected = attributes and methods canonly acess within class and its sub class

#private = __name, ___age,___show()

class Student():
    def __init__(self):
        self.__name = "rita"
        self.__age = 66
    def __show(self):
        print(f"{self.__name} and {self.__age}")
    def display(self):
        self.__show()
a = Student()

#print(a.__name) //cannot access naow cause of private
#print(a.__age)
#a.__show()
a.display()


#protected = _name,_age,_show()

class Student():
    def __init__(self):
        self._name = "rita"
        self._age = 66
    def show(self):
        print(f"{self._name} and {self._age}")
    # def display(self):
        # self.__show()
a = Student()

print(a._name) #can be acess 
#print(a.__age)
#a.show()

class B(Student):
    def __init__(self):
        print(a._name)
b = B()


#create a class Student with private
#attributes __id and __grade and a method to display them.

class Student:
    def __init__(self):
        self.__id = 34
        self.__grade = "A"
    def __display(self):
        print(f"Id = {self.__id}\nGrade={self.__grade}")
    def show(self):
        self.__display()
a = Student()
#a.display()
a.show()