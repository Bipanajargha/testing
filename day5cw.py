#inbuilt method of string
#to call the method use . 
#string is immutable= orginal value cannot be changed
#1st methods
#a.uppper 
#upper() = it change string into uppercase

# a ="bipana"
# a.upper()
# print(a) #donot change cause it is immutable
#but 

a= "bipana JARGHA"
b = a.upper()
print(b)

#lower
c= b.lower()
print(c)
#swapcase = convert lower to upper and upper to lower
b= a.swapcase()
print(b)

#Capitallize() = converts alll character itno lower and make only 1st word 1st letter capital
b= a.capitalize()
print(b)
#startswith() = check the 1st word or letter that start
b = a.startswith("b")
print(b) #if yes print true or false
#b = a.startswith("B") false cause python is case sensitive

#endswith() = check last character or words
#b= a.endswith("A")
b= a.endswith("a")
print(b)

#count()= count no of  character or words in the given string
b=a.count("n") #if there is none it display 0
print(b)

#find() = it findss index
na = "my name"
# e =name.find("m") #gives index of 1st m
# print(e)
e = na.find("m",na.find("name")) #which part of the m so!
print(e)

#navako words or character diyo vani it prints -1 which is wrong so new method is introduced 
#i.e index() = improved version of find (which shows error when character is not given)\


#index()
# b = a.index("z") #shows errors
# print(b)

#replace() = replace character or word of the string value 
var = "i read in ismt"
b= var.replace("ismt","name")
print(b)

#strip() = To remove space of front and back of the string
a ="!!Wel! come!!"
b = a.strip("!") #remove back and front of the symbol by only writing one symbol
#b = a.removeprefix("!!") #have to give num of symbol to remove(front) 
#b = a.removesuffix("!!") #same as prefix but it remove at back
print(b)

#center() = mid ma layuni kam garcha when we give between how many characters

var = "Welocome to nepal"
print(var)
print(len(var))
b= var.center(60,"!") #including the characters of var(17) it display string value in middle within the 60 characters.
print(b)

#day6
#split()
a ="apple banana orange"

b= a.split() #show string data in list type 
print(b)

c= "apple,banana,orange"
b=a.split(",")
print(b)