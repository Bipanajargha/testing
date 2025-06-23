#condtion statement = making decision based on the value of variables


# 4 spaces is called indentation
# syntax
# if condtion:  #comparison or relation operator
# 4space(indentation)     # block of code
#elif: to add  more contions
#else : no condition need



# price = 56
# if price<24:
#     print("Is greater")

# else:
#     print("Is smaller")


# #ticket system
# # a = "Welcome to our bus"
# # print(a.center(70,"!"))

# # age =int(input("Enter your age: "))
# # if age<=12:
# #     print("you have to pay 20rs")

# # elif age<=18 and age >12:
# #     print("You have to pay rs 50")

# # elif age<=40 and age > 18:
# #     print("your have to pay rs80")
# # else :
# #     print("You have to pay 100rs")

# #nested if  means if inside if
# a = "Welcome to our bus"
# print(a.center(70,"!"))

# age =int(input("Enter your age: "))
# if age<=12:
#     print("you have to pay 20rs")

# elif age<=18 and age >12:
#     print("You have to pay rs 50")

# elif age<=40 and age > 18:
#     if age==25:
#         print("no need to pay")
#     else:
#         print("your have to pay rs80")
# else :
#     print("You have to pay 100rs")



# #only one if then (shorthand if) means:
# a = 34
# if a>12:print("a is greater")

# #shorthand #else if
# a=4
# b=7
# print("a is smaller") if a<b else print("b is greater")



# num= int(input("enter a number: "))
# if num%2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

#WAP that takes a score as input

user_marks = int(input("Enter your marks"))
if user_marks>=90 and user_marks<=100:
    print("Grade A")
elif user_marks>=80 and user_marks<=89:
    print("Grade B")
elif user_marks>=70 and user_marks<=79:
    print("Grade C")
else:
    print("Grade D")

