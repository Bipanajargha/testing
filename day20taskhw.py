# Create a list of odd numbers from 1 to 20 using list comprehension.
odd_num = [x for x in range(1,20) if x%2 == 1]
print(odd_num)


# Generate a list of squares of numbers from 1 to 10.
square = [x*x for x in range(1,11) ]
print(square)

# Given a list [1, 2, 3, 4, 5], create a new list where each element is multiplied by 3.
li = [1,2,3,4,5]
b= []
[b.append(i*3) for i in li]

#or
# b = [i*3 for i in li]
# print(b)

#or
# [f"{(i*3)}" for i in li]
# print(li)  ##wrong
# Given a list ["apple", "banana", "cherry"], create a new list with each word reversed.

fruits = ["apple","banana","cherry"]
r=[i[::-1] for i in fruits]
print(r)


a = [
    "youtube.com",
    "facebook.com",
    "whatsapp.com"
]

a = [i.removesuffix(".com") for i in a]

#donot work
# a = [i.strip(".com") for i in a] removes other letters too 
print(a)


#decorators= function that takes another function argument and add some features and functionality (without  changing code structure) and return to a function

# code reusability
#whre used? authentication, acess control...

#four points to remember
#)1 return type
def show():
    print("hello")
print(show()) # ans will be none cause return is not given

def show():
    print("hello")
    return 8
print(show())

#2) everything in the python is an object 
def show():
    print("hello")
#object
obj = show
obj()

#3) nested function
# def outer():
#     def inner():
#         print("I am inner")
#     print("I  am outer")
#     inner()
# outer()
#output : i am outer and then i am inner

# def outer():
#     def inner():
#         print("I am inner")
#     inner()
#     print("I  am outer")
# outer()
#ouyput
# i am inner and then outer

#4) a function can take another function as an argument

# def outer(a): # this is a formal argument 
#     def inner():
#         print("i am inner function")
#         a() # show()
#     inner()
#     print("i am outer functuin")
# def show():
#     print("I am outside function")
# outer(show) # here we pass function show as an actual arguments

#output i am inner ,i am outside , i am outer 

#use method (@)

def outer (a):
    def inner():
        print("i am inner")
        a()
    return inner
@outer
def show():
    print("I am outside function")
show()

#object oreinted programming =