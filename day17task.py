#Write a Python function called print_square that takes a number as an argument and prints the square of that number.

a = int(input("Enter a number: "))
def print_square(a):
    a *=a
    print(a)
print_square(a)


#Write a Python function called print_list_elements that takes a list as an argument and prints each element in the list one by one

l = ["Hello",1,2,3]
def print_list_elements(l):
    for list in l:
        print(list)
print_list_elements(l)


#  Write a Python function called multiply_by_two that takes a number as an argument and prints the number multiplied by 2

num = 2
i = 1
def multiply_by_two(num,i):
    while i<=10:
        print(f"{num}*{i} = {num*i}")
        i+=1
multiply_by_two(num,i)

# Write a program to create a function that takes two arguments, name and age, and print their value.
name = input("Enter your name ")
age = int(input("Enter your age"))
def about_me(name,age):
    print(f"My name is {name}")
    print(f"I am {age} years old ")

about_me(name,age)
#about_me(age,name) #from user input then....
# Write a program to create function func1() to accept a variable length of arguments and print their value.
def func1(*a):
    for i in a:
        print(i)
func1(1,2,"Blueberry")

# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction
a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
def calculation(a,b):
    sum = a+b
    print("Addition",sum)
    sub = a-b
    print("Subtraction",sub)
calculation(a,b)

 