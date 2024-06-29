from matplotlib import pyplot as plt
import random


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
x = range(1, 30)
y = [random.randint(20, 35) for i in range(1, 30)]  # x与y的数量要保持一致
plt.figure(figsize=(15, 8), dpi=80)  # 设置图片大小和分辨率
# fig.canvas.set_window_title("真的是太幽默了")
plt.title('随机生成折线图')  # 子图标题
plt.suptitle("幽默")  # 图像标题
plt.plot(x, y, label='折线图',color='cyan', linestyle='--')  # 绘制折线图,label为图例label,color为折线颜色(单词全称或首字母代替),linestyle为折线类型
xtick = [f'{i}年' for i in range(1, 30)]  # x轴刻度标识
plt.xticks(x, xtick)  # 设置x轴刻度标识
plt.yticks(range(20, 40, 2))
plt.grid(alpha=0.5, linestyle=':')  # 绘制网格, alpha为网格线透明度
plt.xlabel('x轴')
plt.ylabel('y轴')

plt.legend(loc=2)  # 显示图例label, loc为图例位置

plt.show()



