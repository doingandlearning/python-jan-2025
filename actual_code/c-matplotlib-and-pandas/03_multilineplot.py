import matplotlib.pyplot as plt

x = range(1,11)
y1 = [3,4,6,9,11,12,10,11,14,16]
y2 = [4,5,6,7,8,7,6,3,2,1]
y3 = [10,11.5,12,10.5,9,7.5,7,4,2.3,1]

plt.plot(x, y1, label="dataset1", color="blue", linestyle="-.")
plt.plot(x, y2, label="dataset2", color="red", linestyle=":")
plt.plot(x, y3, label="dataset3", color="green", linestyle="-")

plt.legend()
plt.show()