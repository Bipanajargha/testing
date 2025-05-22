#range()= sequence data type
#it generates sequence of numbers,order
#syntax: range(start,end,step)
#for loop ma huncha

a= range(10) #only one data given then end = 10, default start =0,end=1
             #0 1 2 3 4 5 6 7 8 9
#to print range we need loop
b = range(2,11,1)
print(b) #gives in same pattern
#for reverse
c = range(5,0,-1)#5 4 3 2 1

#indexing
d = range(10) #0 1 2 3 4 5 6 7 8 9
print([-1]) #8
print([0]) # 0

#slicing variable_name[start:end:step]
print(a[2:6:1])
print(a[-4::])
#print(a[-4:10:1])