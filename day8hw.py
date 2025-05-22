t = (5,10,15,20,25)
print(t[2])
print(t[-1]) 
print(t[0]) #first element
print(t[-1]) #last element from negative index
 
t=(1,2,3,4,5,6,7,8,9)
print(t[0:4]) #4 elements
print(t[0:6]) #except last indexing

print(t[1::2]) #even
print(t[::-1]) #reverse
print(t[::3]) #3 element extract
print(t[3:6]) #excluding 7 

my_tuple = (10,20,30,40,50) #2nd start
print(my_tuple[2::])

my_tuple = ('a','b','c','d') #len of the tuple
print(len(my_tuple))

tuple1 = (1,2,3,4)
tuple2 = (4,5,6)
tuple3 = tuple1 + tuple2 #concadenate
print(tuple3)

s = {10,20,30,40}
s.add(50)
print(s)

s.remove(20)
print(s)

# s.remove(100)
# print(s)

n =set({})
n.update({5,10,15})
print(n)

