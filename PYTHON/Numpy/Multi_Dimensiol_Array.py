import numpy as np 

array = np.array(["A","B","C"])
print(array)
print(array.ndim) #1

array = np.array([["A","B","C"],
                  ["D","E","F"],
                  ["G","H","I"]])  #2
print(array.ndim)

array = np.array([[["A","B","C"],["D","E","F"],["G","H","I"]],
                  [["J","K","L"],["M","N","O"],["P","Q","R"]],
                  [["S","T","U"],["V","W","X"],["Y","Z"," "]]])
print(array.ndim) #3
print(array.shape) #(3, 3, 3)


array = np.array([[["A","B","C"],["D","E","F"],["G","H","I"]],
                  [["J","K","L"],["M","N","O"],["P","Q","R"]]])
print(array.shape)  #(2,3,4)  two layer , two row , two column

array = np.array([[["A","B","C"],["D","E","F"],["G","H","I"]],
                  [["J","K","L"],["M","N","O"],["P","Q","R"]],
                  [["S","T","U"],["V","W","X"],["Y","Z"," "]]])

print(array[0] [0] [0]) # A  chain indexing
print(array[0] [0] [2]) #c
print(array[0] [1] [2]) #f

print(array[0,0,0]) #A multidimensional array
print(array[0,0,2]) #C
print(array[0,1,2]) #F
print(array[1,2,2]) #R
print(array[2,0,2]) #U

My_Name = array[1,1,0] + array[1,1,2] + array[0,2,1] + array[0,0,0] + array[1,1,1] 
print(My_Name) #MOHAN

