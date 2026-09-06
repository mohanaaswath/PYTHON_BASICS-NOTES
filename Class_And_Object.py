#Object oriented programming  :OOPS is the programming paradigm based on the concept of objects, which can contain data and code: data in the form of fields (often known as attributes), and code, in the form of procedures (often known as methods). A feature of objects is that an object's procedures can access and often modify the data fields of the object with which they are associated (objects have a notion of "this" or "self"). 
# In OOP, computer programs are designed by making them out of objects that interact with one another. OOP languages are diverse, but the most popular ones are class-based, meaning that objects are instances of classes, which also determine their types.


# class goa:
#     name = " "
#     drink = " "
#     def party(self):
#         print("lets party.....")
#     def beach(self):
#         print("Enjoying the beach....")  
          
# ramesh = goa()
# suresh = goa()

# ramesh.name = "Ramesh"
# suresh.name = "Suresh"

# ramesh.drink = "Yes"
# suresh.drink = "No"    

# print(ramesh.name)
# print("Drink : ",ramesh.drink)  
# print(suresh.name) 
# print("Drink : ",suresh.drink)

# ramesh.party()
# suresh.beach()



# class Laptop :
#     Price = 0
#     Processor = " "
#     Ram = " "

# hp = Laptop()
# dell = Laptop()
# Lenovo = Laptop()

# hp.Price = 60000
# hp.Processor = "i5"
# hp.Ram = "8GB" 

# dell.Price = 50000
# dell.Processor = "i6"
# dell.Ram = "6GB"   

# Lenovo.Price = 40000
# Lenovo.Processor = "i6"
# Lenovo.Ram = "4GB"

# print(hp.Price)
# print(hp.Processor)
# print(hp.Ram)
# print(dell.Price)
# print(dell.Processor)
# print(dell.Ram)
# print(Lenovo.Price)
# print(Lenovo.Processor)
# print(Lenovo.Ram)



# class laptops :
#     def __init__(self):
#         self.ram = " "
#         self.process = " "
#     def display(self):
#         print("ram:" , self.ram)  
#         print("process :",self.process)
        
# hp = laptops()
# dell = laptops()

# hp.ram = "8gb"
# hp.process = "i5"
# dell.ram = "6gb"
# dell.process = "i4"

# hp.display()
# dell.display()


# class Student : 
#     def __init__(self):
#         self.name = " "
#         self.age = " " 
#     def display(self):
#         print("Name : ", self.name)  
#         print("Age : ", self.age)   
        
# s1 = Student()
# s2 = Student()

# s1.name = "mohan"  
# s1.age = "20"
# s2.name = "ram"
# s2.age = "21"  

# s1.display()
# s2.display()      


# class fruit : 
#     def __init__(self , col):
#         self.color = col
# apple = fruit("red")  
# print(apple.color)            


# class teacher :
#     def __init__(self , name , reg):
#         self.name = name
#         self.reg = reg
#     def display(self):
#         print("Name: ",self.name)
#         print("Reg no:",self.reg)  
# t1 = teacher("mohan" , "101")    
# t2 = teacher("nithin" , "102")   

# t1.display()
# t2.display()  


# class calculator :
#     def __init__(self,a,b):
#         self.num1 = a
#         self.num2 = b
#     def add(self):
#         print("Add:",self.num1+self.num2)    
# obj1 = calculator(10,2)  
# obj1.add()      



# #instance variable
# #class variable
# class phone :
#     chargerType = "C-Type"  #class variable
#     def __init__(self, Brand , Price):
#         self.brand = Brand   #instance variable
#         self.price = Price
#     def display(self):
#         print("Brand:",self.brand)
#         print("Price:",self.price)  
#         print("ChargerType:",self.chargerType)  
# Samsung = phone("Samsung","50000") 
# Samsung.display()
# Redmi = phone("Redmi", "40000")  
# Redmi.display()
# iPhone = phone("iPhone" , "100000") 
# iPhone.display()   
        
#Syntax of Class 
   #Class ClassName :
       #Constructor(def __init__(self)):
        
       #def FuncName:
        
       #def FuncName:
       
    #object = ClassName()  #object creation
    #object.FuncName()  #function calling              
    
#Self => Self is a reference to the current instance of the class. It is used to access variables that belong to the class. 
# It binds the attributes with the given arguments.
# The self parameter is a reference to the current instance of the class and is used to access variables that belong to the class. 
# It must be the first parameter of any function in the class.   

class python :
    def Students(self):
        print("Students are learning OOPS concept in python") 
Staff = python()  #object creation
Staff.Students()  #function calling        

#Constructor => A constructor is a special type of method that is automatically called when an object of a class is created. 
# It is used to initialize the object's attributes and set up any necessary resources.
# In Python, the constructor method is defined using the __init__() method. 

class ClassName : 
    #name and age is the local variable that is passed as an argument to the constructor method. It is used to initialize the object's attributes with the provided values.
    def __init__(self,name,age): #__init__ is a constructor method that is automatically called when an object of the class is created. It initializes the object's attributes with the provided values.
        self.name = name    #self.name  is the instance variable that is used to store the name of the object. It is prefixed with self to indicate that it belongs to the current instance of the class.
        self.age = age  
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)  

Object1 = ClassName("mohan",20)  #object creation
Object2 = ClassName("Abhishek",20)     
Object1.display()#calling the display method of Object1       
Object2.display()#calling the display method of Object2   


class Students_Details:
    def __init__(self,name,age,roll_no,marks,grade,course):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.marks = marks
        self.grade = grade
        self.course = course
    def Show_Students_Details(self):
        print(f'Hi I am {self.name} and I am {self.age} years old ,I am Studying in {self.course} course and My Roll No is {self.roll_no} and I got {self.marks} marks and My Grade is {self.grade}')    

Student1 = Students_Details("Mohan",20,101,90,"A","AI Engineering") 
Student2 = Students_Details("Abhishek",21,102,90,"A","Data Science")    
Student3 = Students_Details("Nithin",22,103,90,"A","Mern Stack")   
Student4 = Students_Details("Anbu",23,104,90,"A","Python")
Student5 = Students_Details("Gokul",24,105,90,"A","JavaScript")
Student6 = Students_Details("Arun",25,106,90,"A","Network Security")
Student7 = Students_Details("Rocky",26,107,90,"A","Full Stack Development")
Student8 = Students_Details("Sachin",26,107,90,"A","java Development")

Student1.Show_Students_Details()
Student2.Show_Students_Details()
Student3.Show_Students_Details()
Student4.Show_Students_Details()
Student5.Show_Students_Details()
Student6.Show_Students_Details()
Student7.Show_Students_Details()
Student8.Show_Students_Details()

# creating a class for employee details 
class Employee_Details:
    def __init__(self,name,age,emp_id,designation,salary):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary
    def Show_Employee_Details(self):
        print(f'Hi I am {self.name} and I am {self.age} years old ,My Employee ID is {self.emp_id} and I am working as a {self.designation} and My Salary is {self.salary}')
        
Employee1 = Employee_Details("Mohan",30,101,"Software Engineer",50000)
Employee2 = Employee_Details("Abhishek",31,102,"Data Scientist",60000)
Employee1.Show_Employee_Details()    
Employee2.Show_Employee_Details()    