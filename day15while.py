#while loop #goes infinity so while loop is not prefered
#it excute the block of code as long as confition is true
#and terminates whenever condition is false
# while,for = keyword
#range is not used in the while 
#range is used in for because of praticular conditon , range is condition it self
#syntax:
#while condition:
#    #block of code

#while True  #gooes infinite
#    print("hello")

#iteratin\
# i = 0
# while i<8:
#     print(i)
#     if i==4:
#         print("Welcome")
#     i+=1 #step iteration

# #multiplication table
# num = int(input("Enter a number: "))
# i = 1
# while i<=10:
#     print(f"{num}*{i} = {num*i}")
#     i+=1

#write a program that used a while loop to print numbers from 1 to 100.

i = 1
while i<=100:
    print(i)
    i+=1

#WAP to calculate the sum of numbers from 1 T0 50
i = 1
sum = 0
while i<=50:
    sum+=i
    i+=1
print(sum)

#sum of num
i = 2
n = 0
while i<=20:
    if (i%2==0):
        print(i)
    n+=i
    i+=1
print(n)


#reverse 10 to 1
i = 10
while i>0:
    print(i)
    i-=1
