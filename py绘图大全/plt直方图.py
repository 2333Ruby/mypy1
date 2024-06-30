from matplotlib import pyplot as plt
import random

# 组数＝（max-min）/组距,对不齐就是组数出问题了，保证组数十个整数
# 详细标注参见plt折线图.py
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

a = [random.randint(2, 149) for i in range(248)]
a.append(1)
a.append(151)
d = 10
d_bin = (max(a) - min(a))//d
plt.hist(a, bins=d_bin, color='cyan',density=True)  # density=TrueY轴会由数量变为频率
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(range(min(a), max(a)+d, d))
plt.title('直方图')
plt.grid()
plt.show()