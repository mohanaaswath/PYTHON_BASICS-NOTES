# while loop runs the block of code / execution statement 
# until the give condition is true. Once the condition becomes false, the loop stops executing.

#syntax:
  #While condition:
      #block of code / execution statement
      #increment / decrement 
      
# x = 10 
# while x > 5:
#     print(x)
#     x -= 1 
    
# #if we don't decrement the value of x, the loop will run infinitely because the condition will always be true.
# #always make sure to decrement or increment the value of the variable in the loop to avoid infinite loops.

# i = 0 
# while i <= 100:
#     print(i)
    #i += 2
    
#control statement : 
    # break , continue , pass 

# m = 0
# while m<=10:
#     if m==6:
#         m+=1
#         continue
#     print(m)  
#     m+=1 
 # 1 2 3 4 5 7 8 9 10       
 
#While Statement true 
# n = 0
# while True: 
#       print("While true statement is run infinite times")
#       n+=1
          
# Step 1-> User can only enter the Values between 1-250  for 10 times
# Step2-> if user enters any value <1 pr >250 we will give 5 times warning , if it exceed , user lost
# Step3=> we are going keep some numbers as mines. if the user enters those number he lost  
                  
#user can enter the number between 1 to 250 for 10 times. If user enters any number <1 or >250 we will give 5 times warning, if it exceed user lost. We are going to keep some numbers as mines. If the user enters those numbers he lost.                 
                  
m = int(input("Enter the number between 1 to 250 : "))  
while m < 1 or m > 250:
    print("You have entered the wrong number, please enter the number between 1 to 250")
    m = int(input("Enter the number between 1 to 250 : "))
    if m == 40 or m == 20 or m == 30 or m == 80 or m == 50:
        print("You have entered the mine number, you lost")
        break 
    
     
          