
#     #Tuple : A Tuple is a collection used to store multiple items in a single variable, just like a list.
             
#             #The main difference is that tuples are immutable, which means you cannot change, add, or remove items after creating them. 
#             #A tuple is created by placing all the items inside parentheses ()
#             #separated by commas. A tuple can have any number of items.

#     #Create tuple 
#           fruits = ("Apple", "Banana", "Orange")

#           print(fruits) #("Apple" ,"Banana", "Orange")

#           li = [1, 2, 3, 4, 5, 6]
#           print(tuple(li)) #(1,2,3,4,5,6)

#           # Using Built-in Function
#           tup1 = tuple('Mohan')
#           print(tup1) #('M', 'o', 'h', 'a', 'n')

#     #Mixed Datatypes:Tuples can store elements of different data types, such as integers, strings, lists and dictionaries, within a single structure.

#           tup2 = (77, 'Mohan', 7.5, True, [10, 20, 30], {'Job': 'AI Full stack developer'})
#           print(tup2)

#     #Accessing Elements : Like lists, tuples use indexing.

#           print(fruits[0]) // Apple
#           print(fruits[-2]) //Banana

#     #Length of a Tuple

#           print(len(fruits))//3

#     #Loop Through a Tuple
#           for fruit in fruits:
#           print(fruit) // Apple , Banana , Orange 

#     #Real-World Examples

#            Tuples are commonly used for:
#                Database Records
#                Configuration Settings
#                Employee IDs
#                Days and Months     

#Tuple: tuple is the collection of multiple values in a single variable. Tuple is immutable (you cannot change them). Tuple allows duplicate values. Tuple is ordered. Tuple is defined by ().
       #tuple is one of the 4 build data types in python. Other 3 are : list , set , dictionary.
       #tuple is ordered,allows duplicate values, immutable (you cannot change them). Tuple is defined by ().
       #tuple is store the data of different data types like : int , float , string , list , dictionary etc.
       #tuple is indexed and immutable (you cannot change them). Tuple is defined by ().
       #tuple is created using () parenthesis like round bracket 
       
Tuple = () #empty tuple  
print(type(Tuple)) #<class 'tuple'>

# Tuple1 = [1, 2, 3, 4, 5] #list
# print(type(Tuple1)) #<class 'list'>

Group_Data = (1,345,678,[3,6,9],"Python",True,False,3.14,{"Name":"Mohan","Age":25}) #tuple with different data types
print(Group_Data) #(1, 345, 678, [3, 6, 9], 'Python', True, False, 3.14, {'Name': 'Mohan', 'Age': 25})

#same like list :tuple supports both positive and negative indexing. Positive indexing start from 0 and negative indexing start from -1 (last value).
                 #range also 
#tuple have indexing and comprehension

#once a tuple is created using values cannot inserted, updated or deleted. Tuple is immutable. 

#tuple -> list , list operations , list -> tuple 


#Different between list and tuple :
#List is mutable (you can change them) and tuple is immutable (you cannot change them)