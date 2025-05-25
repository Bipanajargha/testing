student = {"name": "Alice", "age": 20, "grade": "A"}
print(student['age']) #acess value of age
student['grade'] = "A+" #changeing value of grade
print(student)
student['city'] = "New york" #add new key
print(student)

#to delete 
student.pop('age')
print(student)


#merge or adding multiple values
dict1 = {"a":1, "b":2}
dict2 = {"c":3, "d":4}
dict1.update(dict2)
print(dict1)


#acessing the values of the nested dictionary
data = {"person": 
        {
            "name": "Jhon",
              "info":
              {
                  "age":25, 
                  "city":"london"
              }
        }
    }
print (data["person"]["info"]["city"])
print(data["person"]["info"]["age"])
