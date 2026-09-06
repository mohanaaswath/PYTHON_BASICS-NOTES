##Local and Global Functions:
#Local => A local function is a function that is defined within another function and can only be accessed and used within that function. It is not visible or accessible outside of the function in which it is defined.
#Global => A global function is accessible from anywhere in the code, including inside other functions.

#Basic Example of Local and Global Functions:
# A = 10 #Global Variable
# def my_function():
#     A = 20 #Local Variable
#     print("Local Variable A:", A) #20
# my_function()  

# print("Global Variable A:", A) #10  

#real world example: 
# college_libary = ["Math", "Science", "History"] #Global Variable
# def add_book():
#     college_libary = ["Tamil", "English"] #Local Variable
#     print("Local Library:", college_libary)
# add_book() #Local Library: ['Tamil', 'English']

# print("Global Library:", college_libary) #Global Library: ['Math', 'Science', 'History']


#Interview Question: 
# high_score = 500
# def update_score():
#     global high_score  # Declare high_score as global to modify it
#     high_score = 600 # Modify the global variable
#     print("Updated High Score:", high_score)
# update_score()  
# print("Global High Score:", high_score)  #Global High Score: 600  


# # #f means format string literals, which allow you to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and then formatted using the format() protocol.
# a = 100
# b= 300
# c = a+b
# print(f'The sum of {a} and {b} is: {c}') #The sum of 100 and 300 is: 400


