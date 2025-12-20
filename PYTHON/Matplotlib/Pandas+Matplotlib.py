import matplotlib.pyplot as plt
import pandas as pd

data_frame = pd.read_csv("data.csv")
type_count = data_frame["Type1"].value_counts(ascending=True)
plt.bar(type_count.index,type_count.values,
        color = "blue",
        edgecolor = "black")

plt.tight_layout()
plt.show()