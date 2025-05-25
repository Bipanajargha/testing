#average percentage of a std
std = {
    'Math': 90,
    'Science': 80,
    'Nepali' : 30,
    'Computer': 95,
    'Health' : 56,
    'Programming': 45
}
b = sum(std.values()) #sum inbuilt function 
print(b)

c = len(std) #to find length of the dictanory
print(c)

avg = b/c #total divide by length 
print(avg)


#nested dictionary
student = {
    'dic1': {
        'name': "bipana",
        'age' : 78
    },

    'dic2' : {
        'name': "reena",
        'age' : 16
    }
}
print(student)


student['dic1']['name'] = 'hari' 
#acess through indexing
print(student)

student['dic1']['address'] = 'butwal' #to add through 
print(student)

print(student['dic2']['age'])