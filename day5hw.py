#upper
a = "bipana"
b = a.upper()
print(b)

#lower()
c= b.lower()
print(c)

#swapcase()
name = "hello, my name is BIPANA"
b = name.swapcase()
print(b)

#capitalize
b= name.capitalize()
print(b)

#startswith
b= name.startswith("hello")
print(b)
#endswith
b=name.endswith("NA")
print(b)

#count()= how many characters
var ="my name is"
c= var.count("m")
print(c)

#find() = index num
c = var.find("m", var.find("name"))
print(c)

#index = improved version of find
c= var.index("m", var.index("name"))
print(c)

#replace()
college_name = "I read in ISMT"
a = college_name.replace("ISMT","Name")
print(a)

#strip()= to remove space
greet = " Welcome to nepal "
b = greet.strip()
print(b)

#prefix
n = "!!wel! come!!"
m = n.removeprefix("!")
print(m)

#sufffix
m = n.removesuffix("!!")
print(m)

#centre
c = "Welcome to nepal"
d = c.center(75,"!")
print(d)