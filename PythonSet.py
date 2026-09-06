#set is one of the 4 built-in data types in Python used to store collections of data, the other 3 are: list, tuple, and dictionary.
#set is unordered, unindexed, and does not allow duplicate values. It is defined by enclosing the elements in curly braces {} or by using the set() function.
#set also stores data of different data types, including integers, strings, and tuples. However, it cannot store mutable data types like lists or dictionaries.

# Set = {4,5,7,8,1,"Python",100,789,"AI"}
# print(Set) #{'Python', 1, 4, 5, 100, 7, 8, 789, 'AI'} #does not maintain the order of elements

# #Set are allow duplicate values. If you try to add a duplicate value to a set, it will be ignored.

# Duplicate_Set = {1,2,3,4,5,6,7,8,9,10,1,2,3}
# print(Duplicate_Set) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10} #duplicate values are ignored.

# #Set is mutable, which means you can add or remove elements from a set after it has been created. You can use the add() method to add an element to a set, and the remove() or discard() method to remove an element from a set.
# #once a set is created, you cannot change its elements, but you can add or remove elements from it.

# Add_and_Remove_Set = {"Python",2,7,20,50,100,80,357,"AI", "Machine Learning", "Data Science"}
# Add_and_Remove_Set.add("Deep Learning")
# print(Add_and_Remove_Set) #{'Python', 2, 7, 20, 50, 100, 80, 357, 'AI', 'Machine Learning', 'Data Science', 'Deep Learning'}

# print(Add_and_Remove_Set)

# Add_and_Remove_Set.remove(100)
# print(Add_and_Remove_Set) #{'Python', 2, 7, 20, 50, 80, 357, 'AI', 'Machine Learning', 'Data Science', 'Deep Learning'}

# #print(Add_and_Remove_Set.remove(1000)) #KeyError: 1000

# #discard() method is similar to remove() method, but it does not raise an error if the element is not found in the set. Instead, it simply does nothing.
# #print(Add_and_Remove_Set.remove(1000)) #KeyError: 1000
# #print(Add_and_Remove_Set.discard(1000)) #None

# #Joins / Venn Diagram : Union , Intersection , Difference , Symmetric Difference
# #Update a set with the union of itself and another set using the update() method.
# #Intersection_update , difference_update , symmetric_difference_update methods are also available to update a set with the intersection, difference, or symmetric difference of itself and another set.

# #Union : union() or | 
# set1 = {1,2,3,4,5} 
# set2 = {"Python", "AI", "Machine Learning", "Data Science"}
# set3 = {"Apple", "Banana", "Mango", "Grapes"}
# #New_set = set1.union(set2,set3)
# New_set = set1.union(set2|set3)
# print(New_set) 

# #update :
# set1.update(set2,set3)
# print(set1) 

#Union vs Update : union() method returns a new set that contains all the elements from both sets, while update() method modifies the original set by adding all the elements from another set to it.
#Example:


#Intersection : join 2 or more set,only take the common value 
Set1 = {"Python", "AI", "Machine Learning", "Data Science"}
Set2 = {"Python", "AI", "Deep Learning", "Data Science"}
Intersection_Set = Set1.intersection(Set2)
print(Intersection_Set) # {'Python', 'AI', 'Data Science'}


#Difference :

# set1 = {'APPLE','BANANA','MANGO','GRAPES'}
# set2 = {"APPLE", "BANANA", "ORANGE", "PINEAPPLE"}
# Difference_set = set1.difference(set2)
# print(Difference_set) # {'MANGO', 'GRAPES'}

Dept_Names = {"HR", "Finance", "IT", "Marketing"}
Marketing_Dept = {"Marketing", "Sales", "Advertising"}
Finance_Dept = {"Finance", "Accounting", "Auditing"}
All_Team_Difference = Dept_Names.difference(Marketing_Dept, Finance_Dept)
print(All_Team_Difference) # {'IT', 'HR'}

#Symmetric Difference :
set1 = {'APPLE','BANANA','MANGO','GRAPES'}
set2 = {"APPLE", "BANANA", "ORANGE", "PINEAPPLE"}
Symmetric_Difference_set = set1.symmetric_difference(set2)
print(Symmetric_Difference_set) # {'MANGO', 'GRAPES', 'ORANGE', 'PINEAPPLE'}
#we cannot give multiple sets in symmetric_difference() method, it will give an error.

#we use ^ operator also to get the symmetric difference of two sets. It returns a new set that contains all the elements that are in either of the sets, but not in both.
Set1 = {'a','b','c','d','Deep Learning','Data Science'}
Set2 = {'Google','Microsoft','Apple','Amazon','a','b'}
Set3 = {'AI','Machine Learning','Deep Learning','Data Science'}
Symmetric_Difference_Set = Set1 ^ Set2
print(Symmetric_Difference_Set) # {'Apple', 'Microsoft', 'Data Science', 'Google', 'Amazon', 'c', 'Deep Learning', 'd'}
#Symmetric_Difference_set = Set1 ^ Set2 ^ Set3
#print(Symmetric_Difference_set) #{'AI', 'Google', 'c', 'Machine Learning', 'Apple', 'Amazon', 'Microsoft', 'd'}

#Write a program to remove the duplicate values from the list without using In build function 
#use enumerate() function 
