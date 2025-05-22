#list in builts methods
#adding methods
#append() = single data adding
a = [12,34.5,"bipana","ram"]
a.append(23) #for single data
#a.append([23,"hello"]) #goes in same index
print(a)
#print(a[-1][0]) #to print -1 index of 0 index data

#extend()= to add multiple data
a.extend([56,"bipana",45,555,"hari"])
print(a)
#insert()= randomly add in middle
a.insert(2,"seema")
print(a)

#deleting
#pop() = remove last data(only one data can be delete)
a.pop() #defalut delete last value if we give index then it willl delete data of that value
print(a)
#for e.g
a.pop(4)
print(a)

#remove = particular data removes (single data)
#multiple data donot removes
a.remove("bipana")
print(a)

#clear() = it delete all content of list and returns empty list
a.clear()
print(a)

#del is a keywords no methods
#del delete listt
# del a
# print(a)

#sorting
#for int
a =[6,7,8,1,2,3,9]
#a.sort() #for acesding order
a.sort(reverse=True) #for decending order
print(a)

# new variable declare
a =[6,7,8,1,2,3,9]
b = sorted(a) #for acesding order
#b = sorted(a,reverse=True) #for decending order
print(b)

#for string
a = ["apple","pea","helloooooo","pineapplesss"]
a.sort(key=len) #acesding order
a.sort(key=len,reverse=True) #descending order
print(a)

b = sorted(a,key=len, reverse=True) #descending order
print(b)
