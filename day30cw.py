#file handling
#file = pernament but in variable ma = temporary
#file = collection of data or information that stores data permanently

#Types of file
#text file
#binary file  = 0 and 1 means image ,audio ,video
#file handling = operations perform in file such
# create, read, write, append,delete ,close 


#opening the file
#perform operation in file
#close the file

#syntax:
#open('file_name','mode')

#mode 
#x= create
#r= read
#w = write
#a = append

#w = write (overwrite)
#a = append(not to overwrite)


#f = open('msg.text','x')
#f = open('msg.text','r')
# a = f.read()
# #read alll
# a = f.read(4) #characters
# print(a)
# a = f.readline() #only one line read
# a = f.readlines() #read all lines in list form
# print(a)


#for write
# f= open('msg.txt','w')
# print(f.write("Welcomesssss"))#overwrite

# f= open('msg.txt','a') #for append donot overwrite
# print(f.write("Welcomesssss"))

#f.close()
#to close



# f = open('srv.txt','x')
# f = open('srv.txt','r')
# a = f.read()
# a = f.read(4)
# a = f.readline()
# a = f.readlines()
# f = open('srv.txt','w')
# print(f.write("Fggghhg"))
#f = open('srv.txt','a')
# print(f.write("Fggghhg"))



#to delete
# import os
# if os.path.exists('msg.txt'):
#     os.remove('msg.txt')
# else:
#     print("File doesnot exist")



#no need to close
#preferable
#with statement
# with open('msg.txt','a') as file:
#     print(file.write("Hellooolloooo"))



