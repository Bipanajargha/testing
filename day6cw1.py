fruits = ["apple","banana","cherry","date","elderberry"]
print(fruits[0]) #apple
print(fruits[-1]) #elderberry
# print(fruits[0])
print(fruits[2]) #cherry

numbers =[10,20,30,40,50,60]
print(numbers[2]) #third element
print(numbers[-1]) #last element
print(numbers[4:6:1]) #second last to last element

colors =  ["red","green","blue","yellow","purple","orange"]
print(colors[0:3:1]) #extract 1st 3 elements
print(colors[4:6:1]) #last tewo elements
print(colors[::2]) #every second element
print(colors[::-1]) # reverse

letters = ["a","b","c","d","e","f","g","h"]
print(letters[2:5:1]) #extract cde
print(letters[0::2])# etract aceg
print(letters[::-2]) #reverse extract h fd b

numbers =[1,2,3,4,5,6]
numbers[2] = 99 #to replace or change number 
print(numbers)

words =["Python","is","a","great","programming","language"]
print(words[1:4:1]) #extract is a great
print(words[::-1]) #reverse the word