#sequence data type = list
#list is mutable(original data changeable)
#allow duplicate value
#order
#data is seperated by comma
#square bracket a=[] means list
#position fixed or display data in order
#len of the list = according to number of the data given

#indexing and silicing (when the data type has a positon fixed)
#indexing= postion of data(why use? to extract one , one data or characters)
#syntax: variable_name=[index]
a = [12,35,"sita",12.34,"bipana",34]
print(a)
print(type(a))
print(len(a))
print(a[1]) #only print data index
print(a[2][0]) #to print index of data inside character index

#slicing : acessing the part(means i want 3 data in once) of the list
#syntax: variable_name[start:end:step] = +1 at end from froward =-1 in end backward
print(a[0:3:1])

print(a[::])#to print all
print(a[::-1]) #reverse
print(a[::2]) #increasing by how many step
print(a[2][0:3:1]) #string part
print(a[4][0:3])

#allow duplicate value
b=[12,12,12,12,"hello","hello",78.78,78.78] #it takes duplicate
print(b)
print(len(b)) #it counts duplicated data also

#mutable(orginal value or data changeable)
b[0] = 45
b[5] = 34
print(b)#changes orginal data