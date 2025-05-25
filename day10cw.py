#methods of dicnatory
a = {
    'name' : 'rita',
    'age' : 89
}
#mutable(original data changeable)
a['name'] = "sita"
a['age'] = 45
print(a)

#order = prints values in order or if we addd new value it will print it in last
# a['address'] = 'butwal'
# a['email'] ="bipanajargha@gmail.com" #for adding value one at a time
# print(a)

#1}update = to add multiple pair at once
b = {
    'email' : "bipanajargha199@gmail.com",
    'subject' : 'computer',
    'age':90,
}
a.update(b)
print(a)

#del is keyword
del a ['name']
print(a)

#2)another method pop() = removing the value according to the given 

a.pop('email')
print(a)

#3)popitem() = removes last
a.popitem()
print(a) 
 
print(a.keys())
print(a.values())
print(a.items())
print(a.sum())