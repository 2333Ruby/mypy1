from matplotlib import pyplot as plt


# 详细标注参见plt折线图.py
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


a = ['大鱼海棠', '千与千寻', '龙猫', '声之形']
b_1 = [10, 20, 25, 40]
b_2 = [15, 30, 35, 50]
b_3 = [20, 25, 30, 45]
a_1 = [i for i in range(len(a))]
a_2 = [i+0.2 for i in a_1]
a_3 = [i+0.4 for i in a_1]

plt.bar(a_1, b_1, label='一号', width=0.2)
plt.bar(a_2, b_2, label='二号', width=0.2)
plt.bar(a_3, b_3, label='三号', width=0.2)

plt.xticks(a_2, a)
plt.grid(axis='y')
plt.legend()
plt.show()
