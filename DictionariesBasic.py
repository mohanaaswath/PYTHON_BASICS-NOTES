
#     #Python Dictionaries : A Dictionary is a collection of data stored as key-value pairs.
#                           #Unlike lists and tuples, Mutable.

#     #Creating a Dictionary
#                 A dictionary is created by writing key-value pairs inside { }, where each key is connected to a value using colon (:).
#                 A dictionary can also be created using dict() function .         

#             student = {
#             "name": "Mohan",
#             "age": 20,
#             "course": "AI Python Full Stack Development"
#             }
#             print(student)
#                     {
#                       'name': 'Mohan',
#                       'age': 20,
#                       'course': 'AI Python Full Stack Development'
#                    }

#             Student = dict(
#                     name="Aswath",
#                     age=20
#                 )

#             print(Student) {'name': 'Aswath', 'age': 20}

#     #Accessing Dictionary Items :
#               A value in a dictionary is accessed by using its key , square brackets [ ] ,  get() also use .


#             print(student["name"])     Mohan
#             print(student.get("age"))  20

#     #Adding a New Item :

#             student["city"] = "Hosur"

#     #Updating a Value :

#             student["age"] = 21

#     #Removing a item :

#             student.pop("course")
#             #del: removes an item using its key
#               del student["age"]
#            #clear(): removes all items from the dictionary  
#               student.clear()  {}

     

#     #Dictionaries are used in:

#                        User Profiles
#                        Login Systems
#                        Product Details
#                        API Responses ,API => Application Programming Interface 
#                        JSON Data => JavaScript Object Notation Data
#                        Configuration Settings

#           That's the basics of Python Dictionaries! 

#Dictionary is one of the 4 build data types in python. Other 3 are : list , set , tuple. 
#Dictionary is mutable (you can change them). Dictionary allows duplicate values. Dictionary is unordered. Dictionary is defined by {}.    
#Dictionary is ordered 
#Dictionary is a collection of key-value pairs. Each key is unique and is used to access its corresponding value.        
#Dictionary can store elements of different data types, such as integers, strings, lists and dictionaries, within a single structure.
#Dictionary is not have index , instead of we have key 
#In value we can store any data type like : int , float , string , list , tuple , dictionary etc.
#In key we can only store like : int , float , string , tuple (immutable data types) . 
#dict is created using {} curly brackets like : {key1:value1 , key2:value2 , key3:value3} or dict() function.


#In real time use dict() function to create dictionary.

# Company_Database = {
#         "Employee_ID": 12345,
#         "Employee_Name": "Mohan",
#         "Employee_Age": 20,
#         "Employee_Designation": "AI Full Stack Developer",
#         "Employee_Salary": 50000,
#         "Employee_Skills": ["Python", "AI", "Machine Learning", "Data Science"], 
# }
# print(Company_Database) # {'Employee_ID': 12345, 'Employee_Name': 'Mohan', 'Employee_Age': 20, 'Employee_Designation': 'AI Full Stack Developer', 'Employee_Salary': 500
# print(Company_Database["Employee_Age"])
# print(Company_Database.keys())
# print(Company_Database.values())

# dct = dict()

#key => int , float , string , tuple acceptable
#value => any data type acceptable

#Adding and updating a values
  #syntax =.> dct_variable[key] = value 
  
# Student_Details = {}

# Student_Details["Student_Name"] = "Mohan"
# Student_Details["Student_Age"] = 20
# Student_Details["Student_Course"] = "AI Full Stack Development"

# print(Student_Details) # {'Student_Name': 'Mohan', 'Student_Age': 20, 'Student_Course': 'AI Full Stack Development'}

# #Both adding and updating in dict has same method 
# #but if key is not present in dict then new key and value will be added to dict
# #but if key is already there in dict , then it is will update with

# Employee_Details = {}

# Employee_Details["Employee_ID"] =221126
# Employee_Details["Employee_Name"] = "MythiliMohan"
# Employee_Details["Employee_Age"] = 20
# Employee_Details["Employee_Mail"] = "mythili.mohan@example.com"
# Employee_Details["Employee_Salary"] = 50000

