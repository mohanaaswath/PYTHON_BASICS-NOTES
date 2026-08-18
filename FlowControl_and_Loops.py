if(True):
    print("I am AI and Machine learning developer")
else:
    print("I am full stack developer")    
    
    
rcb = "win"
if(rcb == "win"):
    print("ee sala cup namdha")
else:
    print("not win")    
    

#meghna = input()
meghna = "died"
if(meghna == "died"):
    print("surya meet priya")
else:
    print("surya will be married meghna")    


#mark = int(input())
mark = 40
if(mark > 35):
    print("pass")
else:
    print("fail")    


score = 80
if(score<35):
    print("poor student")
elif(score>35 and score<70):
    print("average student")
elif(score>70 and score<100):
    print("good student")
else:
    print("invalid score")         

    
score = 70
if(score>=70):
   # name = input("Enter your name : ")
   # age = input("Enter your age : ")
  #  location = input("Enter your location : ")
    print("your are eligible")
else:
    print("your are not eligible")        
    
 #for loop

for i in "Mohana Aswath":
    print(i)    
    
primes = [100,200,300,400,500]
for prime in primes:
    print(prime)    


for i in range(5):
    print(i)    

for i in range(1,21):
    print(i)    
    
names = ["mohan","aswath","madhan"]    
for i , value in enumerate(names):
    print(i, value)
    
for i in range(1,21):
    print(i,"x2=",i*2)
    

count = 0 
for i in range(1,5):
    if(i%2 == 0):
        count = count+1
        print(count)   
    

e_count = 0
o_count = 0
for i in range(1,11):
    if(i%2 == 0):
        e_count = e_count+1
    else:
        o_count = o_count+1
print(e_count) 
print(o_count)               


for i in range(1,6):
    print()
    for j in range(1, i+1):
        print(j , end="")
        

for i in range(1,3):
    print("week : " , i)
    for j in range(1,4):
        print("day : " , j)        
        
#while loop

i = 1
while(i<5):
    print(i)
    i = i+1
    
    
i = 1
while(i<=5):
    print(i)
    i = i+1
                
i = 10
while(i<=200):
    print(i , end=",") 
    i = i+10      
    
i = 10
while(i>0):
    print(i , end=",")   
    i = i-1      