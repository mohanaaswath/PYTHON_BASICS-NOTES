import numpy as np 
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])
#array [ start : end : step]

print(array[1])  # [5 6 7 8]
print(array[0:3])
 # [[ 1  2  3  4]
 #[ 5  6  7  8]
 #[ 9 10 11 12]]
 
print(array[0:4:2])
#[[ 1  2  3  4]
# [ 9 10 11 12]]

print(array[::-1])
#[[13 14 15 16]
 #[ 9 10 11 12]
 #[ 5  6  7  8]
 #[ 1  2  3  4]]
 
print(array[::-2])
#[[13 14 15 16]
# [5 6 7 8]]

#column
print(array[:,0])
# [ 1  5  9 13]
print(array[:,-1])
# [ 4  8 12 16]
print(array[:,0:3])
#[[ 1  2  3]
# [ 5  6  7]
 #[ 9 10 11]
 #[13 14 15]]
print(array[:,::-1])
#[[ 4  3  2  1]
 #[ 8  7  6  5]
 #[12 11 10  9]
 #[16 15 14 13]]
