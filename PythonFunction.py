# Python Functions
#   A function in Python is a block of code that runs only when we call it.

# def greet():
#     print("Hello, welcome to Python!")

# greet() # Hello , welcome to python 

# #def means define a function
# #greet() is the function name
# #greet() at the bottom calls the function

# #Function With Parameter

# def greet(name):
#     print("Hello", name)

# greet("Mohan") #Hello , Mohan

# #Function With Return Value
# #return sends the final result back from the function.

# def add(a, b):
#     return a + b

# result = add(10, 20)
# print(result) #30

# def my_function():
#     print("hello i am mohan")
# my_function()       


# def paint(msg):
#     print("Message :" ,msg)
# paint("paint for my house")


# def greet(name):
#     print(f"Hello,{name}")
# greet("Mohana Aswath")    


# def add(x , y):
#     print("x is %s , y is %s" %(x,y))
#     return x+y
# add(500 , 550)


# def add(x,y=10):
#     return x+y
# a  = add(5)
# b = add(5,20)
# print(a)
# print(b)


# def varargs(*args):
#     return args
# a = varargs(1,2,3,4,5)
# print(a)


# def Find_even_or_odd(b):
#     if(b%2 == 0):
#         print("Even")
#     else:
#         print("Odd") 
# a = 20
# Find_even_or_odd(a) 
       
 
# def Print_range(r1,r2):
#     for i in range(r1,r2):
#         print(i)
# Print_range(4,11)
     
     
# def painter():
#   return "I am painter"
# msg = painter()
# print(msg)           
   
   
# def add(a,b):
#     return a+b   
# result = add(3,5)
# print(result)  


# s_UserName = "mohan"
# s_PassWord = "2212"
# UserName = input("Enter your user name : ")
# Password = input("Enter your password : ")
# def Vail_Data():
#     if(s_UserName == UserName and s_PassWord == Password):
#         print("Correct")
#     else:
#         print("Wrong")   
# Vail_Data()


# def add(n1,n2):
#     return n1+n2
# a = int(input("a:"))
# b = int(input("b:"))
# c = int(input("c:")) 
# added = add(a,b) 
# output = added*c
# print(output)

     
# def Find_pass_or_fail(a):
#     if(a>35):
#         print("Pass")  
#     else:
#         print("Fail")           
# b = int(input("Enter your Maths marks:"))
# Find_pass_or_fail(b)


# def Print_range(r1,r2):
#     for i in range(r1,r2):
#         print(i)
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# Print_range(a,b)


# def add():
#     print("Addition")
#     a = int(input("enter a :"))
#     b = int(input("enter b :"))
#     print(a+b)
# def sub():
#     print("Subtraction")
#     a = int(input("enter a :"))
#     b = int(input("enter b :"))
#     print(a-b) 
# def multi():
#     print("Multiplication")
#     a = int(input("enter a :"))
#     b = int(input("enter b :"))
#     print(a*b)      
# def div():
#     print("Division")
#     a = int(input("enter a :"))
#     b = int(input("enter b :"))
#     print(a/b)   
# add()
# sub()
# multi()
# div()     


# Real-Time Example , This type of function is used in real projects like billing apps, ecommerce websites, cart systems, and invoice systems.

# def calculate_total(price, quantity):
#     return price * quantity

# total = calculate_total(100, 5)
# print("Total amount:", total)  #Total Amount : 500 



# Function is a block of code that is used to perform a specific task. It helps in organizing code, reusability, and modularity. Functions can take inputs (parameters) and return outputs (return values).
# Function has two types : user defined and built-in functions.
# Function keywords: def, return, yield, lambda, global, nonlocal . main we use def and return keywords to define a function and return a value from the function.
# Modules

# parameter and arguments
# *args and **kwargs are used to pass variable number of arguments to a function. *args is used to pass a variable number of non-keyword arguments, while **kwargs is used to pass a variable number of keyword arguments. 
 
