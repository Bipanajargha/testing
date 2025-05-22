my_list = [10,20,30,40,50]
b = my_list[2]
print(b)


new_list = my_list[0:3]
print(new_list)

#string = ["appple","banana","cherry"]
string ="apple,banana,cherry"
b = string.split(",")
print(b)

my_list =[1,2,3]
b =my_list*3
print(b)

a = ["hello",45,46,67,89,45,45,"apple","orange"]
a.append(34)
print(a)

a.extend([23,"hello"])
print(a)

 
print(a[7][0:3]) #add +1 in th end

a.remove("hello")
print(a)

a.clear()
print(a)

a = [2,3,4,"hello"]
b = [34,56,"bipana"]
c = a+b
print(c)

#for num
list = [90,70,60]
list.sort()
print(list)

d = sorted(list)
print(d)

#for string
l = ["seema","bipana","nn"]
l.sort(key=len)
print(l)

f = sorted(l,key=len,reverse=True)
print(f)
