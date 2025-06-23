class ShoopingCentre():
    def __init__(self,name,quantity,quality,price):
        self.name = name
        self.quantity = quantity
        self.quality = quality
        self.price = price
    def product(self):
        total = self.quantity*self.price
        print(total)
        print(f"{self.name},{self.quantity},{self.quality} and {self.price}")
obj = ShoopingCentre("Chips",30,"A",10)
obj.product()
    # def product(self,):


#method overriding
#in different class which have inheiretance

class A:
    def show(self):
        print("I am first class")
class B(A):
    def show(self):
        super().show()
        print("I am second class")
b = B()
b.show()

#super() = it is a methods that acess parent class method

