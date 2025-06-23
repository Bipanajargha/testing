#multiplication
# a = int(input("Enter a number: "))
# for i in range(1,11,1):
#     print(f"{a}*{i} = {a*i}")

for i in range(1,11,1):
    print(f"{i}^2 = {i**2}") #no cap for python= power =double astrick

for i in range(2,21,2):
    print(i)

sum = 0
for i in range(1,51,1):
    sum+=i
print(sum)

  
n = 0
for i in range(1,101,2):
    n+=i
print(n)

print(" ")
list = [2,8,1,16,5,23,7]
largest = list[0] #suppose
for i in list:
   # print(i)  
    if largest< i: #2<2#2<8<1 8<16<5 16<23<7
        largest = i #2 6 16 23
        print(largest)
print(largest)







