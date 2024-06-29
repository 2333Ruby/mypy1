from matplotlib import pyplot as plt
import random


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
x = [i for i in range(1, 31)]
y = [random.randint(0, 30) for i in range(1, 31)]
plt.figure(figsize=(10, 5))
plt.scatter(x, y, c='cyan', label='温度')
plt.xlabel('时间（天）')
plt.ylabel('温度（℃）')
xt = ['{}号'.format(i) for i in range(1, 31)]
yt = ['{}℃'.format(i) for i in y]
plt.xticks(x, xt, rotation=45)  # 旋转45度
plt.yticks(y, yt)
plt.grid(alpha=True)
plt.legend()
plt.show()
