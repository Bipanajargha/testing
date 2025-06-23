#f = open ('sr.txt','x')
# f = open ('sr.txt','r')
# a = f.read()
# print(a)

# f = open ('sr.txt','a')
# print(f.write("Python is fun"))

# f = open('sr.txt','r')
# a = f.readlines()
# print(a)

# import os
# if os.path.exists('sr.txt'):
#     os.remove('sr.txt')
# else:
#     print("File doesnot exists")


with open('msg.text','r') as file:
    a = file.readlines()
    print(a)
    print(len(a))

