import numpy as np 
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

#scalar arithmetic
array = np.array([1,2,3,4])
print(array+1)
print(array-2)
print(array*3)
print(array/4)
print(array**5)

#[2 3 4 5]
#[-1  0  1  2]
#[ 3  6  9 12]
#[0.25 0.5  0.75 1.  ]
#[   1   32  243 1024]

#vectorized math function 

array = np.array([1,2,3,4])
print(np.sqrt(array))  #[1.         1.41421356 1.73205081 2.        ]
array = np.array([1.01,2.5,3.99])
print(np.round(array)) #[1. 2. 4.]
print(np.floor(array)) #[1. 2. 3.]

#comparison operator 

score = np.array([91,55,100,73,82,64])
print(score == 100 ) #[False False  True False False False]
print(score >= 60) #[ True False  True  True  True  True]
score[score < 60] = 0
print(score) #[ 91   0 100  73  82  64]

#broad casting 

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1] , [2] , [3] , [4]])
print(array1.shape) #(1,4)
print(array2.shape) #(4,1)
print(array1 * array2)
# [[ 1  2  3  4]
# [ 2  4  6  8]
# [ 3  6  9 12]
 #[ 4  8 12 16]]