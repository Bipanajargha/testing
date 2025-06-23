# #2) multilevel inheritance
# class A:
#     def first(self):
#         print("i am grand parent")
# class B(A):
#     def second(self):
#         print("I am parent")
# class C(B):
#     def third(self):
#         print("i am child")

# obj = C()
# obj.first()
# obj.second()
# obj.third()

# #3multiple inheritance (mother,father and child)
# class A: #parent
#     def first(self):
#         print("i am father parent")
# class B: #parent
#     def second(self):
#         print("I am mother parent")
# class C(A,B): #child
#     def third(self):
#         print("i am child")

# obj = C()
# obj.first()
# obj.second()
# obj.third()


# #helarchical (Two child one parent)
# class A:
#     def first(self):
#         print("i am grand parent")
# class B(A):
#     def second(self):
#         print("I am parent")
# class C(A):
#     def third(self):
#         print("i am child")

# b = B()
# b.first()
# b.second()

# obj = C()
# obj.third()
# obj.first()


#hybrid inheritance


class A:
    def first(self):
        print("Hello first")
class B(A):
    def second(self):
        print("I am second")
class C(A):
    def third(self):
        print("i am third")
class D(B,C):
    def fourth(self):
        print("I am fourth or child")
class E(D):
    def five(self):
        print("I am five or child")
f = E()
f.five()
f.fourth()
f.third()
f.second()
f.first()

#polymorphism = poly = many morphism = form
#one thing behave different way

#duck type = yeutai kura multiple way ma garna milyo

class MyClass:
    def show(self):
        print("Welcome to name education")
class YourClass:
    def show(self):
        print("Hi i am student")
def display(var):
    var.show()

# a = MyClass()
# a.show()
# b = YourClass()
# b.show()

#another way to print is creating function
a = MyClass()
b = YourClass()

display(a)
display(b)


#2) method overloading (imp) = a class can have more than one method with same name but parameters should be different  cha vani latest or current method le aru lai overload garcha


class A:
    def show(self):
        print("Hello")
    def show(self,a,b):
        print(a+b)
    def show(self,a,b,c):
        print(a+b+c)
    def show(self,a):
        print(a)
a = A()
a.show(5)



class A:
    def show(self,a=None, b= None, c= None):
        if a==None and b==None and c==None:
            print("Hello")
        elif a!=None and b!=None and c==None:
            print(a+b)
        elif a!=None and b!=None and c!=None:
            print(a+b+c)
a = A()
a.show()
a.show(3,4)
a.show(5,6,7)

