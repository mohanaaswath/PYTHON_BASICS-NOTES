a = int(input())
b = int(input())
method = input("+/-/*/div : ")
if(method == "+"):
    print(a+b)
elif(method == "-"):
    print(a-b)  
elif(method == "*"):
    print(a*b)
elif(method == "div"):
    print(a/b)          
else:
    print("Invalid method")  