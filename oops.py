#oops
#object oriented programming System

# oops is an programming language which uses classes and objects to 
# organise in structured data
#oops helps organize code by buliding data and functions together into objects

#class

#it is a blueprint for creating objects
#the plan which is used for creating
#class methods will only work when you give 'self' keyword

class samosa:
    ingredients=["onion","oil","maida","potato"]
    def process(self):
        return "samosa is ready"
s1=samosa()
print(s1.ingredients)
print(s1.process())

#['onion', 'oil', 'maida', 'potato']
#samosa is ready

#object

# an object is a specific instance of a class cretaed using the calss 
# blueprint
# we can create multiple objects by using same classes

class laptop:
    brand="dell"
    ram="16gb"
    storage="512gb"
    price=50000
    def is_working(self):
        return "laptop is working"
l1=laptop()
print(l1.price)
print(l1.ram)
print(l1.brand)
print(l1.is_working())

#output:
# 50000
# 16gb
# dell
# laptop is working


#constructor

# it is a special method which is called automatically when a object is created
# when a object is created then the constructor is called first

class laptop:
    brand="dell"
    def __init__(self,cpu,ram,storage,price):
        self.cpu=cpu
        self.ram=ram
        self.storage=storage
        self.price=price
    def details(self):
        return f"{self.ram,self.cpu,self.storage,self.price}"
    
l1=laptop("i9","64gb","256gb","50000")
print(l1.cpu)
print(l1.storage)
print(l1.ram)
print(l1.details())
l2=laptop("i7","16gb","512gb","40000")
print(l2.cpu)
print(l2.storage)
print(l2.ram)
print(l2.details())

#output:
# i9
# 256gb
# 64gb
# ('64gb', 'i9', '256gb', '50000')
# i7
# 512gb
# 16gb
# ('16gb', 'i7', '512gb', '40000')