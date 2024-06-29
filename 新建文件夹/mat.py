from matplotlib import pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["SimHei"]
x = np.arange(1, 11)
y = x*2+3
x1 = range(1, 5)
y1 = [1, 2, 3, 4]
plt.title('sii')
plt.subplot(2, 2, 1)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, color='r', marker='h')
plt.subplot(2, 2,  4)
plt.bar(x1, y1, color='r', align='center')
plt.legend(labels=['牢底'])
plt.grid(True)
plt.show()
