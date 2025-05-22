#set data type = set
#collection of data, mutable(orginal data changeable)
#doesnot allow duplicate values
#unorder or randomly print and postion not fixed , so no index and silicing donot have
#represtation of the set is {} but have to keep value inside it{1} 
# or set()
#if empty{} dic
a={1,56,7}
#or a= set({1})
print(type(a))

b = {23,"hhh","hrrr",45,35}
print(b)
#or
c = set({24,45,"seema",445,"bipana",445,445,445,"bipana"})
print(c)

#len duplicaate value donot count
print(len(c))


#why mutable
#set inbuilt methods

#adding methods
# 1) add() = single data adding
a.add(87)
print(a) #but randomly gayera bascha 

#2) update()= to add multiple data in set 
a.update({45,67,"hhhh"})
print(a)

#deleting methods
#1)pop() = delete random data of printing data 
#WE can see which data is goint to be remove
print(a.pop())
a.pop()
print(a)

#2) remove = particular data removes
a.remove("hhhh") #if we want to remove not given data then it shows error
print(a)

#discard()=particular data remove
a.discard(87) #it donot show error when trying to discard invalid data
print(a)

#difference remove and discard

#clear()= all data of set will be romve
a.clear()
print(a)

del a #removes whole set
print(a)
