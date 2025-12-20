#private variable data 

class Company():
    def __init__(self):
        self.__CompanyName = "Google"  #private variable
    def CompanyName(self):
        print(self.__CompanyName) 

C1 = Company()
C1.CompanyName() #Google
#print(C1.__CompanyName)   #AttributeError: 'Company' object has no attribute '__CompanyName'. Did you mean: 'CompanyName'?  


class Student : 
    def __init__(self , Name , Marks):
        self.name = Name 
        self.__marks = Marks   #Private variable 
    def get_Marks(self):
        print(self.name)
        print(self.__marks) 
    
        
Student_1 = Student("Mohan" ,"85") 
Student_1.get_Marks()  #access the private variable or data 
#print(Student_1.__marks)

#protected variable data 

class company():
    def __init__(self):
        self._company = "IBM"
c1 = company()
print(c1._company)     


class company():
    def __init__(self):
        self._company = "IBM"
class b(company):
    pass      
b1 = b()
print(b1._company)     