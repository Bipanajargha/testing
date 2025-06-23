#function = block of code that is exceuted whenever it is called
#code resuable
#code maintaibility

#two types 
#inbuilt function
#user defined function

#inbuilt function = pre coded or predefined
#print(),type(),len(),set(),list(),max(),sum()

#when there is same value
# print (max(-0.0,0.0)) #same but answer will show -0.0 cause it will hit first
# print(max(0.0,-0.0)) #0.0
# print(max(1.0,1)) #1
# print(min[True,2,3,4,False]) #ans false =0

#user defined = user ley define garni function
#syntax :
#def function_name:
     #block of code
#call function (function_name())

# def show():
#     print("Hello")
# show()

# def my_function():
#     a=9
#     b=7
#     print(a+b)
# my_function()


#Can be done in next way by passing arguments and parameters

#Two types of argument

#formal arugument = when funtion is define written
#actual arugment = when function call garda use huni

#example:
#def show(argument = formal arguments):
#   #block of code

#show(argument = actual argument)


# def show(a,b):
#     sum = a+b
# show(2,3)



# def display(name, age):
#     print(f"my name is {name}")
#     print(f"my age is {age}")
# display("Amisha",56) # call garda balla value assign huncha


# #cam take input from user 

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# #input function ma nalekehni cause it is called

# def dis(name,age):
#     print(f"my name is {name}")
#     print(f"my age is {age}")
# dis(name, age) #take input from user and goes to up the def dis and then display...

# def dis(name,age):
#     print(f"my name is {name}")
#     print(f"my age is {age}")
# dis("Bipana", 34)  #it will display down one bipana,34 cause


#Types of arguments
#1) positional arguments
#2) keyword arguments
#3) default arguments
#4)Arbitary arguments

#1) postional arguments = have call in exact postion

# def show(name,age):
#     print(f"my name is {name}")
#     print(f"my age is {age}")
# dis(34, "Bipana") #wrong

# #so,

# #2) keyword arguments: call by keywords
# def show(name,age):
#     print(f"my name is {name}")
#     print(f"my age is {age}")
# dis(name = "Bipana",age = 34) #or
# dis(age = 34, name = "Bipana") #display in same position

# #3) default arguments = value is defined when funtion is defined and default must be last value
# def show (name,age = 34):
#     print(f"my name is {name}")
#     print(f"my age is {age}")
# dis(name = "Bipana") 


# #4) arbitary arguments
# #i) arvitary postions = * , accept the value in the function directly
# def show(*a):
#     print(a)
# show(1,2,3,"hello")

# #ii) arbitary keywords = **

# def show (*a,**n): #args, kwargs first value args and then kwargs rule
#     #print(a)
#     for i,j in n.items:
#         print(i,j)
# show(1,2,3,"hello",name = "Bipana",age = 34)

# #return function = it returns value and exit the function

# def display():
#     return 3
# #display() wrong 
# print(display()) #right becuse when we write return function then must use print when calling function


# #return pachi lekheko kura excuted hunna

# def display(n):
#     print("hello")
#     return n*7+4 #it terminates the loop
#     print("WElcome") #this will not be print cause of return 
# #display() wrong 
# print(display(9))



a =int(input("Enter a first number: "))
b =int(input("Enter a second number: "))

def calculation(a,b):
    user_choice = input("Enter + - * /: ")
    if user_choice == "+":
        sum = a+b
        print(sum)
    elif user_choice == "-":
        sub = a-b
        print(sub)
    elif user_choice == "*":
        multi = a*b
        print(multi)
    elif user_choice == "/":
        divide= a/b
        print(divide)
    else:
        print("Invalid choice")
calculation(a,b)