#operator = symbols that performs operations between operands
#a + b
#there are 7 types of operator in python 

#1) Arithematic operator 
#addition, subtraction, multiplaction,divide,modulus(%)
#power, floor(//) first divide but donot take decimal value
# a = int(input("Enter a first number: "))
# b = int(input("Enter a second number: "))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)#remainder modulus #numenator is small then denometer than it will give numenator
# #for e.g : 2%4 ans 2
# print(a**b) #power
# print(a//b) #floor(it does not take decimal)

#2)Relational operator and comparision operator(<,>,==,<=,>=,!=)

a = 23
b = 56
print(a<b) #prints true
print(a>b) #prints false
print(a==b) #false
print(a!=b) #true
print(a>=b) #false
print(a<=b) #true

#3)assignment operator (=, single =(assign value), += ,-=,*=,/=,%=, **=)
a = 56
a +=1 #a = a+1
a -=3
a *=4
print(a)

#4) logical operator(and,or,not)
#and = both operand should be true to return true in the result
#or = it returns true whenever one operand is true

a= True
b= False
print(a and b)
print(a or b)

#not = reverse true=false, false = true
print(not(a))
print(not(b))


#5) Membership operator (in, not in)
a = "My name is amisha"
print("my" in a) #false cause m is small letter
print("My" in a) #true

print("my" not in a) #check the value not have
print("My" not in a)

#6) Identity operator(is, is not)
# a = 20
# b = 20
a = [1,2,3]
b = [1,2,3]
print(id(a)) #gives location address
print(id(b))

print(a is b) #memory location tracker
#difference 
print(a==b) # exact value of variable

#7) Bitwise operator(&,|, ~, ^)
#it takes integer and converts ineteger into binary
# and perform operation in bit
a = 12 #1100
b = 13 #1101

#& (and)
#1100
#1101
#output
#1100
print(a & b)

# | (or)
a = 11 #8 4 2 1 
       #1 0 1 1
#b = 14 #1 1 1 0
b = -14

#1011
#1110
#output
#1 1 1 1
print(a|b)


# negation (~) #1's complement
#~n =-(n+1) #2's complement
print(~(a))
print(~(b))

#xor (^) exclusive
# it returns true when both operand different 
# and returns false when both operands is same
a = 12
b = 13
#1100
#1101
#output
#0001
print(a^b)


a = 9 # 8 4 2 1 # 1001
b = 11 #1011

#1001
#1011
# 1001 # 9
print(a & b)

# for or |
#1001
#1011
#1011 #11
print(a | b)

#negation (~)
# 9 = -(9+1) = -10
#11 = -(11+1) = -12
print(~(a))
print(~(b))

#xor (^)
#1001
#1011
#0010
print(a ^ b)

a = 8 # 8 4 2 1 # 1000
b = 13 #1101
#1000
#1101
#1000 8

print(a&b)

#for or |
#1101 13
print(a|b)

#negation(~)
print(~(a))
print(~(b))

#xor ^
#0101 5
print(a^b)

a = 12 # 8 4 2 1 = 1100
b = 15 #1111
#1100 12
print(a&b)

#or |
#1100
#1111
#1111 15
print(a|b)

#negation
print(~(a))
print(~(b))

#xor ^
#0011 #3
print(a^b)