# print(Employee_Details) 
# #Update 
# Employee_Details["Employee_Salary"] = 60000
# print(Employee_Details) 
# #Technically it should give an error  , but it will add the key and value 
# Employee_Details.update({"Employee_Designation":"AI Full Stack Developer"})
# print(Employee_Details) 

# #Deleting : 
# #if delete any item using key its ok ,but using value it will give an error
# #pop() method removes the item with the specified key name.
# # Employee_Details.pop("Employee_Age") 
# # print(Employee_Details)

# #popitem() method removes the last inserted item .
# # Employee_Details.popitem()
# # print(Employee_Details)

# #for loop in dictionary :
# for key in Employee_Details:
#     print(key, ":", Employee_Details[key])
    
# for i in zip(Employee_Details.keys(), Employee_Details.values()):
#     print(i)    
    
# # ('Employee_ID', 221126)
# # ('Employee_Name', 'MythiliMohan')
# # ('Employee_Age', 20)
# # ('Employee_Mail', 'mythili.mohan@example.com')
# # ('Employee_Salary', 60000)
# # ('Employee_Designation', 'AI Full Stack Developer')
    
# for i , j in zip(Employee_Details.keys(), Employee_Details.values()):
#     print(i, ":", j)
    
# #     Employee_ID : 221126
# #     Employee_Name : MythiliMohan
# #     Employee_Age : 20
# #     Employee_Mail : mythili.mohan@example.com
# #     Employee_Salary : 60000
# #     Employee_Designation : AI Full Stack Developer

# for i ,j in Employee_Details.items():
#     print(i, ":", j)
    
# # Employee_ID : 221126
# # Employee_Name : MythiliMohan
# # Employee_Age : 20
# # Employee_Mail : mythili.mohan@example.com
# # Employee_Salary : 60000
# # Employee_Designation : AI Full Stack Developer

# #Write a program to check the string 
# #each vowels how many times it appearing and store in dictionary  

# Sentence = "I am  MohanMythiliRupa studying AI Powered Full Stack Development Course in Bengaluru"

# vowels = "aeiou"
# Vowel_Dict = {}
# for i in Sentence :
#         i = i.lower()
#         if i in vowels:
#             if i in Vowel_Dict:
#                 Vowel_Dict[i] += 1
#             else:
#                 Vowel_Dict[i] = 1
# print(Vowel_Dict) #{'i': 6, 'a': 6, 'o': 4, 'u': 6, 'e': 7}

#Write a program to get a details from n number employee and store int he dict
#Write a Program to Get a Details from n number employee and store int he dict

# maximum = int(input("Enter the Number of Details You want to enter : "))
# while True:
    
#     emp_id = input('Enter the EMPID:')
#     if emp_id in EMP_Details:
#         print("Employee ID alreay Avaiable")
#         break
#     else:
#         emp_data ={}
#         Name = input("Enter the Name:")
#         Salary = int(input("Enter the Salary:"))
#         Position = input("Enter You Job Poistion: ")

#         emp_data['Name'] =Name
#         emp_data['Salary']= Salary
#         emp_data['Position'] = Position

#         EMP_Details[emp_id] = emp_data
        
#         maximum -=1
        
#         if maximum==0:
#             print("Program Stops")
#             break

#Write a Program to Get a Details from n number employee and store int he dict

#write a python program that takes a dictionary with student names as key and their scores as value .the program should print the name of the student with the highest score 

Student_Details = {
  "Mohan": 99,
  "Madhan": 90,
  "Rockey": 75,
  "Mahesh":70,
  "Suresh": 800
}

Highest_Score = max(Student_Details.values())
Top_Students = [name for name, score in Student_Details.items() if score == Highest_Score]
print("Name :" , Top_Students[0] ,"," "Score:" , Highest_Score) # Name : Suresh , Score: 800




