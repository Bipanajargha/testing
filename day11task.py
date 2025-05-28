a = {
    "name":"bipana",
    "id" : 45,
    "salary": "35k"
}

product = {
    "name": "Laptop",
    "price":800,
    "brand": "Dell"
}
print(product["brand"])
product["price"] = 900
print(product)

product ["stock"] = 50
print(product)

product.pop("brand")
print(product)

print(len(product))
print(tuple(product))
#print(product.items())

dict1 ={"a":1, "b":2}
dict2 = {"c":3, "d":4}
dict1.update(dict2)
print(dict1) #merge


print(list(product.keys()))
print(list(product.values()))

var = [["id",2],["dem",56.7]]
print(dict(var))

data = [["name", "Alice"], ["Age", 25],["city", "Paris"]]
print(dict(data))


data = (("name", "bob"),("age",30),("country", "USA"))
print(dict(data))
print(tuple(data))
