class goa:
    name = " "
    drink = " "
    def party(self):
        print("lets party.....")
    def beach(self):
        print("Enjoying the beach....")  
          
ramesh = goa()
suresh = goa()

ramesh.name = "Ramesh"
suresh.name = "Suresh"

ramesh.drink = "Yes"
suresh.drink = "No"    

print(ramesh.name)
print("Drink : ",ramesh.drink)  
print(suresh.name) 
print("Drink : ",suresh.drink)

ramesh.party()
suresh.beach()



class Laptop :
    Price = 0
    Processor = " "
    Ram = " "

hp = Laptop()
dell = Laptop()
Lenovo = Laptop()

hp.Price = 60000
hp.Processor = "i5"
hp.Ram = "8GB" 

dell.Price = 50000
dell.Processor = "i6"
dell.Ram = "6GB"   

Lenovo.Price = 40000
Lenovo.Processor = "i6"
Lenovo.Ram = "4GB"

print(hp.Price)
print(hp.Processor)
print(hp.Ram)
print(dell.Price)
print(dell.Processor)
print(dell.Ram)
print(Lenovo.Price)
print(Lenovo.Processor)
print(Lenovo.Ram)



class laptops :
    def __init__(self):
        self.ram = " "
        self.process = " "
    def display(self):
        print("ram:" , self.ram)  
        print("process :",self.process)
        
hp = laptops()
dell = laptops()

hp.ram = "8gb"
hp.process = "i5"
dell.ram = "6gb"
dell.process = "i4"

hp.display()
dell.display()


class Student : 
    def __init__(self):
        self.name = " "
        self.age = " " 
    def display(self):
        print("Name : ", self.name)  
        print("Age : ", self.age)   
        
s1 = Student()
s2 = Student()

s1.name = "mohan"  
s1.age = "20"
s2.name = "ram"
s2.age = "21"  

s1.display()
s2.display()      


class fruit : 
    def __init__(self , col):
        self.color = col
apple = fruit("red")  
print(apple.color)            


class teacher :
    def __init__(self , name , reg):
        self.name = name
        self.reg = reg
    def display(self):
        print("Name: ",self.name)
        print("Reg no:",self.reg)  
t1 = teacher("mohan" , "101")    
t2 = teacher("nithin" , "102")   

t1.display()
t2.display()  


class calculator :
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
    def add(self):
        print("Add:",self.num1+self.num2)    
obj1 = calculator(10,2)  
obj1.add()      



#instance variable
#class variable
class phone :
    chargerType = "C-Type"  #class variable
    def __init__(self, Brand , Price):
        self.brand = Brand   #instance variable
        self.price = Price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)  
        print("ChargerType:",self.chargerType)  
Samsung = phone("Samsung","50000") 
Samsung.display()
Redmi = phone("Redmi", "40000")  
Redmi.display()
iPhone = phone("iPhone" , "100000") 
iPhone.display()   
        