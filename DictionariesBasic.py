
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

Company_Database = {
        "Employee_ID": 12345,
        "Employee_Name": "Mohan",
        "Employee_Age": 20,
        "Employee_Designation": "AI Full Stack Developer",
        "Employee_Salary": 50000,
        "Employee_Skills": ["Python", "AI", "Machine Learning", "Data Science"], 
}
print(Company_Database) # {'Employee_ID': 12345, 'Employee_Name': 'Mohan', 'Employee_Age': 20, 'Employee_Designation': 'AI Full Stack Developer', 'Employee_Salary': 500
print(Company_Database["Employee_Age"])
print(Company_Database.keys())
print(Company_Database.values())

dct = dict()

#key => int , float , string , tuple acceptable
#value => any data type acceptable

