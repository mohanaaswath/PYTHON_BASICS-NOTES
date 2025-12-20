import matplotlib.pyplot as plt
import numpy as np

Names = np.array(["Mohan" , "Abi" , "Dhanush" , "Nithin" , "Anbu" , "Guru"])
Marks = np.array([100 , 95 , 75 , 90 , 72 , 78])

plt.bar(Names , Marks , 
                color = "black" )
#plt.barh(Names , Marks)


plt.xlabel('NAMES',fontsize = 20,
                  family = "Ariel",
                  fontweight = "bold",
                  color = "#0e8ee2")
plt.ylabel('MARKS',fontsize = 20,
                  family = "Ariel",
                  fontweight = "bold",
                  color = "#e60914")
plt.title('MARKS ANALYZES' ,fontsize = 20,
                  family = "Ariel",
                  fontweight = "bold",
                  color = "#059b0cc0")

plt.show()