def my_function():
    print("hello i am mohan")
my_function()       


def paint(msg):
    print("Message :" ,msg)
paint("paint for my house")


def greet(name):
    print(f"Hello,{name}")
greet("Mohana Aswath")    


def add(x , y):
    print("x is %s , y is %s" %(x,y))
    return x+y
add(500 , 550)


def add(x,y=10):
    return x+y
a  = add(5)
b = add(5,20)
print(a)
print(b)


def varargs(*args):
    return args
a = varargs(1,2,3,4,5)
print(a)


def Find_even_or_odd(b):
    if(b%2 == 0):
        print("Even")
    else:
        print("Odd") 
a = 20
Find_even_or_odd(a) 
       
 
def Print_range(r1,r2):
    for i in range(r1,r2):
        print(i)
Print_range(4,11)
     
     
def painter():
  return "I am painter"
msg = painter()
print(msg)           
   
   
def add(a,b):
    return a+b   
result = add(3,5)
print(result)  


s_UserName = "mohan"
s_PassWord = "2212"
UserName = input("Enter your user name : ")
Password = input("Enter your password : ")
def Vail_Data():
    if(s_UserName == UserName and s_PassWord == Password):
        print("Correct")
    else:
        print("Wrong")   
Vail_Data()


def add(n1,n2):
    return n1+n2
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:")) 
added = add(a,b) 
output = added*c
print(output)

     
def Find_pass_or_fail(a):
    if(a>35):
        print("Pass")  
    else:
        print("Fail")           
b = int(input("Enter your Maths marks:"))
Find_pass_or_fail(b)


def Print_range(r1,r2):
    for i in range(r1,r2):
        print(i)
a = int(input("Enter a : "))
b = int(input("Enter b : "))
Print_range(a,b)


def add():
    print("Addition")
    a = int(input("enter a :"))
    b = int(input("enter b :"))
    print(a+b)
def sub():
    print("Subtraction")
    a = int(input("enter a :"))
    b = int(input("enter b :"))
    print(a-b) 
def multi():
    print("Multiplication")
    a = int(input("enter a :"))
    b = int(input("enter b :"))
    print(a*b)      
def div():
    print("Division")
    a = int(input("enter a :"))
    b = int(input("enter b :"))
    print(a/b)   
add()
sub()
multi()
div()     
