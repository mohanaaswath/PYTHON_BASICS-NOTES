#single inheritance

class dad():
    def phone(self):
        print("dad phone")
class son(dad):
    def laptop(self):
        print("son laptop")        
        
Mohan = son()
Mohan.phone()


#multiple inheritance

class dad():
    def phone(self):
        print("dad phone")
class mom():
    def sweet(self):
        print("mom sweet")   
class son(dad , mom ):
    def laptop(self):
        print("son laptop")        
        
Mohan = son()
Mohan.phone()
Mohan.sweet()


#Multilevel inheritance  

class Grandpa() :
    def Phone(self):
        print("Grandpa phone")
class Dad(Grandpa): 
    def Money(self):
        print("Dad Money")   
class Son(Dad):
    def Laptop(self):
        print("son laptop")
 
Mohan = Son()
Mohan.Money()
Mohan.Phone()
Mohan.Laptop()

Madhan = Dad()
Madhan.Phone()    


#Hierarchical inheritance 

class dad():
    def Money(self):
        print("Dad money")
class son1(dad):
    pass   
class son2(dad):
    pass  
class son3(dad):
    pass 
s2 = son2()
s2.Money()          


# single , multilevel , multiple , hierarchical = hybrid inheritance 

class dad():
    def Money(self):
        print("Dad money")
class land():
    def important(self):
        print("Important land")        
class son1(dad , land):
    pass   
class son2(dad):
    pass  
class son3(dad):
    pass 
s1 = son1()
s1.Money() 
s1.important()      