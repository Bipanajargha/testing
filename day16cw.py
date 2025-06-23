#pass,break,continue is keyword it is called control statement
# #control statement=control the flow execution
# #pass,break,continue   (for,whileloop)

# #pass=it secure space for future use

# for i in range(1,12,1):
#     pass

# print("hello")    

#reserve keyword
# #break=whenever it encounter loop will be terminated

# i=0
# while i<9:
#     print(i)
#     if i==3:
#         break #(0,1,2,3)
#     i+=1

# #contiue=it skip the current situation or condition and jumps to next iteration


for i in range(1,10,1):
    if i%2!=0:
        continue
    print(i) #prints sarisfied navako number




# #secret game

# secret=7
# i=0
# limit= 5
# guess=""
# while i<limit:
#     guess=int(input("enter your guess number :"))
#     if guess==secret:
#         print("user has won")
#         print("do you want to paly agian ?\n1)yes and \n2)no")
#         choice=input("enter your choice :") 
#         if choice=="yes":
#             continue #again it will start 
#         elif choice=="no":
#             break 
#     i+=1
# else:
#     print("your limit is over")      



#atm machine



#check balanace 2)deposite  3)withdraw  4)exit

# balance=20000
# pin=1234
# pin_code=int(input("enter your pin code"))
# if pin_code==pin:
#     while True:
#         print("1)check balanace 2)deposite  3)withdraw  4)exit")
#         choice=input("enter your choice :")
#         if choice=="1":
#             print(f"my balanceis {balance}")
#         elif choice=="2":
#             amount=float(input("enterr your depodite amount :"))    
#             if amount>0:
#                 balance+=amount
#                 print(f"my new balance is {balance}")
#             else:
#                 print("invalid")
#         elif choice=="3":
#             amount=float(input("entetr your wirthdraw amount :"))
#             if amount>balance:
#                 print("insufficeient balance")
#             elif amount<=balance:
#                 balance-=amount
#                 print(f"my new balance is {balance}")
#         elif choice=="4":
#             print("thaanks for visiting")
#             break           
# else:
#     print("your pin is incorrect")