#inbuilt module = predefined or precoded
#from vanayra lekhnu pardaina user defined jhai, sidai tanayra leuni so import direct lekhni
#1)
import random
a = random.choice(["rita",20,30,"Bipana"])
# a = random.choice(range(1,9)) #range pani linxa 8 samma
print(a)

b=random.randint(1,10) #diff mmethod of random
print(b)

a=[6,7,8,9,3,2,1]
random.shuffle(a) #position change shuffle gareyra
print(a)

#or #* for all
from random import choice,randint, shuffle
a=choice(range(1,9))
print(a)

b = randint(1,10)
print(b)




#2)
import calendar
a = calendar.month(2025,2) #2025 year 2 month, calander dekhauxa
print(a)

#3)
import keyword #35 keyword dekhauxa -module
a=keyword.kwlist
print(a)
print(len(a))

#4)
import time
a=time.ctime() #current time , second ma dinxa
#local time leyh purai structure sanga dekhauxa
b=time.localtime()
print(a)
print(b)


#ask
#5)
import datetime
a = datetime.datetime.now() #milisecond ma dekhauxa
print(a)

#6)
import sys #recursion- limit check garni (1000 limit)
print(sys.setrecursionlimit(4000))
print(sys.getrecursionlimit)

#7)
import math 
a=math.sqrt(36) #aquare root
print(a)
# b=math.sin(30) # yo matra garda value aaudaina so 30 lai radian ma change change garnu parxa
c=math.radians(30)
b=math.sin(c)
print(b)

d=math.cos(c)
print(d)

# floor le paxadiko sabai value hataidinxa
e = math.floor(34.000001)
print(e)

# ceil le paxadi ko value hatayera ek step mathi ko value dinxa
f=math.ceil(56.0000002)
print(f)

#factorial
g=math.factorial(6)
print(g)

#short method
from math import sqrt,radians,sin,cos,factorial,floor,ceil #sabai leuna cha vani * lekhni yesko satta
a=sqrt(36) 
print(a)
c=radians(30)
b=sin(c)
print(b)
d=cos(c)
print(d)
e =floor(34.000001)
print(e)
f=ceil(56.0000002)
print(f)
g=factorial(6)
print(g)

#alisasing = method lai short form ma garna lai , for lenthy method
from math import sqrt as a
z = a(9)
print(z)

#task cw
import random
num = random.randint(1,100)
print(num)
 
a = ["seema","bipana","phibi"]
random.shuffle(a)
print(a)

import math
m = math.radians(45)
s = math.tan(m)
print(s)

q= math.cos(m)
print(q)

w=math.sin(m)
print(w)