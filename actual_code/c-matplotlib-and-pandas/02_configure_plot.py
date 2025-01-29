import matplotlib.pyplot as plt

x = range(1,11)
y = [3,4,6,9,11,12,10,11,14,16]

plt.ylabel('y values', fontsize=12)
plt.xlabel('x values', fontsize=12)

plt.title("Sample Graph Using MatPlotLib")

plt.plot(x,y, linewidth=2.0, label="samples", marker="o", color="blue", linestyle="--")

plt.grid()

plt.show()