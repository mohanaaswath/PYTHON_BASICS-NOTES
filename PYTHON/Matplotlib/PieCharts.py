import matplotlib.pyplot as plt
import numpy as np


Programming_Languages = np.array(["Python" , "Java" , "JavaScript" , "C++" , "C"])
Values = np.array([80, 70 , 60 , 40 ,25])
Colors = ["blue" , "red" , "green" , "yellow" , "orange"]

plt.pie(Values , 
        labels=Programming_Languages,
        autopct="%1.1f%%",
        colors=Colors,
        explode = [0.1, 0, 0, 0, 0],
       # shadow=True,
        startangle=90
         )

plt.show()