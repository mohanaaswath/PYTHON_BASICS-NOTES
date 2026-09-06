#5, 9, 10, 13,14,18 19 20 21 22 23 24 25

#5. Frequency count of elements 

# Numbers = [1,2,2,3,3,3,4,4,4,4,4,8,8,8,8,8,8,4,4,]
# Frequency = {}
# for number in Numbers :
#     if number in Frequency:
#         Frequency[number] += 1
#     else:
#         Frequency[number] =1

# print(Frequency)   #{1: 1, 2: 2, 3: 3, 4: 7, 8: 6}   

#9.Count Vowels and Consonants 

# Text = "MachineLearning"
# Vowels = 0
# Consonants = 0
# for char in Text.lower():
#     if char in "aeiou":
#         Vowels += 1
#     elif char.isalpha():
#         Consonants += 1    
        
# print(Vowels,Consonants)  # vowels => a,i,e,e,a,i =>6
                          # Consonants = >M,c,h,n,l,r,n,n,g => 9
                          
#10.Find Largest word in a sentence

# Normal_Text = "Machine Learning is a field of Artificial Intelligence" 
# Words = Normal_Text.split()

# Largest = Words[0] 

# for w in Words:
#     if len(w) > len(Largest):
#           Largest = w
# print(Largest)    #Intelligence  

#13. Find Duplicate Elements in List 

# Numbers = [1,2,3,4,5,2,1,6,8]
# Duplicates = []
# for i in Numbers: #i = 1  i = 2 i = 3 i = 4 i = 5 i = 2 i = 1 i = 6 i = 8
#     if Numbers.count(i) > 1:  #Numbers.count(1) => 2 Because 1 appears twice.
#       Duplicates.append(i)    
# # | `i` | `Numbers.count(i)` | `> 1`? | Action      |
# # | --: | -----------------: | :----: | ----------- |
# # |   1 |                  2 |   Yes  | Add 1       |
# # |   2 |                  2 |   Yes  | Add 2       |
# # |   3 |                  1 |   No   | Nothing     |
# # |   4 |                  1 |   No   | Nothing     |
# # |   5 |                  1 |   No   | Nothing     |
# # |   2 |                  2 |   Yes  | Add 2 again |
# # |   1 |                  2 |   Yes  | Add 1 again |
# # |   6 |                  1 |   No   | Nothing     |
# # |   8 |                  1 |   No   | Nothing     |
       
# # Initially:       []

# # i = 1 →          [1]

# # i = 2 →          [1, 2]

# # i = 2 →          [1, 2, 2]

# # i = 1 →          [1, 2, 2, 1]             
     
# print(Duplicates)   #[1, 2, 2, 1]

##14.Create Dictionary from two lists    

# Keys = ["MohanaAswath","Vishwa","Abhishek","NithinKishore"] 
# Values = [90,88,88,80]
# Student_Marks = {}
# for i in range(len(Keys)) :
#     Student_Marks[Keys[i]] = Values[i]
# print(Student_Marks)   #{'MohanaAswath': 90, 'Vishwa': 88, 'Abhishek': 88, 'NithinKishore': 80}
                        
##15.Find Union of Two Sets 
# Set1 = {1,2,3,4,5,6,7,8,9,10}
# Set2 = {3,4,5,6,7,8,9,10,11,12} 
# Union_Set = Set1.union(Set2) 
# print(Union_Set)   #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

##16 . Find Intersection of Two Sets 
# Set1 = {5,10,15,20,25,30,35,40,45,50}
# Set2 = {30,35,40,45,50,55,60,65,70,75}
# Intersection_set = Set1.intersection(Set2)
# print(Intersection_set)   #{30, 35, 40, 45, 50}

##17 . Find Difference Between Sets 
# Set1 = {1,3,5,7,9,11,13,15,17,19}
# Set2 = {11,13,15,17,19,21,23,25}   
# Difference_Set = Set1.difference(Set2)               
# print(Difference_Set)   #{1, 3, 5, 7, 9}        

##18 .Count Positive , Negative and zero 
# Whole_Numbers = [-10,-100,-850,-3,-2,-1,0,1,70,45,70,0,200,106,-2005]  
# Positive = 0
# Negative = 0
# Zero = 0
# for i in Whole_Numbers:
#     if i > 0:
#         Positive +=1  #Positive = Positive + 1  
#     elif i < 0:
#         Negative +=1 #Negative = Negative + 1    
#     else:
#         Zero +=1
# print("Positive numbers:", Positive) #Positive numbers: 6
# print("Negative numbers:", Negative)  #Negative numbers: 7
# print("Zero numbers:", Zero)          #Zero numbers: 2

## 19.Nested Dictionary Traversal 
# Employee_Details = {
#     "Employee1": { "Name": "MohanaAswath", "Age": 25, "Department": "AI & ML" },
#     "Employee2": {"Name": "Abhishek", "Age": 30, "Department": "Data Science" },
#     "Employee3": {"Name": "Vishwa", "Age": 28, "Department": "Government Job" }
# }

# for Key , Value in Employee_Details.items():
#     print(Key + ":", Value["Name"] ,Value["Age"] , Value["Department"])
#Employee1: MohanaAswath 25 AI & ML
#Employee2: Abhishek 30 Data Science
#Employee3: Vishwa 28 Government Job 

##20. Find Employee with Highest Salary  
# Employee_Salary = {
#     "MohanaAswath": 100000,
#     "MythiliRupa": 81000,
#     "NithinKishore": 75000,
#     "Abhishek": 80000,
#     "Vishwa": 85000,
# }
# Highest_Salary = max(Employee_Salary.values())
# for Employee, Salary in Employee_Salary.items():
#     if Salary == Highest_Salary:
#         print(Employee) # MohanaAswath
        

