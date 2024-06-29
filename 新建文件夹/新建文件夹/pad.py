import pandas as pd

pd.set_option('display.unicode.east_asian.width', True)
ex = pd.read_excel('text2.xlsx')
'''第二参数usecols=['','']可以指定列'''
# ex = ex.set_index('姓名')
print(ex)

ex['总成绩'] = ex.sum(axis=1, skipna=True)
print(ex)
# print(ex.sort_values(by='英语', ascending=False))
# ex['顺序排名'] = ex['数学'].rank(ascending=False)#默认按顺序
# print(ex)
# # print(ex.reindex(range(6), method= 'ffill'))
# print(ex.reindex(range(6), fill_value=30))
# print(ex.isnull())
