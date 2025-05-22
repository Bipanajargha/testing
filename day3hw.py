s = "HelloWorld"
print(s[0]) #1st character
print(s[-1]) #last character using negative index
print(s[4]) #4th character
print(s[-2]) #2nd last character using negative index

a = "Python"
print(len(a)) #finding length of the string
mid = len(a)//2-1
#formula for the even len
mid1 = len(a)//2 + 1
print(a [mid : mid1]) #mid = t, mid1=h
print(a[mid]) #index of the middile character

s = "Programming"
print(s[0:5:]) #from 1st 5 charachter but index start from 0
print(s[7::]) #last 4 character
print(s[2:7:]) #including 2 and 6
print(s[3:6]) #exlude 2 and 6
#extract gram
print(s[3:7:])


#second character
s = "abcdefghij"
print(s[::2])
print(s[3:8:2]) #dhf

#reverse usinf slicing
print(s[::-1])
print(s[1:9])#expect first and last
print(s[1:10:3]) #every third character from 1 to 9

s = "DataScience"
print(s[4:7:]) #sci  


