import numpy as np
a_list=([1,2,3,4,5])
b_list=[[1,2,3],[4,5,6]]
a_array=np.array(a_list)
b_array=np.array(b_list)
# print(a_array*2)
print(a_array.shape)#元素个数
# print(a_array.dtype)#dtype类型
c=np.array([0,0,1,0,1],dtype=str)
print(c)
d=a_array > 3#符合要求的会返回True，不满足的返回False
print(d)
rand=np.random.rand(10)#随机生成若干个0-1之间的数
print(rand)
e=np.where(d)
print(e)
print(b_array)
'''axis=0是列，=1是行'''
print(b_array.argmax(axis=0))
print(b_array.max(axis=0))
'''argmax,argmin返回索引，max,min返回值'''
print(b_array.mean(axis=0))
'''mean是求平均值，同样接受一个axis,默认返回一个float'''
print(b_array.std())
print(b_array.var())
'''std是标准差，var是方差，同样支持axis作为第二参,必须是numpy对象或者numpy.array[].std'''
'''round(decimals=x)方法是是四舍五入x表示精度，1为保留一位小数，不写为保留整数(默认decimals可以不填)
clip（x，y）接受两个参数，小于x会变成x，大于y的会变成y'''
print(a_array.ndim)
print(b_array.ndim)
'''ndim方法返回维数'''
print(np.sort(a_array))
print(a_array.argsort())
'''sort会返回默认从小到大排序？？不能用对象？，argsort会返回排序后的·索引'''
f=np.linspace(0,10,10)
print(f)
'''linspace是生成若干个有序数'''
value=np.array([2.3,3.4,9.5])
print(np.searchsorted(f,value))
'''！！！x为排好顺序的！！！searchsorted(x,y)接受两个参数，x为待插入数组，y为需要插入的数组，返回可插入的索引'''
g=np.lexsort([b_array[:,0],b_array[:,0]])
print(g)
