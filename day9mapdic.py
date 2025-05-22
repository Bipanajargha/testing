#map data type: dictionary = key value pair,
#  mutable(orginal data changeable)
# duplicate key is not allowed
# order and data will not be add randomly
#dictionary is represeted by {} or dict()

a = {}
#or a = dict()
print(type(a))

#syntax:
#  dict_name = {
#   'key':value #quotation is compusalory
#  'key1':value1
#          }
#a = dict(key = value,key1 = value1 ) #no compusalory to give quoation in key

a = {
    'name':"Bipana",
    'age' :12
}
print(a)
print(len(a)) #len 2 means jati ota pair tei ota len

c = dict(name ="bipana", age=45)
print(c)

#acessing value through key 
#method 
#indexing
#get

print(a['name'])

#get
print(a.get('name'))

#main difference between indexing and get is = indexing shows error and get gives none when invalid input is given

print(a.get('address',"There is no any value")) #print the msg so get is more prefred