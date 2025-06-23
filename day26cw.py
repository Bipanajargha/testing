#abstraction= hiding complex implementation
#and showing only what user request
#what it does we can see but how it does cannot be sen
#there are 2 types i.e:

#abstract class and abstract method
#abstract method = it is declared but doesnot have impelemnation

from abc import ABC,abstractmethod #ABC abstract class ,abstractmethod decorater
class A(ABC):
    #if two or more abstarct methods then it is interface and 
    #if mix of abstractmethod and concrete then it is a abstract class
    @abstractmethod
    def show(self):
        pass
    @abstractmethod
    def display(self): #only ine abstraction means concerete more than one interface
        pass
    # def display(self): #without abstraction it is a concerete 
    #     print("Hello my name ")
class B(A):
    def show(self):
        print("HIi")
    def display(self):
        print("Hellll")
    def hello(self):
        print("Nooo")
b = B()
b.hello()
b.display()


