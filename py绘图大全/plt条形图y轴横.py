from matplotlib import pyplot as plt


# 详细标注参见plt折线图.py
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
a = ['战狼2', '速度与激情8', "功夫瑜伽", '西游伏妖篇', '变形金刚5：最后的骑士', "摔跤吧！爸爸", '加勒比海盗5：死无对证', '金刚：骷岛', '极限特工：终极回归', ' 生化危机6：终章', '乘风破浪' , '神偷奶爸3', '智取威虎山', '大闹天竺', '金刚狼3：殊死一战', '蜘蛛侠：英雄归来', '悟空传', '银河护卫队2', '情圣', '新木乃伊']
b = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.326,6.88,6.86,6.58,6.23,6.09]
# x = [i for i in range(len(a))]
plt.figure(figsize=(16, 8))
plt.barh(range(len(a)), b, height=0.3,  color='cyan', label='票房')
plt.title('2017年票房前20名')
plt.ylabel('电影名称')
plt.xlabel('票房')
plt.yticks(range(len(a)), a)
plt.legend()
plt.grid(alpha=True)

plt.show()

# print(len(a))
# print(len(b))