# #single inheritance

# class dad():
#     def phone(self):
#         print("dad phone")
# class son(dad):
#     def laptop(self):
#         print("son laptop")        
        
# Mohan = son()
# Mohan.phone()


# #multiple inheritance

# class dad():
#     def phone(self):
#         print("dad phone")
# class mom():
#     def sweet(self):
#         print("mom sweet")   
# class son(dad , mom ):
#     def laptop(self):
#         print("son laptop")        
        
# Mohan = son()
# Mohan.phone()
# Mohan.sweet()


# #Multilevel inheritance  

# class Grandpa() :
#     def Phone(self):
#         print("Grandpa phone")
# class Dad(Grandpa): 
#     def Money(self):
#         print("Dad Money")   
# class Son(Dad):
#     def Laptop(self):
#         print("son laptop")
 
# Mohan = Son()
# Mohan.Money()
# Mohan.Phone()
# Mohan.Laptop()

# Madhan = Dad()
# Madhan.Phone()    


# #Hierarchical inheritance 

# class dad():
#     def Money(self):
#         print("Dad money")
# class son1(dad):
#     pass   
# class son2(dad):
#     pass  
# class son3(dad):
#     pass 
# s2 = son2()
# s2.Money()          


# # single , multilevel , multiple , hierarchical = hybrid inheritance 

# class dad():
#     def Money(self):
#         print("Dad money")
# class land():
#     def important(self):
#         print("Important land")        
# class son1(dad , land):
#     pass   
# class son2(dad):
#     pass  
# class son3(dad):
#     pass 
# s1 = son1()
# s1.Money() 
# s1.important()      



#Single inheritance : single inheritance is a type of inheritance where a child class inherits from a single parent class. This allows the child class to access the properties and methods of the parent class.

# class parent :
#     def phone(self):
#         print("parent phone")
# class child(parent):
#     def laptop(self):
#         super().phone()  #super() is used to call the parent class method from the child class
#         print("child laptop")  
        
# access = child()
# access.laptop()  


# class Employee : #Parent class
#     def __init__(self, E_name, E_age):
#         self.E_name = E_name
#         self.E_age = E_age
#     def display(self):
#          print("Employee Name:", self.E_name)  
#          print("Employee Age:", self.E_age) 
# class Hr(Employee): #Child class inherits from parent class Employee
#     def __init__(self, Hr_name, Hr_age, Hr_salary, E_name, E_age):
#         super().__init__(E_name, E_age)  #super() is used to call the parent class constructor from the child class
#         self.Hr_name = Hr_name
#         self.Hr_age = Hr_age
#         self.H_salary = Hr_salary
#     def display(self):
#         super().display()  #super() is used to call the parent class method from the child class
#         print(f"Hr Details: {self.Hr_name}, {self.Hr_age}, {self.H_salary}")

# Hr = Hr("Mohan", 25, "50000" ,"Aswath", 30)  #creating an object of the child class and passing the values to the constructor
# Hr.display()  #calling the display method of the child class which also calls the display method of the parent class
       
 
# #MultiLevel inheritance : Multi-level inheritance is a type of inheritance where a child class inherits from a parent class, and then another child class inherits from that child class. This creates a chain of inheritance.

# class Grandparent:
#     def phone(self):
#         print("Grandparent phone")  
# class Parent(Grandparent):
#     def laptop(self):
#         print("Parent laptop")
# class Child(Parent): 
#     def tablet(self):
#         print("Child tablet")
# son = Child()
# son.phone()  #calling the method of the grandparent class from the child class        
# son.laptop()  #calling the method of the parent class from the child class
# son.tablet()  #calling the method of the child class from the child class   

# class Student:
#     def __init__(self, name, age , roll_no ,Class):
#         self.name = name
#         self.age = age
#         self.roll_no = roll_no
#         self.Class = Class                    
#     def display(self):
#         print(f"Student Details: {self.name}, {self.age}, {self.roll_no}, {self.Class}")

# class Teacher(Student):
#     def __init__(self, name, age , roll_no ,Class, subject, salary):
#         super().__init__(name, age , roll_no ,Class)  #super() is used to call the parent class constructor from the child class
#         self.subject = subject
#         self.salary = salary
#     def display(self):
#         super().display()  #super() is used to call the parent class method from the child class
#         print(f"Teacher Details: {self.subject}, {self.salary}")    

# class Principal(Teacher):
#     def __init__(self, name, age , roll_no ,Class, subject, salary, P_name,experience):
#         super().__init__(name, age , roll_no ,Class, subject, salary)  
#         self.P_name = P_name
#         self.experience = experience
#     def display(self):
#         super().display()  #super() is used to call the parent class method from the child class
#         print(f"Principal Details: {self.P_name}, {self.experience}")        

# Teacher = Teacher("Mohan", 25, 101, "10th", "Maths", 50000)  
# Teacher.display() 
# #Student Details: Mohan, 25, 101, 10th
# #Teacher Details: Maths, 50000
# Principal = Principal("Mohan", 25, 101, "10th", "Maths", 50000 ,"Aswath",5)  
# Principal.display()  
# # Student Details: Mohan, 25, 101, 10th
# # Teacher Details: Maths, 50000
# # Principal Details: Aswath, 5 


#Hierarchical inheritance : Hierarchical inheritance is a type of inheritance where multiple child classes inherit from a single parent class. 
# This allows the child classes to access the properties and methods of the parent class.

# class A :
#     def phone(self):
#         print("A phone")
# class B(A):
#     def laptop(self):
#         print("B laptop")  
# class C(A):
#     def tablet(self):
#         print("C tablet")  
        
# B = B()
# B.phone()  #calling the method of the parent class from the child class
# B.laptop()  #calling the method of the child class from the child class
# B = C()
# B.phone()  #calling the method of the parent class from the child class
# B.tablet()  #calling the method of the child class from the child class


class IT_JOBS :
    def IT(self):
        print("IT JOBS")     
class ML_Developer(IT_JOBS):
    def ML(self):
        print("ML Developer")  
class Data_Analyst(IT_JOBS):
    def DA(self):
        print("Data Analyst")    
class Digital_Marketing(IT_JOBS):
    def DM(self):
        print("Digital Marketing")
    
Object = Digital_Marketing()
Object.DM()  #calling the method of the child class from the child class
Object.IT()  #calling the method of the parent class from the child class       


#Multiple inheritance : Multiple inheritance is a type of inheritance where a child class inherits from multiple parent classes.

class  Front_End():
    def React(self):
        print("Front End React")  
class Back_End():
    def Django_and_Node(self):
        print("Back End Django and Node.js(Express.js)") 
class Full_Stack_Developer(Front_End, Back_End):
    def Full_Stack(self):
        print("Full Stack Developer")   
        
Full_Stack = Full_Stack_Developer()
Full_Stack.React()  
Full_Stack.Django_and_Node() 
Full_Stack.Full_Stack()  
