s = set({10,20,30,40,50})
s.add(60)
print(s) #to add

s.remove(20)
print(s) #to remove

print(len(s)) #lenght of set s

a = {1,2,3,4} 
b = {3,4,5,6}

c = a.union(b) #union of a and b
print(c)

d = a.intersection(b) 
print(d)

e = a.difference(b)
print(e)

f = b.difference(a)
print(f)

g = a.symmetric_difference(b)
print(g)

h = b.symmetric_difference(a)
print(h)

var = a.issubset(b)
print(var)

var1 = a.issuperset(b)
print(var1)

var3 = a.isdisjoint(b)
print(var3)

set1 ={1,2,3}
set2 = {1,2,3,4,5}
var4 = set1.issubset(set2)
print(var4)

set1 = {1,2,3}
set2 = {3,4,5}
a = set1.difference(set2)
print(a)

set1 = {1,2,3}
set2 = {2,3,4}
b = set1.union(set2)
print(b)

s = {1,2,3}
s.remove(3)
print(s)

student = {
    'name': "Alice",
    'age': 20,
    'grade': "A"
    }
print(student.get("age"))
print(student.get("grade")) 