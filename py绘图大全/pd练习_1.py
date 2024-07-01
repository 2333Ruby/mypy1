import pandas as pd
import numpy as np

#  pandas的大部分东西与numpy一样的
#  pandas中算术运算不会处理NaN，但是numpy中会处理NaN

# t = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], name='test', dtype='float64')
# print(t)
# print(t['b'])
# print(t[2])

# t1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])
# print(t1)

# d1 = {"name": ["xia0ming", "xia0gang"], "age": [20, 32], "tel": [10086, 10010]}
# d2 = pd.DataFrame(d1, index=['a', 'b'])
# print(d2)
# # print(d2.sort_values(by='age', ascending=False))

# d3 = d2.loc[['a'], ['age']]
# print(d3)
# d4 = d2.iloc[0:2, 0:2]
# print(d4)
# d5 = d2.loc[:, 'name':'tel']
# print(d5)

# t2 = pd.DataFrame(np.arange(12).reshape(3, 4), index=['a', 'b', 'c'], columns=['A', 'B', 'C', 'D'])
# t2.loc[['a'], ['A']] = np.nan
# print(t2)
# print(t2.isnull())
# print(t2.notnull())
# print(t2.dropna(axis=1))  # 在DataFrame中axis=1表示行，0表示列，与numpy不相同
# print(t2.fillna(0))

# 同类的还有drop_duplicates()，drop_duplicates(subset=['A'])，drop_duplicates(subset=['A', 'B'])
t3 = pd.DataFrame(np.arange(12).reshape(3, 4))
# print(t3)
# print('type:', type(t3))
# print('dtype:', t3.dtypes)
# print('*' * 20)
# t4 = t3.values
# print(t4)
# print('type:', type(t4))
# print('dtype:', t4.dtype)
t5 = t3[1]
print(t5)
print(type(t5))