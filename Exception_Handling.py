# try :
#     a = int(input())
#     b = int(input())
#     print(a + b)
# except Exception:
#     print("Have Error")    
# # 10 mohan have error    
    
# try :
#     a = int(input())
#     b = int(input())
#     print(a + b)
# except Exception as e:
#     print("Have Error",e)    
# #10 hi  Have Error invalid literal for int() with base 10: 'h1'    
   
# try :
#     a = input()
#     b = input()
#     print(a / b)
# except Exception as e:
#     print("Have Error",e)    
# #Have Error unsupported operand type(s) for /: 'str' and 'str'    
    
# try :
#     a = int(input())
#     b = int(input())
#     c = input()
#     print(c / a)
# except ValueError as e:
#     print("value error",e) 
# except TypeError as e:
#     print("type error" ,e)     
# #type error unsupported operand type(s) for /: 'str' and 'int'    
    
 
# try :
#     a = int(input())
#     b = int(input())
#     c = input()
#     #print(d)
# except ValueError as e:
#     print("value error",e) 
# except TypeError as e:
#     print("type error" ,e) 
# except Exception :
#     print("error")    
# #error 
 

# try :
#     a = int(input())
#     b = int(input())
#     print(a+b)
# except ValueError as e:
#     print("value error",e) 
# except TypeError as e:
#     print("type error" ,e) 
# finally :
#     print("Bye")   
# #20 Bye                          

#Exception Handling : Exception handling is a mechanism to handle runtime errors, allowing the normal flow of the program to be maintained. 
     #In Python, exceptions are handled using try and except blocks. 
     #The code that may raise an exception is placed inside the try block, and the code to handle the exception is placed inside the except block.
     
# => KeyWords : try, except, else, finally, raise     
# => Error Types : SyntaxError, NameError, TypeError, ValueError, IndexError, KeyError, AttributeError, ZeroDivisionError, FileNotFoundError, ImportError, ModuleNotFoundError.

#how many standard errors are there in Core Python : There are 67 standard errors in Core Python.

#SyntaxError : This error occurs when there is a mistake in the syntax of the code. For example, missing a colon at the end of a statement or using incorrect indentation.
#NameError : This error occurs when a variable or function name is not defined or is misspelled. For example, trying to access a variable that has not been assigned a value.

#Syntax : 
# try:
#     # block of code 
# except #ErrorName / ExceptionType :
#else:
#    Block of code / execution statement 
#finally:
#     Block of code / execution statement   


# try : 
#     User_Input = int(input("Enter Your Phone Number : "))
# except ValueError as e: 
#     print("Value Error",e)  
# else :  #else means if have no error run this block of code
#     for i in range(User_Input):
#         print("Your are in Alone") 
        
try : 
    a = int(input("Enter the first value : "))
    b = int(input("Enter the second value : "))
    c = a /b 
except ValueError :   
    print("Kindly enter numeric value only") 
except ZeroDivisionError :
    print("You cannot divide by zero")  
except Exception :
    print("An error occurred") 
else :
    print("The result of the division is:", c)   
finally :
    print("Successfully code executed ")         
              
        