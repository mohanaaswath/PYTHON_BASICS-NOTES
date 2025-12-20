def add(a,b,c=0):
    print(a+b+c)
add(1,2)
add(1,2,3)    

class Animals():
    def sound(self):
        print("animal makes sound")
class dog(Animals):
    def sound(self):
        print("dogs barks")
d1 = dog()
d1.sound()         

#overrides method 

class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        l=20
        b=20
        print(l*b)  
r1 = rectangle()
r1.area()           
 
 
class person():
    def __init__(self, name):
        self.name = name  
class student(person):
    def __init__(self , name , grade ):
        super().__init__(name)
        self.grade = grade
    def display(self):
        print(self.name , self.grade)    
s1 = student("mohan" , "a") 
s1.display()           
         
         
class vehicle():
    def start(self):
        print("vehicle started") 
class car(vehicle):
    def start(self):
        print("car started") 
car = car()
car.start()


class Employee():
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def __init__(self, name, salary , department):
        super().__init__(name, salary)   
        self.department = department  
    def display(self):
        print(self.name , self.salary , self.department)  

Manager_1 = Manager("Mohan" , "50000" , "AI&ML") 
Manager_1.display()            
                             