def show(n):
    return n*n
n = [1,2,3,4,5]
a = map(show,n)
print(list(a))

a = lambda x:x*x
n = [1,2,3,4,5]
b = map(a,n)
print(list(b))

def show(n):
    if n%10==0:
        return n
n = [10,15,20,25,30]
a = filter(show,n)
print(list(a))


b = lambda x:x%10==0
n = [10,15,20,25,30]
a = filter(b,n)
print(list(a))

from functools import reduce

n = [1,2,3,4,5]
def sum(x,y):
    return x*y
a = reduce(sum,n)
print(a)

b = lambda x,y:x*y
n = [1,2,3,4,5]
a = reduce(b,n)
print(a)



###list comprehensive = it tak3es one list and apply condition and expression on that list and give result in new list 
#memomry space less
# it takes less time 
# it gives clean project
#formula:(Expression for loop if statement)
a = [1,2,3,4]
b = [] #declare garna sikako
# for i in a:
#     b.append(i+2)
#print(b)
#using list comprehensive
[b.append(i+2) for i in a]
print(b)

a = ["sita","gita","rita","ram"]
# a=[f"{(i): len(i)}"for i in a] 
# you can do 
#b = []
# a=[f"{(i): b.append(i) len(i)}"for i in a] 
a=[f"{(i): len(i)}"for i in a] 
print(a)








