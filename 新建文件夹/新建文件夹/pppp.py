import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
pd.set_option('display.unicode.east_asian.width', True)
# data = {'2': [2, 3, 4, 5], '3': [5, 6, 7, 8], '4': [5, 6, 7, 8]}
index = ['李向东', '朱文博', '张兵']
columns = ['语文', '数学', '英语', 'A']
data = [[60.1, 60, 60,0.5333333], [60, 85, 85,0.243322], [100, 60, 60,0.8886654]]
df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)
df['总成绩'] = df.sum(axis=1)

# df =df._append (df.median(),ignore_index=True)
'''最大值max，最小值min，总和sum，中位数median，平均数mean'''
print(df.round(decimals=3))
df['百分比'] = df['A'].apply(lambda x : format(x,'.2%'))
'''apply()==map()'''
print(df)

'''
round保留小数位数，其值要是小数且位数大于decimals=的位数，round(decimals=3)==round(3)
round还可以接收一个Series对象和字典（可以指定每一列的保留位数）
！！！！四舍五入！！！
'''
# print(df.mode())
'''var方差   std标准差'''
# df = df.iloc[]
# print(df.iloc[0:2,2:])
# print(df.iloc[:, 1:])
# print(df.loc['李向东':'张兵'])
# print(df.iloc[0:2])
# a = pd.Series(np.arange(10),index=np.arange(1, 11))
# print(a)
# writer = pd.ExcelWriter('text2.xlsx')
# df.to_excel('text2.xlsx')
# writer.save()
'''
axis在进行运算时0是行1是列
其他部分时候0是列1是行
apply()可以用于Series和DataFrame的每个对象
map()只用于Series，map的参数可以是一个函数也可以是一个字典
applymap()将函数应用到DataFrame的每个元素上，与·apply的区别apply只能应用在每列或每行
groupby(分组依据)[](单列)[][][](多列).(函数)
groupby对象类型为DataFrameGroupBy类似于requests最后，都要用for迭代下才能打印
有两个·参数name,group，name为组名，group为组内参


df = df[[],[],[]]数据提取



agg（）函数，多元参数
agg([])接受列表['']和{‘’：[]}和{'':''}

shift()函数对列进行下移，如[1,2,3,4,5].shift()->[NaN,1,2,3,4],可以做减法算差值

value_counts()对DateFrame对象求和并排序

DataFrame对象的str.split('',expand=True)第一参是分割符，第二参是是否转化为DataFrame
'''





# df1 = pd.DataFrame(np.random.randn(8, 4), index=pd.date_range('2/1/2020', periods=8), columns=list('ABCD'))
# df1.plot.bar()
# plt.show()