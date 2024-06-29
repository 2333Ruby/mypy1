import requests
from bs4 import BeautifulSoup


res = requests.get('https://www.runoob.com/try/xml/books.xml').text

soup = BeautifulSoup(res, 'lxml')
res1 = soup.find_all(name='year')
res2 = soup.select('book title')
res3 = soup.find_all(attrs={'lang': 'en'})
print(res)
print('-------------'*10,sep='\n')
print(res1)
print(res2)
print(res3)
for i in res3:
    print(i.string)

print('-------------'*10,sep='\n')
# for i in res1:
#     print(i.string)
'''
1,select是css选择器一般有四种用法
（1）id选择器，用#号来定位，#+id属性
（2）类选择器，用.来定位元素，.+class后面的类值
（3）标签选择器，用标签名来定位元素，除了第一个标签外都要加空格
（4）混合使用
2,节点选择器，通过soup.节点名称来选择元素
3，方法选择器
用find_all()方法的*kwargs其他属性时id=，name= ，class_=，因为class与关键字重名了，所以要加下划线
attrs={'str':'str'}来定位元素
'''