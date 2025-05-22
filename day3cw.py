#len()= to know the length of character
#index= postion of variable syntax: variable_name[1 
name= "my name is bipana"
print(len(name))
mid = len(name)//2-1
mid2 = len(name)//2 +1
result = mid // mid2
print(name[result])

#print((len//2-1)/(len//2+1))
# mid = len//2
# print(mid)

#sclicing=acessing the part of the string
#syntax: varuable_name(start:end:step)
a="My name is bipana"
print(a[3:7]) #end value +1 #if i donot write the step default value is 1

#reverse
print(a[6:2:-1]) #end value -1 and # index -1 decreasing

print(a[::]) #using slicing
print(a[::-1]) #for reverse

print(a[2::]) #including 2 index(start) print all 
print(a[:7]) #end = 7 from 0 to 7 only take 

print(a[::1]) #gives normal as 1 is default
print(a[::2])