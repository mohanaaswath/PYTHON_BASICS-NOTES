import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026, 2027, 2028])
y1 = np.array([15, 20, 25, 28, 18, 10])
y2 = np.array([17, 18, 21, 10, 5, 40])

line_style = dict(
    marker='.',
    markersize=8,
    markerfacecolor="#1cd3fc",
    markeredgecolor="#1cd3fc",
    linestyle='-',
    color="#1c56fc",
)

plt.plot(x, y1, **line_style)
plt.plot(x, y2, **line_style)

#labels
plt.xlabel('Year',fontsize = 25,
                  family = "Ariel",
                  fontweight = "bold",
                  color = "#2d4cfc")
plt.ylabel('students',fontsize = 30,
                  family = "Ariel",
                  fontweight = "bold",
                  color = "#2dbefe")
plt.title('class size' ,fontsize = 25,
                  family = "Ariel",
                  fontweight = "bold",
                  color = "#d31a23")

plt.tick_params(axis="both",
                colors = "#05ee2c")

#grid
plt.grid(axis="both",
         linewidth = 2,
         color = "yellow",
         linestyle = "dashed")
plt.show()