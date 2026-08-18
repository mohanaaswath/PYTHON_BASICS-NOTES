#Python input() Function

 #The input() function is used to take input from the user while the program is running.
 
name = input("Enter your name: ")
print("Hello", name)
#Enter your name: Mohan   Hello Mohan


#Even if the user enters 20, Python treats it as "20"   
a = int(input())
b = int(input())
c = int(input())
d = a + b + c
print(d) #10 , 10 , 10 , d = 30


#To take decimal input, use float():

price = float(input("Enter price: "))
print(price) #10.0


#real time example : Student mark result

name = input("Enter student name : ")
mark = int(input("Enter mark : "))

if mark >= 35:
    print(name, "Passed")
else :
    print(name, "Failed")
    
 #i enter Mohan ,40 output : Mohan Passed
 #i enter Mohan , 20 output : Mohan Failed 
