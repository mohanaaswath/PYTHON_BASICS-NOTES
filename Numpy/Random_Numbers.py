import numpy as np

random = np.random.default_rng()
print(random.integers(5,9))

print(random.integers(low=100,high=500)) 

print(random.integers(low=100,high=500 , size=3)) 

print(random.integers(low=100,high=500 , size=(3 , 4))) 


rng = np.random.default_rng()
array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)


names = np.array(["mohan" , "mythili" , "aswath" , "rupa"])
name = rng.choice(names)
print(name)

name = rng.choice(names , size=3)
print(name)