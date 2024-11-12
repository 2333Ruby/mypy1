import pandas as pd
import numpy as np

# pd.set_option('display.max_rows', None), pd.set_option('display.max_columns', None)  # 行和列显示不完全
# pandas对象的tolist方法，而DataFrame对象是to_list方法


# t = [0, 1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 0]
# print(len(t))
# print(len(set(t)))  # 去重
# print(set(t))  # set()以字典形式返回
# t1 = pd.Series(t)
# print(t1.unique())  # unique()去重这个方法只有pandas的series对象有，而pandas的dataframe对象没有，以列表形式返回
# print(t1.value_counts())  # value_counts()统计每个元素出现的次数
# print(t1.value_counts().index)
# t3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# t4 = pd.DataFrame(t3, columns=['A', 'B', 'C'])
# print(t3)
# print(t3.flatten())  # flatten()将数组展开成一维数组，要求里面的每个元素都是数字且维度一致
# print(t4.set_index('A'))
# print(t4.set_index('A', drop=False))
# pd/groupby(by='A')来分组，groupby()方法返回一个DataFrameGroupBy对象，它包含一个或多个列，这些列被用来对数据进行分组。
# df.info()可以展示数据的统计信息
# d = pd.date_range('20130101', '20140101',freq='M') # date_range()函数生成一个日期序列， periods参数指定生成日期的个数
# # print(d)
# print(d)
#
# d1 = pd.to_datetime('2025-01-01', format='%Y-%m-%d')
# print(d1)

# date = {'date_str':['2023-01-01','2024-01-01','2024-08-15']}
# df = pd.DataFrame(date)
# print(df)
# print('*'*100)
# df['date_time'] = pd.to_datetime(df['date_str'])
# print(df)
# print('*'*100)
# df['year'] = df['date_time'].dt.year
# df['month'] = df['date_time'].dt.month
# df['day'] = df['date_time'].dt.day
# print(df)
# print('*'*100)
# print(df.info())
# print(df.__dir__())  # dir()查看可用的方法


data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]],index=['a', 'b', 'c'], columns=['A', 'B', 'C'])
print(data)
# data_list = data['A'].tolist()
# print(data_list)
data_1 = data.groupby('A')
print('-'*100)
print(data_1.apply(lambda x: x))
print('-'*100)
print(data_1.head(2))
print('-'*100)
for i in data_1:
    print(i)
# data.set_index('A', inplace=True)
# print(data['B'])

