import numpy as np
import random

# 广播运算，加减乘除都会被应用到所有的元素上，多个元素加减时候，必须保证两个数组的行或列数相等
# python中并不存在数组，只有ndarray，通过numpy的array函数来创建数组

# t1 = np.array([1, 2, 3, 4, 5])  # 转置t1.T or t1.transpose() or t1.swapaxes(1, 0)
# print(t1)
# print(type(t1))
# print(t1.dtype)
#
#
# t2 = np.array(range(1, 6))
# print(t2)
# print(type(t2))
# print(t2.dtype)
#
#
# t3 = np.arange(1, 6)
# print(t3)
# print(type(t3))
# print(t3.dtype)
#
#
# t4 = np.array(range(1, 6), dtype=np.float64)
# print(t4)
#
# t5 = np.array([random.random() for i in range(5)])
# print(t5)
# t5 = t5.round(2)
# print(t5)

# t6 = np.array([[1, 2, 3], [4, 5, 6]])
# print(t6.shape)
# print(t6.shape[0]*t6.shape[1])
# print(t6.size)
# print(t6.flatten())


# t7 = t6.reshape(3, 2)
# print(t7)
# t6 = t6.reshape(3, 2)
# print(t6)

# k1 = np.loadtxt("GB_video_data_numbers.csv", delimiter=",", dtype=int, unpack=False)  # unpack=True表示转置
# k2 = np.loadtxt("US_video_data_numbers.csv", delimiter=",", dtype=int)
#  ,前面是行，后面是列，要传入多个不连续的的数字可以[1,3,5]外面再加一个[]
#  [[1,2,3],[3,2,5]]取值时表示取的是(1,3),(2,2),(3,5)这三个点
# print(k1)
# print(k2)
# print(k1[2])
# print(k1[:2:])
# print(k1[0, 1])
# print(k1[:, :2])

# k3 = np.arange(1, 10)
# k5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# k4 = k3[k3 < 5]
# print(k3[k3 > 5])  # 可以通过这种方式来筛选出满足条件的元素，但是不能改变原数组，在改变原数组需要使用[k3[k3 < 5]] = 0
# print(k4)  # 可以在]后=赋值，但是不能改变原数组，在改变原数组需要使用[k3[k3 < 5]] = 0
# k6 = np.where(k3 < 5, 0, 10)  # where(条件，满足条件时，替换的值，不满足条件时，替换的值),同python里的if else语句
# print(k6)
# print(k5.clip(5, 6))  # clip(最小值，最大值)，限制数组中的元素在指定范围内，超出范围则替换为指定范围


# k7 = np.array([[1, 0, 0], [4, 0, 6]])
# t = np.count_nonzero(k7)
# print(t)
# t_1 = np.isnan(k7)
# print(t_1)
# t_2 = np.count_nonzero(t_1)
# print(t_2)

# k8 = np.array([[1, 2, 3], [4, 5, 6]])
# print(k8)
# print(k8.sum())
# print(k8.sum(axis=0))
# print(k8.sum(axis=1))  # 对于二维数组axis=0表示按列求和，axis=1表示按行求和


# k9 = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)
# k9[1, 1] = np.nan
# print(k9.mean(axis=0))  # mean()函数可以求均值，axis=0表示按列求均值，axis=1表示按行求均值
# print(np.median(k9, axis=1))  # median()函数可以求中位数，axis=0表示按列求中位数，axis=1表示按行求中位数
# print(k9)  # np.ptp()求极值，即数组中的最大值减去最小值|||np.std()求标准差|||np.var()求方差|||默认返回多维数组的全部的统计结果，如果指定axis则返回一个当前轴上的结果
'''
标准差是一组数据平均值分散程度的一种度量。一个较大的标准差，代表大部分数值和其平均值之间差异较大；
一个较小的标准差，代表这些数值较接近平均值反映出数据的波动稳定情况，，越大表示波动越大，约不稳定
'''
# print(np.isnan(k9))
# k9[np.isnan(k9)] = 0  # 将nan替换为0
# print(k9)

'''
np.isnan()函数用来判断一个元素是否为nan，返回一个布尔值，True表示为nan，False表示不是nan
np.count_nonzero()函数用来统计数组中非0元素的个数，返回一个整数
'''

# 将nan替换为均值
# k10 = np.arange(12).reshape(3, 4).astype(np.float64)
# k10[1, 1] = np.nan
# print(k10)
# print('*'*100)
# print(k10[k10 == k10])
# print('*'*100)
# print(k10 != k10)
# print('*'*100)
# print(np.isnan(k10))
# print('*'*100)
# print(np.count_nonzero(k10))
# print(np.count_nonzero(k10 != k10))
# print('*'*100)
# for i in range(k10.shape[1]):
#     num1 = k10[:, i]
#     not_nan = np.count_nonzero(num1 != num1)
#     if not_nan != 0:
#         temp_not = num1[num1 == num1]
#         num1[np.isnan(num1)] = temp_not.mean()
# print(k10)

# 拼接数组
# k11 = np.array([1, 2, 3])
# k12 = np.array([4, 5, 6])
# k13 = np.vstack([k11, k12])  # vstack()函数将数组竖直方向上堆叠起来
# print(k13)
# k14 = np.hstack([k11, k12])  # hstack()函数将数组水平方向上堆叠起来
# print(k14)
#
# zero = np.zeros((2, 1))
# print(zero)
#
# one = np.ones((2, 1))
# print(one)
#
# ey = np.eye(3)
# print(ey)
# ey[0, 2] = 3
# print(ey)
# e = np.argmax(ey, axis=1)
# print(e)
# ey[ey == 1] = -1
# print(ey)

k15 = np.random.randn(2, 5)
print(k15)

k16 = np.random.uniform(10, 20, (3, 4))
print(k16.round(2))