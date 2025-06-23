#loop = repeating something over and over
#until particular condition is stastified
a = "Welcome"
#print(a*10)

#two types of loop
#for loop 
#while loop

#for loop = repeating something over and over 
#until particular condition is satisfied

#range() = sequence data
#syntax: range (start,end,step)
# a = range(10) #end=10, default start =0,step=1
#print(a)

#for loop syntax:
#for index in variable_name(condition):
#    (indentation)#block of code

#vertically
for a in range(10):
    print(a)
#for horizontally
for a in range(10):
    print(a, end= " ")

for a in range(10):
    print(a) 
    if(a==3): #print after 3  
        print("Age")

for a in range(1,10,1):
    if(a==4):
        print("Hello")
    print(a)
    

for i in range(7,0,-1):
    print(i) #printn7654321

a=["sita","hari","gita","ram"]
for i in a:
    print(i) #sita
    for j in i: #sita ..s i t a #Hari ..H a r i
        print(j)
    