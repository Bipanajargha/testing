# Create a class Student with the following attributes:

# name (string)
# age (integer)
# grade (float)
# Write a method display_details() to print the student's information.

class Student:
    def __init__(self,name,age,grade): #methods
        self.name = name #attributes
        self.age = age
        self.grade = grade
    def display_details(self):
        print(f"Hi, my name is {self.name}.I am {self.age} years old. Grade {self.grade}")
a = Student("Bipana",34,45.5)
a.display_details()



# Create a class Car with the following attributes:

# brand (string)
# model (string)
# year (integer)
# Write a method show_info() to print the car’s details
class Car:
    def __init__(self,brand, model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def show_info(self):
        print(f"Brand:{self.brand}\nModel={self.model}\nYear={self.year}\n")
a = Car("BMW","X5",2022)
a.show_info()

# Create a Python class called Book that has the following attributes:

# title (string)
# author (string)
# pages (integer)
# Write a method called display_info() that prints the book's title, author, and the number of pages.

class Book():
    def __init__(self,title,author,pages):
        self.t = title
        self.au= author
        self.pg = pages
    def display_info(self):
        print(f"Title={self.t}\nAuthor={self.au}\nPages={self.pg}\n")
obj = Book("Starts with us","Coolean hoover", 200)
obj.display_info()


# Create a class BankAccount with the following attributes:
# account_holder (string)
# balance (float)
# Write a method deposit(amount) to add money to the balance and a method withdraw(amount) to subtract money from the balance. Also, create a method display_balance() to show the current

class BankAccount():
    def __init__(self, account_holder, balance):
        self.ac_name = account_holder
        self.balance = balance
    def deposite(self,amount):
        if amount>0:
            self.balance +=amount
            print(f"Deposited amount={self.balance}")
        else:
            print("Enter positive amount")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw amount={self.balance}")
        else:
            print("Enter valid amount")
    def display_balance(self):
        print(f"Current balance={self.balance}")
a = BankAccount("Bipana",5000.89)

a.deposite(400)
a.withdraw(400)
a.display_balance()

#asking user
class BankAccount():
    def __init__(self, account_holder, balance):
        self.ac_name = account_holder
        self.balance = balance
    def deposite(self,amount):
        if amount>0:
            self.balance +=amount
            print(f"Deposited amount={self.balance}")
        else:
            print("Enter positive amount")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw amount={self.balance}")
        else:
            print("Enter valid amount")
    def display_balance(self):
        print(f"Current balance={self.balance}")

amount = float(input("Enter your depostite amount: "))
amount1 = float(input("Enter your withdraw amount: "))

a = BankAccount("Bipana",5000.89)
a.deposite(amount)
a.withdraw(amount1) #arugment what user take variable
a.display_balance()

            