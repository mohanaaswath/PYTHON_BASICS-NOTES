import matplotlib.pyplot as plt
import numpy as np

scores = np.random.normal(loc=80 , scale=10 , size=100)
scores = np.clip(scores , 0 , 100)

#scores = [20,3040,50,60,70,70,80,90,100,10,60,80,90]

plt.hist(scores , bins=10,
                  color="blue",
                  edgecolor = "black")

plt.title("Exam scores ")
plt.xlabel("scores")
plt.ylabel("no of students")

plt.show()