##21 . Membership operator validation 
# Users = ["MohanaAswath","Abhishek","Vishwa","NithinKishore"] 
# Employee = input("Enter Users Name: ")  
# if Employee in Users:
#     print("Valid User")
# else:
#     print("Invalid User")
#I enter MohanaAswath => Valid User
#I enter Abhishek => Valid User
#I enter Gokul => Invalid User


##22 . Login Attempt using While Loop 
Password = "MohanaAswath@22122005"
Attempts = " "

while Attempts != Password:
    Attempts = input("Enter Password: ")
    if Attempts == Password:
        print("Login Successful")
    else:
        print("Invalid Password. Please try again.")
#I enter MohanaAswath@22122005 => Login Successful
#I enter MohanaAswath@22 => Invalid Password. Please try again.

##23. Categorize Marks using Nested if 

# Marks = int(input("Enter Marks: "))
# if Marks >= 35:
#     if Marks >= 90:
#          print("First Class with Distinction") 
#     elif Marks >= 75:
#          print("First Class")   
#     elif Marks >= 60: 
#          print("Second Class")   
#     else:
#          print("Pass")          
# else:
#     print("Fail") 

#I enter 95 => First Class with Distinction 
#I enter 80 => First Class  
#I enter 65 => Second Class
#I enter 40 => Pass   
#I enter 20 => Fail  


##24 .Find Unique Elements from two Lists
# List1 = [1, 2, 3, 4, 5]
# List2 = [4, 5, 6, 7, 8]
# for i in List1 + List2:
#     if i not in List1 or i not in List2:
#         print(i) #1 2 3 6 7 8 


##25 . Students Result Analysis using Dictionary
# Students_Marks = {
#     "MohanaAswath" :90,
#     "Abhishek" :88,
#     "Vishwa" :78,
#     "NithinKishore" :60,
#     "Ganesh" :55
# }

# for Students_Name , Students_Marks in Students_Marks.items():
#     if Students_Marks >= 90:
#         print(Students_Name +":Outstanding")
#     elif Students_Marks >= 80:  
#         print(Students_Name +":Excellent")
#     elif Students_Marks >= 70:  
#         print(Students_Name +":Very Good")
#     elif Students_Marks >= 60:  
#         print(Students_Name +":Good")
#     else:
#         print(Students_Name +":Needs Improvement")  
# MohanaAswath:Outstanding
# Abhishek:Excellent
# Vishwa:Very Good
# NithinKishore:Good
# Ganesh:Needs Improvement             


##11.Merge Two Dictionaries
# Dictionary1 = {"a": 95, "b":90, "c":85}
# Dictionary2 = {"d": 80, "e":75, "f":70}
# Dictionary1.update(Dictionary2)
# print(Dictionary1)  #{'a': 95, 'b': 90, 'c': 85, 'd': 80, 'e': 75, 'f': 70}

##12. Sort Dictionary by Values 
# Data = {"a": 95, "b":90, "c":85, "d":80, "e":75, "f":70}
# Sorted_Data = dict(sorted(Data.items(), key=lambda x:x[1]))
# print(Sorted_Data)  #{'f': 70, 'e': 75, 'd': 80, 'c': 85, 'b': 90, 'a': 95}

##8.Check Palindrome String
# Text = "mom"
# # if Text == Text[::-1]:
# #     print("Palindrome String") 
# # else:
# #     print("Not a Palindrome String")    
# if Text == ".join(reversed(Text))":
#     print("Palindrome String")
# else:
#     print("Not a Palindrome String")    

##7.Find Missing Numbers from Range
# Numbers = [23,30,35,40,20,21,45,43,5,10,7,32,4,15,25]
# for i in range(1,51):
#     if i not in Numbers:
#         print(i)


# ##6.Reverse a list without slicing
# Numbers = [1,2,3,4,5,6,7,8,9,10]
# Reverse_Numbers =[]
# for i in Numbers:
#     Reverse_Numbers.insert(0,i)
# print(Reverse_Numbers)  #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


##1. count even and odd numbers in a list
# Numbers = [1,4,8,3,5,9,6,34,12,13,15,1,16,8,17,8,10,20,7]
# Even = 0
# Odd = 0

# for i in Numbers:
#     if i%2 == 0:
#         Even += 1
#     else:
#         Odd += 1
# print("Even Numbers:",Even) #Even Numbers : 10 => 4,8,6,34,12,16,8,8,10,20
# print("Odd Numbers: " ,Odd) #Odd Numbers : 9 => 1,3,5,9,13,15,1,17,7  


##2 .Find Second Largest Number in a list 
# Numbers = [10,45,23,89,67,34,12,90,100] 
# Numbers.sort()  
# print(Numbers[-2])  #Second Largest Number => 90

##3 . Remove Duplicate using set 
# Numbers = [10,23,45,10,23,60,8,1,2,3,4,5,2,1,6,8]
# Unique_Numbers = list(set(Numbers))
# print(Unique_Numbers)  #[1, 2, 3, 4, 5, 6, 8, 10, 23, 45, 60]


##4. find common elements between two lists 
# List1 = [1,2,3,4,5,6,7,8,9]
# List2 = [5,6,7,8,9,10,11,12,13]
# Common_Elements = []
# for i in List1:
#     if i in List2:
#         Common_Elements.append(i)
# print(Common_Elements)  #[5, 6, 7, 8, 9]