#lambda function = anynoumous function that doesnot have identity
#similar to def function
#jun varible ma store garincha tei function ho eg: a

#syntax: lambda argument:Expression
# a=lambda x,y,z:x+y+z
# print(a(4,5,6))

#def show():
#    id x%2==0

#lambda takes less memory space than def
##fast performance
#it takes less times


#recursion function =  function that calling itself again and again
#recursion function
#limit is 1k

# def show():
#     print("hello")
#     show() # 1k choti repeat huncha or recursion limit is 1k
# show()



# import sys #module sys = recursion limit check

# #to set recursion limmit
# print(sys.setrecursionlimit(3000))
# print(sys.getrecursionlimit())

# def show():
#     print("hello")
#     show() #3000 choti run huncha cause it is seet 3k
# show()

#Two cases recursion
#1) base case(stopping case)
#2) recursion case


# def show(n):
#     print("hello",n)
#     show(n+1) #recursion case
# show(0)

# def show(n):
#     if n==30:
#         return #base case 29 samma print huncha
#     print("hello",n)
#     show(n+1) #recursion case
# show(0)


#factorial = n*(n-1)
#5!=5*4*3*2*1
#1!=1
#0!=1

# def show(n):
#     if n == 0 or n == 1:
#         return 1
#     return n*show(n-1)  #5*4*3*2*1*1 = 120
# print(show(5))

# a = 0
# b = 1
# def fib(a,b):
#     b = a
#     a+b = b


# a = 0
# b = 1


#fibonacci seriest
# def show(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     return show(n-1)+show(n-2)
# print(show(3))

#iterator and iteration difference
#iterator = object that contain countable numbers of value eglist tuple set


# def show(n):
#     return n+2
# n=2
# print(show(n))

#wrong cause normal function cannot concadenate so map inbuilt function is used
# def show(n):
#     return n+2
# n=[1,2,3,4]
# print(show(n))

#inbuilt function

#map() = inbuilt function, that takes function and iterator,
#kam k ho vnad? shows simple map location or address stored
#it applies function to each elements
#syntax: map(Function,iterator)

# def show(n):
#     return n+2
# n = [1,2,3,4]
# a= map(show,n)
# print(list(a))

#lambda argument:expression

a = lambda x:x+2
n = [1,2,3,4]
b = map(a,n)
print(list(b))
#filter()= inbuilt function , that takes function and iterator
# it process according to the condition
#syntax: filter(function,iterator)

# def show(n):
#     if n%2==0:
#         return n #[2,4] satisfied number only takes 
# n = [1,2,3,4]
# a = filter(show,n)
# print(list(a))

a = lambda x:x%2==0
n = [1,2,3,4]
b = filter(a,n)
print(list(b))

#reduce()=inbuilt function, that take function and iterator
# #we have to import
#reduce take 2 arguments
# from functools model

# from functools import reduce
# n =[1,2,3,4,5]
# def sum(x,y):
#     return x+y
# a = reduce(sum,n)
# print(a)
 
#Through lambda
#for reduce donot need to write list
from functools import reduce
a = lambda x,y:x+y
n = [1,2,3,4,5] #1+2 = 3
                #3+3 = 6
                #6+4 = 10
                #10+5 = 15
b = reduce(a,n)
print(b)

#when iterator object aauch teti bela dini
