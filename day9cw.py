#set methods
#1)union()
a = {1,2,3,4}
b = {2,4,5,6,7}
var = a.union(b)
print(var)

#2)intersection
var1 = a.intersection(b)
print(var1)

var2 = b.intersection(a)
print(var2)

#3)difference
# for only a or a-b
var3 = a.difference(b)
print(var3)

#for only b or b-a
var4 = b.difference(a)
print(var4)

#4)symmetric_difference = similar value will be exlcuded and print remaing value
var5 = a.symmetric_difference(b) #2,4 will be removed
print(var5)


#5)issuperset
var6 = a.issuperset(b)
print(var6)

#6)issubset
var7 = a.issubset(b)
print(var7)

#7)isdisjoint
var8 = a.isdisjoint(b)
print(var8)

#frozen set = immutable(original data not changeable)
a = frozenset({1,2,3,4})
print(type(a))
print(a)

#a.add()cammpt be done cause of immutable
b= a.union({4,5,6,7})
print(b)

c = a.intersection({2,4,6,8})
print(c)