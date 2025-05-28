#6)binary data type =memory managements and it handels binary files
# i)bytes = 
# ii)bytearry =
# 
# i) bytes = it generates sequence of numbers, range(0,256),immutable(orignial data not changeable)
# writes in list forms 
a = bytes([1,2,3,4,5,6,7,8,9,10]) 
print(type(a))
print(a)

#indexing and silicing to print but no to update value cause it is immutable
print(a[-5])
print(a[0:5])

#a[0] = 5
#print(a) #it will display error cause of immutable value cannot be update


#bytesarray - it generates sequence of numbers , range(0,256)
#mutable
a = bytearray([1,2,3,4,5,6])
print(type(a))
print(a) # from 9 it will display in the symbolic form

#indexing to update the value or print cause it is mutable
a[3] = 9
print(a)


#boolean data type  = True or False
a = True
print(type(a))

#none data type(last) #absent of value 
name = None
print(type(name))

#Type casting and Type conversion(data conversion)
#data conversion = python interpter
#converts one data type to another

a = 12
b = 12.3
c = a + b
print(c)
print(type(c)) # python interpeter converts the data type means it prints float


#type casting = developer converts one data type to another
a = 34
b = 56.67
c = int(a+b) #according to the developer 
print(c)
print(type(c))

a = "12" #shows error when a = int("rita") means cotation vitra number scha vani we can change to interger but characters or words cha vani we cannot change it to interger

b = "14"
c = int(a+b)
print(c)
print(type(c))



n = [1,2,3,4]
f = [3,4,5,6]
d = tuple(n+f)
print(d)
print(type(d))


a = bool(1)
print(type(a))
print(a)


#input() #inbuilt function asking data from uers

a = input("Enter a your naumber:") #whatever data it takes it shows string form type
print(a)
print(type(a))

a = int(input("Enter a your naumber:")) #whatever data it takes it shows string form type
print(a)
print(type(a))