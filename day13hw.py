# #WAP that asks the use to input a number and check odd or even
# a = int(input("Enter a number: "))
# if(a % 2 == 0):
#     print("Input number is even")
# else:
#     print("Input number is odd")

# #WAP to check a eligible to vote (age 18 or above to vote)
# age = int(input("Enter your age: "))
# if(age >= 18):
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")
# #or
# #print("Eligible to vote ") if age >=18 else print("Not eligible to vote")

# #WAP to print largest number among 3 numbers
# num1 = int(input("Enter a first number: "))
# num2 = int(input("Enter a second number: "))
# num3 = int(input("Enter a third number: "))
# if(num1>num2 & num1>num3):
#     print("num1 is greatest")
# elif(num2>num1 & num2>num3):
#     print("Num2 is greatest")
# else:
#     print("Num3 is greatest")
    
# #WAP to print leap year 
# year=int(input("Enter a year: "))
# if(year%4 == 0 and year%100 != 0) or (year%40 == 0):
#     print("Year is a leap year")
# else:
#     print("Year is not a leap year")

#WAP to simple calculator
string= "Calculator"
print(string.center(70,"!"))
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
print("Choose Addition,Subtraction,Multiplication,Divide")
s_choice = str(input("Choose:Add/Sub/Multipli/Divide: "))
if(s_choice == "Add"):
    print("Sum is:",num1+num2)
elif(s_choice== "Sub"):
    print("Subtraction is:",num1-num2)
elif(s_choice== "Multi"):
    print("Multiplication is:",num1*num2)
else:
    print("Divide is:",num1/num2)

num = int(input("Enter a number"))
if(num%3==0 and num%5==0):
    print("FizzBuzz")
elif(num%5==0):
    print("Fizz")
elif(num%3==0):
    print("Buzz")
else:
    print(num)

# Given two variables x = 15 and y = 20, use conditional statements to print which variable is larger, or if they are equal.
x = 15
y = 20
if(x>=y):print("x is larger")
else:
    print("y is number")
#  Given a variable num = 7, use a conditional statement to check if the number is even or odd and print the result. 
num = 7
if(num%2==0):
    print("Number is even")
else:
    print("Number is odd")
# Write a Python Program to Check weather a candidate Eligible for Vote or not. 
# Write a Python program to check weather Given Number is Divisible by 7 or Not.
num = int(input("Enter a number "))
if(num%7==0):
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7")
# Check if the value 10 is not present in the tuple t = (5, 15, 20, 25).
t = (5,15,20,25)
print(10 is not t)
# Determine if the value 25 is present in the list lst = [10, 20, 30, 40, 50] using a simple conditional statement
lst = [10,20,30,40,50]
print(25 is lst)
# Check if the value 100 exists in the set s = {50, 75, 100, 125}.
s = {50,75,100,125}
print(100 in s)