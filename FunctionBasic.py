#Python Functions
  #A function in Python is a block of code that runs only when we call it.

def greet():
    print("Hello, welcome to Python!")

greet() # Hello , welcome to python 

#def means define a function
#greet() is the function name
#greet() at the bottom calls the function

#Function With Parameter

def greet(name):
    print("Hello", name)

greet("Mohan") #Hello , Mohan

#Function With Return Value
#return sends the final result back from the function.

def add(a, b):
    return a + b

result = add(10, 20)
print(result) #30


#Real-Time Example , This type of function is used in real projects like billing apps, ecommerce websites, cart systems, and invoice systems.

def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(100, 5)
print("Total amount:", total)  #Total Amount : 500
