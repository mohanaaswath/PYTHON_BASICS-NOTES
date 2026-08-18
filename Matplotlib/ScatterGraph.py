import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0,1,1,2,3,4,5,6,6,7,8])
y1 = np.array([55,60,54,70,72,65,55,56,78,80,90]) 

x2 = np.array([0,1,1,2,3,4,4,5,6,6,7])
y2 = np.array([10,20,20,40,45,45,50,60,60,80,80]) 

plt.scatter(x1,y1 , color = "blue",
                    alpha=0.5,
                    s=200,
                    label = "Class A")

plt.scatter(x2,y2 , color = "red",
                    alpha=0.5,
                    s=200,
                    label = "Class B")

plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Study Time Analyzes")
plt.legend()  #access the that scatter label = class a , class b
 
plt.show()
