try :
    a = int(input())
    b = int(input())
    print(a + b)
except Exception:
    print("Have Error")    
# 10 mohan have error    
    
try :
    a = int(input())
    b = int(input())
    print(a + b)
except Exception as e:
    print("Have Error",e)    
#10 hi  Have Error invalid literal for int() with base 10: 'h1'    
   
try :
    a = input()
    b = input()
    print(a / b)
except Exception as e:
    print("Have Error",e)    
#Have Error unsupported operand type(s) for /: 'str' and 'str'    
    
try :
    a = int(input())
    b = int(input())
    c = input()
    print(c / a)
except ValueError as e:
    print("value error",e) 
except TypeError as e:
    print("type error" ,e)     
#type error unsupported operand type(s) for /: 'str' and 'int'    
    
 
try :
    a = int(input())
    b = int(input())
    c = input()
    #print(d)
except ValueError as e:
    print("value error",e) 
except TypeError as e:
    print("type error" ,e) 
except Exception :
    print("error")    
#error 
 

try :
    a = int(input())
    b = int(input())
    print(a+b)
except ValueError as e:
    print("value error",e) 
except TypeError as e:
    print("type error" ,e) 
finally :
    print("Bye")   
#20 Bye                          