# User defines function : max() , min() , sum() , len() , range() , print() , input() , type() , int() , float() , str() , list() , dict() , set() , tuple() , open() , close() , read() , write() , append() , insert() , remove() , pop() , sort() , reverse()

# Function syntax : def function_name(parameters):
#                     Block of code / statements
#                    function_name(arguments) #function call
                    

# you can only call the function after defining it. If you try to call the function before defining it, you will get a NameError.                    

# def add():
#     a = 80
#     b = 20
#     print(a+b)
# add()#100

# Parameter is a variable that is defined in the function definition. It acts as a placeholder for the value that will be passed to the function when it is called.
# Argument is the actual value that is passed to the function when it is called. It can be a constant, variable, or expression.

# Function with parameter and argument:
# def Student_name(name):#name is a parameter
#     print("Student name is:",name)
# Student_name("Mohana Aswath") #Mohana Aswath is an argument passed to the function
# Student name is: Mohana Aswath    

# def add(a,b):
#     print("Addition is:",a+b)
# add(10,20) #Addition is: 30 

# Write a function to create a sum of N numbers 

# def sum_of_n_numbers(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#         print("Sum of numbers from 1 to", n, "is:", total)
# sum_of_n_numbers(5)   # 15 
# Sum of numbers from 1 to 5 is: 1
# Sum of numbers from 1 to 5 is: 3
# Sum of numbers from 1 to 5 is: 6
# Sum of numbers from 1 to 5 is: 10
# Sum of numbers from 1 to 5 is: 15     

# Write a simple calculator function 


# #*args : 
# *args take a tuple of arguments and allows you to pass a variable number of non-keyword arguments to a function. It is used when you want to pass a variable number of arguments to a function. The *args syntax allows you to pass any number of positional arguments to the function, which are then collected into a tuple.
# def sum_of_numbers(*args):
#     print(args)
# sum_of_numbers(1,2,3,4,5) #(1, 2, 3, 4, 5)    

# real time example of *args :
# def calculate_total(*args):
#     total = 0
#     for price in args:
#         total += price  #total = total + price
#     return total
# cart_total = calculate_total(100, 200, 300)
# print("Total amount:", cart_total) #Total amount: 600


# ##**kwargs : 
# #**kwargs take a dictionary of arguments and allows you to pass a variable number of keyword arguments to a function. It is used when you want to pass a variable number of keyword arguments to a function. The **kwargs syntax allows you to pass any number of keyword arguments to the function, which are then collected into a dictionary.
# def Start_Up_Users(**kwargs):
#     print(kwargs)
# Start_Up_Users(name="Mohana Aswath", age=22, city="Bangalore") #{'name': 'Mohana Aswath', 'age': 22, 'city': 'Bangalore'}

# #real time example of **kwargs :
# def create_user_profile(**kwargs):
#     profile = {}
#     for key, value in kwargs.items():
#         profile[key] = value
#     return profile
# User_Profile = create_user_profile(name="Mohana Aswath", age=22, city="Bangalore")
# print("User Profile:", User_Profile) #User Profile: {'name': 'Mohana Aswath', 'age': 22, 'city': 'Bangalore'}


# ##print vs return :
#    #print => print is used to display output to the console. It does not return any value from the function. It is used for debugging and displaying information to the user.
#    #return => return is used to send a value back from the function to the caller. It allows you to capture the result of the function and use it in other parts of your code. A function can have multiple print statements but only one return statement.

# #Simple example of print vs return :
# def add(a, b):
#     #print("Inside the function: a =", a, ", b =", b) 
#     return a + b
# added_value = add(10, 20)
# print("added_value =", added_value) #added_value = 30


# #beginners level example of print vs return :
# def profile(name, age):
#     return {"name": name, "age": age}
# User_profile = profile("Mohana Aswath", 22)
# print("User Profile:", User_profile) #User Profile: {'name': 'Mohana Aswath', 'age': 22}


