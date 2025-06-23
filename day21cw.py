#oop= object oriented programming , complex structure or complex program into simpler program
# it  is used to map real world concept or entity
#oop uses class and object
#class = blueprints of object or templates of creating object
#class has attributes and methods

#class reserved word 

#syntax: 
#class ClassName:
      #attributes and methods
#Object = instance of class
## syntax:
# object_name = ClassName()

#attribute it reoresents variable that stores data or value
#methods = similar to function that perform task
#default parameter = self it contains current object(self must)

# # class Student:
# #     def show(self):
# #         print("hello")
# # ram = Student()
# # ram.show()


# #_init_ = dunder function(_) or magic function(automaticalyy called) or constructor
# #It is a constructor it is automatically called when object of class is created
# #it initilizes variables


# #class vitra ko varible lai attribute vanincha
# class Person:
#     def __init__(self):
#         print("Hii")
# o=Person()


class Person:
#     #__init__ ,show means methods
#     #self le current object lai acess garcha
    def __init__(self,name,age): #name self parameters
        self.nm = name #self.nm is variable means inside the class attributes 
        #and name means parameters must match mathi ko
        self.ag = age
    def show(self):
        print(f"My name is {self.nm} and I am {self.ag} years old")

a = Person ("rita",9) #value assign #a is object because person is class
a.show()
# #when _init or contruction value parameters declare garnu vacha vani class ko name ma value pass garnu parcha

# #to access the attributes
# #class vitra methods through
# #class bahira object through

# #acessing attributed outside the clss
# #object_name.variable name
# class Person:
#     #__init__ ,show means methods
#     #self le current object lai acess garcha
#     def __init__(self,name,age): #name self parameters
#         self.nm = name #self.nm is variable means inside the class attributes 
#         #and name means parameters must match mathi ko
#         self.ag = age
#     def show(self):
#         print(f"My name is {self.nm} and I am {self.ag} years old")

# a = Person ()
#  #value assign #a is object because person is class
# print(a.ag)
# print(a.nm)
# a.show()





class Person:
    def __init__(self):
        self.nm = "Rita"
        self.age = 34
        #to acess varible or attirubes inside the class in through creating we methods
    def show(self):
        print(f"{self.nm}{self.age}")
a= Person()  
a.show()

ob = Person()
ob.show()

syma = Person()
syma.show()


#attributes
#types
#instance variable   class variable   static variable
#methods types
#instance method   class method  static variable


#instance method = each object has its own variable file . if  we change variable in one object it is applied for that object only

#in one object it is applied for that object only 
#it is defined and initialize using self parameters


#instance method
class Person:
    def __init__(self):
        self.nm = "Rita"
        self.age = 34
    def show(self):
        print(f"{self.nm} {self.age}")
a= Person() 
a.nm = "Bipana" #a object ma matra change huncha because of self parameters
a.show()

ob = Person()
a.age = 86
ob.show()

syma = Person()
syma.show()



