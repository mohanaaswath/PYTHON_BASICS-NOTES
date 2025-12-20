class a():
    def __init__(self):
        print("A")
    def display(self):
        print("you are in class a")   

class b(a):
    def __init__(self):
        super().__init__()  
        print("B")     
    def display(self):
        print("your are in class b")

Object_1 = b()          

